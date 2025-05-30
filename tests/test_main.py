from unittest.mock import patch, MagicMock
import pytest
from importlib import reload
import sys
import src.main  # Импортируем модуль для перезагрузки

import src


def test_main_flow():
    # Подготовка тестовых данных с ВСЕМИ необходимыми полями
    test_transaction = {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "operationAmount": {
            "amount": "16210.0",
            "currency": {
                "name": "Sol",
                "code": "PEN"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397"
    }

    # Полное мокирование всех зависимостей
    with patch('builtins.input', MagicMock(side_effect=['1', 'EXECUTED', 'нет', 'нет', 'нет'])), \
            patch('builtins.print', MagicMock()), \
            patch('src.utils.json_to_list', MagicMock(return_value=[test_transaction])), \
            patch('src.processing.filter_by_state', MagicMock(return_value=[test_transaction])), \
            patch('src.processing.sort_by_date', MagicMock(return_value=[test_transaction])), \
            patch('src.generators.filter_by_currency', MagicMock(return_value=iter([test_transaction]))), \
            patch('src.reg_exp.reg_proc_search', MagicMock(return_value=[test_transaction])):
        # Перезагружаем модуль для применения моков
        reload(src.main)
        from src.main import main

        # Выполняем тестируемую функцию
        result = main()

        # Проверяем результаты
        assert len(result) == 1
        assert result[0]["id"] == "650703"
        assert result[0]["state"] == "EXECUTED"