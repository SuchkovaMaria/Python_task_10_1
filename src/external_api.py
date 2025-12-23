import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")

def convertions_currency_transaction(transaction):
    """Функция возвращающая сумму транзакции в рублях (при необходимости осуществляет конвертацию валюты)"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        result_amount = float(transaction.get("operationAmount").get("amount"))
    else:
        now_currency = transaction.get("operationAmount").get("currency").get("code")
        now_amount = float(transaction.get("operationAmount").get("amount"))
        result_amount = convertions_currency(now_currency, now_amount)
    return result_amount

def convertions_currency(currency_from, amount):
    """ Функция конвертации валюты в рубли """

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"

    headers = {"apikey": os.getenv('API_KEY')}

    response = requests.get(url, headers=headers, data={})

    return response.json().get("result")
