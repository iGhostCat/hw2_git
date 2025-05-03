from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('5555') == 'Номер карты должен состоять из 16 цифр!'
    assert get_mask_card_number('') == 'Номер карты должен состоять из 16 цифр!'
    assert get_mask_card_number('7000 7922 8960 6361') == '7000 79** **** 6361'


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('73654108') == 'Номер счёта должен состоять из 20 цифр!'
    assert get_mask_account('') == 'Номер счёта должен состоять из 20 цифр!'