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
        'result_stylish': os.path.join('tests', 'fixtures', 'result_style.txt'),
        'result_plain': os.path.join('tests', 'fixtures', 'result_plain.txt')
    }


@pytest.fixture
def expected_result(file_path):
    results = {}
    for key in ['stylish', 'plain']:
        result_path = file_path[f'result_{key}']
        with open(result_path, 'r') as file:
            results[key] = file.read()
    return results


def test_gendiff_json_style(file_path, expected_result):
    diff = generate_diff(file_path['json1'],
                         file_path['json2'],
                         formatter='stylish')
    assert diff == expected_result['stylish']


def test_gendiff_yaml_style(file_path, expected_result):
    diff = generate_diff(file_path['yaml1'],
                         file_path['yaml2'],
                         formatter='stylish')
    assert diff == expected_result['stylish']


def test_gendiff_json_plain(file_path, expected_result):
    diff = generate_diff(file_path['json1'],
                         file_path['json2'],
                         formatter='plain')
    assert diff == expected_result['plain']


def test_gendiff_yaml_plain(file_path, expected_result):
    diff = generate_diff(file_path['yaml1'],
                         file_path['yaml2'],
                         formatter='plain')
    assert diff == expected_result['plain']
