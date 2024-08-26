#!/usr/bin/env python3
import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output (default: "stylish")',
                        default='stylish')
    args = parser.parse_args()
#   parser.print_help()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
