def get_mask_card_number(card_num: str) -> str | None:
    # Функцию маскировки номера банковской карты
    if card_num.isdigit() and len(card_num) == 16:
        return (f'{card_num[4:]}{card_num[4:6]}'
                f'{"*" * 2}{"*" * 4}{card_num[12:]}')
    else:
        return None


def get_mask_account(account_number: str) -> str | None:
    # Функцию маскировки номера банковского счета
    if account_number.isdigit() and len(account_number) == 20:
        return f'{"*" * 2} {account_number[-4::]}'
    else:
        return None


print(get_mask_card_number("7000792289606361"))
