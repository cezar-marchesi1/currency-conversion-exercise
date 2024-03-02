from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from unittest.mock import patch


class HelpersTests(TestCase):
    def setUp(self):
        pass

    def test_helpers(self):
        self.assertTrue(True)