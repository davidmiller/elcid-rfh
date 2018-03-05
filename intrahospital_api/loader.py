"""
    Get a loader this.

    This is the entry point to the api.

    The api handles all interaction with the external
    system.

    This handles our internals and relationship
    between elcid.

    We have 7 entry points.

    load_demographics(hospital_number)
    returns the demographcis for that hospital number
    without saving.

    load_lab_tests_for_patient(patient, async=False):
    nukes all existing lab tests and replaces them.

    this is run in the inital load below. When we add a patient for the
    first time, when we add a patient who has demographics or when we've
    reconciled a patient.

    initial_load()
    iterates over all patiens and runs load_lab_tests_for_patient.

    batch_load()
    runs the batch load for all patients that are reconciled.
    currently not being loaded in.

    this is run every 5 mins and after deployments

    Loads everything since the start of the previous
    successful load so that we paper over any cracks.

    update_external_demographics()
    for all demographics that have not been sourced from
    upstream, load in their latest information for
    the reconcile list. Used by a management command
"""

import datetime
import logging
import traceback
from django.db import transaction
from django.utils import timezone
from django.db.models import Q
from django.conf import settings
from intrahospital_api import models
from elcid import models as emodels
from elcid.utils import timing
from opal.models import Patient
from intrahospital_api.apis import get_api
from intrahospital_api.exceptions import BatchLoadError
from intrahospital_api.constants import EXTERNAL_SYSTEM

api = get_api()
logger = logging.getLogger('intrahospital_api')


@timing
def initial_load():
    models.InitialPatientLoad.objects.all().delete()
    models.BatchPatientLoad.objects.all().delete()
    batch = models.BatchPatientLoad()
    batch.start()
    try:
        update_external_demographics()
        # only run for reconciled patients
        patients = Patient.objects.filter(
            demographics__external_system=EXTERNAL_SYSTEM
        )
        total = patients.count()

        for iterator, patient in enumerate(patients.all()):
            logger.info("running {}/{}".format(iterator, total))
            load_lab_tests_for_patient(patient, async=False)
    except:
        batch.failed()
        log_errors("initial_load")
    else:
        batch.complete()


def log_errors(name):
    email_logger = logging.getLogger('error_emailer')
    email_logger.error("unable to run {}".format(name))
    logger.error(traceback.format_exc())


def any_loads_running():
    """
        returns a boolean as to whether any loads are
        running, for use by things that synch databases
    """
    patient_loading = models.InitialPatientLoad.objects.filter(
        state=models.InitialPatientLoad.RUNNING
    ).exists()

    batch_loading = models.BatchPatientLoad.objects.filter(
        state=models.BatchPatientLoad.RUNNING
    ).exists()

    return patient_loading or batch_loading


def load_demographics(hospital_number):
    started = timezone.now()
    try:
        result = api.demographics(hospital_number)
        stopped = timezone.now()
        logger.info("demographics load complete in {}".format(
            (stopped - started).seconds
        ))
    except:
        stopped = timezone.now()
        logger.info("demographics load failed in {}".format(
            (stopped - started).seconds
        ))
        log_errors("load_demographics")

    return result


def load_lab_tests_for_patient(patient, async=None):
    """
        Load all the things for a patient.

        This is called by the admin and by the add patient pathways
        Nuke all existing lab tests for a patient. Synch lab tests.

        will work asynchronously based on your preference.

        it will default to settings.ASYNC_API.
    """
    if async is None:
        async = settings.ASYNC_API

    patient_load = models.InitialPatientLoad(
        patient=patient,
    )
    patient_load.start()
    if async:
        async_load(patient, patient_load)
    else:
        _load_lab_tests_for_patient(patient, patient_load)


def async_load(patient, patient_load):
    from intrahospital_api import tasks
    tasks.load.delay(patient, patient_load)


def good_to_go():
    """ Are we good to run a batch load, returns True if we should.
        runs a lot of sanity checks.
    """
    current_running = models.BatchPatientLoad.objects.filter(
        Q(stopped=None) | Q(state=models.BatchPatientLoad.RUNNING)
    )

    if current_running.count() > 1:
        # we should never have multiple batches running at the same time
        raise BatchLoadError(
            "We appear to have {} concurrent batch loads".format(
                current_running.count()
            )
        )

    last_run_running = current_running.last()

    if last_run_running:
        time_ago = timezone.now() - last_run_running.started

        # If a batch load is still running and started less that
        # 10 mins ago, the let it run and don't try and run a batch load.
        #
        # Examples of when this might happen are when we've just done a
        # deployment.
        if time_ago.seconds < 600:
            return False
        else:
            raise BatchLoadError(
                "Last load is still running and has been for {} mins".format(
                    time_ago.seconds/60
                )
            )

    twenty_mins_ago = timezone.now() - datetime.timedelta(seconds=20 * 60)
    if models.BatchPatientLoad.objects.last().stopped < twenty_mins_ago:
        raise BatchLoadError("Last load has not run since {}".format(
            models.BatchPatientLoad.objects.last().stopped
        ))

    if not models.BatchPatientLoad.objects.filter(
        state=models.BatchPatientLoad.SUCCESS
    ).exists():
        err = "No previous run has completed, please run ./manage.py"
        err += "initial_load before you run a batch load"
        raise BatchLoadError("err {}".format(
            models.BatchPatientLoad.objects.last().stopped
        ))


