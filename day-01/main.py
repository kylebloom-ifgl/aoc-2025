from argparse import ArgumentParser
from pathlib import Path


class Safe:
    def __init__(self, start=0, size=100):
        self.dial = start
        self.size = size

    def left(self, distance):
        pass_zero = distance // self.size
        distance %= self.size
        new_loc = self.dial - distance
        pass_zero += 1 if new_loc <= 0 and self.dial != 0 else 0
        self.dial = new_loc % self.size
        return pass_zero

    def right(self, distance):
        pass_zero = distance // self.size
        distance %= self.size
        new_loc = self.dial + distance
        pass_zero += 1 if new_loc >= self.size and self.dial != 0 else 0
        self.dial = new_loc % self.size
        return pass_zero


def parse(str_data: str):
    return [(line[0], int(line[1:])) for line in str_data.split()]


def part1(data):
    safe = Safe(start=50)
    count = 0

    for direction, distance in data:
        if direction == "R":
            safe.right(distance)
        elif direction == "L":
            safe.left(distance)
        else:
            raise ValueError("Invalid direction")

        count += 1 if safe.dial == 0 else 0

    print(count)


def part2(data):
    safe = Safe(start=50)
    count = 0

    for direction, distance in data:
        if direction == "R":
            count += safe.right(distance)
        elif direction == "L":
            count += safe.left(distance)
        else:
            raise ValueError("Invalid direction")

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
