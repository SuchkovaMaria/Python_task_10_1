import logging
import os
from typing import Union

current_dir = os.path.dirname(__file__)
absolute_path = os.path.join(current_dir, "..")
os.chdir(absolute_path)
logger = logging.getLogger("mask")
logger.setLevel(logging.DEBUG)
file_handler_mask = logging.FileHandler("logs/mask.log", mode="w", encoding="utf-8")
file_formatter_mask = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler_mask.setFormatter(file_formatter_mask)
logger.addHandler(file_handler_mask)


def get_mask_account(number_account: Union[str]) -> Union[str]:
    """Функция маскирует номер счета"""

    new_number_account = []
    mask_number_account = []
    logger.debug("Созданы пустые вспомогательные списки: new_number_account, mask_number_account")

    try:
        if number_account.isalpha() is False:
            logger.debug("Номер счета не содержит букв")
            for number in number_account:
                new_number_account.append(number)

            lenght_new_number_account = len(new_number_account)
            logger.debug("Маскировка номера счета")
            if lenght_new_number_account == 20:
                for num in range(len(new_number_account)):
                    index_num = num
                    if 14 <= index_num <= 15:
                        mask_number_account.append("*")
                    elif index_num >= 16:
                        mask_number_account.append(new_number_account[num])
                mask_number_account_str = "".join(mask_number_account)
                logger.info("Вывод замаскированного номера счета")
                return mask_number_account_str
            else:
                logger.debug("Вывод сообщения о неверно введенных данных")
                return "Невернно введены данные"
        else:
            logger.debug("Вывод сообщения о неверно введенного номер счета")
            return "Введен неверный номер счета"
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


def get_mask_card_number(number_card: Union[str]) -> Union[str]:
    """Функция маскирует номер карты"""

    new_number_card = []
    mask_card_number = []
    logger.debug("Созданы пустые вспомогательные списки: new_number_card, mask_card_number")
    count = 0
    logger.debug("Обнуление счетчика count")

    try:
        if number_card.isalpha() is False:
            logger.debug("Номер карты не содержит букв")
            lenght_number_card = len(number_card)
            if lenght_number_card == 16:
                logger.debug("Маскировка номера карты")
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
                logger.info("Вывод замаскированного номера карты")
                return mask_card_number_str
            else:
                logger.debug("Вывод сообщения о неверно введенных данных")
                return "Невернно введены данные"
        else:
            logger.debug("Вывод сообщения о неверно введенного номера карты")
            return "Введен неверный номер карты"
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
