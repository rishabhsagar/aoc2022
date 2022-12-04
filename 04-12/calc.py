
import os

folder = os.path.dirname(os.path.realpath(__file__))
test = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.split('\n')


def part1(inp):
    def check_overlap(range1, range2):
        return range1[0] >= range2[0] and range1[1] <= range2[1]

    count = 0
    for line in inp:
        line = list(line.strip().split(','))
        line = list(map(lambda x: [int(el) for el in x], 
                        list(map(lambda x: x.split('-'), line))))
        if check_overlap(line[0], line[1]) or check_overlap(line[1], line[0]):
            count += 1

    return count
        
print('Part 1:')
print(f"Test: {part1(test)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")


def part2(inp):
    def check_overlap(range1, range2):
        return range1[0] <= range2[1] and range1[1] >= range2[1]

    count = 0
    for line in inp:
        line = list(line.strip().split(','))
        line = list(map(lambda x: [int(el) for el in x], 
                        list(map(lambda x: x.split('-'), line))))
        if check_overlap(line[0], line[1]) or check_overlap(line[1], line[0]):
            count += 1

    return count

print('\nPart 2:')
print(f"Test: {part2(test)}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")