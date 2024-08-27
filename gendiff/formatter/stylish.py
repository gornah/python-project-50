def format_stylish(diff, depth=0):
    lines = []
    indent_size = 4
    indent = ' ' * (depth * indent_size)

    for key, value in sorted(diff.items()):
        lines.extend(process_diff_entry(key, value, depth))

    return '{\n' + '\n'.join(lines) + f'\n{indent}}}'


def process_diff_entry(key, value, depth):
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
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    nested = format_stylish(children, depth + 1)
    return [f"{indent}    {key}: {nested}"]


def format_changed_entry(key, value, depth):
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    return [
        f"{indent}  - {key}: {format_value(value['old_value'], depth + 1)}",
        f"{indent}  + {key}: {format_value(value['new_value'], depth + 1)}"
    ]


def format_value(value, depth):
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
