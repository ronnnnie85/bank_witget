import functools
import os
from time import strftime, localtime, time


def print_message(filename, text_message):
    if filename is None:
        print(text_message)
    else:
        current_dir = os.path.dirname(__file__)  # Папка, где лежит модуль
        log_path = os.path.join(current_dir, "../logs/" + filename) # Абсолютный путь к файлу
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"{text_message}\n")


def log(filename=None):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            #Блок запуска функции и получения лог сообщений
            err = None

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
