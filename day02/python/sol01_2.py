from pathlib import Path
from enum import Enum

input_file = Path('../data/input.txt')



class PlayerMove(Enum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3

if __name__ == "__main__":
    total_score = 0
    with open(input_file) as file:
        while (line := file.readline().rstrip()):
            play = line.split()
            print(play)
            their_play = play[0]
            expected_result = play[1]

            score = dict()
            score['Z'] = 6
            score['Y'] = 3
            score['X'] = 0

            result_score = score[expected_result]

            if expected_result == 'Y':
                play_score = PlayerMove[their_play].value
            elif expected_result == 'X':
                play_score = PlayerMove[their_play].value - 1
                if play_score == 0: play_score = 3
            elif expected_result == 'Z':
                play_score = PlayerMove[their_play].value + 1
                if play_score == 4: play_score = 1

            round_score = result_score + play_score
            total_score = total_score + round_score
            print(f'Play Score = {play_score}; expected result score = {result_score}')
            print(f'Running total score {total_score}')