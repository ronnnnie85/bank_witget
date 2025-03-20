from typing import Iterator


def filter_by_currency(
    lst_transactions: list[
        dict[str : int | str | dict[str : str | dict[str:str]]]
    ],
    currency: str,
) -> Iterator[dict[str : int | str | dict[str : str | dict[str:str]]]]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    pass
