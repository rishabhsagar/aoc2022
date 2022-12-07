
from email.policy import default
import os
from collections import defaultdict
from turtle import update

folder = os.path.dirname(os.path.realpath(__file__))
test = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split('\n')


def compute_size(el, all_sizes):
    if not isinstance(el, dict):
        return el
    current_size = 0
    for key, item in el.items():
        item_size = compute_size(item, all_sizes)
        if item_size is None:
            current_size = None
        elif current_size is not None:
            current_size += item_size
    
    if current_size is not None and current_size <= 100000:
        all_sizes[0] += current_size
    else:
        current_size = None

    return None if current_size is None else current_size
 
                
def part1(inp):
    all_sizes = [0]
    directories = {}
    current_path = ''

    for line in inp:
        line = line.strip().split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    current_path = 'root'
                elif line[2] == '..':
                    current_path = current_path.split('/')
                    current_path = '/'.join(current_path[:-1])
                else:
                    current_path = line[-1] if current_path.endswith('/') else f'{current_path}/{line[-1]}'

        elif line[0][:1].isdigit():
            current_path_list = current_path.split('/')
            current_dict = directories
            for i, el in enumerate(current_path_list):
                if len(el) > 0:
                    try:
                        current_dict = current_dict[el]
                    except KeyError:
                        current_dict[el] = {}
                        current_dict = current_dict[el]
                    if i == len(current_path_list) - 1:
                        current_dict[line[-1]] = int(line[0])
                        
    compute_size(directories, all_sizes)
    return all_sizes[0]



print('Part 1:')
print(f"Test: {part1(test)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")


def compute_size2(el, element_name, all_sizes):
    if not isinstance(el, dict):
        return el
    current_size = 0
    for key, item in el.items():
        item_size = compute_size2(item, key, all_sizes)
        current_size += item_size

    if isinstance(el, dict):
        all_sizes[element_name] = current_size
        
    return current_size


def part2(inp):
    all_sizes = {}
    directories = {}
    current_path = ''

    for line in inp:
        line = line.strip().split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    current_path = 'root'
                elif line[2] == '..':
                    current_path = current_path.split('/')
                    current_path = '/'.join(current_path[:-1])
                else:
                    current_path = line[-1] if current_path.endswith('/') else f'{current_path}/{line[-1]}'

        elif line[0][:1].isdigit():
            current_path_list = current_path.split('/')
            current_dict = directories
            for i, el in enumerate(current_path_list):
                if len(el) > 0:
                    try:
                        current_dict = current_dict[el]
                    except KeyError:
                        current_dict[el] = {}
                        current_dict = current_dict[el]
                    if i == len(current_path_list) - 1:
                        current_dict[line[-1]] = int(line[0])
                        
    compute_size2(directories, 'root', all_sizes)
    
    
    root_size = all_sizes['root']
    required_size = 30000000
    missing_size = abs(70000000 - root_size - required_size)
    closest_match = ''
    closest_match_size = 70000000
    for d, size in all_sizes.items():
        if d != 'root':
            diff = size-missing_size
            if diff < closest_match_size and diff > 0:
                closest_match = d
                closest_match_size = diff
                
    return all_sizes[closest_match]

print('\nPart 2:')
print(f"Test: {part2(test)}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")