def compare_files(file1, file2):
    """
    Compare two dictionaries representing file contents and return their
    differences.
    -------
    Returns a dictionary representing the differences between the two files.
    The keys represent the property names, and the values are dictionaries
    describing the status ('added', 'removed', 'nested', 'changed', 'unchanged')
    and relevant data (e.g., 'value', 'old_value', 'new_value', 'children').
    """

    diff = {}
    all_keys = set(file1.keys()).union(file2.keys())

    for key in all_keys:
        if key not in file2:
            diff[key] = {'status': 'removed', 'value': file1[key]}
        elif key not in file1:
            diff[key] = {'status': 'added', 'value': file2[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = {
                'status': 'nested',
                'children': compare_files(file1[key], file2[key])
            }
        elif file1[key] != file2[key]:
            diff[key] = {
                'status': 'changed',
                'old_value': file1[key],
                'new_value': file2[key]
            }
        else:
            diff[key] = {'status': 'unchanged', 'value': file1[key]}

    return diff
