def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Показывает первые 6 и последние 4 цифры, остальные заменяет на *.
    """

    card_str = str(card_number).replace(" ", "")
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")
    # Разбиваем на части и маскируем
    first_part = card_str[:4]  # Первые 4 цифры
    second_part = card_str[4:6]  # Следующие 2 цифры (5-6)
    last_part = card_str[-4:]  # Последние 4 цифры

    # Собираем замаскированный номер
    masked_number = f"{first_part} {second_part}** **** {last_part}"

    return masked_number


def get_mask_account(acc_number: int) -> str:
    """Функция получения маски номера банковской карты,
    принимает номер карты числом, возвращает его маску в виде:
    **XXXX"""

    return "**" + str(acc_number[-4 : len(str(acc_number))])
