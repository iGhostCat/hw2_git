transaction_list = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transaction_input, currency="USD"):
    """Функция фильтрации по типу валюты, принимает на вход список словарей,
    представляющих транзакции. Функция возвращает итератор,
    который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)"""
    found = False
    for transaction in transaction_input:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            found = True
            yield transaction
    if not found:  # Если ни одной транзакции не найдено
        return "Транзакции в выбранной валюте отсутствуют!"


def transaction_descriptions(transactions_in):
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions_in:
        yield transaction["description"]


def card_number_generator(start, end):
    """Генератор принимает начальное и конечное значение диапазона генерации
    и выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты. Генератор может сгенерировать номера карт
    в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if int(start) < int(end):
        start_int = int(start) if isinstance(start, str) else start
        end_int = int(end) if isinstance(end, str) else end
    else:
        start_int = int(end)
        end_int = int(start)

    for num in range(start_int, end_int + 1):
        # Форматируем число в 16-значную строку с заполнением нулями слева
        card_num = f"{num:016d}"
        # Разбиваем на группы по 4 цифры и разделяем пробелами
        formatted_num = " ".join([card_num[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_num


# print(list(filter_by_currency(transaction_list, 'RUB')))
print(list(transaction_descriptions(transaction_list)))
