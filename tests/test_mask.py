import pytest

from src.mask import get_mask_account, get_mask_card_number


def test_1_get_mask_account(mask_account_1):
    assert get_mask_account(mask_account_1) == "**4305"


def test_2_get_mask_account_2(mask_account_2):
    assert get_mask_account(mask_account_2) == "Невернно введены данные"


def test_get_mask_account_(mask_account_3):
    assert get_mask_account(mask_account_3) == "Невернно введены данные"


def test_get_mask_account(mask_account_4):
    assert get_mask_account(mask_account_4) == "Введен неверный номер счета"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896063610167567489", "Невернно введены данные"),
        ("70007922896", "Невернно введены данные"),
        ("hello", "Введен неверный номер карты"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected
