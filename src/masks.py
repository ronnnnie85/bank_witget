from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу"""
    if card_number == "":
        raise ValueError("Ошибка: пустое значение номера карты.")

    if not (type(card_number) == int or (type(card_number) == str and card_number.isdigit())):
        raise TypeError("Ошибка: некорректный формат входных данных.")

    card_number_str = str(card_number)  # Преобразуем номер карты в строку

    if len(card_number_str) != 16 :
        raise ValueError("Ошибка: некорректная длина входных данных.")

    first_part = card_number_str[:6]
    last_part = card_number_str[-4:]

    masked_part = "** ****"  # Замаскированная часть

    masked_card_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"

    return masked_card_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу"""
    account_number_str = str(account_number)  # Преобразуем номер счета в строку

    last_four_digits = account_number_str[-4:]

    masked_account = f"**{last_four_digits}"

    return masked_account
