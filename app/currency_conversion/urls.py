"""
URL mappings for the Currency Conversion API.
"""

from django.urls import path
from .views import CurrencyConversionView


app_name = 'currency_conversion'

urlpatterns = [
    path('convert/', CurrencyConversionView.as_view(), name='currency-conversion'),
]
