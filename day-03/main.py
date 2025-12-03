from argparse import ArgumentParser
from pathlib import Path
from functools import lru_cache


def list_to_tuple(function):
    def wrapper(*args):
        args = [tuple(x) if isinstance(x, list) else x for x in args]
        result = function(*args)
        result = tuple(result) if isinstance(result, list) else result
        return result

    return wrapper


@list_to_tuple
@lru_cache
def biggest_n(ln: tuple[int], n: int):
    if len(ln) == 0:
        return None
    if n == 1:
        return max(ln)

    ignore = 0
    while ignore < len(ln):
        skip = len(ln) - ignore
        (i, biggest) = max(enumerate(ln[:skip]), key=lambda v: v[1])
        i += 1
        sub = biggest_n(ln[i:], n - 1)
        if sub is None:
            ignore += 1
        else:
            return int(f"{biggest}{sub}")
    return None


def parse(str_data: str):
    return [list(map(int, line)) for line in str_data.split()]


def part1(data):
    print(sum(biggest_n(ln, 2) for ln in data))


def part2(data):
    print(sum(biggest_n(ln, 12) for ln in data))


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
