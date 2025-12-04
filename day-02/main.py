from argparse import ArgumentParser
from pathlib import Path


def window(iter):
    prev = next(iter)
    for cur in iter:
        yield (prev, cur)
        prev = cur


def chunk(s, width):
    for i in range(0, len(s), width):
        yield s[i : i + width]


def range_from(s):
    start, end = map(int, s.split('-'))
    return range(start, end + 1)


def is_repeat(i):
    s = str(i)
    mid = len(s) // 2
    return s[:mid] == s[mid:]


def is_silly(i):
    s = str(i)
    return any(
        all(a == b for a, b in window(chunk(s, pos)))
        for pos in range(1, (len(s) // 2) + 1)
    )


def parse(str_data):
    return [range_from(s) for s in str_data.split(',')]


def part1(data):
    answer = sum(i for r in data for i in r if is_repeat(i))
    print(answer)


def part2(data):
    answer = sum(i for r in data for i in r if is_silly(i))
    print(answer)


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
