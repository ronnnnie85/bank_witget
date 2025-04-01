from src.external_api import get_transaction_amount


def test_get_transaction_amount_good_rub(good_transaction_rub):
    assert get_transaction_amount(good_transaction_rub) == float(good_transaction_rub["operationAmount"]["amount"])


def test_get_transaction_amount_bad_rub(good_transaction_usd):
