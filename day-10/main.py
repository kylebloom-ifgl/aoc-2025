from argparse import ArgumentParser
from pathlib import Path
from typing import Iterable
from z3 import Optimize, Int, Sum, sat
import re


def dbg(a):
    print(a)
    return a


def Eq(a, b):
    return a == b


class Button:
    def __init__(self, data: str | Iterable[int]):
        if isinstance(data, str):
            self.indexes = {int(c) for c in data.split(',')}
        else:
            self.indexes = set(data)

    def bool_mask(self, size):
        return [i in self.indexes for i in range(size)]


class LightPanel:
    lights: list[bool]

    def __init__(self, data: str | Iterable[bool]):
        if isinstance(data, str):
            self.lights = [c == '#' for c in data]
        else:
            self.lights = list(data)

    def __hash__(self):
        h = 0
        for light in self.lights:
            h = (h << 1) ^ int(light)
        return h

    def __eq__(self, value: 'LightPanel'):
        return self.lights == value.lights

    def __str__(self):
        return f'LightPanel({"".join("#" if light else "." for light in self.lights)})'

    def off(self):
        return LightPanel(False for _ in self.lights)

    def toggle(self, button: Button) -> 'LightPanel':
        return LightPanel(
            p ^ b
            for p, b in zip(self.lights, button.bool_mask(len(self.lights)))
        )


class BatteryBank:
    def __init__(self, power_levels: str):
        self.power_levels = [int(p) for p in power_levels.split(',')]

    def __len__(self):
        return len(self.power_levels)


class Machine:
    def __init__(self, str_data: str):
        temp = re.match(r'^\[([.#]+)\] \(([0-9,)( ]+)\) {([\d,]+)}$', str_data)
        lights, buttons, batteries = temp.groups()
        self.lights = LightPanel(lights)
        self.buttons = [Button(s) for s in buttons.split(') (')]
        self.batteries = BatteryBank(batteries)


def parse(str_data: str):
    return [Machine(line) for line in str_data.splitlines()]


def part1(machines: list[Machine]):
    total = 0
    for m in machines:
        tries = set([m.lights.off()])
        count = 0
        while True:
            count += 1
            tries = tries.union(
                set(
                    panel.toggle(button)
                    for panel in tries
                    for button in m.buttons
                )
            )
            if m.lights in tries:
                total += count
                break
    print(total)


def part2(data: list[Machine]):
    count = 0
    for m in data:
        button_masks = [
            button.bool_mask(len(m.batteries)) for button in m.buttons
        ]

        op = Optimize()
        buttons = [Int(f'Button {i}') for i in range(len(m.buttons))]

        op.add(0 <= b for b in buttons)

        op.add(
            Eq(
                Sum(
                    z_button
                    for z_button, m_button in zip(buttons, button_masks)
                    if m_button[dim]
                ),
                battery,
            )
            for dim, battery in enumerate(m.batteries.power_levels)
        )

        op.minimize(Sum(buttons))

        if op.check() == sat:
            model = op.model()
            count += sum(model[b].py_value() for b in buttons)
        else:
            print('Unsolvable')
    print(count)


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
