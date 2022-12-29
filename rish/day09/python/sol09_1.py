from pathlib import Path

input_file = Path('../data/sample.txt')

with open(input_file) as file:
    instructions = [line.rstrip() for line in file.readlines()]

def follow_leader(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    print(f'x_diff is: {x_diff}; y_diff is {y_diff}')

    old_x = tail[0]
    old_y = tail[1]


    if (abs(y_diff) == 2) and (abs(x_diff) == 2):
        tail[0] += x_diff // 2
        tail[1] += y_diff // 2
    else:
        if abs(x_diff) == 2:
            tail[0] += x_diff // 2
            tail[1] = head[1]   # move diagonally
        elif abs(y_diff) == 2:
            tail[1] += y_diff // 2
            tail[0] = head[0] # move d

    new_x = tail[0]
    new_y = tail[1]

    # return location if the tail moves
    return ((new_x != old_x) or (new_y != old_y))
    
if __name__ == "__main__":

