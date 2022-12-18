import os

folder = os.path.dirname(os.path.realpath(__file__))

def part1(inp):
    X = 1
    cycles = 0
    check = 20
    to_add = 0
    strength = 0
    for row in inp:
        row = row.strip()
        if row == 'noop':
            new_cycles = 1
            to_add = 0
        elif row.startswith('addx'):
            to_add = int(row.split()[1])
            new_cycles = 2
        
        for _ in range(1, new_cycles + 1):
            cycles += 1
            if cycles == check:
                strength += cycles * X
                check = check + 40
        X += to_add
    return strength
        
print('Part 1:')
print(f"Test: {part1(open(f'{folder}/test.txt', 'r'))}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")


def part2(inp):
    X = 1
    cycles = 0
    crt = []
    to_add = 0
    pos = -1
    for row in inp:
        row = row.strip()
        if row == 'noop':
            new_cycles = 1
            to_add = 0
        elif row.startswith('addx'):
            to_add = int(row.split()[1])
            new_cycles = 2

        pixel = X
        for _ in range(1, new_cycles + 1):
            if cycles % 40 == 0:
                crt.append([' '] * 40)
                pos += 1
                print('.........')
                
            crt_pixel = cycles - (40 * pos)
            print(f'cycles: {cycles}, X: {X}, crt_pixel: {crt_pixel}, center pixel: {pixel}')
            if (pixel >= (crt_pixel - 1)) and (pixel <= (crt_pixel + 1)):
                crt[pos][crt_pixel] = '#'
            else:
                print(f'{pixel} does not fit')
                
            cycles += 1
            
        X += to_add

    for _ in crt:
        print('|' + ''.join(_) + '|')

print('\nPart 2:')
print(f"Test: {part2(open(f'{folder}/test.txt', 'r'))}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")
