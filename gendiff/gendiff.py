import os
from gendiff.loader import load_json, load_yaml
from gendiff.formatter.stylish import format_stylish
from gendiff.formatter.plain import format_plain
from gendiff.formatter.json import format_json


def load_file(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == '.json':
        return load_json(file_path)
    elif extension == '.yaml' or extension == '.yml':
        return load_yaml(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")


def compare_files(file1, file2):
    diff = {}
    all_keys = set(file1.keys()).union(file2.keys())

    for key in all_keys:
        if key not in file2:
            diff[key] = {'status': 'removed', 'value': file1[key]}
        elif key not in file1:
            diff[key] = {'status': 'added', 'value': file2[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = {
                'status': 'nested',
                'children': compare_files(file1[key], file2[key])
            }
        elif file1[key] != file2[key]:
            diff[key] = {
                'status': 'changed',
                'old_value': file1[key],
                'new_value': file2[key]
            }
        else:
            diff[key] = {'status': 'unchanged', 'value': file1[key]}

    return diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    differences = compare_files(data1, data2)

    if formatter == 'stylish':
        return format_stylish(differences, depth=0)
    if formatter == 'plain':
        return format_plain(differences, path='')
    if formatter == 'json':
        return format_json(differences)
    else:
        raise ValueError(f"Unknown formatter: {formatter}")
