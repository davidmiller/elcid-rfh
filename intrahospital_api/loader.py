"""
    Get a loader this.

    This is the entry point to the api.

    The api handles all interaction with the external
    system.

    This handles our internals and relationship
    between elcid.

    we have 5 entry points

    initial_load()
    nukes all existing lab tests and replaces them.

    this is run in the inital load below. When we add a patient for the
    first time, when we add a patient who has demographics or when we've
    reconciled a patient.

    batch_load()
    Tries to reconcile all unreconciled demographics

    runs the batch load for all patients that are reconciled.
    currently not being loaded in.

    this is run every 5 mins and after deployments

    Loads everything since the start of the previous
    successful load so that we paper over any cracks.

    load_patient()
    is what is run when we run it from the admin, or
    after a patient has been reconciled from teh reconciliation pathway.
    It loads in data for a single specific patient.

    any_loads_running()
    returns true if any, ie initial or batch, loads are running
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
from opal.models import Patient
from elcid.utils import timing
from intrahospital_api import get_api
from intrahospital_api.exceptions import BatchLoadError
from intrahospital_api.constants import EXTERNAL_SYSTEM
from intrahospital_api import update_demographics
from intrahospital_api import update_lab_tests

api = get_api()
logger = logging.getLogger('intrahospital_api')


@timing
def initial_load():
    models.InitialPatientLoad.objects.all().delete()
    models.BatchPatientLoad.objects.all().delete()
    batch = models.BatchPatientLoad()
    batch.start()

    try:
        _initial_load()
    except:
        batch.failed()
        log_errors("initial_load")
        raise
    else:
        batch.complete()


def _initial_load():
    update_demographics.reconcile_all_demographics()
    # only run for reconciled patients
    patients = Patient.objects.filter(
        demographics__external_system=EXTERNAL_SYSTEM
    )
    total = patients.count()

    for iterator, patient in enumerate(patients.all()):
        logger.info("running {}/{}".format(iterator+1, total))
        load_patient(patient, async=False)


def log_errors(name):
    logger.error("unable to run {} \n {}".format(
        name, traceback.format_exc()
    ))


def any_loads_running():
    """
        returns a boolean as to whether batch loads are
        running, for use by things that synch databases
    """
    return models.BatchPatientLoad.objects.filter(
        state=models.BatchPatientLoad.RUNNING
    ).exists()


@timing
def load_demographics(hospital_number):
    started = timezone.now()
    try:
        result = api.demographics(hospital_number)
    except:
        stopped = timezone.now()
        logger.info("demographics load failed in {}".format(
            (stopped - started).seconds
        ))
        log_errors("load_demographics")
        return

    return result


def cancel_and_load(patients):
    """
    cancels an existing loads and kick off a new one asynchronously
    """
    ipls = models.InitialPatientLoad.objects.filter(patient__in=patients)
    ipls.update(state=models.InitialPatientLoad.CANCELLED)
    for patient in patients:
        load_patient(patient, async=False)


def load_patient(patient, async=None):
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
        async_task(patient, patient_load)
    else:
        _load_patient(patient, patient_load)


def async_task(patient, patient_load):
    from intrahospital_api import tasks
    tasks.load.delay(patient, patient_load)


def test_long_running_initial_loads():
    """
    Initial Patient Loads should take < 5 mins. If they take longer than
    10 mins I would like an email please
    """
    ipls = models.InitialPatientLoad.objects.filter(
        state=models.InitialPatientLoad.RUNNING
    )
    now = timezone.now()
    for ipl in ipls:
        diff = now - ipl.started
        if diff.seconds > 600:
            err_str = "Initial Patient Load {} has been running for {} seconds"
            err_str = err_str.format(ipl.id, diff.seconds)
            logger.error(err_str)


def good_to_go():
    """ Are we good to run a batch load, returns True if we should.
        runs a lot of sanity checks.
    """
    if not models.BatchPatientLoad.objects.all().exists():
        # an inital load is required via ./manage.py initial_test_load
        raise BatchLoadError(
            "We don't appear to have had an initial load run!"

        )

    # give us an email if any initial patient loads have been running
    # for a while
    test_long_running_initial_loads()

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
            logger.info(
                "batch still running after {} seconds, skipping".format(
                    time_ago.seconds
                )
            )
            return False
        else:
            if models.BatchPatientLoad.objects.all().count() == 1:
                # we expect the inital batch patient load to take ages
                # as its the first and runs the initial load
                # so cut it some slack
                logger.info(
                    "batch still running after {} seconds, but its the first \
load".format(time_ago.seconds)
                )
                return False
            else:
                raise BatchLoadError(
                    "Last load is still running and has been for {} mins".format(
                        time_ago.seconds/60
                    )
                )

    one_hour_ago = timezone.now() - datetime.timedelta(seconds=60 * 60)
    if models.BatchPatientLoad.objects.last().stopped < one_hour_ago:
        raise BatchLoadError("Last load has not run since {}".format(
            models.BatchPatientLoad.objects.last().stopped
        ))

    return True


def batch_load(force=False):
    all_set = None

    # validate that we can run without exception
    if not force:
        try:
            all_set = good_to_go()
        except:
            log_errors("batch load")

        if not all_set:
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


def get_batch_start_time():
    """
        we need to paper over the cracks.

        usually this just means get me everything since the start
        of the last successful batch run.

        ie batch A starts at 10:00 and finishes at 10:03
        batch B will get all data since 10:00 so that nothing is lost

        however...
        the batches exclude initial patient loads, but usually that's ok
        but we have extra cracks to paper over...

        a patient load starts during the batch A load, at 9:58. It finishes
        the db load from the upstream db at 9:59 but is still saving the data
        to our db at 10:00

        it is excluded from the batch A, so batch B goes and starts its run
        from 9:59 accordingly.

    """
    last_successful_run = models.BatchPatientLoad.objects.filter(
        state=models.BatchPatientLoad.SUCCESS
    ).order_by("started").last()

    long_patient_load = models.InitialPatientLoad.objects.filter(
        state=models.InitialPatientLoad.SUCCESS
    ).filter(
        started__lt=last_successful_run.started
    ).filter(
        stopped__gt=last_successful_run.started
    ).order_by("started").first()

    if long_patient_load:
        return long_patient_load.started
    else:
        return last_successful_run.started


@timing
def _batch_load():
    started = get_batch_start_time()

    # update the non reconciled
    update_demographics.reconcile_all_demographics()

    data_deltas = api.data_deltas(started)
    update_from_batch(data_deltas)


@transaction.atomic
def update_patient_from_batch(demographics_set, data_delta):
    upstream_demographics = data_delta["demographics"]
    patient_demographics_set = demographics_set.filter(
        hospital_number=upstream_demographics["hospital_number"]
    )
    if not patient_demographics_set.exists():
        # this patient is not in our reconcile list,
        # move on, nothing to see here.
        return

    patient = patient_demographics_set.first().patient
    update_demographics.update_patient_demographics(
        patient, upstream_demographics
    )
    update_lab_tests.update_tests(
        patient,
        data_delta["lab_tests"],
    )


@timing
def update_from_batch(data_deltas):
    # only look at patients that have been reconciled
    demographics_set = emodels.Demographics.objects.filter(
        external_system=EXTERNAL_SYSTEM
    )

    # ignore patients that have not had an existing patient load
    demographics_set = demographics_set.filter(
        patient__initialpatientload__state=models.InitialPatientLoad.SUCCESS
    )
    for data_delta in data_deltas:
        update_patient_from_batch(demographics_set, data_delta)


def async_load_patient(patient, patient_load):
    try:
        _load_patient(patient, patient_load)
    except:
        log_errors("_load_patient")
        raise


@transaction.atomic
def _load_patient(patient, patient_load):
    try:
        hospital_number = patient.demographics_set.first().hospital_number
        patient.labtest_set.filter(
            lab_test_type__in=[
                emodels.UpstreamBloodCulture.get_display_name(),
                emodels.UpstreamLabTest.get_display_name()
            ]
        ).delete()

        results = api.results_for_hospital_number(hospital_number)
        update_lab_tests.update_tests(patient, results)
        update_demographics.update_patient_demographics(patient)
    except:
        patient_load.failed()
        raise
    else:
        patient_load.complete()
