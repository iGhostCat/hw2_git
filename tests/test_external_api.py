import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

load_dotenv("../.env")

# Тестируемые функции
from src.external_api import api_convert_in_rubles, to_rubles_convert


def test_to_rubles_convert_empty_list():
    """Тест для пустого списка транзакций"""
    with patch("src.external_api.json_to_list", return_value=[]):
        assert to_rubles_convert("any_path.json") == []


@patch("src.external_api.requests.get")
def test_api_convert_in_rubles_success(mock_get):
    """Тест успешной конвертации валюты"""
    # Настраиваем мок API
    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1747746484, "rate": 80.573609},
        "date": "2025-05-20",
        "result": 662425.451824,
    }
    mock_get.return_value = mock_response

    # Тестовая транзакция
    test_transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

    result = api_convert_in_rubles(test_transaction)
    assert result["success"] is True
    assert result["result"] == 662425.451824


@patch("src.external_api.json_to_list")
@patch("src.external_api.requests.get")
def test_to_rubles_convert_with_mocks(mock_get, mock_json):
    """Итоговый тест работы функций со списком транзакций"""
    mock_json.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]

    # Настраиваем мок API
    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1747752484, "rate": 80.750359},
        "date": "2025-05-20",
        "result": 663878.578972,
    }
    mock_get.return_value = mock_response

    # Вызываем функцию
    result = to_rubles_convert("any_path.json")

    # Проверяем результаты
    assert len(result) == 2
    assert result == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
                "conversion": {
                    "success": True,
                    "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
                    "info": {"timestamp": 1747752484, "rate": 80.750359},
                    "date": "2025-05-20",
                    "result": 663878.578972,
                },
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
