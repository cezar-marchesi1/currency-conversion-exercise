"""
Views for the Currency Conversion API
"""
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from currency_conversion.serializers import CurrencyConversionSerializer
from .helpers import convert_currency


class CurrencyConversionView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CurrencyConversionSerializer(data=request.query_params)
        
        if serializer.is_valid():
            from_currency = serializer.validated_data['from_currency']
            to_currency = serializer.validated_data['to_currency']
            amount = serializer.validated_data['amount']
            
            result = convert_currency(
                amount=amount,
                from_currency=from_currency,
                to_currency=to_currency
            )
            

            data = {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "result": result,
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
