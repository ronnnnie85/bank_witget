from unittest.mock import patch

from main import main


@patch("main.search_for_string")
@patch("main.mask_account_card")
@patch("main.sort_by_date")
@patch("main.filter_by_state")
@patch("builtins.input")
def test_main(
    mock_input,
    mock_filter_by_state,
    mock_sort_by_date,
    mock_mask_account_card,
    mock_search_for_string,
    true_transactions,
):
    mock_search_for_string.side_effect = Exception("Тестовая ошибка")
    mock_mask_account_card.side_effect = Exception("Тестовая ошибка")
    mock_sort_by_date.side_effect = Exception("Тестовая ошибка")
    mock_filter_by_state.side_effect = Exception("Тестовая ошибка")
    mock_input.side_effect = [
        "4",
        "1",
        "Ex",
        "EXECUTED",
        "y",
        "y",
        "y",
        "y",
        "Открытие",
        "N",
    ]
    main()
    mock_input.side_effect = [
        "2",
        "EXECUTED",
        "y",
        "y",
        "N",
        "y",
        "Открытие",
        "N",
    ]
    main()
    mock_input.side_effect = [
        "3",
        "EXECUTED",
        "y",
        "y",
        "N",
        "y",
        "Открытие",
        "N",
    ]
    main()


@patch("main.filter_by_state")
@patch("builtins.input")
def test_main_no_trans(mock_input, mock_filter_by_state, true_transactions):
    mock_filter_by_state.side_effect = [[], true_transactions]
    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "1",
        "EXECUTED",
        "N",
        "N",
        "N",
        "Перевод",
        "N",
    ]
    main()


@patch("main.filter_by_currency")
@patch("builtins.input")
def test_main_no_trans1(
    mock_input, mock_filter_by_currency, true_transactions
):
    mock_filter_by_currency.side_effect = [[], true_transactions]
    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "N",
        "y",
        "1",
        "EXECUTED",
        "N",
        "N",
        "N",
        "N",
    ]
    main()


@patch("main.search_for_string")
@patch("builtins.input")
def test_main_no_trans2(mock_input, mock_search_for_string, true_transactions):
    mock_search_for_string.return_value = []
    mock_input.side_effect = [
        "1",
        "EXECUTED",
        "N",
        "N",
        "y",
        "Перевод",
        "1",
        "EXECUTED",
        "N",
        "N",
        "N",
        "N",
    ]
    main()
