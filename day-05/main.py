from argparse import ArgumentParser
from pathlib import Path


class InventorySystem:
    def __init__(self, fresh_ids: range, produce: list[int]):
        self.fresh_ids = fresh_ids
        self.produce = produce

    def __str__(self):
        return f'({self.fresh_ids}, {self.produce})'


def parse(str_data: str):
    ids, produce = str_data.split('\n\n')

    init_ids: list[range] = []
    for id in ids.split():
        start, stop = map(int, id.split('-'))
        init_ids.append(range(start, stop + 1))
    init_ids.sort(key=lambda r: r.start)

    fresh_ids = [init_ids[0]]
    for ids in init_ids[1:]:
        last = fresh_ids[-1]
        if ids.start in last and (ids.stop - 1) in last:
            continue
        elif last.start in ids and (last.stop - 1) in ids:
            fresh_ids[-1] = ids
        elif ids.start in last or last.stop == ids.start:
            fresh_ids[-1] = range(last.start, ids.stop)
        elif last.start in ids or ids.stop == ids.start:
            fresh_ids[-1] = range(ids.start, last.stop)
        else:
            fresh_ids.append(ids)

    produce = list(map(int, produce.split()))
    return InventorySystem(fresh_ids, produce)


def part1(data):
    print(
        sum(1 for p in data.produce if any(p in ids for ids in data.fresh_ids))
    )


def part2(data):
    print(sum(map(len, data.fresh_ids)))


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
