import os
from gendiff.gendiff import generate_diff


def test_gendiff():
    file1 = os.path.join('tests', 'fixtures', 'file1.json')
    file2 = os.path.join('tests', 'fixtures', 'file2.json')
    result_file = os.path.join('tests', 'fixtures', 'result.txt')
    with open(result_file, 'r') as file:
        result_diff = file.read()
    diff = generate_diff(file1, file2)
    assert diff == result_diff
