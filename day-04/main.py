from argparse import ArgumentParser
from pathlib import Path
from itertools import product
from copy import deepcopy


def neighbors_count(nh: list[str], row: int, col: int):
    rows, cols = len(nh), len(nh[0])
    up, down = row - 1, row + 1
    left, right = col - 1, col + 1

    rs = (r for r in (up, row, down) if 0 <= r and r < rows)
    cs = (c for c in (left, col, right) if 0 <= c and c < cols)

    return sum(
        1 for r, c in product(rs, cs) if (r != row or c != col) and nh[r][c] == "@"
    )


def parse(str_data: str):
    return str_data.splitlines()


def part1(data):
    print(
        sum(
            1
            for r, row in enumerate(data)
            for c, roll in enumerate(row)
            if roll == "@" and neighbors_count(data, r, c) < 4
        )
    )


def part2(data):
    data = deepcopy(data)
    count = 0
    removed = True

    while removed:
        removals = list(
            (r, c)
            for r, row in enumerate(data)
            for c, roll in enumerate(row)
            if roll == "@" and neighbors_count(data, r, c) < 4
        )
        for r, c in removals:
            data[r] = data[r][:c] + "." + data[r][c + 1 :]
        count += len(removals)
        removed = len(removals) > 0
    print(count)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "input",
        default=Path("./input.txt"),
        type=Path,
        nargs="?",
        help="Path to the input file",
    )
    parser.add_argument(
        "-p", "--part", default="both", choices=["both", "part1", "part2"]
    )
    args = parser.parse_args()

    with open(args.input, "r") as input_file:
        file_data = input_file.read()

    data = parse(file_data)

    if args.part in ["both", "part1"]:
        part1(data)

    if args.part in ["both", "part2"]:
        part2(data)


if __name__ == "__main__":
    main()
