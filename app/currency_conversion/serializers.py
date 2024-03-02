"""
Serializers for the Currency Conversion API View
"""

from rest_framework import serializers


class CurrencyConversionSerializer(serializers.Serializer):
    from_currency = serializers.CharField(max_length=3, required=True)
    to_currency = serializers.CharField(max_length=3, required=True)
    amount = serializers.DecimalField(max_digits=20, decimal_places=2, required=True)
