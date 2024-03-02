from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from unittest.mock import patch


class CurrencyConversionViewTests(TestCase):
    def setUp(self):
        pass

    def test_view(self):
        self.assertTrue(True)