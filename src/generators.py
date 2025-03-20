from typing import Iterator


def filter_by_currency(
    lst_transactions: list[
        dict[str : int | str | dict[str : str | dict[str:str]]]
    ],
    currency: str,
) -> Iterator[dict[str : int | str | dict[str : str | dict[str:str]]]]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной."""
    pass


def transaction_descriptions(
    lst_transactions: list[
        dict[str : int | str | dict[str : str | dict[str:str]]]
    ],
) -> Iterator[str]:
    """Принимает список словарей с транзакциями. Возвращает описание каждой операции по очереди."""
    pass


def card_number_generator(begin: int, end: int) -> Iterator[str]:
    """Принимает начальное и конечное значения для генерации. Возвращает номера карт в заданном диапазоне"""
    pass
