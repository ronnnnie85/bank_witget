import pytest

from src.widget import get_date, mask_account_card


# Функция mask_account_card
@pytest.mark.parametrize(
    "data, excepted",
    [
        ("Счет 20304050607080901050", "Счет **1050"),
        ("Visa 1020304050607080", "Visa 1020 30** **** 7080"),
        (
            "Visa Platinum 5060807090203040",
            "Visa Platinum 5060 80** **** 3040",
        ),
    ],
)
def test_mask_account_card(data, excepted):
    assert mask_account_card(data) == excepted


def test_mask_account_card_non_str_value(non_str_value):
    with pytest.raises(TypeError) as exc_info:
        mask_account_card(non_str_value)

    assert str(exc_info.value) == "Ошибка: некорректный тип входных данных."


@pytest.mark.parametrize(
    "data", ["Счет01010101020202020202", "1234567899876543", "Visa platinum"]
)
def test_mask_account_card_wrong_template(data):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(data)

    assert str(exc_info.value) == "Ошибка: некорректный формат входных данных."


@pytest.mark.parametrize(
    "data", ["Счет 123456789987654321", "Visa platinum 123456789987654"]
)
def test_mask_account_card_wrong_len(data):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(data)

    assert str(exc_info.value) == "Ошибка: некорректная длина входных данных."


# Функция get_date
@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-04-12T02:26:18", "12.04.2025"),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected


def test_get_date_non_str_value(non_str_value):
    with pytest.raises(TypeError) as exc_info:
        get_date(non_str_value)

    assert str(exc_info.value) == "Ошибка: некорректный тип входных данных."


@pytest.mark.parametrize("date", ["2024-03-11", "2024/03/11", "12.04.2025"])
def test_get_date_wrong_str_value(date):
    with pytest.raises(ValueError) as exc_info:
        get_date(date)

    assert str(exc_info.value) == "Ошибка: некорректный формат даты."


@pytest.mark.parametrize(
    "date",
    [
        "2024-02-30T02:26:18.671407",
        "2025-02-29T02:26:18.671407",
    ],
)
def test_get_date_wrong_str_value_leap(date):
    with pytest.raises(ValueError) as exc_info:
        get_date(date)

    assert (
        str(exc_info.value)
        == "Ошибка: некорректный формат даты в високосный год."
    )
