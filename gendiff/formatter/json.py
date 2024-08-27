import json


def format_json(diff):
    return json.dumps(format_diff(diff), indent=4)


def format_diff(diff):
    result = {}
    for key, value in sorted(diff.items()):
        status = value['status']

        if status == 'nested':
            result[key] = format_diff(value['children'])
        elif status == 'added':
            result[key] = {
                'status': status,
                'value': format_value_json(value.get('value'))
            }
        elif status == 'removed':
            result[key] = {
                'status': status
            }
        elif status == 'changed':
            result[key] = {
                'status': status,
                'old_value': format_value_json(value.get('old_value')),
                'new_value': format_value_json(value.get('new_value'))
            }

    return result


def format_value_json(value):
    if isinstance(value, dict):
        return {k: format_value_json(v) for k, v in value.items()}
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return value
    return value
