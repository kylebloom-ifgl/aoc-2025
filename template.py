from argparse import ArgumentParser
from pathlib import Path


def parse(str_data: str):
    pass


def part1(data):
    pass


def part2(data):
    pass


def main():
    parser = ArgumentParser()
    parser.add_argument(
        'input',
        default=Path('./input.txt'),
        type=Path,
        nargs='?',
        help='Path to the input file',
    )
    parser.add_argument(
        '-p', '--part', default='both', choices=['both', 'part1', 'part2']
    )
    args = parser.parse_args()

    with open(args.input, 'r') as input_file:
        file_data = input_file.read()

    data = parse(file_data)

    if args.part in ['both', 'part1']:
        part1(data)

    if args.part in ['both', 'part2']:
        part2(data)


if __name__ == '__main__':
    main()
