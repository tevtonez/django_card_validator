"""Unit tests for card validation number functionality."""
from django.test import TestCase, Client
import json


class TestApiEndpoint(TestCase):
    """Testing card number validation endpoint."""

    def setUp(self):
        """Test setup."""
        self.client = Client()
        self.valid_card_number = '349489219405037'
        self.invalid_card_number = '349489219405039'
        self.chars_input = 'abc234543636'
        self.empty_input = ''

    def test_correct_num(self):
        """Happy path: card number is valid."""
        self.response = self.client.post('/api/check_number/', {
            'card_number': self.valid_card_number
        })

        response_dict = json.loads(self.response.content.decode("utf-8"))

        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(response_dict['result_class'], 'success')
        self.assertEqual(
            response_dict['result'],
            'Your card number is Valid.'
        )

    def test_incorrect_num(self):
        """Unhappy path: card number is invalid."""
        self.response = self.client.post('/api/check_number/', {
            'card_number': self.invalid_card_number
        })

        response_dict = json.loads(self.response.content.decode("utf-8"))

        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(response_dict['result_class'], 'danger')
        self.assertEqual(
            response_dict['result'],
            'Entered card number is Invalid!'
        )

    def test_incorrect_input(self):
        """Unhappy path: non-integers input."""
        self.response = self.client.post('/api/check_number/', {
            'card_number': self.chars_input
        })

        response_dict = json.loads(self.response.content.decode("utf-8"))

        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(response_dict['result_class'], 'danger')
        self.assertEqual(
            response_dict['result'],
            "Please enter digits only."
        )

    def test_empty_input(self):
        """Unhappy path: empty input."""
        self.response = self.client.post('/api/check_number/', {
            'card_number': self.empty_input
        })

        response_dict = json.loads(self.response.content.decode("utf-8"))

        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(response_dict['result_class'], 'danger')
        self.assertEqual(
            response_dict['result'],
            "Please enter card number."
        )
