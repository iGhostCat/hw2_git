import random


def filter_by_currency(transaction_list, currency="USD"):
    """Функция фильтрации по типу валюты, принимает на вход список словарей,
    представляющих транзакции. Функция возвращает итератор,
    который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)"""
    yield (transaction for transaction in transaction_list if dict["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transaction_list):
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transaction_list:
        yield transaction["description"]


def card_number_generator(range_down, range_up):
    """Генератор принимает начальное и конечное значение диапазона генерации
    и выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    card_number = str(random.randint(range_down, range_up)).zfill(16)
    yield " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
