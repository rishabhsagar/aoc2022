from pathlib import Path

input_file = Path('../data/input.txt')

def is_overlap(range_1, range_2):
    overlap_range = (min(range_1[0], range_2[0]), max(range_1[1], range_2[1]))
    print(f"\tOverlapping range is: {overlap_range}")

    # Calculate the numbers contained in each range
    nums_range_1 = range_1[1] - range_1[0]
    nums_range_2 = range_2[1] - range_2[0]
    num_overlap_range = overlap_range[1] - overlap_range[0]

    # if two input ranges were laid side to side with no overlap
    # their sum of numbers will be full range.
    # For there to be no overlap, this is the min len of overlapping range
    min_unoverlapping_range = nums_range_1 + nums_range_2

    print(f"\tNumbers in range 1 = {nums_range_1}")
    print(f"\tNumbers in range 2 = {nums_range_2}")
    print(f"\tMinimum range for no overlap = {min_unoverlapping_range}")
    print(f"\tNumbers in overlap range = {num_overlap_range}")

    # nums in overlapping range should be greater than or equal to the min_unoverlapping_range
    # otherwise there is some overlap
    if num_overlap_range > min_unoverlapping_range:
        return False
    else:
        return True


if __name__ == "__main__":
    overlap_count = 0
    with open(input_file) as file:
        while (assignment_pair := file.readline().rstrip()):
            # read assignment pairs
            assign_1 = (int(assignment_pair.split(',')[0].split('-')[0]), int(assignment_pair.split(',')[0].split('-')[1]))
            assign_2 = (int(assignment_pair.split(',')[1].split('-')[0]), int(assignment_pair.split(',')[1].split('-')[1]))

            # calculate if there is any overlap and account
            if is_overlap(assign_1, assign_2):
                overlap_count = overlap_count + 1

    print(f"Total overlap count: {overlap_count}")
