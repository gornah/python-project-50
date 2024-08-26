import os
import pytest
from gendiff.gendiff import generate_diff
# from gendiff.loader import load_json, load_yaml


@pytest.fixture
def file_path():
    return {
        'json1': os.path.join('tests', 'fixtures', 'file1.json'),
        'json2': os.path.join('tests', 'fixtures', 'file2.json'),
        'yaml1': os.path.join('tests', 'fixtures', 'file1.yml'),
        'yaml2': os.path.join('tests', 'fixtures', 'file2.yml'),
        'result': os.path.join('tests', 'fixtures', 'result.txt')
    }


@pytest.fixture
def expected_result(file_path):
    with open(file_path['result'], 'r') as file:
        return file.read()


def test_gendiff_json(file_path, expected_result):
    # data1 = load_json(file_path['json1'])
    # data2 = load_json(file_path['json2'])
    diff = generate_diff(file_path['json1'],
                         file_path['json2'],
                         formatter='stylish')
    assert diff == expected_result


def test_gendiff_yaml(file_path, expected_result):
    # data1 = load_yaml(file_path['yaml1'])
    # data2 = load_yaml(file_path['yaml2'])
    diff = generate_diff(file_path['yaml1'],
                         file_path['yaml2'],
                         formatter='stylish')
    assert diff == expected_result
