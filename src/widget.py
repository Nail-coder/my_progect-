from datetime import datetime

from src.macks import get_mask_account, get_mask_card_number


def mask_account_card(nums: str) -> str:
    nums_list = nums.split()
    if nums_list[0] == 'Счет':
        account = get_mask_account(nums[-20:])
        new_account = nums.replace(nums[-20:], account)
        return new_account
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 12345678901234567892"))


def get_data(data: str) -> str:
    if data == "":
        return ""

    d = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
    return d.strftime("%d.%m.%Y")


print(get_data("2024-03-11T02:26:18.671407"))
