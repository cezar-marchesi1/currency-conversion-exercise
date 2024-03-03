import os
from dotenv import load_dotenv

from currencyapicom import Client


load_dotenv()

api_key = os.getenv("CURRENCY_API_KEY")

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Converts an amount from one currency to another using the latest exchange rates
    using the API Client provided by currencyapi.com.
    
    Args:
        amount (float): The amount to be converted.
        from_currency (str): The currency code of the original amount.
        to_currency (str): The currency code to which the amount should be converted.
    
    Returns: float
    """
    client = Client(api_key)
    rates = client.latest(from_currency, [to_currency])

    result = amount * rates.get("data").get(to_currency).get("value")
    
    return result
