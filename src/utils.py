import json
import logging
import os

current_dir = os.path.dirname(__file__)
absolute_path = os.path.join(current_dir, "..")
os.chdir(absolute_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler_utils = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter_utils = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler_utils.setFormatter(file_formatter_utils)
logger.addHandler(file_handler_utils)


def convertions_json_in_list(path_to_file):
    """Функция получения списка транзакций из файла json"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            list_transactions = json.load(file)
        logger.info("Данные из файла загружены в Python-объект")
        data_transactions = []
        for transaction in list_transactions:
            amount = transaction.get('operationAmount', {}).get('amount')
            currency_name = transaction.get('operationAmount', {}).get('currency', {}).get('name')
            currency_code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
            data_transactions.append({
                'id': transaction.get("id"), 'state': transaction.get("state"),
                'date': transaction.get("date"), 'amount': amount,
                'currency_name': currency_name,
                'currency_code': currency_code,
                'from': transaction.get("from"), 'to': transaction.get("to"),
                'description': transaction.get("description")})

    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Файл не найден")
        data_transactions = []
        return data_transactions
    if isinstance(data_transactions, list) is False:
        logger.info(f"Данные в файле {data_transactions} не являются списком")
        data_transactions = []
    elif data_transactions == []:
        logger.info(f"Список {data_transactions} пуст")
        data_transactions = []
    logger.debug("Функция возвращает список транзакций")
    return data_transactions
