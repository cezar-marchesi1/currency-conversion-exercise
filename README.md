# currency-conversion-exercise
Django exercise to convert currencies using the [currencyapi.com](https://currencyapi.com/)

By passing the original currency, target currency and an amount to be converted it will return a json with the result.
#
# Endpoint
# Currency conversion

|Method|Endpoint                            | Resource                      |
|------|------------------------------------|-------------------------------|
|GET   |`/api/currency_conversion/convert/` | Return converted amount       |

#### Example:
```
/api/currency_conversion/convert?from_currency=USD&to_currency=BRL&amount=1
```

### Result example:
```json
{
    "from_currency": "USD",
    "to_currency": "BRL",
    "result": 4.9527108667
}
```

## Usage

To use the application you will need your own api key provided by the Currency Conversion API. You can get it [here](https://currencyapi.com/) for free.

Create a `.env` file inside `/app` containing the API Key - There's a [`.env_example`](app/.env_example) with the correct variable name that must be used.

Run `docker-compose up -d` to get the application running.

Run `docker-compose run --rm app sh -c "python manage.py test"` to run tests.