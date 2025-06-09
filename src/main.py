import re

from src.csv_pd_converter import csv_to_list_of_dicts, excel_to_list_of_dicts
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reg_exp import reg_proc_search
from src.utils import json_to_list
from src.widget import get_date


def main():
    success_proc_choice = False
    transactions_data = []
    while not success_proc_choice:

        file_type = int(
            input(
                """Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:
                    1. Получить информацию о транзакциях из JSON-файла
                    2. Получить информацию о транзакциях из CSV-файла
                    3. Получить информацию о транзакциях из XLSX-файла\n"""
            )
        )
        if file_type == 1:
            print("Для обработки выбран JSON-файл.")
            transactions_data = json_to_list("../data/operations.json")
            success_proc_choice = True
        elif file_type == 2:
            print("Для обработки выбран CSV-файл.")
            transactions_data = csv_to_list_of_dicts("../data/transactions.csv")
            success_proc_choice = True
        elif file_type == 3:
            print("Для обработки выбран XLSX-файл.")
            transactions_data = excel_to_list_of_dicts("../data/transactions_excel.xlsx")
            success_proc_choice = True
        else:
            print("Неверный ввод варианта обработки!")
            success_proc_choice = False
    success_status_choice = False
    while not success_status_choice:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
        )
        trans_status = str(input())
        if trans_status.upper() == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            transactions_data = filter_by_state(transactions_data, "EXECUTED")
            success_status_choice = True
        elif trans_status.upper() == "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"')
            transactions_data = filter_by_state(transactions_data, "CANCELED")
            success_status_choice = True
        elif trans_status.upper() == "PENDING":
            print('Операции отфильтрованы по статусу "PENDING"')
            transactions_data = filter_by_state(transactions_data, "PENDING")
            success_status_choice = True
        else:
            print("Выбранный статус недоступен, выберите другой статус!")
            success_status_choice = False

    success_date_filter_choice = False
    while not success_date_filter_choice:
        print("Отсортировать операции по дате? Да/Нет")
        date_filter = str(input())
        if date_filter.lower() == "да":
            success_date_filter_choice = True
        elif date_filter.lower() == "нет":
            success_date_filter_choice = True
        else:
            print("Неверный ввод! Попробуйте ещё раз")
            success_date_filter_choice = False
    date_ascending = False
    ascending_choice = False
    while not ascending_choice:
        print("Отсортировать по возрастанию или по убыванию?")
        asc = str(input())
        if asc.lower() == "по возрастанию":
            ascending_choice = True
            date_ascending = True
        elif asc.lower() == "по убыванию":
            ascending_choice = True
            date_ascending = False
        elif asc.lower() == "нет":
            ascending_choice = True
        else:
            print("Неверный ввод! Попробуйте ещё раз")
            ascending_choice = False

    transactions_data = sort_by_date(transactions_data, date_ascending)

    ruble_choice = False
    while not ruble_choice:
        print("Выводить только рублёвые транзакции? Да/Нет")
        ruble_or_not = str(input())
        if ruble_or_not.lower() == "да":
            ruble_choice = True
            transactions_data = list(filter_by_currency(transactions_data, "RUB"))
        elif ruble_or_not.lower() == "нет":
            ruble_choice = True
        else:
            print("Неверный ввод! Попробуйте ещё раз")
            ruble_choice = False

    query_choice = False
    while not query_choice:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        query_search = str(input())
        if query_search.lower() == "да":
            query_phrase = str(input("Введите слово или фразу для поиска:"))
            transactions_data = reg_proc_search(transactions_data, query_phrase, True, re.IGNORECASE)
            query_choice = True

        elif query_search.lower() == "нет":
            query_choice = True
        else:
            print("Неверный ввод! Попробуйте ещё раз")
            query_choice = False
    if not transactions_data:
        print("""Не найдено ни одной транзакции, подходящей под ваши условия фильтрации""")
        return transactions_data
    trans_count = len(transactions_data)

    print(f"Всего банковских операций в выборке: {trans_count}")
    for trans in transactions_data:
        print(f'{get_date(trans["date"])} {trans["description"]}')
        if "Открытие" in trans["description"]:
            print(trans["to"])
        else:
            print(f"{trans["from"]} -> {trans['to']}")
        print(f'Сумма: {trans["operationAmount"]["amount"]} {trans["operationAmount"]["currency"]["code"]}\n')
    return transactions_data


if __name__ == "__main__":
    #############################################
    main()
