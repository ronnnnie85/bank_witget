import re
from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_data: str) -> str:
    """Обрабатывает информацию о картах и счетах"""
    if not isinstance(account_card_data, str):
        raise TypeError("Ошибка: некорректный тип входных данных.")

    match = re.search(
        r"(\D+)\s(\d+)", account_card_data
    )  # Получаю группировки строки по шаблону (буквы) (цифры)

    if match is None:
        raise ValueError("Ошибка: некорректный формат входных данных.")

    prefix, number = match.groups()

    if len(number) == 20:  # Первым идет Счет, значит обрабатываем как счет
        masked_number = get_mask_account(number)
    elif len(number) == 16:  # Обрабатываем как карту
        masked_number = get_mask_card_number(number)
    else:
        raise ValueError("Ошибка: некорректная длина входных данных.")

    return f"{prefix.strip()} {masked_number}"


def get_date(raw_date: str) -> str:
    """Конвертирует строку с датой из формата ISO 8601 в DD-MM-YYYY"""
    if not isinstance(raw_date, str):
        raise TypeError("Ошибка: некорректный тип входных данных.")

    pattern = (r"[0-9][0-9](0[1-9]|[1-9][0-9])\-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])"
               r"T([0-1][0-9]|2[0-3]):([0-4][0-9]|5[0-9]):([0-4][0-9]|5[0-9])"
               r"(\.[0-9][0-9][0-9][0-9](0[1-9]|[1-9][0-9])){0,1}")
    match = re.search(pattern, raw_date)

    if match is None:
        raise ValueError("Ошибка: некорректный формат даты.")

    dt = datetime.fromisoformat(raw_date)  # Получаем из строки объект datetime по шаблону

    return dt.strftime("%d.%m.%Y")  # Преобразуем в нужный формат в строку
