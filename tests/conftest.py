import pytest


@pytest.fixture
def mask_account_1():
    return "73654108430135874305"


@pytest.fixture
def mask_account_2():
    return "736541084301358743050203405"


@pytest.fixture
def mask_account_3():
    return "73654108430135"


@pytest.fixture
def mask_account_4():
    return "hello"


@pytest.fixture
def account_card_1():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_card_2():
    return "Счет 73654108430135874305"


@pytest.fixture
def account_card_3():
    return "Счет 7365410843"


@pytest.fixture
def account_card_4():
    return "Visa Platinum 700079228960636164757636"


@pytest.fixture
def test_list_3():
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_list_sort_date_2():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "T08:21:33.419441"},
    ]


@pytest.fixture
def test_list_sort_date_3():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def transactions_1():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264778,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206828",
            "operationAmount": {"amount": "9114.93", "currency": {"name": "rub", "code": "rub"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227681542",
            "to": "Счет 75651673383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def transactions_2():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "rub", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264778,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206828",
            "operationAmount": {"amount": "9114.93", "currency": {"name": "rub", "code": "rub"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227681542",
            "to": "Счет 75651673383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "rub", "code": "USD"}},
            "description": "Перевод со счета на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]

@pytest.fixture
def transactions_3():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264778,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206828",
            "operationAmount": {"amount": "9114.93", "currency": {"name": "rub", "code": "rub"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227681542",
            "to": "Счет 75651673383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
