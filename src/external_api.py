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

    try:
        currency_amount = ["USD", "EUR"]

        if currency_from not in currency_amount:
            raise ValueError("Введены неверные данные")

        if not isinstance(amount, (int, float)):
            raise ValueError(f"Введены неверные данные")
    except ValueError:
        return "Введены неверные данные"

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"

    payload = {}
    headers = {"apikey": API_KEY}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    result: float = round(response_json['result'], 1)

    return result
