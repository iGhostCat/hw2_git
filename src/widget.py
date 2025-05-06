from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str) -> str:

    if "Visa" in input_str:
        return get_mask_card_number(input_str[-16:])
    elif "Master" in input_str:
        return get_mask_card_number(input_str[-16:])
    elif "Maestro" in input_str:
        return get_mask_card_number(input_str[-16:])
    elif "Счет" in input_str:
        return get_mask_account(input_str[-20:])
    else:
        return "Неверный ввод!"


def get_date(date_iso: str) -> str:
    if len(date_iso) == 0:
        return "Неверный ввод!"
    year = date_iso[0:4]
    month = date_iso[5:7]
    day = date_iso[8:10]
    return f"{day}.{month}.{year}"
