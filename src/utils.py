import json
import logging
import os

os.chdir(r'C:\\Users\\Rabota\\PycharmProjects\\Python_task')
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler_utils = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter_utils = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler_utils.setFormatter(file_formatter_utils)
logger.addHandler(file_handler_utils)


def convertions_json_in_list(path_to_file):
    """Функция получения списка транзакций из файла json"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            file_operations = file.read()
        logger.debug(f'Функция открыла файл по  пути: {path_to_file}')
        list_transactions = json.loads(file_operations)
        logger.info('Данные из файла переведены в Python-объект')
    except FileNotFoundError:
        logger.error('Файл не найден')
        print("Файл не найден")
        list_transactions = []
        return list_transactions
    if isinstance(list_transactions, list) is False:
        logger.info(f'Данные в файле {list_transactions} не являются списком')
        list_transactions = []
    elif list_transactions == []:
        logger.info(f'Список {list_transactions} пуст')
        list_transactions = []
    logger.debug('Функция возвращает список транзакций')
    return list_transactions
