import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency(true_refactoring_transactions_short):
    generator = filter_by_currency(true_refactoring_transactions_short, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "amount": "9824.07",
        "currency_name": "USD",
        "currency_code": "USD",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency_another(true_refactoring_transactions_short):
    generator = filter_by_currency(true_refactoring_transactions_short, "EUR")
    assert list(generator) == []


def test_filter_by_currency_empty():
    generator = filter_by_currency([], "USD")
    assert list(generator) == []


def test_filter_by_currency_none():
    transactions = [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    generator = filter_by_currency(transactions, "USD")
    assert list(generator) == []


def test_transaction_descriptions(true_transactions):
    generator = transaction_descriptions(true_transactions)
    assert list(generator) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_descriptions_empty():
    generator = transaction_descriptions([])
    assert list(generator) == []


def test_transaction_descriptions_none():
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

    generator = transaction_descriptions(transactions)
    assert list(generator) == [
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "begin, end, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (10511, 10512, ["0000 0000 0001 0511", "0000 0000 0001 0512"]),
        (2, 1, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (0, 0, []),
        (-5, -1, []),
    ],
)
def test_card_number_generator(begin, end, expected):
    generator = card_number_generator(begin, end)
    assert list(generator) == expected
