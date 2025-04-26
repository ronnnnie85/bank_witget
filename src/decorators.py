import functools
import os
from time import localtime, strftime, time
from typing import Any, Callable, Iterable


def print_message(filename: str | None, text_message: str) -> None:
    """Вспомогательная функция для записи логов в файл
    или вывода в консоль"""
    if filename is None:
        print(text_message)
    else:
        current_dir = os.path.dirname(__file__)  # Папка, где лежит модуль
        log_path = os.path.join(
            current_dir, "../logs/" + filename
        )  # Абсолютный путь к файлу
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"{text_message}\n")


def log(filename: str | None = None) -> Callable:
    """Декоратор для логирования выполнения функций."""

    def decorator(function: Callable) -> Callable:
        @functools.wraps(function)
        def wrapper(*args: Iterable, **kwargs: Iterable) -> Any:
            # Блок запуска функции и получения лог сообщений

            log_text_start = (
                f"{strftime("[%Y-%m-%d %H:%M:%S]", localtime(time()))} "
                f"{function.__name__} started with args: {args} "
                f"and kwargs: {kwargs}"
            )

            print_message(filename, log_text_start)

            try:
                result = function(*args, **kwargs)
                log_text_end = (
                    f"{strftime("[%Y-%m-%d %H:%M:%S]", localtime(time()))} "
                    f"{function.__name__} finished successfully "
                    f"with result: {result}\n"
                )

                print_message(filename, log_text_end)

                return result
            except Exception as e:
                log_text_end = (
                    f"{strftime("[%Y-%m-%d %H:%M:%S]", localtime(time()))} "
                    f"{function.__name__} error: {type(e).__name__}. "
                    f"Args: {args} and kwargs: {kwargs}\n"
                )

                print_message(filename, log_text_end)
                raise e

        return wrapper

    return decorator
