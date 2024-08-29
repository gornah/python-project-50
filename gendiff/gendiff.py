from gendiff.engine.loader import load_file
from gendiff.engine.comparer import compare_files
from gendiff.formatter import get_format


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    differences = compare_files(data1, data2)
    format_style = get_format(formatter)
    return format_style(differences)
