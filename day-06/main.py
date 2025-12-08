from argparse import ArgumentParser
from pathlib import Path


def dbg(x):
    print(x)
    return x


def product(iter):
    prod = 1
    for i in iter:
        prod *= i
    return prod


def part1(data: str):
    operations, *rows = reversed(data.splitlines())
    operations = operations.split()
    rows = zip(*(map(int, row.split()) for row in rows))
    print(
        sum(
            sum(row) if op == '+' else product(row)
            for op, row in zip(operations, rows)
        )
    )


def part2(data: str):
    operations, *rows = reversed(data.splitlines())
    operations = list(reversed(operations.split()))
    rows = (
        map(int, row.split(','))
        for row in ','.join(
            ''.join(reversed(row)).strip()
            for row in zip(*(reversed(line) for line in rows))
        ).split(',,')
    )
    print(
        sum(
            sum(row) if op == '+' else product(row)
            for op, row in zip(operations, rows)
        )
    )


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

    if args.part in ['both', 'part1']:
        part1(file_data)

    if args.part in ['both', 'part2']:
        part2(file_data)


if __name__ == '__main__':
    main()
