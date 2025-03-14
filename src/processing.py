import re
from datetime import datetime
from typing import Union


def filter_by_state(
    lst_dct: list[dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> list[dict[str, Union[str, int]]]:
    """Принимает список и ключ, возвращает отфильтрованный список"""
    if is_wrong_parameter(lst_dct):
        raise TypeError("Ошибка: некорректный тип входных данных.")

    # Использую генератор списка для фильтрации
    return [dct for dct in lst_dct if dct.get("state", "") == state]


def sort_by_date(
    lst_dct: list[dict[str, Union[str, int]]], descending: bool = True
) -> list[dict[str, Union[str, int]]]:
    """Принимает список и ключ, возвращает отсортированный список"""
    pattern = (
        r"[0-9][0-9](0[1-9]|[1-9][0-9])\-(0[1-9]|1[0-2])-"
        r"(0[1-9]|[1-2][0-9]|3[0-1])"
        r"T([0-1][0-9]|2[0-3]):([0-4][0-9]|5[0-9]):([0-4][0-9]|5[0-9])"
        r"(\.[0-9][0-9][0-9][0-9](0[1-9]|[1-9][0-9])){0,1}"
    )

    if is_wrong_parameter(lst_dct):
        raise TypeError("Ошибка: некорректный тип входных данных.")

    for dct in lst_dct:
        if not dct.get("date") is None:
            match = re.search(pattern, str(dct["date"]))
            if match is None:
                raise ValueError("Ошибка: некорректный формат даты.")

    # Сортирую, ключ - объект datetime, из строковой даты в формате ISO
    return sorted(
        lst_dct,
        key=lambda x: (
            datetime.min
            if x.get("date") is None
            else datetime.fromisoformat(str(x.get("date")))
        ),
        reverse=descending,
    )


def is_wrong_parameter(lst_dct: list[dict[str, Union[str, int]]]) -> bool:
    """Вспомогательная функция для проверки параметров"""
    if not isinstance(lst_dct, list):
        return True
    else:
        for dct in lst_dct:
            if not isinstance(dct, dict):
                return True
            else:
                for key, value in dct.items():
                    if not (
                        type(value) is str or type(value) is int
                    ) or not isinstance(key, str):
                        return True

    return False
