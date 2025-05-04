from typing import List, Dict, Union


def filter_by_state(
    list_input: List[Dict[str, Union[int, str, bool]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[int, str, bool]]]:
    """Функция фильтрации списка операций пользователя по статусу выполнения, принимает
    на вход список словарей операций, возвращает список словарей, отфильтрованный по
    значению статуса выполнения"""

    list_output = []
    for element in list_input:
        if element["state"] == state:
            list_output.append(element)
    return list_output


def sort_by_date(
    list_input: List[Dict[str, Union[int, str, bool]]], direction: bool = False
) -> List[Dict[str, Union[int, str, bool]]]:
    """Функция сортировки словарей в списке по дате, принимает список словарей и
    необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате"""
    sorted_list = sorted(list_input, key=lambda d: d["date"], reverse=direction)
    return sorted_list
