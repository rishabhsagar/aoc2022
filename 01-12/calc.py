
import os
folder = os.path.dirname(os.path.realpath(__file__))

test = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''.split('\n')

def part1(inp):
    def check(counter, max_count):
        if counter > max_count:
            max_count = counter
        
        return max_count
                
    counter = 0
    max_count = 0
    for line in inp:
        line = line.strip().lstrip()
        if not line[:1].isdigit():
            max_count = check(counter, max_count)
            counter = 0
        else:
            counter += int(line)
    max_count = check(counter, max_count)
    return max_count        

print('Part 1:')
print(f"Test: {part1(test)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")


def part2(inp):
    def check(counter, max_count):
        for i, el in enumerate(max_count):
            if counter > el:
                max_count[i] = counter
                max_count = sorted(max_count)
                break
        return max_count
                
    counter = 0
    max_count = [0] * 3
    for line in inp:
        line = line.strip().lstrip()
        if not line[:1].isdigit():
            max_count = check(counter, max_count)
            counter = 0
        else:
            counter += int(line)
            
    check(counter, max_count)
    return sum(max_count)

print('\nPart 2:')
print(f"Test: {part2(test)}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")