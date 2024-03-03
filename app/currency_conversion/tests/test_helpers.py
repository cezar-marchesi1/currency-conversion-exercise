from django.test import TestCase
from currency_conversion import helpers

from unittest.mock import patch, Mock


class HelpersTests(TestCase):    

    @patch('currency_conversion.helpers.Client')
    def test_convert_currency_is_successful(self, mock_client):
        mock_rates = {
            "data": {
                "BRL": {"value": 4.5}
            }
        }
     
        mock_client_instance = Mock()
        mock_client_instance.latest.return_value = mock_rates
        mock_client.return_value = mock_client_instance

        result = helpers.convert_currency(100, "USD", "BRL")

        self.assertEqual(result, 450.0)
