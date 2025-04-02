import json


def get_operations_data(filename: str) -> list:
    """Обрабатывает JSON-файл и преобразует в список транзакций"""
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError:
                return []
            else:
                if not type(data) is list:
                    return []

                return data
    except FileNotFoundError:
        return []
