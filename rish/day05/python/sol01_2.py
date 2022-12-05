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

input_file = Path('../data/input.txt')

if __name__ == "__main__":
    with open(input_file) as file:
        while (movement_instructions := file.readline().rstrip()):
            num_moves, from_stack, to_stack = [ int(s) for s in movement_instructions.split(' ') if s.isnumeric() ]
            print(f'Instruction read: {num_moves} times move items from stack {from_stack} to {to_stack}.')

            # reduce the stack numbers by 1 to match list indexes
            from_stack = from_stack - 1
            to_stack = to_stack - 1

            # execute the required movements
            temp_stack = []
            for move in range(num_moves):
                temp_stack.append(input[from_stack].pop())

            # reverse the temp stack
            temp_stack.reverse()

            # add the crates in the temp stack to the to_stack
            input[to_stack] = input[to_stack] + temp_stack

            # print stack status
            print(f'Stack status: {input}')
    
    print(f'Final stack status: {input}')
    crates_on_top = [ stack[-1] for stack in input]
    print(f'Crates on top: {crates_on_top}')