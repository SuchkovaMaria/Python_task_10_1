import os

from src.generators import filter_by_currency
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.reading_operations import reading_fin_operations_csv, reading_fin_operations_xlsx
from src.utils import convertions_json_in_list
from src.widget import get_date, mask_account_card

BASE_DIR = os.path.dirname(__file__)
answer_options = {"1": convertions_json_in_list, "2": reading_fin_operations_csv, "3": reading_fin_operations_xlsx}
path_options = {
    "1": BASE_DIR + "/data/operations.json",
    "2": BASE_DIR + "/data/transactions.csv",
    "3": BASE_DIR + "/data/transactions_excel.xlsx",
}
message_options = {
    "1": "Для обработки выбран JSON-файл",
    "2": "Для обработки выбран CSV-файл",
    "3": "Для обработки выбран XLSX-файл",
}
status = ["EXECUTED", "CANCELED", "PENDING"]


def main():

    transaction = []
    while True:
        users_input_1 = input(
            "Программа: Привет! Добро пожаловать в программу работы\n"
            "с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        get_func = answer_options.get(users_input_1)
        if get_func:
            print(message_options.get(users_input_1))
            path = path_options.get(users_input_1)
            transaction = get_func(path)
            break
    while True:
        users_input_2 = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {','.join(status)}\n"
        ).upper()
        if users_input_2 in status:
            transaction = filter_by_state(transaction, users_input_2)
            print(f"Операции отфильтрованы по статусу '{users_input_2}'")
            break
        else:
            print(f"Статус операции '{users_input_2}' недоступен")

    users_input_3 = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if users_input_3 == "да":
        users_input_3_1 = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if users_input_3_1 == "по убыванию":
            transaction = sort_by_date(transaction)
        elif users_input_3_1 == "по возрастанию":
            transaction = sort_by_date(transaction, False)
        else:
            print(f"{users_input_3_1} недоступен")

    users_input_4 = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if users_input_4 == "да":
        transaction = list(filter_by_currency(transaction, "RUB"))

    users_input_5 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if users_input_5 == "да":
        users_input_5_1 = input("Введите слово для сортировки:\n")
        transaction = filter_by_description(transaction, users_input_5_1)
    if len(transaction) == 0 or len(transaction[0]) == 0:
        print("операций не найдено")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transaction)}")
        for transac in transaction:
            print(transac)
            date = get_date(transac.get("date"))
            amount = transac.get("amount")
            currency_name = transac.get("currency_name")
            to_from = transac.get("from")
            to = mask_account_card(transac.get("to"))
            description = transac.get("description")

            esc_print = f"{date} {description}"
            account_from = mask_account_card(to_from) if to_from else "" + " -> "
            account_to = f"{to}"
            sum_print = f"Сумма: {amount} {currency_name}"

            print(f"{esc_print}\n{account_from} {account_to}\n{sum_print}")


if __name__ == "__main__":
    main()
