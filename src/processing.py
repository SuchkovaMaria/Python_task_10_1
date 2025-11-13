from typing import Union


def filter_by_state(list_of_dict: Union[list], entered_state: Union[str]="EXECUTED") -> Union[list]:
    """Функуия фильтрует список словарей и выводет выполненые"""
    filter_list = []
    for i_list in list_of_dict:
        for key, value in i_list.items():
            if key == "state" and value == entered_state:
                filter_list.append(i_list)
    return filter_list


def sort_by_date(list_of_dict: Union[list], sort_order: Union[bool]=True) -> Union[list]:
    """Функция сортирует список словарей по дате"""
    sort_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_order)
    return sort_list


x = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
    False,
)
print(x)
