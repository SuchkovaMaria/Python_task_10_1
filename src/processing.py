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
        return "В списке отсутствует нужный статус"
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
        return "Отсутствуют даты"

    for dict_i in list_of_dict:
        for key, value in dict_i.items():
            if key == "date" and value[0] == "T":
                return "Невернно введены данные"

    sort_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_order)
    return sort_list
