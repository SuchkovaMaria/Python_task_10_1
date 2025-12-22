import csv
import os
from unittest.mock import Mock, patch


from src.reading_operations import reading_fin_operations_csv, reading_fin_operations_xlsx


def test_reading_fin_operations_csv_1(dict_csv_1):
    dir = os.getcwd()
    absolute_path = os.path.join(dir, "..")
    os.chdir(absolute_path)
    path_to_direct = os.path.dirname(__file__)
    path_to_file_1 = os.path.join(path_to_direct, "..", "data", "transactions.csv")
    mock_csv = Mock(return_value=dict_csv_1)
    csv.DictReader = mock_csv
    assert reading_fin_operations_csv(path_to_file_1) == dict_csv_1
    mock_csv.assert_called_once()


def test_reading_fin_operations_csv_2():
    dir = os.getcwd()
    absolute_path = os.path.join(dir, "..")
    os.chdir(absolute_path)
    path_to_direct = os.path.dirname(__file__)
    path_to_file_1 = os.path.join(path_to_direct, "..", "dat", "transactions.csv")
    assert reading_fin_operations_csv(path_to_file_1) == []


def test_reading_fin_operations_csv_3():
    dir = os.getcwd()
    absolute_path = os.path.join(dir, "..")
    os.chdir(absolute_path)
    path_to_direct = os.path.dirname(__file__)
    path_to_file_1 = os.path.join(path_to_direct, "..", "data", "transactions.csv")
    mock_csv = Mock(return_value=[])
    csv.DictReader = mock_csv
    assert reading_fin_operations_csv(path_to_file_1) == []
    mock_csv.assert_called_once()


@patch("src.reading_operations.pd.read_excel")
def test_reading_fin_operations_xlsx_1(mock_xlsx, dict_xlsx_1):
    dir = os.getcwd()
    absolute_path = os.path.join(dir, "..")
    os.chdir(absolute_path)
    path_to_direct = os.path.dirname(__file__)
    path_to_file_2 = os.path.join(path_to_direct, "..", "data", "transactions_excel.xlsx")
    mock_xlsx.return_value.to_dict.return_value = dict_xlsx_1
    assert reading_fin_operations_xlsx(path_to_file_2) == dict_xlsx_1
    mock_xlsx.assert_called_once()


@patch("src.reading_operations.pd.read_excel")
def test_reading_fin_operations_xlsx_2(mock_xlsx, dict_xlsx_1):
    dir = os.getcwd()
    absolute_path = os.path.join(dir, "..")
    os.chdir(absolute_path)
    path_to_direct = os.path.dirname(__file__)
    path_to_file_2 = os.path.join(path_to_direct, "..", "data", "transactions_excel.xlsx")
    mock_xlsx.return_value = dict_xlsx_1
    assert reading_fin_operations_xlsx(path_to_file_2) == {}
    mock_xlsx.assert_called_once()
