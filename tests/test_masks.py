import pytest
from mypy.dmypy.client import request

from src.masks import get_mask_card_number, get_mask_account, is_wrong_input_format


# Функция get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected", [(1234567887654321, "1234 56** **** 4321"), ("9876543219876543", "9876 54** **** 6543")]
)
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


# Функция get_mask_account
@pytest.mark.parametrize("account, expected", [(12345678876543212224, "**2224"), ("98765432198765433538", "**3538")])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_account_empty():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")

    assert str(exc_info.value) == "Ошибка: пустое значение номера счета."


@pytest.mark.parametrize("account_fixture", ["non_int_str_value", "non_digit_str_value"])
def test_get_mask_account_wrong_type(request, account_fixture):
    with pytest.raises(TypeError) as exc_info:
        account = request.getfixturevalue(account_fixture)
        get_mask_account(account)

    assert str(exc_info.value) == "Ошибка: некорректный формат входных данных."


@pytest.mark.parametrize("account", [123456788765432128769, "987654321987654127215", 0, "0"])
def test_get_mask_account_wrong_len(account):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account)

    assert str(exc_info.value) == "Ошибка: некорректная длина входных данных."


@pytest.mark.parametrize("account_fixture", ["non_int_str_value", "non_digit_str_value"])
def test_is_wrong_input_format_wrong(request, account_fixture):
    account = request.getfixturevalue(account_fixture)
    assert is_wrong_input_format(account) == True


@pytest.mark.parametrize("account", ["01234568", 5678922])
def test_is_wrong_input_format_not_wrong(account):
    assert is_wrong_input_format(account) == False
