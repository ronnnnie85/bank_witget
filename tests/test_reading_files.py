from unittest.mock import patch

import pandas as pd

from src.reading_files import read_transactions_from_csv


@patch("pandas.read_csv")
def test_transactions_from_csv(mock_csv, good_df):
    mock_csv.return_value = good_df
    assert read_transactions_from_csv("file.csv") == good_df.to_dict('records')

