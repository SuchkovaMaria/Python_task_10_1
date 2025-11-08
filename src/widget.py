from typing import Union
from mask import get_mask_account, get_mask_card_number


def mask_account_card(card: Union[str]) -> Union[str]:
    """Функция для маскировки счета или карты"""

    name_card = []
    list_card = card.split(sep=" ", maxsplit=3)
    for element in list_card:
        if element.isdigit() is True:
            number_card = element
        else:
            name_card.append(element)

    lenght_number_card = len(number_card)

    if lenght_number_card > 16:
        mask_number_card = get_mask_account(number_card)
    else:
        mask_number_card = get_mask_card_number(number_card)

    full_name_card = " ".join(name_card)

    return f"{full_name_card} {mask_number_card}"


def get_date(date_time: Union[str]) -> Union[str]:
    """Функция для вывода даты"""

    separation_date_time = date_time.split(sep="T", maxsplit=1)
    reverse_date = separation_date_time[0].split(sep="-", maxsplit=3)
    coup_date = reverse_date[::-1]
    date = ".".join(coup_date)

    return date
