from unittest.mock import Mock, patch

import requests

from src.external_api import convertions_currency, convertions_currency_transaction


def test_convertions_currency_transaction_1(transactions_to_api_1):
    assert convertions_currency_transaction(transactions_to_api_1) == 31957.58


# Альтернативный вариант @patch для функции convertions_currency (необходимо указывать путь к функции)
# @patch("src.external_api.convertions_currency", return_value=321.1)
# def test_convertions_currency_transaction_2(transactions_to_api_2):
# assert convertions_currency_transaction(transactions_to_api_2) == 321.1


@patch("src.external_api.convertions_currency")  # в @patch необходимо указывать путь к функции
def test_convertions_currency_transaction_2(mock_conv, transactions_to_api_2):
    mock_conv.return_value = 321.1
    assert convertions_currency_transaction(transactions_to_api_2) == 321.1


def test_convertions_currency_3():
    with patch("requests.get") as mock_conv:
        mock_conv.return_value.json.return_value = {"result": 321.1}
        result = convertions_currency("USD", "8221.37")
        assert result == 321.1

