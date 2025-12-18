import os

from src.utils import convertions_json_in_list


def test_convertions_json_in_list_1(list_transactions_1):
    dir = os.getcwd()
    absolute_path = os.path.join(dir, "..")
    os.chdir(absolute_path)
    path_to_direct = os.path.dirname(__file__)
    path_to_file_1 = os.path.join(path_to_direct, "..", "data", "operations.json")
    assert convertions_json_in_list(path_to_file_1) == list_transactions_1


def test_convertions_json_in_list_2():
    path_to_direct = os.path.dirname(__file__)
    path_to_file_1 = os.path.join(path_to_direct, "..", "dat", "operations.json")
    assert convertions_json_in_list(path_to_file_1) == []
