def format_plain(diff, path=''):
    """
    Format the difference between two data structures in a plain text style.

    This function generates a plain text representation of the differences
    between two data structures, typically JSON or YAML, by traversing
    through the nested dictionary `diff`. The output reflects the changes
    in a human-readable format that highlights added, removed, and modified
    properties.
    """
    lines = []

    for key, value in sorted(diff.items()):
        current_path = f'{path}.{key}' if path else key
        status = value['status']

        if status == 'nested':
            lines.append(format_plain(value['children'], current_path))
        elif status == 'added':
            formated_value = format_value_plain(value['value'])
            lines.append(
                f"Property '{current_path}' was added with value: "
                f"{formated_value}"
            )
        elif status == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif status == 'changed':
            old_value = format_value_plain(value['old_value'])
            new_value = format_value_plain(value['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return '\n'.join(lines)


def format_value_plain(value):
    """
    Format a value for plain text representation.

    This function takes a value and formats it for inclusion in a plain text
    difference report. The formatting is based on the type of the value:
    - Dictionaries are represented as '[complex value]'.
    - Booleans are converted to 'true' or 'false'.
    - None is represented as 'null'.
    - Strings are enclosed in single quotes.
    - Other types are converted to their string representation.
    """
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
