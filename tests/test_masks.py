import pytest
from mypy.dmypy.client import request

from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [(1234567887654321, "1234 56** **** 4321"),
                                                   ("9876543219876543", "9876 54** **** 6543")])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")

    assert str(exc_info.value) == "Ошибка: пустое значение номера карты."


@pytest.mark.parametrize("card_fixture", ["non_int_str_value", "non_digit_str_value"])
def test_get_mask_card_number_wrong_type(request, card_fixture):
    with pytest.raises(TypeError) as exc_info:
        card_number = request.getfixturevalue(card_fixture)
        get_mask_card_number(card_number)

    assert str(exc_info.value) == "Ошибка: некорректный формат входных данных."


@pytest.mark.parametrize("card_number", [12345678876543212, "98765432198765412", 0, "0"])
def test_get_mask_card_number_wrong_len(card_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)

    assert str(exc_info.value) == "Ошибка: некорректная длина входных данных."

