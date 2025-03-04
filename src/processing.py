from typing import Union
from datetime import datetime


def filter_by_state(
    lst_dct: list[dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> list[dict[str, Union[str, int]]]:
    """Принимает список и ключ, возвращает отфильтрованный список"""
    return [dct for dct in lst_dct if dct.get("state", "") == state]


def sort_by_date(
    lst_dct: list[dict[str, Union[str, int]]], descending: bool = True
) -> list[dict[str, Union[str, int]]]:
    """Принимает список и ключ, возвращает отсортированный список"""
    return sorted(
        lst_dct,
        key=lambda x: datetime.min if x.get("date") is None else datetime.fromisoformat(x.get("date")),
        reverse=descending,
    )
