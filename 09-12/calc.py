import os
from dataclasses import dataclass, field

folder = os.path.dirname(os.path.realpath(__file__))

test = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
test2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

@dataclass
class Bridge:
    n_knots: int = 2
    row_pointer: int = 0
    col_pointer: int = 0
    n_new_rows: int = 0
    n_new_cols: int = 0
    old_pointer: int = 0
    new_pointer: int = 0
    current_matrix: list = field(default_factory=lambda: [[1]])
    last_position: dict = field(default_factory=lambda: {})
    vertical_directions: dict = field(default_factory=lambda: {'D': -1, 'U': 1})
    horizontal_directions: dict = field(default_factory=lambda: {'R': 1, 'L': -1})
    n_movements: int = 1
    
    def add_rows(self, steps, direction):
        self.row_pointer += steps * self.vertical_directions[direction]
        self.n_new_rows = self.how_many_extra(self.row_pointer, len(self.current_matrix))

        if self.n_new_rows > 0:
            new_rows = [[0] * len(self.current_matrix[0]) for _ in range(self.n_new_rows)]
            if direction == 'U':
                self.current_matrix = self.current_matrix + new_rows 
            else:
                self.current_matrix = new_rows + self.current_matrix
        self.row_pointer = max(0, self.row_pointer)
        if self.vertical_directions[direction] < 0:
            for knot in range(self.n_knots):
                self.last_position[knot][0] += self.n_new_rows

    def add_cols(self, steps, direction):
        self.col_pointer += steps * self.horizontal_directions[direction]
        self.n_new_cols = self.how_many_extra(self.col_pointer, len(self.current_matrix[0])) 

        if self.n_new_cols > 0:
            for i in range(len(self.current_matrix)):
                new_cols = [0 for _ in range(self.n_new_cols)]
                if direction == 'R':
                    self.current_matrix[i] = self.current_matrix[i] + new_cols
                else:
                    self.current_matrix[i] = new_cols + self.current_matrix[i]         
        self.col_pointer = max(0, self.col_pointer)
        if self.horizontal_directions[direction] < 0:
            for knot in range(self.n_knots):
                self.last_position[knot][1] += self.n_new_cols

    def how_many_extra(self, pointer, current_matrix_size):
        return abs(pointer) if pointer < 0 else max(0, pointer - current_matrix_size + 1)
    
    def set_movement_parameters(self, movement_type, direction, steps):
        if movement_type == 'horizontal':
            new_pointer = self.col_pointer
            reference = self.horizontal_directions[direction]
            other_coord = self.row_pointer
        else:
            new_pointer = self.row_pointer
            reference = self.vertical_directions[direction]
            other_coord = self.col_pointer
            
        old_pointer = new_pointer - (reference * steps)
        if old_pointer < new_pointer:
            old_pointer += 1
        else:
            old_pointer -= 1
        return old_pointer, new_pointer + reference, other_coord, reference
    
    def check_if_detached_v(self, point1, point2):
        return abs(point1[0] - point2[0]) > 1 
    
    def check_if_detached_h(self, point1, point2):
        return abs(point1[1] - point2[1]) > 1
    
    def parse_matrix(self, list_of_movements):
        for i in range(self.n_knots + 1):
            self.last_position[i] = [0, 0]
            
        for movement in list_of_movements:
            movement = movement.split(' ')
            direction, steps = movement[0], int(movement[1])
            
            if direction in self.vertical_directions:
                movement_type = 'vertical'
                self.add_rows(steps, direction)
            else:
                movement_type = 'horizontal'
                self.add_cols(steps, direction)

            self.parse_new_movement(movement_type, direction, steps)
            
    def move_node(self, knot):
        heading_knot = self.last_position[knot-1]
        detached_h = self.check_if_detached_h(heading_knot, self.last_position[knot])
        detached_v = self.check_if_detached_v(heading_knot, self.last_position[knot])
        if not (detached_h or detached_v):
            return [None, None]
        
        coord1, coord2 = self.last_position[knot]
        if detached_h or coord2 != heading_knot[1]:
            if self.last_position[knot][1] > heading_knot[1]:
                coord2 = self.last_position[knot][1] - 1
            elif self.last_position[knot][1] < heading_knot[1]:
                coord2 = self.last_position[knot][1] + 1
            else:
                coord2 = self.last_position[knot][0]

        if detached_v or coord1 != heading_knot[0]:
            if self.last_position[knot][0] > heading_knot[0]:
                coord1 = self.last_position[knot][0] - 1
            elif self.last_position[knot][0] < heading_knot[0]:
                coord1 = self.last_position[knot][0] + 1
            else:
                coord1 = self.last_position[knot][0]
        
        return [coord1, coord2]
       
    def parse_new_movement(self, movement_type, direction, steps):    
        count = 0
        start_coord, new_coord, other_coord, reference = \
            self.set_movement_parameters(movement_type, direction, steps)
            
        for i in range(start_coord, new_coord, reference):
            for knot in range(self.n_knots):
                if knot == 0:
                    if movement_type == 'horizontal':
                        coord2, coord1 = i, other_coord
                    else:
                        coord1, coord2 = i, other_coord
                else:
                    coord1, coord2 = self.move_node(knot)
                    if coord1 is None:
                        break

                if knot == (self.n_knots - 1):
                    if self.current_matrix[coord1][coord2] == 0:
                        count += 1
                    self.current_matrix[coord1][coord2] = 1
                self.last_position[knot] = [coord1, coord2]

        self.n_movements += count

    def print_matrix(self):
        to_do_knots = set(range(self.n_knots))
        for row in range(len(self.current_matrix) - 1, -1, -1):
            for col in range(len(self.current_matrix[0])):
                found = False
                for knot in to_do_knots:
                    if self.last_position[knot] == [row, col]:
                        if knot == 0:
                            knot = 'H'
                        print(knot, end = '')
                        found = True
                        break
                if not found:
                    print('.', end = '')
            print('\n')

def part1(inp):
    bridge = Bridge()
    bridge.parse_matrix(inp.split('\n'))
    return bridge.n_movements

print('Part 1:')
print(f"Test: {part1(test)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r').read())}")

def part2(inp):
    bridge = Bridge(n_knots=10)
    bridge.parse_matrix(inp.split('\n'))
    return bridge.n_movements

print('Part 2:')
print(f"Test: {part2(test)}")
print(f"Test2: {part2(test2)}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r').read())}")