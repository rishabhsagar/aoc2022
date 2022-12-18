import os
from copy import deepcopy
folder = os.path.dirname(os.path.realpath(__file__))

def compare_elements(left, right):
    output = -1
    for _ in range(len(left) + 1):
        if len(left) == 0 or len(right) == 0:
            return output
        curr_left, curr_right = left.pop(0), right.pop(0)
        if isinstance(curr_left, int) and isinstance(curr_right, int):
            if curr_left < curr_right:
                output = 1
            elif curr_left == curr_right:
                output = -1
            else:
                output = 0
        else:
            if not isinstance(curr_left, list):
                curr_left = [curr_left]
            if not isinstance(curr_right, list):
                curr_right = [curr_right]
            output = compare_elements(curr_left, curr_right)

        if output != -1:
            return output
        
        if isinstance(curr_left, list):
            if len(curr_left) < len(curr_right):
                return 1
            elif len(curr_right) < len(curr_left):
                return 0
            
    return output

def read_packets(inp):
    packets = []
    for row in inp:
        left, right = row.split('\n')
        left, right = eval(left), eval(right)
        packets.extend((left, right))
    return packets

def compare_packets(left, right):
    output = compare_elements(left, right)
    if output == -1:
        output = 1 if len(left) < len(right) else 0
    return output
    
def part1(packets):
    count = 0
    for i in range(0, len(packets), 2):
        left, right = packets[i], packets[i+1]
        output = compare_packets(left, right)
        count += (i//2+1) * max(0, output)
    return count

def part2(packets):
    before2 = 1
    before6 = 2
    for packet in packets:
        output = compare_packets(deepcopy(packet), [[2]])
        before2 += output
        before6 += output
        
        if output != 1:
            before6 += compare_packets(packet, [[6]])
            
    return before2 * before6
    
print('~~Part 1~~')
test_inp = read_packets(open(f'{folder}/test.txt', 'r').read().split('\n\n'))
print(f"Test: {part1(test_inp)}")
inp = read_packets(open(f'{folder}/input.txt', 'r').read().split('\n\n'))
print(f"Final: {part1(inp)}")

print('~~Part 2~~')
test_inp = read_packets(open(f'{folder}/test.txt', 'r').read().split('\n\n'))
print(f"Test: {part2(test_inp)}")
inp = read_packets(open(f'{folder}/input.txt', 'r').read().split('\n\n'))
print(f"Final: {part2(inp)}")