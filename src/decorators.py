import functools
import os


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
            return function(*args, **kwargs)
        return wrapper
    return decorator