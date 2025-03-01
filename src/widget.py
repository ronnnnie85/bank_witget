import re
from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_data: str) -> str:
    """Обрабатывает информацию о картах и счетах"""
    match = re.search(r"(\D+)\s(\d+)", account_card_data)  # Получаю группировки строки по шаблону (буквы) (цифры)

    if match is None:
        return "Некорректный формат данных"

    prefix, number = match.groups()

    # if prefix.lower().startswith("счет"):  # Первым идет Счет, значит обрабатываем как счет
    #     masked_number = get_mask_account(int(number))
    # elif len(number) == 16:  # Обрабатываем как карту
    #     masked_number = get_mask_card_number(int(number))
    # else:
    #     return "Некорректный формат данных"

    if len(number) == 20:  # Первым идет Счет, значит обрабатываем как счет
        masked_number = get_mask_account(number)
    elif len(number) == 16:  # Обрабатываем как карту
        masked_number = get_mask_card_number(number)
    else:
        return "Некорректный формат данных"

    return f"{prefix.strip()} {masked_number}"


def get_date(raw_date: str) -> str:
    """Конвертирует строку с датой из формата ISO 8601 в DD-MM-YYYY"""
    dt = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%f")  # Получаем из строки объект datetime по шаблону

    return dt.strftime("%d.%m.%Y")  # Преобразуем в нужный формат в строку
