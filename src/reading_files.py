import logging
import os

import pandas as pd

from src import loggers

name = os.path.splitext(os.path.basename(__file__))[0]
file_name = f"{name}.log"
logger = loggers.create_logger(name, file_name, logging.DEBUG)


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """
    Читает финансовые операции из CSV-файла
    и возвращает список словарей с транзакциями"""
    try:
        df = pd.read_csv(file_path, delimiter=";")
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return []
    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        return []
    transactions = df.to_dict("records")
    logger.info(f"Файл {file_path} успешно обработан")
    return transactions


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """
    Читает финансовые операции из Excel-файла
    и возвращает список словарей с транзакциями"""
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return []
    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        return []

    transactions = df.to_dict("records")
    logger.info(f"Файл {file_path} успешно обработан")
    return transactions
