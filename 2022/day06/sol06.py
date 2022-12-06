""" Advent Of Code 2022 - Day 6: Tuning Trouble
puzzle: https://adventofcode.com/2022/day/6
input:  https://adventofcode.com/2022/day/6/input
"""


def find_start(s: str, chars: int) -> int:
    for i in range(chars, len(s) + 1):
        if len(set(s[i-chars:i])) == chars:
            return i
    return -1


def start_of_packet(s: str) -> int:
    return find_start(s, chars=4)


def start_of_message(s: str) -> int:
    return find_start(s, chars=14)


if __name__ == '__main__':

    # Tests
    
    test_data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    
    assert start_of_packet(test_data) == 7
    assert start_of_message(test_data) == 19

    # Puzzles

    with open(r'2022\day06\input06.txt') as f:
        data = f.read().split('\n')[:-1]

    print(f"Puzzle 1: {sum(map(start_of_packet, data))}")       # 1578
    print(f"Puzzle 2: {sum(map(start_of_message, data))}")      # 2178
