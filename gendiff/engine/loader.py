import json
import yaml
import os


def load_json(file_path):
    """
    Safty load .json files.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def load_yaml(file_path):
    """
    Safty load .yaml files.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def load_file(file_path):
    """
    Load the contents of a file based on its extension.
    """
    _, extension = os.path.splitext(file_path)
    if extension == '.json':
        return load_json(file_path)
    elif extension == '.yaml' or extension == '.yml':
        return load_yaml(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")
