from unittest.mock import Mock, patch

import requests

from src.external_api import convertions_currency, convertions_currency_transaction


def test_convertions_currency_transaction_1(transactions_to_api_1):
    assert convertions_currency_transaction(transactions_to_api_1) == 31957.58


@patch("src.external_api.convertions_currency", return_value=321.1)
def test_convertions_currency_transaction_2(transactions_to_api_2):
    assert convertions_currency_transaction(transactions_to_api_2) == 321.1


def test_convertions_currency_1():
    assert convertions_currency("USS", "8221.37") == "Введены неверные данные"


def test_convertions_currency_2(transactions_to_api_3, transactions_to_api_4):
    assert convertions_currency(transactions_to_api_3, transactions_to_api_4) == "Введены неверные данные"


def test_convertions_currency_3(response_1):
    mock_response = Mock()
    mock_response.json = Mock(return_value=response_1)
    requests.request = Mock(return_value=mock_response)
    assert convertions_currency("USD", 8221.37) == 655053.8
    mock_response.json.assert_called_once()
