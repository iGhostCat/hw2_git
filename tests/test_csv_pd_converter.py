from unittest.mock import MagicMock, mock_open, patch

import pandas as pd
import pytest

from src.csv_pd_converter import csv_to_list_of_dicts, excel_to_list_of_dicts


def test_excel_to_list_of_dicts():
    # Подготовка тестовых данных
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

    # Ожидаемый результат
    expected = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210.0", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740.0", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]

    mock_df = MagicMock(spec=pd.DataFrame)
    mock_df.iterrows.return_value = [(i, pd.Series(row)) for i, row in enumerate(test_data)]

    with patch("pandas.read_excel", return_value=mock_df) as mock_read_excel:
        result = excel_to_list_of_dicts("dummy_path.xlsx")

        mock_read_excel.assert_called_once_with(
            "dummy_path.xlsx",
            usecols=["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
        )

        # Проверяем результат
        assert result == expected


def test_csv_to_list_of_dicts():
    mock_csv_data = """id;state;date;amount;currency_name;currency_code;description;from;to
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Перевод организации;Счет 58803664561298323391;Счет 39745660563456619397
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Перевод с карты на карту;Discover 3172601889670065;Discover 0720428384694643"""

    expected = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
    ]

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        mock_rows = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
            },
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": "29740",
                "currency_name": "Peso",
                "currency_code": "COP",
                "description": "Перевод с карты на карту",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
            },
        ]

        with patch("csv.DictReader") as mock_reader:
            mock_reader.return_value = mock_rows
            result = csv_to_list_of_dicts("fignya.csv")
            assert result == expected
