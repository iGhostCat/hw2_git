import csv
import datetime

import pandas as pd


def csv_to_list_of_dicts(path_to_file):
    """Функция, преобразовывающая содержимое файла .CSV в объект python
    для дальнейшей обработки. Возвращает список словарей."""
    with open(path_to_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        result = []
        for row in reader:
            transaction = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            }
            result.append(transaction)
    return result


# print(csv_to_list_of_dicts('../data/test_transactions_csv.csv'))


def excel_to_list_of_dicts(path_to_file):
    """Функция преобразования таблицы .xlsx в список словарей"""
    df = pd.read_excel(
        path_to_file,
        usecols=["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
    )
    transactions = []
    for _, row in df.iterrows():
        transaction = {
            "id": str(row["id"]),
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": str(row["amount"]),
                "currency": {"name": row["currency_name"], "code": row["currency_code"]},
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        }
        transactions.append(transaction)

    return transactions


# print(excel_to_list_of_dicts('../data/test_transactions_excel.xlsx'))
