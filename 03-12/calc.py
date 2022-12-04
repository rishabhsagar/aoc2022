
import os
import string

folder = os.path.dirname(os.path.realpath(__file__))
test = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split('\n')

priorities = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))

def part1(inp):  
    score = 0
    for line in inp:
        line = list(line.strip())
        mid = len(line) // 2
        part1, part2 = set(line[:mid]), set(line[mid:])
        duplicate = next(iter(part1.intersection(part2)))
        score += priorities[duplicate]
        
    return score

print('Part 1:')
print(f"Test: {part1(test)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")


def part2(inp): 
    counter = 0 
    for i, line in enumerate(inp):
        line = set(list(line.strip()))
        if i%3 == 0:
            if i != 0:
                counter += priorities[next(iter(badge))]
            badge = line
        else:
            badge = badge.intersection(line)
    counter += priorities[next(iter(badge))]
    return counter

print('\nPart 2:')
print(f"Test: {part2(test)}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")