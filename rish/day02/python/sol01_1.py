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

def result(my_move, their_move):
    # Translate the move
    if my_move == 'X':
        my_move = 'ROCK'
    elif my_move == 'Y':
        my_move = 'PAPER'
    elif my_move == 'Z':
        my_move = 'SCISSORS'
    else:
        print(f"ILLEGAL MOVE, your move can't be {my_move}.")

    # Translate the move
    if their_move == 'A':
        their_move = 'ROCK'
    elif their_move == 'B':
        their_move = 'PAPER'
    elif their_move == 'C':
        their_move = 'SCISSORS'
    else:
        print(f"ILLEGAL MOVE, your move can't be {their_move}.")
    
    score = dict()
    score['WIN'] = 6
    score['DRAW'] = 3
    score['LOSS'] = 0

    # Analyse the move and declare result
    print(f"Analysing move: My Move = {my_move} vs Thier Move = {their_move}")
    if my_move == their_move:
        result = 'DRAW'
    elif my_move == 'ROCK':
        if their_move == 'SCISSORS':
            result = 'WIN'
        else:
            result = 'LOSS'
    elif my_move == 'PAPER':
        if their_move == 'ROCK':
           result = 'WIN'
        else:
            result = 'LOSS'
    elif my_move == 'SCISSORS':
        if their_move == 'PAPER':
            result = 'WIN'
        else:
            result = 'LOSS'
    print(f"RESULT: {result} resulting in score of {score[result]}")
    return score[result]

if __name__ == "__main__":
    total_score = 0
    with open(input_file) as file:
        while (line := file.readline().rstrip()):
            play = line.split()
            print(play)
            their_play = play[0]
            my_play = play[1]

            play_score = PlayerMove[my_play].value
            result_score = result(my_play, their_play)

            round_score = play_score + result_score
            print(f"This round score is {round_score}")
            total_score = total_score + round_score
            print(f"Running total of the score {total_score}")
    
    print(f"Final total score {total_score}")