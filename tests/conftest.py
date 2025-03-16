import pytest


@pytest.fixture
def non_int_str_value():
    return True


@pytest.fixture
def non_digit_str_value():
    return "value"


@pytest.fixture
def non_str_value():
    return 0.0


@pytest.fixture
def default_list():
    return [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
    ]


@pytest.fixture
def wrong_type_col():
    return {"key": "value"}


@pytest.fixture
def wrong_list():
    return ["key1", "key2"]


@pytest.fixture
def wrong_dict_key():
    return [
        {
            15: 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
    ]


@pytest.fixture
def wrong_dict_value():
    return [
        {
            "id": 41428829,
            "state": True,
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
    ]


@pytest.fixture
def right_list_1():
    return [
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


@pytest.fixture
def right_list_2():
    return [
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
    ]


@pytest.fixture
def empty_list():
    return []
