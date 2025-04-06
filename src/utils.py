import json
import logging
import os

from src import loggers

name = os.path.splitext(os.path.basename(__file__))[0]
filename = os.path.join(os.path.dirname(__file__), "..\\logs\\",
                        f"{name}.log")
logger = loggers.create_logger(name, filename, logging.DEBUG)


def get_operations_data(filename: str) -> list:
    """Обрабатывает JSON-файл и преобразует в список транзакций"""
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError as e:
                logger.error(f"Функция get_operations_data. Ошибка: {e}")
                return []
            else:
                if not type(data) is list:
                    logger.critical(
                        f"Функция get_operations_data. В полученном файле "
                        f"не {type(list)}, а {type(data)}"
                    )
                    return []
                logger.info(
                    f"Функция get_operations_data. Файл {filename} "
                    f"успешно обработан"
                )
                return data
    except FileNotFoundError as e:
        logger.error(f"Функция get_operations_data. Ошибка: {e}")
        return []
