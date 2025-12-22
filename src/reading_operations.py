import csv
import pandas as pd


def reading_fin_operations_csv(path_to_file):
    """Функция для считывания финансовых операций из файла csv"""

    list_dict_transactions = []
    try:
        with open(path_to_file, encoding="utf--8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                list_dict_transactions.append(row)
    except FileNotFoundError as e:
        print(e)
    return list_dict_transactions


def reading_fin_operations_xlsx(path_to_file):
    """Функция для считывания финансовых операций из файла .xlsx"""

    try:
        excel_data = pd.read_excel(path_to_file)
        list_dict_transactions = excel_data.to_dict(orient="records")
    except FileNotFoundError:
        list_dict_transactions = {}
        print("Возникла ошибка: файл не найден")
    except Exception as ex:
        list_dict_transactions = {}
        print(f"Возникла ошибка: {ex}")
    return list_dict_transactions
