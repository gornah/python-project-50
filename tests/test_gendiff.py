import os
import pytest
import json
from gendiff.gendiff import generate_diff
from gendiff.engine.loader import load_file


@pytest.fixture
def file_path():
    return {
        'json1': os.path.join('tests', 'fixtures', 'file1.json'),
        'json2': os.path.join('tests', 'fixtures', 'file2.json'),
        'yaml1': os.path.join('tests', 'fixtures', 'file1.yml'),
        'yaml2': os.path.join('tests', 'fixtures', 'file2.yml'),
        'result_stylish': os.path.join('tests', 'fixtures', 'result_style.txt'),
        'result_plain': os.path.join('tests', 'fixtures', 'result_plain.txt'),
        'result_json': os.path.join('tests', 'fixtures', 'result_json.txt')
    }


@pytest.fixture
def expected_result(file_path):
    results = {}
    for key in ['stylish', 'plain', 'json']:
        result_path = file_path[f'result_{key}']
        with open(result_path, 'r') as file:
            if key == 'json':
                results[key] = json.load(file)
            else:
                results[key] = file.read()
    return results


@pytest.mark.parametrize("file1_key, file2_key, formatter, result_key", [
    ('json1', 'json2', 'stylish', 'stylish'),
    ('yaml1', 'yaml2', 'stylish', 'stylish'),
    ('json1', 'json2', 'plain', 'plain'),
    ('yaml1', 'yaml2', 'plain', 'plain'),
    ('json1', 'json2', 'json', 'json'),
    ('yaml1', 'yaml2', 'json', 'json'),
])
def test_gendiff(file_path, expected_result,
                 file1_key, file2_key, formatter, result_key):

    diff = generate_diff(file_path[file1_key], file_path[file2_key],
                         formatter=formatter)
    if formatter == 'json':
        assert json.loads(diff) == expected_result[result_key]
    else:
        assert diff == expected_result[result_key]


def test_unsupported_file_extension():
    with pytest.raises(ValueError,
                       match='Unsupported file format: .unsupported'):
        load_file('file.unsupported')


def test_unsupported_format():
    with pytest.raises(ValueError,
                       match='Unknown formatter: Unsupported_formatter'):
        generate_diff('tests/fixtures/file1.json',
                      'tests/fixtures/file2.json',
                      formatter='Unsupported_formatter')
