""" Advent Of Code 2022 - Day 7: No Space Left On Device
puzzle: https://adventofcode.com/2022/day/7
input:  https://adventofcode.com/2022/day/7/input
"""

from collections import defaultdict


def parse(commands: list) -> defaultdict:
    parsed, stack = defaultdict(int), list()
    for line in commands:
        match line.split(' '):
            # Dir operations
            case '$', 'cd', '..':
                stack.pop()
            case '$', 'cd', d:
                stack.append(d)
            # No adction needed
            case '$', 'ls':
                pass
            case 'dir', _:
                pass        
            # File operations
            case size, _:
                # Add size for child & update size for all parents
                for i in range(1, len(stack) + 1):
                    parsed['/'.join(stack[:i])] += int(size)
    
    return parsed

if __name__ == '__main__':

    # Tests

    test_data = ['$ cd /',
                 '$ ls',
                 'dir a',
                 '14848514 b.txt',
                 '8504156 c.dat',
                 'dir d',
                 '$ cd a',
                 '$ ls',
                 'dir e',
                 '29116 f',
                 '2557 g',
                 '62596 h.lst',
                 '$ cd e',
                 '$ ls',
                 '584 i',
                 '$ cd ..',
                 '$ cd ..',
                 '$ cd d',
                 '$ ls',
                 '4060174 j',
                 '8033020 d.log',
                 '5626152 d.ext',
                 '7214296 k']
    
    assert sum([v for v in parse(test_data).values() if v <= 100000]) == 95437

    # Puzzles

    with open(r'2022\day07\input07.txt') as f:
        data = f.read().split('\n')[:-1]
        dirs = parse(data)
        clean = dirs.get('/') - (70000000 - 30000000)

    print(f"Puzzle 1: {sum([v for v in dirs.values() if v <= 100000])}")    # 1490523
    print(f"Puzzle 2: {min([v for v in dirs.values() if v >= clean])}")     # 12390492
