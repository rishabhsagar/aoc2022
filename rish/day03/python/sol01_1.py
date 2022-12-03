from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

input_file = Path('../data/input.txt')

# create priority mapping dict
priority_map = {letter: index for index, letter in enumerate(ascii_lowercase + ascii_uppercase, start=1)}
total_score = 0

if __name__ == "__main__":
    with open(input_file) as file:
        while (rucksack_contents := file.readline().rstrip()):
            # read contents and slice into equal lists
            comp_1 =  rucksack_contents[:int(len(rucksack_contents) / 2)]
            comp_2 =  rucksack_contents[int(len(rucksack_contents) / 2):]
            print(f"Rucksack: {rucksack_contents}")
            print(f"\tCompartment 1: {comp_1}")
            print(f"\tCompartment 2: {comp_2}")

            # identify the common character
            common_snack = list(set(comp_1).intersection(comp_2))[0]
            print(f"\tCommon snack: {common_snack}")

            # add the priority of this snack to running total of the score
            total_score = total_score + priority_map[common_snack]
            print(f"\tRunning total of the score: {total_score}")


    # print total score
    print(f"Total score is: {total_score}")
