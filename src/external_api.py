import os
import requests
from dotenv import load_dotenv


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

    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Не получилось получить сумму")

    if currency_code == "RUB":
        return amount
    else:
        return round(float(convert_amount(amount, currency_code)), 2)


def convert_amount(amount: float|int, currency_code: str) -> float|int:
    """Переводит сумму из валюты в рубли через API"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    load_dotenv()
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
            try:
                result = float(result)
            except ValueError:
                raise ValueError("Получено не число по запросу")

    return result


if __name__ == "__main__":
    transaction = {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  }

    res = get_transaction_amount(transaction)
    print(res)