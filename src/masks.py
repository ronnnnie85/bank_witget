def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу"""
    card_number_str = str(card_number)  # Преобразуем номер карты в строку

    first_part = card_number_str[:6]
    last_part = card_number_str[-4:]

    masked_part = "** ****"  # Замаскированная часть

    masked_card_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"

    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу"""
    account_number_str = str(account_number)  # Преобразуем номер счета в строку

    last_four_digits = account_number_str[-4:]

    masked_account = f"**{last_four_digits}"

    return masked_account
