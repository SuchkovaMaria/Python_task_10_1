import pytest

@pytest.fixture
def mask_account_1():
    return '73654108430135874305'

@pytest.fixture
def mask_account_2():
    return '736541084301358743050203405'

@pytest.fixture
def mask_account_3():
    return '73654108430135'

@pytest.fixture
def mask_account_4():
    return 'hello'

@pytest.fixture
def account_card_1():
    return 'Visa Platinum 7000792289606361'

@pytest.fixture
def account_card_2():
    return 'Счет 73654108430135874305'

@pytest.fixture
def account_card_3():
    return 'Счет 7365410843'

@pytest.fixture
def account_card_4():
    return 'Visa Platinum 700079228960636164757636'

