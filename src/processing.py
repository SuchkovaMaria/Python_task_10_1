import re
from collections import Counter
from typing import Union


def filter_by_state(
    list_of_dict: Union[list[dict[str, int]]], entered_state: Union[str] = "EXECUTED"
) -> Union[list[dict[str, int]]]:
    """Функуия фильтрует список словарей и выводет выполненые (по умолчанию выводит со статусом ВЫПОЛНЕНО)"""
    filter_list = []
    for i_list in list_of_dict:
        for key, value in i_list.items():
            if key == "state" and value == entered_state:
                filter_list.append(i_list)
    if filter_list == []:
        print("В списке отсутствует нужный статус")
        return filter_list
    else:
        return filter_list


def sort_by_date(
    list_of_dict: Union[list[dict[str, int]]], sort_order: Union[bool] = True
) -> Union[list[dict[str, int]]]:
    """Функция сортирует список словарей по дате (по умолчанию фильтрует по убыванию даты)"""

    count = 0
    lenght_list = len(list_of_dict)

    for dict_i in list_of_dict:
        if "date" in dict_i:
            count += 1

    if lenght_list != count:
        print("Отсутствуют даты")
        return []

    for dict_i in list_of_dict:
        for key, value in dict_i.items():
            if key == "date" and value[0] == "T":
                print("Невернно введены данные")
                return []

    sort_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_order)
    return sort_list


def filter_by_description(
    list_of_dict: Union[list[dict[str, int]]], circumscribing: str
) -> Union[list[dict[str, int]]]:
    """Функция фильтрации списка словарей по описанию (description)"""

    filter_list_by_description = []
    if circumscribing == "" or circumscribing == " ":
        print("неверное слово")
        filter_list_by_description = []
    else:
        pattern = re.compile(rf"{circumscribing}", re.IGNORECASE)
        for dict_i in list_of_dict:
            if pattern.search(dict_i.get("description", "")):

                filter_list_by_description.append(dict_i)
        if len(filter_list_by_description) == 0:
            print("Операций не найдено")
    return filter_list_by_description


def counting_categories(list_of_dict):
    """Функция подсчета операций по статусу"""
    counted = dict(Counter([i["state"] for i in list_of_dict]))
    return counted
