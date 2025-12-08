from argparse import ArgumentParser
from pathlib import Path
from copy import deepcopy


def parse(str_data: str):
    start, *rows = str_data.splitlines()
    return (
        [c == 'S' for c in start],
        [[c == '^' for c in row] for row in rows if any(c != '.' for c in row)],
    )


def part1(data):
    line, rows = deepcopy(data)
    count = 0
    for row in rows:
        for i, r in enumerate(row):
            if line[i] and r:
                line[i - 1], line[i + 1], line[i] = True, True, False
                count += 1
    print(count)


def part2(data):
    line, rows = data
    line = list(map(int, line))
    for row in rows:
        for i, r in enumerate(row):
            if line[i] and r:
                line[i - 1] += line[i]
                line[i + 1] += line[i]
                line[i] = 0
    print(sum(line))


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
