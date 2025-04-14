import json
import logging
import os

from src import loggers

name = os.path.splitext(os.path.basename(__file__))[0]
file_name = f"{name}.log"
logger = loggers.create_logger(name, file_name, logging.DEBUG)


def get_operations_data(filename: str) -> list:
    """Обрабатывает JSON-файл и преобразует в список транзакций"""
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError as e:
                logger.error(f"Ошибка: {e}")
                return []
            else:
                if not type(data) is list:
                    logger.critical(
                        f"В полученном файле не {type(list)}, а {type(data)}"
                    )
                    return []
                logger.info(f"Файл {filename} успешно обработан")

                result = []
                for transaction in data:
                    transformed = {
                        "id": transaction.get("id", ""),
                        "state": transaction.get("state", ""),
                        "date": transaction.get("date", ""),
                        "amount": transaction.get("operationAmount", {}).get(
                            "amount", ""
                        ),
                        "currency_name": transaction.get("operationAmount", {})
                        .get("currency", {})
                        .get("name", ""),
                        "currency_code": transaction.get("operationAmount", {})
                        .get("currency", {})
                        .get("code", ""),
                        "description": transaction.get("description", ""),
                        "from": transaction.get("from", ""),
                        "to": transaction.get("to", ""),
                    }
                    result.append(transformed)

                return result
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return []
