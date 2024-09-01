import argparse


def parse_arguments():
    """
    Parse and return command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output (default: "stylish")',
        default='stylish'
    )
    return parser.parse_args()
