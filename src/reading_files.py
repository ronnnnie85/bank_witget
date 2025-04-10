import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """
    Читает финансовые операции из CSV-файла
    и возвращает список словарей с транзакциями"""
    try:
        df = pd.read_csv(file_path, delimiter=';')
    except FileNotFoundError as e:
        return []
    except ValueError as e:
        return []
    transactions = df.to_dict('records')
    return transactions


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """
    Читает финансовые операции из Excel-файла
    и возвращает список словарей с транзакциями"""
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError as e:
        return []
    except ValueError as e:
        return []

    transactions = df.to_dict('records')
    return transactions
