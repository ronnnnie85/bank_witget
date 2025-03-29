import os

import pytest

from src.decorators import log, print_message


def test_print_message_to_console(capsys):
    test_message = "Test console message"
    print_message(None, test_message)

    # Проверяем, что сообщение вывелось в stdout
    captured = capsys.readouterr()
    assert captured.out.strip() == test_message


def test_print_message_to_file():
    test_filename = "test_log.txt"
    current_dir = os.path.dirname(__file__)  # Папка, где лежит модуль
    test_file = os.path.join(current_dir, "../logs/" + test_filename)

    # Первое сообщение
    first_message = "First message"
    print_message(test_filename, first_message)

    # Второе сообщение
    second_message = "Second message"
    print_message(test_filename, second_message)

    # Проверяем, что оба сообщения в файле
    with open(test_file, "r", encoding="utf-8") as f:
        content = f.read().splitlines()
    assert content == [first_message, second_message]
    os.remove(test_file)


def test_log_file():
    @log("log.txt")
    def foo(x, y):
        return y / x

    assert foo(10, 20) == 2.0

    with pytest.raises(Exception):
        foo(0, 10)


def test_log_console(capsys):
    @log()
    def foo(x, y):
        res = y / x
        return res

    foo(10, 20)
    captured = capsys.readouterr()
    assert (
        "foo started with args: (10, 20) and kwargs: {}" in captured.out
        and "foo finished successfully with result: 2.0" in captured.out
    )


def test_log_console_error(capsys):
    @log()
    def foo(x, y):
        res = y / x
        return res

    try:
        res = foo(0, 12)
    except Exception as e:
        res = 0

    captured = capsys.readouterr()
    assert (
        "foo started with args: (0, 12) and kwargs: {}" in captured.out
        and "foo error: ZeroDivisionError. Args: (0, 12) and kwargs: {}" in captured.out
    )