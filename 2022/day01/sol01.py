""" Advent Of Code 2022 - Day 1: Calorie Counting
puzzle: https://adventofcode.com/2022/day/1
input:  https://adventofcode.com/2022/day/1/input
"""

from itertools import groupby

if __name__ == '__main__':

    with open(r'2022\day01\input01.txt') as f:
        data = f.read().split('\n')
    
    kcal_grouped = [list(g) for k, g in groupby(data, key=''.__ne__) if k]

    kcal_summed = [sum(map(int, x)) for x in kcal_grouped]

    print(f"Puzzle 1: {max(kcal_summed)} Calories ")                 # 69836
    print(f"Puzzle 2: {sum(sorted(kcal_summed)[-3:])} Calories ")    # 207968
