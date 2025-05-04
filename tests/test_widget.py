from src.widget import mask_account_card
from src.widget import get_date
import pytest


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Счет 64686473678894779589", "**9589"),
        ("MasterCard 7158300734726758", "7158 30** **** 6758"),
        ("Счет 35383033474447895560", "**5560"),
        ("Visa Classic 6831982476737658", "6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "5999 41** **** 6353"),
        ("Счет 73654108430135874305", "**4305"),
        ("", "Неверный ввод!"),
    ],
)
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "date_iso, expected_date",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("", "Неверный ввод!"),
    ],
)
def test_get_date(date_iso, expected_date):
    assert get_date(date_iso) == expected_date
