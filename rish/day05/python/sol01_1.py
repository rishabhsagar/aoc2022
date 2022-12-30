from pathlib import Path

sample = [ ['Z', 'N'], ['M','C','D'], ['P'] ]

input = [ ['G', 'T','R', 'W']
            , ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W']
            , ['C', 'L', 'T', 'S', 'G', 'M']
            , ['J', 'H', 'D', 'M', 'W', 'R', 'F'] 
            , ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J']
            , ['P', 'J', 'D', 'N', 'F', 'M', 'S']
            , ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J']
            , ['R', 'T', 'B']
            , ['H', 'N', 'W', 'L', 'C']
        ]

input_file = Path('../data/sample.txt')

if __name__ == "__main__":
    with open(input_file) as file:
        while (movement_instructions := file.readline().rstrip()):
            num_moves, from_stack, to_stack = [ int(s) for s in movement_instructions.split(' ') if s.isnumeric() ]
            print(f'Instruction read: {num_moves} times move items from stack {from_stack} to {to_stack}.')

            # reduce the stack numbers by 1 to match list indexes
            from_stack = from_stack - 1
            to_stack = to_stack - 1

            # execute the required movements
            for move in range(num_moves):
                sample[to_stack].append(sample[from_stack].pop())
            
            # print stack status
            print(f'Stack status: {sample}')
    
    print(f'Final stack status: {sample}')
    crates_on_top = [ stack[-1] for stack in sample]
    print(f'Crates on top: {crates_on_top}')
