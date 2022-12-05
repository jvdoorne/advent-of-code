""" Advent Of Code 2022 - Day 5: Supply Stacks
puzzle: https://adventofcode.com/2022/day/5
input:  https://adventofcode.com/2022/day/5/input
"""

import re

RE_MOVE = re.compile('move (\d+) from (\d+) to (\d+)')


def parse_puzzle_input(data: list) -> tuple:
    raw_crates, moves = data[:data.index('')], data[data.index('') + 1:]
    # Populate stacks
    crates = []
    for i in range(1, len(raw_crates[-1]), 4):
        crates.append([x[i] for x in raw_crates[:-1] if x[i] != ' '][::-1])
    return crates, moves


def move_crates(crates: list, command: str, move_multiple=False):
    n, src, dst = map(int, RE_MOVE.findall(command)[0])
    if move_multiple:
        crates[dst-1].extend(crates[src-1][-n:])
        crates[src-1] = crates[src-1][:-n]
    else:
        for _ in range(n): 
            crates[dst-1].append(crates[src-1].pop())


def solve(data: list, move_multiple=False) -> str:
    crates, moves = parse_puzzle_input(data)
    for command in moves:
        move_crates(crates, command, move_multiple)
    return ''.join([x[-1] for x in crates])


if __name__ == '__main__':

    # Tests

    test_data = ['    [D]    ',
                 '[N] [C]    ',
                 '[Z] [M] [P]',
                 ' 1   2   3 ',
                 '',
                 'move 1 from 2 to 1',
                 'move 3 from 1 to 3',
                 'move 2 from 2 to 1',
                 'move 1 from 1 to 2']

    assert solve(test_data) == 'CMZ'
    assert solve(test_data, move_multiple=True) == 'MCD'

    # Puzzles

    with open(r'2022\day05\input05.txt') as f:
        data = f.read().split('\n')[:-1]

    print(f"Puzzle 1: {solve(data)}")                           # TLNGFGMFN
    print(f"Puzzle 2: {solve(data, move_multiple=True)}")       # FGLQJCMBD
