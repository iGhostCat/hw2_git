import json
import logging
import os
from pathlib import Path
import csv
import pandas as pd
from collections import OrderedDict

utils_logger = logging.getLogger("utils")
utils_file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8", mode="w")
utils_file_formatter = logging.Formatter("%(asctime)s: %(filename)s: %(funcName)s: %(levelname)s: %(message)s")
utils_file_handler.setFormatter(utils_file_formatter)
utils_logger.addHandler(utils_file_handler)
utils_logger.setLevel(logging.DEBUG)


def csv_to_list(path_to_file):
    '''Функция, преобразовывающая содержимое файла .CSV в объект python
       для дальнейшей обработки. Возвращает список словарей.'''
    with open(path_to_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        result = []
        for row in reader:
            transaction = {
                'id': row['id'],
                'state': row['state'],
                'date': row['date'],
                'amount': row['amount'],
                'currency_name': row['currency_name'],
                'currency_code': row['currency_code'],
                'from': row['from'],
                'to': row['to'],
                'description': row['description']
            }
            result.append(transaction)
    return result
#print(csv_to_list("../data/transactions.csv"))

def json_to_list(file_path):
    '''Функция, преобразовывающая содержимое файла .json в объект python
       для дальнейшей обработки. Возвращает список словарей.'''
    path = Path(file_path)
    if not path.exists():
        utils_logger.error(f"Ошибка: по указанному пути {path} не найдено файла")
        raise FileNotFoundError(f"Файл не найден: {path.absolute()}")
    utils_logger.info(f"Путь {path} принят, производится преобразование содержимого файла в объект Python")
    with path.open(encoding="utf-8") as f:
        if os.path.getsize(file_path) > 0:
            utils_logger.info("Содержимое преобразовано и готово к дальнейшей обработке")
            return json.load(f)
        else:
            utils_logger.info("Полученный файл пуст, возвращается пустой список")
            return []


#print(json_to_list("../data/test_operations.json"))
