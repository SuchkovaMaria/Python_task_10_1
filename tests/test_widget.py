import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(account_card_1):
    assert mask_account_card(account_card_1) == "Visa Platinum 7000 79** **** 6361"


def test_2_mask_account_card(account_card_2):
    assert mask_account_card(account_card_2) == "Счет **4305"


def test_3_mask_account_card(account_card_3):
    assert mask_account_card(account_card_3) == "Невернно введены данные"


def test_4_mask_account_card(account_card_4):
    assert mask_account_card(account_card_4) == "Невернно введены данные"


@pytest.mark.parametrize(
    "time_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("T02:26:18.671407", "Неверно введены данные"),
    ],
)
def test_get_date(time_date, expected):
    assert get_date(time_date) == expected
