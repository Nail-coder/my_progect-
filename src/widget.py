from src import macks

def mask_account_card(nums: str) -> str:
    if 'счет' in nums:
        return macks.get_mask_account(nums)
    else:
        cards = macks.get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card

print(mask_account_card("Visa Platinum 7000792289606361"))

def get_data(data:str) -> str:
    return f'{data[8:10], {data[5:7]}, {data[0:4]}}'

print(get_data("2024-03-11T02:26:18.671407"))