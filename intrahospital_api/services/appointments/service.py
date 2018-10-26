import datetime
from django.utils import timezone
from opal.models import Patient
from opal.core import serialization
from elcid import models as elcid_models
from apps.tb.episode_categories import TbEpisode
from intrahospital_api.services.base import service_utils, db
from intrahospital_api.constants import EXTERNAL_SYSTEM
from intrahospital_api.services.base import load_utils
from apps.tb.episode_categories import TbEpisode
from apps.tb.patient_lists import TbPatientList


def refresh_patient(patient):
    if patient.episode_set.filter(
        category_name=TbEpisode.display_name
    ).exists():
        patient.appointment_set.all().delete()
        load_patient(patient)


def load_patient(patient):
    api = service_utils.get_api("appointments")
    appointments = api.tb_appointments_for_hospital_number(
        patient.demographics_set.first().hospital_number
    )
    save_appointments(patient, appointments)


def has_changed(appointment, appointment_dict):
    """
    Returns True if an appointment has changed
    """
    for key in appointment_dict.keys():
        model_value = getattr(appointment, key)
        if isinstance(model_value, datetime.datetime):
            model_value = db.to_datetime_str(model_value)
        elif isinstance(model_value, datetime.date):
            model_value = db.to_date_str(model_value)

        if not model_value == appointment_dict[key]:
            return True
    return False


def save_appointments(patient, appointment_dicts):
    user = service_utils.get_user()
    for appointment_dict in appointment_dicts:
        appointment, is_new = get_or_create_appointment(
            patient, appointment_dict
        )
        if is_new or has_changed(appointment, appointment_dict):
            appointment.update_from_api_dict(appointment_dict, user)


def get_or_create_appointment(patient, appointment_dict):
    start = serialization.deserialize_datetime(
            appointment_dict["start"]
    )
    appointment = patient.appointment_set.filter(
        start=start
    ).first()

    if appointment:
        return appointment, False
    else:
        return elcid_models.Appointment(patient=patient), True


def load_patients():
    """
    Loads in all appointments for all patients with the category of tb
    """
    patients = Patient.objects.filter(
        episode__category_name=TbEpisode.display_name
    )

    for patient in patients:
        load_patient(patient)


# not an invalid, name, its not a constant, seperate out
# for testing purposes
# pylint: disable=invalid-name
batch_load = load_utils.batch_load(
    service_name="appointments"
)(
    load_patients
)
