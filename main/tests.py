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
