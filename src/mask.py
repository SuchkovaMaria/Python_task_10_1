from typing import Union


def get_mask_account(number_account: Union[str]) -> Union[str]:
    """Функция маскирует номер счета"""

    new_number_account = []
    mask_number_account = []

    if number_account.isalpha() == False:
        for number in number_account:
            new_number_account.append(number)

        lenght_new_number_account = len(new_number_account)
        if lenght_new_number_account == 20:
            for num in range(len(new_number_account)):
                index_num = num
                if 14 <= index_num <= 15:
                    mask_number_account.append("*")
                elif index_num >= 16:
                    mask_number_account.append(new_number_account[num])
            mask_number_account_str = "".join(mask_number_account)
            return mask_number_account_str
        else:
            return "Невернно введены данные"
    else:
        return "Введен неверный номер счета"


def get_mask_card_number(number_card: Union[str]) -> Union[str]:
    """Функция маскирует номер карты"""

    new_number_card = []
    mask_card_number = []
    count = 0

    if number_card.isalpha() == False:
        lenght_number_card = len(number_card)
        if lenght_number_card == 16:
            for number in number_card:
                new_number_card.append(number)

            new_number_card.insert(4, " ")
            new_number_card.insert(9, " ")
            new_number_card.insert(14, " ")

            for num_card in new_number_card:
                if num_card != " ":
                    if count < 7:
                        mask_card_number.append(num_card)
                        count += 1
                    elif 7 <= count <= 13:
                        mask_card_number.append("*")
                        count += 1
                    elif count > 14:
                        mask_card_number.append(num_card)
                elif num_card == " ":
                    mask_card_number.append(num_card)
                    count += 1
            mask_card_number_str = "".join(mask_card_number)
            return mask_card_number_str
        else:
            return "Невернно введены данные"
    else:
        return "Введен неверный номер карты"


