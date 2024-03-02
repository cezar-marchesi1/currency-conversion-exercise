import currencyapicom
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("CURRENCY_API_KEY")

def convert_currency(amount, from_currency, to_currency):
    client = currencyapicom.Client(api_key)
    rates = client.latest(from_currency, [to_currency])
    
    result = float(amount) * rates.get("data").get(to_currency).get("value")
    
    return result
