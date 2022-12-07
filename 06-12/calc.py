
import os

folder = os.path.dirname(os.path.realpath(__file__))
test = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''.split('\n')

def part1(inp, len_seq=4, test=False):
    for line in inp:
        line = list(line)
        counter = set()
        last_matches = {}
        start_seq = 0
        char_seq = 0

        for i, el in enumerate(line):
            if el in counter:
                if last_matches[el] >= start_seq:
                    start_seq = last_matches[el] + 1
                    char_seq = i - start_seq + 1
                else:
                    char_seq += 1
            else:
                counter.add(el)
                char_seq += 1

            last_matches[el] = i
            if char_seq == len_seq:
                break

        if test is True:
            print(''.join(line), i+1)

    return i + 1 if test is not True else 'done'

print('Part 1:')
print(f"Test: {part1(test, test=True)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")

print('\nPart 2:')
print(f"Test: {part1(test, len_seq=14, test=True)}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'), len_seq=14)}")