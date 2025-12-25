import json


def convertions_json_in_list(path_to_file):
    """Функция получения списка транзакций из файла json"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            file_operations = file.read()
        list_transactions = json.loads(file_operations)
    except FileNotFoundError:
        print("Файл не найден")
        list_transactions = []
        return list_transactions
    if isinstance(list_transactions, list) is False:
        list_transactions = []
    elif list_transactions == []:
        list_transactions = []
    return list_transactions
