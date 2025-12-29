from src.processing import filter_by_state, sort_by_date, filter_by_description, counting_categories


def test_filter_by_state_1():
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_2():
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    ) == (
        [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )


def test_filter_by_state_3(test_list_3):
    assert filter_by_state(test_list_3) == []


def test_sort_by_date_1():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_2(test_list_sort_date_2):
    assert sort_by_date(test_list_sort_date_2) == []


def test_sort_by_date_3(test_list_sort_date_3):
    assert sort_by_date(test_list_sort_date_3) == []


def test_sort_by_date_4():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

def test_filter_by_description_1(dict_csv_1):
    assert filter_by_description(dict_csv_1, "организации") == [{'amount': '16210', 'currency_code': 'PEN', 'currency_name': 'Sol', 'date': '2023-09-05T11:30:32Z', 'description': 'Перевод организации', 'from': 'Счет 58803664561298323391', 'id': '650703', 'state': 'EXECUTED', 'to': 'Счет 39745660563456619397'}]

def test_filter_by_description_2(dict_csv_1):
    assert filter_by_description(dict_csv_1, "123") == []

def test_filter_by_description_3(dict_csv_1):
    assert filter_by_description(dict_csv_1, "") == []

def test_filter_by_description_4():
    assert filter_by_description([], "перевод") == []

def test_counting_categories_1(dict_csv_1):
    assert counting_categories(dict_csv_1) == {'EXECUTED': 2, 'CANCELED': 1}

def test_counting_categories_2():
    assert counting_categories([]) == {}