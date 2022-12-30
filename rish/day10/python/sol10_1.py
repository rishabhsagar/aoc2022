from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

input_file = Path('../data/sample2.txt')

# create global vars
register_x = 1
current_cycle = 0
milestone_cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = list()

def schedule_command(command: str) -> None:
    # schedules run cycles based on command
    # after required cycles have completed, updates register

    global register_x
    print(f"Processing command: {command}")
    match command:
        case c if c.startswith("addx"):
            # schedule run of 2 cycles
            run_cycles(2) 
            # cycles have completed, update the register value
            increment_value = int(command.split(' ')[1])
            register_x = register_x + increment_value
            print(f"Register value updated to: {register_x}")
        case c if c.startswith("noop"):
            # schedule run of 1 cycles
            run_cycles(1)
            print(f"Register value remains at: {register_x}")

def run_cycles(num_cycles: int) -> None:
    # runs cycles one by one, 
    #   if the milestone cycle is met then:
    #       prints out a message with current register value and step #
    #       calculates the signal strength at milestone cycle and prints it.
    #       appends the signal strength value to global observation log list

    global current_cycle, signal_strengths
    print(f"\tStarting schedule of {num_cycles} cycles")
    for cycle in range(num_cycles):
        current_cycle = current_cycle + 1
        if current_cycle in milestone_cycles:
            signal_strength = register_x * current_cycle
            signal_strengths.append(signal_strength)
            print(f"\tMILESTONE: register value = {register_x}; "
                    f"current cycle = {current_cycle}; signal strength = {signal_strength}")

if __name__ == "__main__":
    with open(input_file) as file:
        file_items = file.readlines()
        commands = [ x.rstrip() for x in file_items ]
        print(f"Total commands in code: {len(commands)}")

        for command in commands:
            schedule_command(command)

        print(f"FINAL: register value = {register_x}; current cycle = {current_cycle}")
        print(f"SIGNAL STRENGTH = {signal_strengths}")
        print(f"TOTAL SIGNAL STRENGTH = {sum(signal_strengths)}")

