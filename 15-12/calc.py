import os
import re
folder = os.path.dirname(os.path.realpath(__file__))

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def extract_data(inp):
    data = []
    for line in inp:
        line = re.findall(r'-*\d+', line)
        sensor = [int(line[0]), int(line[1])]
        beacon = [int(line[2]), int(line[3])]
        md = manhattan(sensor, beacon)
        data.append((sensor, md))
    return data
        
def find_interval(data, target_y):
    all_range_min, all_range_max = float('inf'), float('-inf')
    for sensor in data:
        md_with_closest_beacon = sensor[1]
        md_y_axis = abs(sensor[0][1] - target_y)
        
        if md_with_closest_beacon > md_y_axis:
            allowed_md_x_axis = md_with_closest_beacon - md_y_axis
            x_sensor = sensor[0][0]
            covered_range_min = x_sensor - allowed_md_x_axis
            covered_range_max = x_sensor + allowed_md_x_axis
            if covered_range_min < all_range_min:
                all_range_min = covered_range_min
            if covered_range_max > all_range_max:
                all_range_max = covered_range_max
            
    return abs(all_range_min - all_range_max)
    
def part1(inp, target_y=10):
    data = extract_data(inp)
    return find_interval(data, target_y)

print('~~Part 1~~')
test_inp = open(f'{folder}/test.txt', 'r').read().split('\n')
print(f"Test: {part1(test_inp)}")
inp = open(f'{folder}/input.txt', 'r').read().split('\n')
print(f"Final: {part1(inp, target_y=2000000)}")


def merge_ranges(intervals):
    intervals.sort(key=lambda x: x[0])
    merged_intervals = [intervals[0]]

    for current_interval in intervals:
        previous_interval = merged_intervals[-1]
        if (current_interval[0] - 1) <= previous_interval[1]:
            previous_interval[1] = max(previous_interval[1], current_interval[1])
        else:
            merged_intervals.append(current_interval)
            
    return merged_intervals[0][1] + 1 if len(merged_intervals) == 2 else False
        
def find_gaps(data, min_coord, max_coord):
    res = None
    for target_y in range(min_coord, max_coord + 1):
        ranges = []
        for sensor in data:
            md_with_closest_beacon = sensor[1]
            md_y_axis = abs(sensor[0][1] - target_y)
            
            if md_with_closest_beacon > md_y_axis:
                allowed_md_x_axis = md_with_closest_beacon - md_y_axis
                x_sensor = sensor[0][0]
                covered_range_min = x_sensor - allowed_md_x_axis
                covered_range_max = x_sensor + allowed_md_x_axis
                ranges.append([covered_range_min, covered_range_max])
        
        found = merge_ranges(ranges)
        if found is not False:
            res = [found, target_y]
            break
                
    return res[0] * 4000000 + res[1]
    
def part2(inp, min_coord, max_coord):
    data = extract_data(inp)
    return find_gaps(data, min_coord, max_coord)
    
print('~~Part 2~~')
test_inp = open(f'{folder}/test.txt', 'r').read().split('\n')
print(f"Test: {part2(test_inp, 0, 20)}")
inp = open(f'{folder}/input.txt', 'r').read().split('\n')
print(f"Final: {part2(inp, 0, 4000000)}")