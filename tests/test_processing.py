import pytest

from src.processing import filter_by_state, sort_by_date


# Функция mask_account_card
@pytest.mark.parametrize(
    "data_fixture, state, excepted",
    [
        (
            "right_list_1",
            "CANCELED",
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                }
            ],
        ),
        (
            "right_list_2",
            "EXECUTED",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                }
            ],
        ),
        ("empty_list", "CANCELED", []),
    ],
)
def test_filter_by_state(request, data_fixture, state, excepted):
    data = request.getfixturevalue(data_fixture)
    assert filter_by_state(data, state) == excepted


def test_filter_by_state_empty(default_list):
    assert filter_by_state(default_list) == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        }
    ]


@pytest.mark.parametrize(
    "col_fixture",
    ["wrong_type_col", "wrong_list", "wrong_dict_key", "wrong_dict_value"],
)
def test_filter_by_state_wrong_types(request, col_fixture):
    with pytest.raises(TypeError) as exc_info:
        data = request.getfixturevalue(col_fixture)
        filter_by_state(data)

    assert str(exc_info.value) == "Ошибка: некорректный тип входных данных."


# Функция sort_by_date
@pytest.mark.parametrize(
    "data_fixture, descending, excepted",
    [
        (
            "right_list_1",
            True,
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
            ],
        ),
        (
            "right_list_2",
            False,
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
        ),
        ("empty_list", False, []),
    ],
)
def test_sort_by_date(request, data_fixture, descending, excepted):
    data = request.getfixturevalue(data_fixture)
    assert sort_by_date(data, descending) == excepted


def test_sort_by_date_empty(default_list):
    assert sort_by_date(default_list) == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
    ]


@pytest.mark.parametrize(
    "col_fixture",
    ["wrong_type_col", "wrong_list", "wrong_dict_key", "wrong_dict_value"],
)
def test_sort_by_date_wrong_types(request, col_fixture):
    with pytest.raises(TypeError) as exc_info:
        data = request.getfixturevalue(col_fixture)
        sort_by_date(data)

    assert str(exc_info.value) == "Ошибка: некорректный тип входных данных."


@pytest.mark.parametrize(
    "data",
    [
        [
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12",
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019/07/03T18:35:29.512364",
            },
        ],
        [
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018.09.12",
            },
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019.12.15",
            },
        ],
    ],
)
def test_sort_by_date_wrong_date(data):
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(data)

    assert str(exc_info.value) == "Ошибка: некорректный формат даты."
