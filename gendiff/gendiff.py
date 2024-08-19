import json


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def compare_json(json1, json2):
    differences = []
    all_keys = sorted(set(json1.keys()).union(json2.keys()))
    for key in all_keys:
        if key in json1 and key not in json2:
            differences.append(f'- {key}: {json1[key]}')
        elif key in json2 and key not in json1:
            differences.append(f'+ {key}: {json2[key]}')
        elif json1[key] != json2[key]:
            differences.append(f'- {key}: {json1[key]}')
            differences.append(f'+ {key}: {json2[key]}')
        else:
            differences.append(f'  {key}: {json1[key]}')
    return differences


def generate_diff(file_path1, file_path2):
    json1 = load_json(file_path1)
    json2 = load_json(file_path2)
    differences = compare_json(json1, json2)
    return '{\n'+'\n'.join(differences)+'\n}'
