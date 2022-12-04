""" Advent Of Code 2022 - Day 4: Camp Cleanup
puzzle: https://adventofcode.com/2022/day/4
input:  https://adventofcode.com/2022/day/4/input
"""


def elf_sections(section: str) -> set:
    bounds = [int(x) for x in section.split('-')]
    return set(range(bounds[0], bounds[1] + 1))


def elf_pair(pair: str) -> tuple:
    return tuple(map(elf_sections, pair.split(',')))


def overlap(elves: tuple) -> bool:
    return any(elves[0].intersection(elves[1]))


def overlap_fully(elves: tuple) -> bool:
    return elves[0].intersection(elves[1]) in elves


if __name__ == '__main__':

    # Tests

    test_data = ['2-4,6-8', '2-3,4-5', '5-7,7-9',
                 '2-8,3-7', '6-6,4-6', '2-6,4-8']

    assert sum(map(overlap_fully, map(elf_pair, test_data))) == 2
    assert sum(map(overlap, map(elf_pair, test_data))) == 4

    # Puzzles

    with open(r'2022\day04\input04.txt') as f:
        data = f.read().split('\n')[:-1]

    print(f"Puzzle 1: {sum(map(overlap_fully, map(elf_pair, data)))}")    # 526
    print(f"Puzzle 2: {sum(map(overlap, map(elf_pair, data)))}")          # 886
