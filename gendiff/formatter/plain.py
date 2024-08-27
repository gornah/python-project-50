def format_plain(diff, path=''):
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
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
