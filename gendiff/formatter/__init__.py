from .stylish import format_stylish
from .plain import format_plain
from .json import format_json


def get_format(formatter_name):
    if formatter_name == 'stylish':
        return format_stylish
    elif formatter_name == 'plain':
        return format_plain
    elif formatter_name == 'json':
        return format_json
    else:
        raise ValueError(f"Unknown formatter: {formatter_name}")
