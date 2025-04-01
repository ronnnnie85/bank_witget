import os
import requests


def get_transaction_amount(transaction: dict) -> float:
    """Получает данные о транзакции и возвращает сумму в рублях"""
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if currency_code is None:
        raise KeyError("Отсутствует ключ code")
    if not type(currency_code) is str:
        raise TypeError("Получена не строка по ключу code")
    if len(currency_code) == 0:
        raise ValueError("По ключу code - пустая строка")

    amount = transaction.get("operationAmount", {}).get("amount")
    if amount is None:
        raise KeyError("Отсутствует ключ amount")
    if type(amount) is not float|int:
        raise TypeError("Получено не число по ключу amount")

    if currency_code == "RUB":
        return float(amount)
    else:
        return round(float(convert_amount(amount, currency_code)), 2)


def convert_amount(amount, currency_code):
    """Переводит сумму из валюты в рубли через API"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    result = 0
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Ошибка запроса. {str(e)}.")
    else:
        if response.status_code != 200:
            raise requests.exceptions.RequestException(f"Ошибка запроса. {response.reason}.")
        else:
            result = response.json().get("result")
            if result is None:
                raise ValueError("Значение по запросу не получено")
            if not type(result) is float|int:
                raise TypeError("Получено не число по запросу")

    return result
