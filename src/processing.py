from typing import Union


def filter_by_state(list_of_dict: Union[list], entered_state: Union[str] = "EXECUTED") -> Union[list]:
    """Функуия фильтрует список словарей и выводет выполненые"""
    filter_list = []
    for i_list in list_of_dict:
        for key, value in i_list.items():
            if key == "state" and value == entered_state:
                filter_list.append(i_list)
    return filter_list


def sort_by_date(list_of_dict: Union[list], sort_order: Union[bool] = True) -> Union[list]:
    """Функция сортирует список словарей по дате"""
    sort_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_order)
    return sort_list

print(sort_by_date(1,2,))