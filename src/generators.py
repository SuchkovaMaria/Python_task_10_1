from typing import Union


def filter_by_currency(
    transactions: Union[list[dict[str, int, dict]]], valuta: Union[str]
) -> Union[list[dict[str, int]], str]:
    """Функция для фильтрации транзакций по указанной валюте"""

    list_dict_1 = []

    lenght_transactions = len(transactions)
    if lenght_transactions == 0:
        return ("Список транзакций пуст")
    else:
        for i_dict in transactions:
            for key, value in i_dict.items():
                if key == "operationAmount":
                    for key_oper, value_oper in value.items():
                        if key_oper == "currency":
                            for key_currency, value_currency in value_oper.items():
                                if key_currency == "name" and value_currency == valuta:
                                    list_dict_1.append(i_dict)
    if len(list_dict_1) == 0:
        return f"Отсутствуют транзакции с валютой - {valuta}"
    else:
        return  list_dict_1


def transaction_descriptions(transactions: Union[list[dict[str, int, dict]]]) -> Union[str]:
    """Функция для вывода описания транзакции"""
    try:
        lenght_transactions = len(transactions)
        if lenght_transactions != 0:
            for i_dict in transactions:
                for key, value in i_dict.items():
                    if key == "description":
                        yield value
        elif lenght_transactions == 0:
            yield "Список транзакций пуст"
    except StopIteration:
        yield "Итерации завершены"


def card_number_generator(start: Union[int], stop: Union[int]) -> Union[str]:
    """Генератор номеров карт"""

    try:
        if isinstance(start, int) == True and isinstance(stop, int) == True:
            if start < stop:
                for num in range(start, stop+1):
                    numbers = str(num).zfill(16)
                    num_card = numbers[:4] + " " + numbers[4:8] + " " + numbers[8:12] + " " + numbers[12:]
                    yield num_card
            else:
                yield "Начальное значение должно быть меньше конечного"
        else:
            yield "Введите целые числа"
    except StopIteration:
        yield "Итерации завершены"


