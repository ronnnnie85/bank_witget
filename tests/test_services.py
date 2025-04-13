import pytest

from src.services import counting_operations, search_for_string


def test_search_for_string(true_transactions):
    assert search_for_string(true_transactions, "перевод") == true_transactions


def test_search_for_string_empty_str(true_transactions):
    with pytest.raises(ValueError, match="Пустая срока поиска"):
        search_for_string(true_transactions, "")


def test_counting_operations(true_transactions):
    assert counting_operations(true_transactions, ["Перевод"]) == {
        "Перевод": 5
    }


def test_counting_operations_empty_str(true_transactions):
    with pytest.raises(
        TypeError, match="В списке категорий присутствуют не строки"
    ):
        assert counting_operations(true_transactions, [True])
