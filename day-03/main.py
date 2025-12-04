from argparse import ArgumentParser
from pathlib import Path


def biggest_n(ln: list[str], n: int):
    acc = ''
    for r in range(n - 1, -1, -1):
        skip = len(ln) - r
        (i, biggest) = max(enumerate(ln[:skip]), key=lambda v: v[1])
        acc += biggest
        ln = ln[i + 1 :]
    return acc


def parse(str_data: str):
    return str_data.split()


def part1(data):
    print(sum(int(biggest_n(ln, 2)) for ln in data))


def part2(data):
    print(sum(int(biggest_n(ln, 12)) for ln in data))


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
