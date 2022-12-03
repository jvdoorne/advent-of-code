""" Advent Of Code 2022 - Day 3: Rucksack Reorganization
puzzle: https://adventofcode.com/2022/day/3
input:  https://adventofcode.com/2022/day/3/input
"""

from string import ascii_letters


def priority(items: set):
    return 0 if not items else ascii_letters.index(items.pop()) + 1


def group_elves(elves, size=3):
    return [elves[x:x+size] for x in range(0, len(elves), size)]


def analyze_rucksack(rucksack: str) -> int:
    pivot = len(rucksack) // 2
    error = set(rucksack[:pivot]).intersection(rucksack[pivot:])
    return priority(error)


def analyze_group(group):
    error = set(group[0]).intersection(group[1]).intersection(group[2])
    return priority(error)


if __name__ == '__main__':

    # Tests

    test_data = ['vJrwpWtwJgWrhcsFMMfFFhFp',
                 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                 'PmmdzqPrVvPwwTWBwg',
                 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                 'ttgJtRGJQctTZtZT',
                 'CrZsJsPPZsGzwwsLwLmpwMDw']
    
    assert sum(map(analyze_rucksack, test_data)) == 157
    assert sum(map(analyze_group, group_elves(test_data))) == 70

    # Puzzles

    with open(r'2022\day03\input03.txt') as f:
        data = f.read().split('\n')[:-1]

    print(f"Puzzle 1: {sum(map(analyze_rucksack, data))}")              # 8185
    print(f"Puzzle 2: {sum(map(analyze_group, group_elves(data)))}")    # 2817
