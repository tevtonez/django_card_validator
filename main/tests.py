"""Unit tests for card validation number functionality."""
from django.test import TestCase, Client
import json


class TestApiEndpoint(TestCase):
    """Testing card number validation endpoint."""

    def assert_response(
        self,
        response,
        str_response,
        str_class
    ):
        """
        Assert response from the api endpoint.

        Takes response, expected message as a string 'str_response'
        and expected css class as a string 'str_class' then asserts api
        endpoint response.
        """
        response_dict = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_dict['result_class'], str_class)
        self.assertEqual(
            response_dict['result'],
            str_response
        )

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

        self.assert_response(
            self.response, 'Your card number is Valid.', 'success')

    def test_incorrect_num(self):
        """Unhappy path: card number is invalid."""
        self.response = self.client.post('/api/check_number/', {
            'card_number': self.invalid_card_number
        })

        self.assert_response(
            self.response, 'Entered card number is Invalid!', 'danger')

    def test_incorrect_input(self):
        """Unhappy path: non-integers input."""
        self.response = self.client.post('/api/check_number/', {
            'card_number': self.chars_input
        })

        self.assert_response(
            self.response, 'Please enter digits only.', 'danger')

    def test_empty_input(self):
        """Unhappy path: empty input."""
        self.response = self.client.post('/api/check_number/', {
            'card_number': self.empty_input
        })

        self.assert_response(
            self.response, 'Please enter a card number.', 'danger')
