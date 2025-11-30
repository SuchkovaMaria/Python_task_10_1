from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


def test_filter_by_currency_1(transactions_1):
    assert filter_by_currency(transactions_1, "USD") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_filter_by_currency_2(transactions_2):
    assert filter_by_currency(transactions_2, "USD") == "Отсутствуют транзакции с валютой - USD"


def test_filter_by_currency_3():
    assert filter_by_currency([], "USD") == "Список транзакций пуст"


def test_transaction_descriptions_1(transactions_3):
    assert next(transaction_descriptions(transactions_3)) == "Перевод организации"


def test_transaction_descriptions_2():
    assert next(transaction_descriptions([])) == "Список транзакций пуст"


def test_card_number_generator_1():
    assert next(card_number_generator(1, 5)) == "0000 0000 0000 0001"


def test_card_number_generator_2():
    assert next(card_number_generator(6, 1)) == "Начальное значение должно быть меньше конечного"


def test_card_number_generator_3():
    assert next(card_number_generator("1", 3)) == "Введите целые числа"
