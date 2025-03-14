from datetime import datetime
from typing import Union


def filter_by_state(
    lst_dct: list[dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> list[dict[str, Union[str, int]]]:
    """Принимает список и ключ, возвращает отфильтрованный список"""
    if not isinstance(lst_dct, list):
        raise TypeError("Ошибка: некорректный тип входных данных.")
    else:
        for dct in lst_dct:
            if not isinstance(dct, dict):
                raise TypeError("Ошибка: некорректный тип входных данных.")
            else:
                for key, value in dct.items():
                    if not (type(value) is str or  type(value) is int) or not isinstance(key, str):
                        raise TypeError("Ошибка: некорректный тип входных данных.")

    # Использую генератор списка для фильтрации
    return [dct for dct in lst_dct if dct.get("state", "") == state]


def sort_by_date(
    lst_dct: list[dict[str, Union[str, int]]], descending: bool = True
) -> list[dict[str, Union[str, int]]]:
    """Принимает список и ключ, возвращает отсортированный список"""
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
