import logging
from pathlib import Path

# Создаем папку logs
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)


masks_logger = logging.getLogger("masks")
masks_file_handler = logging.FileHandler(log_dir / "masks.log", encoding="utf-8", mode="w")
masks_file_formatter = logging.Formatter("%(asctime)s: %(filename)s: %(funcName)s: %(levelname)s: %(message)s")
masks_file_handler.setFormatter(masks_file_formatter)
masks_logger.addHandler(masks_file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Показывает первые 6 и последние 4 цифры, остальные заменяет на *.
    """

    card_str = str(card_number).replace(" ", "")  # Удаление пробелов из номера, если есть:
    masks_logger.info("Начало работы функции, обработка пробелов в номере")
    if len(card_str) != 16 or not card_str.isdigit():
        masks_logger.error(
            "Ошибка: неверный ввод номера, присутствуют нецифровые символы или неподходящая длина строки"
        )
        return "Неверный ввод!"
    # Разбиваем на части и маскируем
    first_part = card_str[:4]  # Первые 4 цифры
    second_part = card_str[4:6]  # Следующие 2 цифры (5-6)
    last_part = card_str[-4:]  # Последние 4 цифры

    # Собираем замаскированный номер
    masked_number = f"{first_part} {second_part}** **** {last_part}"
    masks_logger.info("Обработка завершена успешно")
    return masked_number


def get_mask_account(acc_number: int | str) -> str:
    """Функция получения маски номера банковской карты,
    принимает номер карты числом, возвращает его маску в виде:
    **XXXX"""
    masks_logger.info("Начало работы функции")
    if len(acc_number) != 20 or not acc_number.isdigit():
        masks_logger.error("Ошибка: неверный ввод, недостаточный размер строки или присутствуют нецифровые символы")
        return "Неверный ввод!"
    masks_logger.info("Обработка завершена успешно")
    return "**" + str(acc_number[-4 : len(str(acc_number))])


# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("73654108430135874305"))
