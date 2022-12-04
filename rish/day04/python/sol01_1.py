from pathlib import Path

input_file = Path('../data/input.txt')

def is_complete_overlap(range_1, range_2):
    overlap_range = (min(range_1[0], range_2[0]), max(range_1[1], range_2[1]))
    print(f"\tOverlapping range is: {overlap_range}")
    if overlap_range == range_1 or overlap_range == range_2:
        print(f"\tRange overlapping? Yes")
        return True
    else:
        return False

if __name__ == "__main__":
    overlap_count = 0
    with open(input_file) as file:
        while (assignment_pair := file.readline().rstrip()):
            # read assignment pairs
            assign_1 = (int(assignment_pair.split(',')[0].split('-')[0]), int(assignment_pair.split(',')[0].split('-')[1]))
            assign_2 = (int(assignment_pair.split(',')[1].split('-')[0]), int(assignment_pair.split(',')[1].split('-')[1]))

            # print assignment pairs
            print(f"Assignment 1 - {assign_1}, Assignment 2 - {assign_2}")
            if is_complete_overlap(assign_1, assign_2):
                overlap_count = overlap_count + 1

    print(f"Total complete overlaps: {overlap_count}")
