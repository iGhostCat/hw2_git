import pytest

from src.processing import count_operations_by_category, filter_by_state, sort_by_date
from tests.conftest import list_of_dicts


@pytest.mark.parametrize(
    "state,expected",
    [
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state(list_of_dicts, state, expected):
    assert filter_by_state(list_of_dicts, state) == expected


@pytest.mark.parametrize(
    "direction,expected_result",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_sort_by_date(list_of_dicts, direction, expected_result):
    assert sort_by_date(list_of_dicts, direction) == expected_result


def test_count_operations():
    # Тестовые данные
    operations = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
    ]

    # Тест 1: Стандартный случай
    categories = ["Перевод организации", "Перевод с карты на карту"]
    result = count_operations_by_category(operations, categories)
    assert result == {"Перевод организации": 2, "Перевод с карты на карту": 1}

    # Тест 2: Категории, которых нет в данных
    categories = ["Открытие вклада", "Закрытие счета"]
    result = count_operations_by_category(operations, categories)
    assert result == {"Открытие вклада": 0, "Закрытие счета": 0}

    # Тест 3: Пустые данные
    result = count_operations_by_category([], categories)
    assert result == {"Открытие вклада": 0, "Закрытие счета": 0}

    # Тест 4: Операции без описания
    operations = [{"id": 1}, {"description": None}, {"description": ""}]
    result = count_operations_by_category(operations, ["Перевод"])
    assert result == {"Перевод": 0}

    print("Все тесты пройдены!")


test_count_operations()
