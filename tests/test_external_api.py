import os

import pytest
import requests
from dotenv import load_dotenv

from src.external_api import get_transaction_amount, convert_amount
from unittest.mock import patch, MagicMock


def test_get_transaction_amount_good_rub(good_transaction_rub):
    assert get_transaction_amount(good_transaction_rub) == float(
        good_transaction_rub["operationAmount"]["amount"]
    )


@patch("src.external_api.convert_amount")
def test_get_transaction_amount_bad_rub(mock_convert, good_transaction_usd):
    ret_value = 100.0
    mock_convert.return_value = ret_value
    assert get_transaction_amount(good_transaction_usd) == ret_value

    mock_convert.assert_called_once_with(
        float(good_transaction_usd["operationAmount"]["amount"]),
        good_transaction_usd["operationAmount"]["currency"]["code"],
    )


@patch("requests.get")
def test_convert_amount_good(mock_get):
    res_value = "100.0"
    load_dotenv()
    api_key = os.getenv("API_KEY")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": res_value}

    assert convert_amount(10.0, "USD") == float(res_value)
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10.0",
        headers={"apikey": api_key},
    )


@patch("requests.get")
def test_convert_amount_bad_request(mock_get):
    load_dotenv()
    api_key = os.getenv("API_KEY")

    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.reason = "Internal Server Error"
    mock_get.return_value = mock_response

    with pytest.raises(requests.exceptions.RequestException) as exc_info:
        convert_amount(10.0, "USD")

    assert str(exc_info.value) == "Ошибка запроса. Internal Server Error."

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10.0",
        headers={"apikey": api_key},
    )


@patch("requests.get")
def test_convert_amount_request_exception(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Connection error")

    with pytest.raises(requests.exceptions.RequestException, match="Ошибка запроса. Connection error."):
        convert_amount(10.0, "USD")

    mock_get.assert_called_once()


@patch("requests.get")
def test_convert_amount_request_none(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"res": 100}

    with pytest.raises(ValueError, match="Значение по запросу не получено"):
        convert_amount(10.0, "USD")

    mock_get.assert_called_once()


@patch("requests.get")
def test_convert_amount_request_not_num(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": "res"}

    with pytest.raises(ValueError, match="Получено не число по запросу"):
        convert_amount(10.0, "USD")

    mock_get.assert_called_once()