import pytest
from src.reg_exp import reg_proc_search  # Замените your_module на имя вашего модуля

@pytest.fixture
def test_data():
    return [
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

def test_search_by_status(test_data):
    # Поиск по статусу (без учета регистра)
    result = reg_proc_search(test_data, 'executed', False, False)
    assert len(result) == 2
    assert all(tx['state'] == 'EXECUTED' for tx in result)

def test_search_by_description(test_data):
    # Поиск по описанию (точное совпадение)
    result = reg_proc_search(test_data, 'Перевод с карты на карту', False, True)
    assert len(result) == 1
    assert result[0]['id'] == 3598919

def test_search_by_regex(test_data):
    # Поиск по регулярному выражению (номер счета)
    result = reg_proc_search(test_data, r'Счет \d{20}', True, True)
    assert len(result) == 1
    assert result[0]['id'] == 650703

def test_search_by_amount(test_data):
    # Поиск по числовому значению (amount)
    result = reg_proc_search(test_data, '16210', False, False)
    assert len(result) == 1
    assert result[0]['amount'] == 16210.0

def test_search_case_sensitive(test_data):
    # Поиск с учетом регистра (должен вернуть 0 результатов)
    result = reg_proc_search(test_data, 'перевод', False, True)
    assert len(result) == 0

def test_search_special_chars(test_data):
    # Поиск с специальными символами (экранирование)
    result = reg_proc_search(test_data, 'Счет (588)', True, False)
    assert len(result) == 0  # Должен вернуть 0, так как скобки экранируются

def test_empty_query(test_data):
    # Пустой запрос
    result = reg_proc_search(test_data, '', False, False)
    assert len(result) == 2  # Пустой паттерн совпадает с любым значением

def test_invalid_regex(test_data):
    # Некорректное регулярное выражение
    result = reg_proc_search(test_data, '[invalid-regex', True, False)
    assert len(result) == 0  # Должен корректно обработать ошибку regex