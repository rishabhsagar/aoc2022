import os
from re import S

folder = os.path.dirname(os.path.realpath(__file__))
test = '''30373
25512
65332
33549
35390'''.split('\n')

                
def part1(inp):
    row_size = len(inp[0]) - 1
    col_size = len(inp) - 1
    count = row_size*2 + col_size*2
    for i, row in enumerate(inp[1:-1]):
        i += 1
        for j in range(1, row_size):
            left_pointer = 0
            top_pointer = 0
            current_tree = row[j]
            count += 1
            right_pointer = row_size
            bottom_pointer = col_size
            stop = 0
            while (left_pointer < j) or (right_pointer > j) or (top_pointer < i) or (bottom_pointer > i):          
                if left_pointer < j and (row[left_pointer] >= current_tree):
                    left_pointer = j - 1
                    stop += 1
                if right_pointer > j and (row[right_pointer] >= current_tree):
                    right_pointer = j + 1
                    stop += 1
                if top_pointer < i and (inp[top_pointer][j] >= current_tree):
                    top_pointer = i - 1
                    stop += 1
                if bottom_pointer > i and (inp[bottom_pointer][j] >= current_tree):
                    bottom_pointer = i + 1
                    stop += 1
                 
                if stop == 4:
                    count -= 1
                    break

                left_pointer += 1
                top_pointer += 1
                right_pointer -= 1
                bottom_pointer -= 1
                
    return count

print('Part 1:')
print(f"Test: {part1(test)}")
inp = open(f'{folder}/input.txt', 'r').read().split('\n')
print(f"Final: {part1(inp)}")


def part2(inp):
    row_size = len(inp[0]) - 1
    col_size = len(inp) - 1
    product = 0
    for i, row in enumerate(inp[1:-1]):
        i += 1
        for j in range(1, row_size):
            left_pointer = j - 1
            top_pointer = i - 1
            current_tree = row[j]
            right_pointer = j + 1
            bottom_pointer = i + 1
            stop = [0, 0, 0, 0]
            
            while (left_pointer >= 0) or (right_pointer <= row_size) or (top_pointer >= 0) or (bottom_pointer <= col_size):          
                if left_pointer >= 0 and left_pointer < j:
                    if (row[left_pointer] >= current_tree):
                        left_pointer = 0
                    stop[0] += 1    
                if right_pointer <= row_size and right_pointer > j:
                    if (row[right_pointer] >= current_tree):
                        right_pointer = row_size
                    stop[1] += 1
                if top_pointer >= 0 and top_pointer < i:
                    if (inp[top_pointer][j] >= current_tree):
                        top_pointer = 0
                    stop[2] += 1
                if bottom_pointer <= col_size and bottom_pointer > i:
                    if (inp[bottom_pointer][j] >= current_tree):
                        bottom_pointer = col_size
                    stop[3] += 1
                 
                left_pointer -= 1
                top_pointer -= 1
                right_pointer += 1
                bottom_pointer += 1
            
            product2 = 1
            for x in stop:
                product2 *= x
            product = max(product, product2)   
                     
    return product

print('\nPart 2:')
print(f"Test: {part2(test)}")
print(f"Final: {part2(inp)}")
