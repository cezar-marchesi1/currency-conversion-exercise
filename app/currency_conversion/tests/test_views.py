from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch


currency_conversion_endpoint = "/api/currency_conversion/convert/"

class CurrencyConversionViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('currency_conversion.views.convert_currency')
    def test_successful_conversion(self, mock_convert_currency):
        """
        Test for successful request.
        convert_currency method is mocked
        """
        mock_convert_currency.return_value = {
            "from_currency": "USD",
            "to_currency": "BRL",
            "result": 9
        }
        params = {'from_currency': 'USD', 'to_currency': 'BRL', 'amount': 100}
        response = self.client.get(currency_conversion_endpoint, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['from_currency'], 'USD')
        self.assertEqual(response.data['to_currency'], 'BRL')
        self.assertIsNotNone(response.data['result'])
        mock_convert_currency.assert_called_once_with(
            amount=params['amount'],
            from_currency=params['from_currency'],
            to_currency=params['to_currency']
        )


    @patch('currency_conversion.views.convert_currency')
    def test_invalid_currency(self, mock_convert_currency):
        """
        Test for invalid currency.
        """
        mock_convert_currency.side_effect = Exception("Something went wrong")

        params = {'from_currency': 'USD', 'to_currency': 'XYZ', 'amount': 100}
        response = self.client.get(currency_conversion_endpoint, params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        mock_convert_currency.assert_called_once_with(
            amount=params['amount'],
            from_currency=params['from_currency'],
            to_currency=params['to_currency']
        )


    def test_missing_argument(self):
        """
        Test for missing argument.
        """
        params = {'from_currency': 'USD', 'to_currency': 'BRL'}  # 'amount' is missing
        response = self.client.get(currency_conversion_endpoint, params)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('amount', response.data)
