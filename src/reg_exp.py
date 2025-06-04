import re

test_data = [
    {
        "id": 650703,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
    },
    {
        "id": 3598919,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "description": "Перевод с карты на карту",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
    },
]


def reg_proc_search(database, search_query, use_regex, case_sensitive):
    """
    Умный поиск с автоматическим определением/преобразованием запроса.

    :param database: Список словарей с данными
    :param search_query: Строка поиска
    :param use_regex: Если True, обрабатывать как regex, иначе как обычную строку
    :param case_sensitive: Чувствительность к регистру
    :return: Список найденных записей
    """
    flags = 0 if case_sensitive else re.IGNORECASE

    if not use_regex:
        # Автоматическое экранирование для обычных строк
        search_query = re.escape(search_query)

    try:
        pattern = re.compile(search_query, flags)
    except re.error:
        # Если даже после экранирования ошибка (маловероятно), ищем точное совпадение
        pattern = re.compile(f"^{re.escape(search_query)}$", flags)

    results = []

    for record in database:
        for value in record.values():
            if isinstance(value, (str, int, float)):
                if pattern.search(str(value)):
                    results.append(record)
                    break

    return results


# print(reg_proc_search(test_data, 'executed', True, False))
