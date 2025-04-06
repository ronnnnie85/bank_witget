import logging
import os
from typing import Union

from src import loggers

name = os.path.splitext(os.path.basename(__file__))[0]
filename = os.path.join(os.path.dirname(__file__), "..\\logs\\", f"{name}.log")
logger = loggers.create_logger(name, filename, logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу"""
    if card_number == "":
        logger.error("Ошибка: пустое значение номера карты.")
        raise ValueError("Ошибка: пустое значение номера карты.")

    if is_wrong_input_format(card_number):
        logger.error("Ошибка: некорректный формат входных данных.")
        raise TypeError("Ошибка: некорректный формат входных данных.")

    card_number_str = str(card_number)  # Преобразуем номер карты в строку

    if len(card_number_str) != 16:
        logger.error("Ошибка: некорректная длина входных данных.")
        raise ValueError("Ошибка: некорректная длина входных данных.")

    first_part = card_number_str[:6]
    last_part = card_number_str[-4:]

    masked_part = "** ****"  # Замаскированная часть

    masked_card_number = (
        f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"
    )
    logger.info("Маскирование номера карты произошло успешно")
    return masked_card_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу"""
    if account_number == "":
        logger.error("Ошибка: пустое значение номера счета.")
        raise ValueError("Ошибка: пустое значение номера счета.")

    if is_wrong_input_format(account_number):
        logger.error("Ошибка: некорректный формат входных данных.")
        raise TypeError("Ошибка: некорректный формат входных данных.")

    account_number_str = str(
        account_number
    )  # Преобразуем номер счета в строку

    if len(account_number_str) != 20:
        logger.error("Ошибка: некорректная длина входных данных.")
        raise ValueError("Ошибка: некорректная длина входных данных.")

    last_four_digits = account_number_str[-4:]

    masked_account = f"**{last_four_digits}"
    logger.info("Маскирование номера счета произошло успешно")
    return masked_account


def is_wrong_input_format(number: Union[int, str]) -> bool:
    """Вспомогательная функция проверки корректности данных"""
    return not (
        type(number) is int or (type(number) is str and number.isdigit())
    )
