import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_files import read_transactions_from_csv, read_transactions_from_excel
from src.services import search_for_string
from src.utils import get_operations_data
from src.widget import get_date, mask_account_card

VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def main():
    """Общая функция по сборке всего проекта"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        while True:
            choice = input().strip()
            if choice in {"1", "2", "3"}:
                break
            print("Пожалуйста, введите 1, 2 или 3")

        transactions = []
        path = os.path.dirname(__file__)
        match choice:
            case "1":
                print("Для обработки выбран JSON-файл.")
                file_path = os.path.join(path, "data", "operations.json")
                transactions = get_operations_data(file_path)
            case "2":
                print("Для обработки выбран CSV-файл.")
                file_path = os.path.join(path, "data", "transactions.csv")
                transactions = read_transactions_from_csv(file_path)
            case "3":
                print("Для обработки выбран XLSX-файл.")
                file_path = os.path.join(path, "data", "transactions_excel.xlsx")
                transactions = read_transactions_from_excel(file_path)
            # case _:
            #     print("Неверный выбор.")
            #     return

        while True:
            status = input(
                "\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные статусы: EXECUTED, CANCELED, PENDING\n").strip().upper()
            if status in VALID_STATUSES:
                print(f"Операции отфильтрованы по статусу \"{status}\"")
                break
            print(f"Статус операции \"{status}\" недоступен.")

        try:
            transactions = filter_by_state(transactions, status)
        except Exception as e:
            print(f"Возникла ошибка: {e}")

        if not transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            continue

        sort_answer = input("Отсортировать операции по дате? y/N\n").strip().lower()
        if sort_answer == "y":
            order = input("Отсортировать по возрастанию? y/N\n").strip().lower()
            descending = order != "y"
            try:
                transactions = sort_by_date(transactions, descending)
            except Exception as e:
                print(f"Возникла ошибка: {e}")

        currency_answer = input("Выводить только рублевые транзакции? y/N\n").strip().lower()
        if currency_answer == "y":
            transactions = list(filter_by_currency(transactions, "RUB"))

        if not transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            continue

        description_filter = input(
            "Отфильтровать список транзакций по определенному слову в описании? y/N\n").strip().lower()
        if description_filter == "y":
            keyword = input("Введите слово для поиска: ").strip()
            try:
                transactions = search_for_string(transactions, keyword)
            except Exception as e:
                print(f"Возникла ошибка: {e}")

        if not transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            continue

        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

        for transaction in transactions:
            date = get_date(transaction["date"])

            desc = transaction.get("description", "Без описания")

            from_info = transaction.get("from", "")
            to_info = transaction.get("to", "")

            try:
                from_masked = mask_account_card(from_info) if from_info and type(from_info) is str else ""
            except Exception as e:
                from_masked = ""
                print(f"Возникла ошибка: {e}")

            try:
                to_masked = mask_account_card(to_info) if to_info and type(to_info) is str else ""
            except Exception as e:
                from_masked = ""
                print(f"Возникла ошибка: {e}")

            amount_info = transaction.get("operationAmount", {})
            amount = amount_info.get("amount", "")
            currency = amount_info.get("currency", {}).get("name", "")

            print(f"{date} {desc}")
            if from_masked and to_masked:
                print(f"{from_masked} -> {to_masked}")
            elif to_masked:
                print(f"{to_masked}")
            print(f"Сумма: {amount} {currency}\n")

        currency_answer = input("Продолжить получение информации о транзакциях? y/N\n").strip().lower()
        if currency_answer != "y":
            break
    pass


if __name__ == "__main__":
    main()