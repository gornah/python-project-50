from gendiff.engine.loader import load_file
from gendiff.engine.comparer import compare_files
from gendiff.formatters import get_format


def generate_diff(file_path1, file_path2, formatter='stylish'):
    """
    Generate a difference between two configuration files.

    This function compares the contents of two files and returns the difference
    in a specified format. Supported formats include "stylish", "plain", "json".
    """
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    differences = compare_files(data1, data2)
    format_style = get_format(formatter)
    return format_style(differences)
