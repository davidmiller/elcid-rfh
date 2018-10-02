import datetime
import mock
from opal.core.test import OpalTestCase
from opal.core import serialization
from intrahospital_api.services.lab_tests.backends import dev


class DevApiTestCase(OpalTestCase):
    def setUp(self):
        self.api = dev.Api()

    def test_get_external_identifier(self):
        external_identifier = self.api.get_external_identifier()
        self.assertEqual(len(external_identifier), 9)

    def test_get_observation_value(self):
        some_val = self.api.get_observation_value("10 - 12")
        self.assertTrue(bool(some_val))
        self.assertTrue(isinstance(some_val, float))

    def test_cooked_lab_tests(self):
        cooked_lab_tests = self.api.cooked_lab_tests("q2343424")
        self.assertTrue(len(cooked_lab_tests) > 1)
        expected_fields = [
            'observation_value',
            'hospital_number',
            'units',
            'external_system',
            'reference_range',
            'observation_number',
            'last_updated',
            'observation_datetime',
            'observation_name',
        ]
        self.assertEqual(
            set(expected_fields), set(cooked_lab_tests[0].keys())
        )

    def test_raw_lab_tests(self):
        self.assertEqual(len(self.api.raw_lab_tests("2323441312")), 1)