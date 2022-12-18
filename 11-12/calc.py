import os
from dataclasses import dataclass, field
from math import lcm 
folder = os.path.dirname(os.path.realpath(__file__))

@dataclass
class Monkey:
    identifier: int
    items: list
    operation: staticmethod
    operator: str
    times: int
    test_value: int
    if_true: int
    if_false: int
    divide_factor: int
    other_monkeys: list = field(default_factory=lambda: [])
    n_inspections: int = 0

    def update_monkeys(self, monkeys):
        self.other_monkeys = monkeys
        
    def add_item(self, item):
        self.items.append(item)
        
    def update_worry(self, item, shared_m):
        item = self.operation(item)
        if self.divide_factor != 1:
            item = item//self.divide_factor
        item = item % shared_m
        return item
    
    def test_item(self, item):
        return item % self.test_value == 0
    
    def run_round(self, shared_m):
        if len(self.items) == 0:
            return
                
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.n_inspections += 1
            item = self.update_worry(item, shared_m)
            if self.test_item(item):
                self.other_monkeys[self.if_true].add_item(item)
            else:
                self.other_monkeys[self.if_false].add_item(item)

def load_monkeys(inp, divide_factor):
    monkeys = []
    for i, monkey in enumerate(inp.read().split('\n\n')):
        kwargs = {'identifier': i, 'divide_factor': divide_factor}
        for line in monkey.split('\n')[1:]:
            line = line.strip().lstrip()
            if line.startswith('Starting'):
                items = [int(item) for item in line.split(':')[1].lstrip().split(',')]
                kwargs['items'] = items
            elif line.startswith('Operation'):
                line = line.split('=')[-1].strip().lstrip()
                kwargs['operation'] = eval(f'lambda old: {line}')
                kwargs['operator'], kwargs['times'] = line.split()[1:]
            elif line.startswith('Test'):
                kwargs['test_value'] = int(line.split()[-1])
            elif line.startswith('If true'):
                kwargs['if_true'] = int(line.split()[-1])
            elif line.startswith('If false'):
                kwargs['if_false'] = int(line.split()[-1])
        monkeys.append(Monkey(**kwargs))

    return monkeys

def get_mb(monkeys, n_rounds=20):
    for monkey in monkeys:
        monkey.update_monkeys(monkeys)
        shared_m = lcm(*[monkey.test_value for monkey in monkeys])
    
    for _ in range(n_rounds):
        for monkey in monkeys:
            monkey.run_round(shared_m)

    max_mb = [0, 0]
    for monkey in monkeys:
        mb = monkey.n_inspections
        for i in range(2):
            if mb > max_mb[i]:
                max_mb[i] = mb
                max_mb = sorted(max_mb)
                break
            
    return max_mb[0] * max_mb[1]
   
def part1(inp, divide_factor, n_rounds):
    monkeys = load_monkeys(inp, divide_factor)
    return get_mb(monkeys, n_rounds)
         
print('Part 1:')
print(f"Test: {part1(open(f'{folder}/test.txt', 'r'), 3, 20)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'), 3, 20)}")

print('Part 1:')
print(f"Test: {part1(open(f'{folder}/test.txt', 'r'), 1, 10000)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'), 1, 10000)}")