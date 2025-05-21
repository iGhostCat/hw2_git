import json
import os

import requests
from dotenv import load_dotenv

from src.utils import json_to_list

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


def api_convert_in_rubles(transaction):
    """Функция для работы с внешним API по получению данных о курсах валют:
    https://apilayer.com/marketplace/exchangerates_data-api#authentication
    Принимает словарь с данными о транзакции, возвращает словарь с данными
    о размере транзакции в переводе в рубли"""
    url = (
        f"https://api.apilayer.com/exchangerates_data/convert?"
        f"to=RUB&from={transaction['operationAmount']['currency']['code']}"
        f"&amount={transaction['operationAmount']['amount']}"
    )

    response = requests.get(url, headers={"apikey": API_KEY}, timeout=10)
    return response.json()


def to_rubles_convert(transactions_list_json):
    """Функция вывода всех транзакций в рублях, принимает список транзакций в формате json, проверяет все транзакции,
    если транзакция не в рублях, то происходит обращение к внешнему API и выводится результат в рублях, переведённый
    по актуальному курсу данной валюты к рублю. Возвращается список словарей всех транзакций, в транзакциям
    в иностранных валютах прикладывается раздел с конвертированной суммой каждой транзакции в рублях"""
    transactions_list = json_to_list(transactions_list_json)
    transactions_out = []

    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            conversion = api_convert_in_rubles(transaction)
            if conversion:
                transaction["operationAmount"]["conversion"] = conversion
        transactions_out.append(transaction)

    return transactions_out


# print(to_rubles_convert('../data/test_operations.json'))
# print(API_KEY)
