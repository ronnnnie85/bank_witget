import pytest


@pytest.fixture
def non_int_str_value():
    return True


@pytest.fixture
def non_digit_str_value():
    return "value"
