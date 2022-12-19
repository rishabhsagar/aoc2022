import os
folder = os.path.dirname(os.path.realpath(__file__))
from dataclasses import dataclass, field

@dataclass
class Cave:
    coord_ranges: dict = field(default_factory=lambda: {'x': [float('inf'), 500], 'y': [0, float('-inf')]})
    obstacles: set = field(default_factory=lambda: set())
    paths: set = field(default_factory=lambda: set())
    sand_source: list = field(default_factory=lambda: [500, 0])
    is_floor: bool = False

    def read_paths(self, inp):
        for line in inp:
            line = line.strip().split(' -> ')
            blocks = []
            for x in line:
                y = x.split(',')
                blocks.append([int(y[0]), int(y[1])])
            self.size_cave(blocks)
            self.add_paths(blocks)
            
    def add_blocks(self, new_coord, current_coord, other_coord, coord_type):
        max_coord = max(current_coord, new_coord)
        min_coord = min(current_coord, new_coord)
        
        for coord in range(min_coord, max_coord + 1):
            if coord_type == 'x':
                this = (coord, other_coord)
                self.obstacles.add(this)
                self.paths.add(this)
            elif coord_type == 'y':
                this = (other_coord, coord)
                self.obstacles.add(this)
                self.paths.add(this)

    def add_paths(self, blocks):
        current_x, current_y = blocks[0]
        for block in blocks[1:]:
            if block[0] == current_x:
                self.add_blocks(block[1], current_y, current_x, 'y')
            elif block[1] == current_y:
                self.add_blocks(block[0], current_x, current_y, 'x')
            else:
                self.add_blocks(block[0], block[0], block[1], 'x')
                
            current_x, current_y = block
                     
    def size_cave(self, blocks):
        for n in blocks:
            if n[0] < self.coord_ranges['x'][0]:
                self.coord_ranges['x'][0] = n[0]
            elif n[0] > self.coord_ranges['x'][1]:
                self.coord_ranges['x'][1] = n[0]
            if n[1] < self.coord_ranges['y'][0]:
                self.coord_ranges['y'][0] = n[1]
            elif n[1] > self.coord_ranges['y'][1]:
                self.coord_ranges['y'][1] = n[1]

    def print_cave(self):
        for y in range(self.coord_ranges['y'][0], self.coord_ranges['y'][1] + 1):
            print('\n', end='')
            for x in range(self.coord_ranges['x'][0], self.coord_ranges['x'][1] + 1):
                if (x, y) in self.paths:
                    print('#', end='')
                elif (x, y) in self.obstacles:
                    print('o', end='')
                else:
                    print('.', end='')
        print('\n')
        
    def add_floor(self):
        floor_y = self.coord_ranges['y'][1] + 2
        self.is_floor = True
        self.coord_ranges['y'][1] = floor_y
        
    def simulate_grain(self):
        sand_position = tuple(self.sand_source)
        blocked = False
        former_sand_position = sand_position
        
        while not blocked:
            if sand_position in self.obstacles:
                if sand_position == former_sand_position:
                    return False
                
                sand_position = former_sand_position
                diag_left = sand_position[0] - 1, sand_position[1] + 1
                if diag_left not in self.obstacles:
                    sand_position = diag_left
                else:
                    blocked = True
                if blocked:
                    diag_right = sand_position[0] + 1, sand_position[1] + 1
                    if diag_right not in self.obstacles:
                        sand_position = diag_right
                        blocked = False
                    else:
                        blocked = True

            former_sand_position = sand_position
            if not blocked:
                sand_position = sand_position[0], sand_position[1] + 1
                if self.is_floor and sand_position[1] >= self.coord_ranges['y'][1]:
                    sand_position = former_sand_position
                    blocked = True
            if blocked:
                self.obstacles.add(sand_position)
            if sand_position[1] > self.coord_ranges['y'][1]:
                return False
            if sand_position == self.sand_source:
                return False
        # self.print_cave()
        return True

    def simulate_sand(self):
        n_grains = -1
        sand_flows = True
        while sand_flows:
            sand_flows = self.simulate_grain()
            n_grains += 1
        return n_grains
            
def part1(inp):
    cave = Cave()
    cave.read_paths(inp)
    return cave.simulate_sand()    

def part2(inp):
    cave = Cave()
    cave.read_paths(inp)
    cave.add_floor()
    return cave.simulate_sand()        
    
print('~~Part 1~~')
test_inp = open(f'{folder}/test.txt', 'r').read().split('\n')
print(f"Test: {part1(test_inp)}")
inp = open(f'{folder}/input.txt', 'r').read().split('\n')
print(f"Final: {part1(inp)}")

print('~~Part 2~~')
print(f"Test: {part2(test_inp)}")
print(f"Final: {part2(inp)}")