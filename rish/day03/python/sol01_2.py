from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

input_file = Path('../data/input.txt')

# create priority mapping dict
priority_map = {letter: index for index, letter in enumerate(ascii_lowercase + ascii_uppercase, start=1)}
total_score = 0

if __name__ == "__main__":
    with open(input_file) as file:
        file_items = file.readlines()
        rucksack_contents = [ x.rstrip() for x in file_items ]
        print(rucksack_contents)

        # divide the rucksack items in groups
        groups = [ rucksack_contents[i:i+3] for i in range(0, len(rucksack_contents), 3) ]

        # for each group identify the common element
        for i, group in enumerate(groups):
            sacks = [ set(x) for x in group ]
            badge = list(sacks[0].intersection(sacks[1]).intersection(sacks[2]))[0]
            print(f"Group #{i}: badge is {badge}")

            # convert the badge into priority
            badge_priority = priority_map[badge]
            print(f"\tBadge priority is: {badge_priority}")
            total_score = total_score + badge_priority


    # total score is
    print(f"Total score is {total_score}")
