import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_1(transactions_1):
    assert next(filter_by_currency(transactions_1, "USD")) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_filter_by_currency_2(transactions_2):
    assert next(filter_by_currency(transactions_2, "USD")) == "Отсутствуют транзакции с валютой - USD"


def test_filter_by_currency_3():
    assert next(filter_by_currency([], "USD")) == "Список транзакций пуст"


def test_transaction_descriptions_1(transactions_3):
    assert next(transaction_descriptions(transactions_3)) == "Перевод организации"


def test_transaction_descriptions_2():
    assert next(transaction_descriptions([])) == "Список транзакций пуст"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, "0000 0000 0000 0001"),
        (6, 1, "Начальное значение должно быть меньше конечного"),
        ("1", 3, "Введите целые числа"),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert next(card_number_generator(start, stop)) == expected
