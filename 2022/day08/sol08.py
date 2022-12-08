""" Advent Of Code 2022 - Day 8: Treetop Tree House
puzzle: https://adventofcode.com/2022/day/8
input:  https://adventofcode.com/2022/day/8/input
"""


def neighbours(tree_x: int, tree_y: int, forest: list) -> tuple:
    ns = [forest[y][tree_x] for y in range(len(forest))]
    we = list(forest[tree_y])
    return ns[:tree_y+1][::-1], we[tree_x:], ns[tree_y:], we[:tree_x+1][::-1]


def is_visible(tree_x: int, tree_y: int, forest: list) -> bool:
    for n in neighbours(tree_x, tree_y, forest):
        tree = n[0]
        if tree == max(n) and n.count(tree) == 1:
            return True
    return False


def trees_visible(forest: list) -> int:
    n = 0
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            n += is_visible(x, y, forest)
    return n


def scenic_score(tree_x: int, tree_y: int, forest: list) -> int:
    for n in neighbours(tree_x, tree_y, forest):
        print([n[1+x:] for x in range(len(n)) if n[1+x:]== sorted(n[1+x:])])


if __name__ == '__main__':

    # Tests

    test_data = ["30373",
                "25512",
                "65332",
                "33549",
                "35390"]

    assert trees_visible(test_data) == 21
    assert True

    # Puzzles

    with open(r'2022\day08\input08.txt') as f:
        data = f.read().split('\n')[:-1]

    print(f"Puzzle 1: {trees_visible(data)}")
    print(f"Puzzle 2: TODO")
