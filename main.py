from src.widget import get_date, mask_account_card

print(mask_account_card("Maestro         1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 715830073476758"))
print(mask_account_card("account 35383033474447895560"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))

print(get_date("2024-03-11T02:26:18.671407"))