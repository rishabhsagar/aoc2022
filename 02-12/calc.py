
import os
folder = os.path.dirname(os.path.realpath(__file__))
test = '''A Y
B X
C Z'''.split('\n')

def part1(inp):  
    mappings = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    scores = {'X': 1, 'Y': 2, 'Z': 3}

    my_score = 0   
    for line in inp:
        line = line.strip().split(' ')
        them = scores[mappings[line[0]]]
        me = scores[line[1]]

        if abs(them - me) == 1:
            my_score += me + 6 if me > them else me
        elif abs(them - me) == 2:
            my_score += me + 6 if me < them else me
        elif me == them:
            my_score += me + 3
    print(my_score)

print('Part 1:')
print(f"Test: {part1(test)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")


def part2(inp):  
    mappings = {'Y': 'draw', 'X': 'lose', 'Z': 'win'}
    scores = {'A': 1, 'B': 2, 'C': 3}

    my_score = 0
    for line in inp:
        line = line.strip().split(' ')
        them = scores[line[0]]
        outcome = mappings[line[1]]

        if outcome == 'draw':
            my_score += them + 3
        elif outcome == 'lose':
            my_choice = them - 1 if them != 1 else 3
            my_score += my_choice
        elif outcome == 'win':
            my_choice = them + 1 if them != 3 else 1
            my_score += my_choice + 6
            
    return my_score

print('\nPart 2:')
print(f"Test: {part2(test)}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")