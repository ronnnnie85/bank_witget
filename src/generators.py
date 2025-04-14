from typing import Any, Iterator


def filter_by_currency(
    lst_transactions: list[dict[str, int | str | dict]],
    currency: str,
) -> Iterator[dict[str, int | str | dict]]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной."""
    filtered_transactions: Any = filter(
        lambda dct: dct.get("currency_code", "") == currency,
        lst_transactions,
    )

    for transaction in filtered_transactions:
        yield transaction


def transaction_descriptions(
    lst_transactions: list[dict[str, int | str | dict]],
) -> Iterator[str]:
    """Принимает список словарей с транзакциями.
    Возвращает описание каждой операции по очереди."""
    lst_descriptions = [
        str(dct.get("description"))
        for dct in lst_transactions
        if not dct.get("description") is None
        and isinstance(dct.get("description"), str)
    ]

    for description in lst_descriptions:
        yield description


def card_number_generator(begin: int, end: int) -> Iterator[str]:
    """Принимает начальное и конечное значения для генерации.
    Возвращает номера карт в заданном диапазоне"""
    if begin > end:
        begin, end = end, begin

    lst_card_num = [x for x in range(begin, end + 1) if x > 0]

    for card_num in lst_card_num:
        card_number = f"{card_num:016d}"
        formatted_card_number = " ".join(
            [card_number[i: i + 4] for i in range(0, 16, 4)]
        )
        yield formatted_card_number
