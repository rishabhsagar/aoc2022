from pathlib import Path

input_file = Path('../data/input.txt')

if __name__ == "__main__":
    with open(input_file) as file:
        while (signal_string := file.readline().rstrip()):
            # extracts parts of signal sequentially to identify segment
            for seq_end in range(14, len(signal_string)):
                seq_start = seq_end - 14
                signal = signal_string[seq_start:seq_end]
                print(f'Checking signal segment {signal}')

                # check if the segment has repeated characters
                if len(set(signal)) == 14:
                    # no repeated characters
                    print(f'Signal segement found - {signal}')
                    print(f'starts at location: {seq_end}')
                    break