def format_stylish(diff, depth=0):
    """
    Format a nested dictionary into a stylish string representation.

    This function takes a dictionary representing the differences between two
    configuration files and formats it into a string with a "stylish" format.
    The stylish format uses indentation to represent the hierarchy of the
    nested structures, making it easy to read.
    """
    lines = []
    indent_size = 4
    indent = ' ' * (depth * indent_size)

    for key, value in sorted(diff.items()):
        lines.extend(process_diff_entry(key, value, depth))

    return '{\n' + '\n'.join(lines) + f'\n{indent}}}'


def process_diff_entry(key, value, depth):
    """
    Process a single entry in the difference dictionary and generate the
    corresponding formatted output line(s).

    This function handles formatting of a single key-value entry in the
    difference dictionary based on its status. It produces appropriately
    indented lines for each type of status: 'nested', 'added', 'removed',
    'changed', and 'unchanged'. It calls helper functions to handle
    specific formatting requirements.
    """
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    status = value.get('status')

    if status == 'nested':
        return format_nested_entry(key, value['children'], depth)
    if status == 'added':
        return [f"{indent}  + {key}: {format_value(value['value'], depth + 1)}"]
    if status == 'removed':
        return [f"{indent}  - {key}: {format_value(value['value'], depth + 1)}"]
    if status == 'changed':
        return format_changed_entry(key, value, depth)
    return [f"{indent}    {key}: {format_value(value['value'], depth + 1)}"]


def format_nested_entry(key, children, depth):
    """
    Format a nested entry in the difference dictionary.

    This function handles the formatting of properties that have nested
    differences. It generates a properly indented formatted block for
    nested properties and their differences.
    """
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    nested = format_stylish(children, depth + 1)
    return [f"{indent}    {key}: {nested}"]


def format_changed_entry(key, value, depth):
    """
    Format a changed entry in the difference dictionary.

    This function generates a formatted representation for properties that have
    changed values between two configurations. It produces two lines:
    one indicating the old value (with a minus sign) and one indicating the
    new value (with a plus sign). The lines are indented according to the
    specified depth.
    """
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    return [
        f"{indent}  - {key}: {format_value(value['old_value'], depth + 1)}",
        f"{indent}  + {key}: {format_value(value['new_value'], depth + 1)}"
    ]


def format_value(value, depth):
    """
    Format a value for inclusion in a difference output.

    This function formats various types of values for inclusion in the output
    of a difference comparison. It handles:
    - nested dictionaries
    - boolean values
    - `None` values
    and formats them with proper indentation based on the specified depth.
    """
    indent_size = 4
    indent = ' ' * ((depth + 1) * indent_size)

    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            lines.append(f"{indent}{key}: {format_value(val, depth + 1)}")
        lines.append(f"{' ' * (depth * indent_size)}}}")
        return '\n'.join(lines)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return "null"
    return str(value)
