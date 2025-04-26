import logging
import os
import re
from collections import Counter

from src import loggers

name = os.path.splitext(os.path.basename(__file__))[0]
file_name = f"{name}.log"
logger = loggers.create_logger(name, file_name, logging.DEBUG)


def search_for_string(
    operations: list[dict], description_string: str
) -> list[dict]:
    """Поиск в списке операций по заданной строке.
    Возвращает список операций с подходящим описанием"""
    if description_string == "":
        raise ValueError("Пустая срока поиска")

    pattern = re.compile(description_string, re.IGNORECASE)
    filtered_ops = [
        op for op in operations if pattern.search(op.get("description", ""))
    ]
    return filtered_ops


def counting_operations(operations: list[dict], categories: list) -> dict:
    """Функция подсчета операций по заданным пользователем категориям.
    Возвращает словарь с названиями категорий и их количеством"""
    if any(type(category) is not str for category in categories):
        raise TypeError("В списке категорий присутствуют не строки")

    lst_categories = [
        category.lower()
        for category in categories
        for operation in operations
        if category.lower() in operation.get("description", "").lower()
    ]

    category_count = Counter(lst_categories)

    result = {}
    for category in categories:
        result[category] = category_count.get(category.lower(), 0)

    return result
