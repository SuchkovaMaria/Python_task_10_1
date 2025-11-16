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
    return filter_list


def sort_by_date(
    list_of_dict: Union[list[dict[str, int]]], sort_order: Union[bool] = True
) -> Union[list[dict[str, int]]]:
    """Функция сортирует список словарей по дате (по умолчанию фильтрует по убываю даты)"""
    sort_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_order)
    return sort_list