def batch_load():
    if not good_to_go():
        return
    batch = models.BatchPatientLoad()
    batch.start()
    try:
        _batch_load()
    except:
        batch.failed()
        log_errors("batch load")
    else:
        batch.complete()


@transaction.atomic
def update_external_demographics():
    """
        If the patient has not been loaded in from upstream,
        check to see if they have demographics upstream and populate
        the external demographics accordingly.

        This will then put them on the reconciliation patient list
    """
    patients = Patient.objects.exclude(
        demographics__external_system=EXTERNAL_SYSTEM
    )
    patients = patients.filter(
        externaldemographics__hospital_number=None
    )
    for patient in patients:
        demographics = patient.demographics_set.get()
        external_demographics_json = api.demographics(
            demographics.hospital_number
        )
        if not external_demographics_json:
            print "unable to find {}".format(demographics.hospital_number)
            continue

        external_demographics = patient.externaldemographics_set.get()
        external_demographics_json.pop('external_system')
        external_demographics.update_from_dict(
            external_demographics_json, api.user
        )


@transaction.atomic
@timing
def _batch_load():
    last_successful_run = models.BatchPatientLoad.objects.filter(
        status=models.BatchPatientLoad.SUCCESS
    ).order_by("started").last()
    # update the non reconciled
    update_external_demographics()

    data_deltas = api.data_deltas(last_successful_run)
    update_from_batch(data_deltas)


@timing
def update_from_batch(data_deltas):
    # only look at patients that have been reconciled
    demographics_set = emodels.Demographics.objects.filter(
        external_system=EXTERNAL_SYSTEM
    )

    # ignore patients that have not had an existing patient load
    demographics_set = demographics_set.filter(
        initialpatientload__status=models.InitialPatientLoad.SUCCESS
    )
    for data_delta in data_deltas:
        demographics = data_delta["demographics"]
        patient_demographics_set = demographics_set.filter(
            hospital_number=demographics["hospital_number"]
        )
        if not patient_demographics_set.exists():
            # this patient is not in our reconcile list,
            # move on, nothing to see here.
            continue

        # our patients demographics have changed.
        if not patient_demographics_set.filter(
            **demographics
        ).exists():
            # get the demographics for this patient
            patient_demographics = patient_demographics_set.get()
            patient_demographics.update_from_dict(
                data_delta["demographics"], api.user
            )
            patient = patient_demographics.patient
            update_tests(
                patient,
                data_delta["lab_tests"],
                api.user
            )


@timing
def update_tests(patient, lab_tests):
    """
        takes in all lab tests, saves those
        that need saving updates those that need
        updating.
    """
    for lab_test in lab_tests:
        lab_model = get_model_for_lab_test_type(lab_test)
        lab_model.update_from_api_dict(patient, lab_test, api.user)


@transaction.atomic
def _load_lab_tests_for_patient(patient, patient_load):
    try:
        hospital_number = patient.demographics_set.first().hospital_number
        patient.labtest_set.filter(
            lab_test_type__in=[
                emodels.UpstreamBloodCulture.get_display_name(),
                emodels.UpstreamLabTest.get_display_name()
            ]
        ).delete()

        results = api.results_for_hospital_number(hospital_number)
        update_tests(patient, results)
    except:
        patient_load.failed()
        log_errors("_load_lab_tests_for_patient")
    else:
        patient_load.complete()


def get_model_for_lab_test_type(lab_test):
    if lab_test["test_name"] == "BLOOD CULTURE":
        mod = emodels.UpstreamBloodCulture
    else:
        mod = emodels.UpstreamLabTest

    external_identifier = lab_test["external_identifier"]
    lab_test_type = lab_test["test_name"]
    filtered = mod.objects.filter(
        external_identifier=external_identifier,
    )
    by_test_type = [
        f for f in filtered if f.extras["test_name"] == lab_test_type
    ]

    if len(by_test_type) > 1:
        raise ValueError(
            "multiple test types found for {} {}".format(
                external_identifier, lab_test_type
            )
        )

    if by_test_type:
        return by_test_type[0]
    else:
        return mod()
