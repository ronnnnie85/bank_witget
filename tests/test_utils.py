import json
import os
import tempfile

import pytest

from src.utils import get_operations_data


def test_get_operations_data_valid_file(true_transactions):
    test_data = true_transactions

    tmp_path = tempfile.mktemp(suffix='.json')
    with open(tmp_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)

    result = get_operations_data(tmp_path)
    assert result == test_data

    if os.path.exists(tmp_path):
        os.remove(tmp_path)


def test_get_operations_data_invalid_content():
    test_data = {"key" : "value"}
    tmp_path = tempfile.mktemp(suffix='.json')
    with open(tmp_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)
    result = get_operations_data(tmp_path)
    assert result == []

    if os.path.exists(tmp_path):
        os.remove(tmp_path)


def test_get_operations_data_decode_error():
    test_data = {"key" : "value"}
    tmp_path = tempfile.mktemp(suffix='.json')
    with open(tmp_path, 'w', encoding='utf-8') as f:
        f.write(str(test_data))
    result = get_operations_data(tmp_path)
    assert result == []

    if os.path.exists(tmp_path):
        os.remove(tmp_path)


def test_get_operations_data_wrong_file():
    test_data = {"key" : "value"}
    tmp_path = tempfile.mktemp(suffix='.json')
    with open(tmp_path, 'w', encoding='utf-8') as f:
        f.write(str(test_data))
    result = get_operations_data("tmp_path")
    assert result == []

    if os.path.exists(tmp_path):
        os.remove(tmp_path)