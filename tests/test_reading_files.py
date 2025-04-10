from unittest.mock import patch

import pandas as pd

from src.reading_files import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_transactions_from_csv(mock_csv, good_df):
    mock_csv.return_value = good_df
    assert read_transactions_from_csv("file.csv") == good_df.to_dict('records')


@patch("pandas.read_csv")
def test_read_transactions_from_csv_wrong_type(mock_csv):
    mock_csv.side_effect = ValueError("Тестовая ошибка")
    assert read_transactions_from_csv("file.csv") == []


def test_read_transactions_from_csv_file_not_found():
    assert read_transactions_from_csv("") == []


@patch("pandas.read_excel")
def test_transactions_from_xlsx(mock_xlsx, good_df):
    mock_xlsx.return_value = good_df
    assert read_transactions_from_excel("file.csv") == good_df.to_dict('records')


@patch("pandas.read_excel")
def test_read_transactions_from_xlsx_wrong_type(mock_xlsx):
    mock_xlsx.side_effect = ValueError("Тестовая ошибка")
    assert read_transactions_from_excel("file.csv") == []


def test_read_transactions_from_xlsx_file_not_found():
    assert read_transactions_from_excel("") == []