
import os

folder = os.path.dirname(os.path.realpath(__file__))
test = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n')


def define_stacks(line, stacks):
    '''Imports the structure of all stacks'''
    line = line
    stack = 0
    crate = ''
    spacer = 0
    for el in line:
        if el.isupper():
            crate = el
        elif el == ']':
            stacks[stack].append(crate)
        elif el.isdigit():
            return True
        if el != '\n':
            spacer += 1
            if spacer == 4:
                spacer = 0
                stack += 1
                if stack > (len(stacks) - 1):
                    stacks.append([])
    return False

def move_crates(line, stacks, group=False):
    '''Moves crates around (one by one if group==False, else in blocks)'''
    line = line.strip().split(' ')
    quantity, start, end = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
    if group is False:
        for _ in range(quantity):
            crate = stacks[start].pop()
            stacks[end].append(crate)
    else:
        move = stacks[start][-quantity:]
        stacks[start] = stacks[start][:(len(stacks[start]) - quantity)]
        stacks[end] = stacks[end] + move
    
    
def part1(inp):
    stacks = [[]]
    counter = 0
    stacks_defined = False
    for line in inp:
        if stacks_defined is True:
            for stack in stacks:
                stack.reverse()
            stacks_defined = False
        elif not line.startswith('m'):
            stacks_defined = define_stacks(line, stacks)
        else:
            move_crates(line, stacks)
            counter += 1
    sol = [stack[-1] for stack in stacks if len(stack) > 0]
    return ''.join(sol)

print('Part 1:')
print(f"Test: {part1(test)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")


def part2(inp):
    stacks = [[]]
    counter = 0
    stacks_defined = False
    for line in inp:
        if stacks_defined is True:
            for stack in stacks:
                stack.reverse()
            stacks_defined = False
        elif not line.startswith('m'):
            stacks_defined = define_stacks(line, stacks)
        else:
            move_crates(line, stacks, group=True)
            counter += 1
    sol = [stack[-1] for stack in stacks if len(stack) > 0]
    return ''.join(sol)

print('\nPart 2:')
print(f"Test: {part2(test)}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")