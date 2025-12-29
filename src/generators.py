from collections.abc import Generator, Iterator
from typing import Union


def filter_by_currency(
    transactions: Union[list[dict]], valuta: Union[str]
) -> Iterator:
    """Функция для фильтрации транзакций по указанной валюте"""

    try:
        lenght_transactions = len(transactions)
        if lenght_transactions == 0:
            raise ValueError("Список транзакций пуст")
        else:
            for i_dict in transactions:
                for key, value in i_dict.items():
                    if key == "currency_code" and value == valuta:
                        yield i_dict
    except Exception:
        yield {}


def transaction_descriptions(transactions) :
    """Функция для вывода описания транзакции"""

    try:
        lenght_transactions = len(transactions)
        if lenght_transactions == 0:
            raise ValueError("Список транзакций пуст")

        lenght_transactions = len(transactions)
        if lenght_transactions != 0:
            for i_dict in transactions:
                for key, value in i_dict.items():
                    if key == "description":
                        yield value
    except ValueError:
        yield "Список транзакций пуст"
    except StopIteration:
        yield ""


def card_number_generator(start: Union[int], stop: Union[int]) -> Union[Generator[str, None, None]]:
    """Генератор номеров карт"""

    try:
        if isinstance(start, int) is True and isinstance(stop, int) is True:
            if start < stop:
                for num in range(start, stop + 1):
                    numbers = str(num).zfill(16)
                    num_card = numbers[:4] + " " + numbers[4:8] + " " + numbers[8:12] + " " + numbers[12:]
                    yield num_card
            else:
                yield "Начальное значение должно быть меньше конечного"
        else:
            yield "Введите целые числа"
    except StopIteration:
        yield "Итерации завершены"
