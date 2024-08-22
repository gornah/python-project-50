import os
from gendiff.loader import load_json, load_yaml


def load_file(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == '.json':
        return load_json(file_path)
    elif extension == '.yaml' or extension == '.yml':
        return load_yaml(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")


def compare_files(file1, file2):
    differences = []
    all_keys = sorted(set(file1.keys()).union(file2.keys()))
    for key in all_keys:
        if key in file1 and key not in file2:
            differences.append(f'  - {key}: {file1[key]}')
        elif key in file2 and key not in file1:
            differences.append(f'  + {key}: {file2[key]}')
        elif file1[key] != file2[key]:
            differences.append(f'  - {key}: {file1[key]}')
            differences.append(f'  + {key}: {file2[key]}')
        else:
            differences.append(f'    {key}: {file1[key]}')
    return differences


def generate_diff(file_path1, file_path2):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    differences = compare_files(data1, data2)

    return '{\n' + '\n'.join(differences) + '\n}'
