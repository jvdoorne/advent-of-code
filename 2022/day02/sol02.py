""" Advent Of Code 2022 - Day 2: Rock Paper Scissors
puzzle: https://adventofcode.com/2022/day/2
input:  https://adventofcode.com/2022/day/2/input
"""

SHAPE_SCORES = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}



def calc_score(game: str) -> int:
    opp, own = SHAPE_SCORES[game[0]], SHAPE_SCORES[game[-1]]
    # Draw
    if opp == own:
        return own + 3
    # Rock v Scissors
    if opp * own == 3:
        return own + (own < opp) * 6
    # Other matchups
    return own + (own > opp) * 6


def determine_move(opp: str, win=True) -> str:
    if win:
        return chr(ord(opp)+1) if opp != 'C' else 'A'
    return chr(ord(opp)-1) if opp != 'A' else 'C'   


def determine_strat(guide: list) -> list:
    strat = []
    for game in guide:
        opp, res = game[0], game[-1]
        # Draw
        if res == 'Y':
            strat.append(opp + opp)
        # Win/Lose
        else:
            strat.append(opp + determine_move(opp, win=(res=='Z')))
    return strat

  
if __name__ == '__main__':

    # Tests

    test_data = ['A Y', 'B X', 'C Z']
    assert sum(map(calc_score, test_data)) == 15
    assert sum(map(calc_score, determine_strat(test_data))) == 12

    # Puzzles

    with open(r'2022\day02\input02.txt') as f:
        data = f.read().split('\n')[:-1]
    
    print(f"Puzzle 1: {sum(map(calc_score, data))}")                    # 12772
    print(f"Puzzle 2: {sum(map(calc_score, determine_strat(data)))}")   # 11618
