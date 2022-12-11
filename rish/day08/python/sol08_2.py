from pathlib import Path

input_file = Path('../data/input.txt')

def print_tree(message, tree_map):
    print(message.center(len(tree_map[0]), '*'))
    for row_num, tree_row in enumerate(tree_map):
        print(f"{row_num}: {tree_row}")
    print(''.center(len(tree_map[0]), '*'))

def num_visible_trees(current_tree, line_of_sight):
    num_visible_trees = 0
    for tree in line_of_sight:
        if tree < current_tree:
            num_visible_trees = num_visible_trees + 1
        elif tree == current_tree:
            num_visible_trees = num_visible_trees + 1
            return num_visible_trees
        else:
            if num_visible_trees == 0:
                return 1
            else:
                return num_visible_trees + 1
    return num_visible_trees

if __name__ == "__main__":
    tree_map = list()
    with open(input_file) as file:
        while(tree_row := file.readline().rstrip()):
            tree_row = [int(x) for x in tree_row]
            tree_map.append(tree_row)

    #print_tree('Full Map', tree_map)

    interior_trees = list()
    for tree_row in tree_map[1:-1]:
        interior_trees.append(tree_row[1:-1])

    #print_tree('Interior Trees', interior_trees)

    interior_rows = range(1, len(tree_map) -1)
    interior_cols = range(1, len(tree_map[0]) -1)
    
    forest_rows = len(tree_map)
    forest_cols = len(tree_map[0])

    #exterior_trees = (len(tree_map) * 2) + ((len(tree_map[0]) - 2) * 2)

    best_tree_coords = (0,0)
    max_scenic_score = 0

    # count number of trees visible from inside
    for row in interior_rows:
        for col in interior_cols:
            current_tree = tree_map[row][col]
            print(f"scanning item location : {row}, {col} with tree height {current_tree}")
            left_trees = tree_map[row][0:col]
            left_trees.reverse()
            right_trees = tree_map[row][col+1:]
            up_trees = [ x[col] for x in tree_map[0:row] ]
            up_trees.reverse()
            down_trees = [ x[col] for x in tree_map[row + 1:] ]

            # calculate scenic scores
            left_scenic_score = num_visible_trees(current_tree, left_trees)
            right_scenic_score = num_visible_trees(current_tree, right_trees)
            top_scenic_score = num_visible_trees(current_tree, up_trees)
            bottom_scenic_score = num_visible_trees(current_tree, down_trees)

            tree_scenic_score = left_scenic_score * right_scenic_score * top_scenic_score * bottom_scenic_score

            #print(f"\tLeft Trees: {left_trees}; # visible trees {left_scenic_score}")
            #print(f"\tRight Trees: {right_trees};# visible trees {right_scenic_score}")
            #print(f"\tUp Trees: {up_trees};# visible trees {top_scenic_score}")
            #print(f"\tDown Trees: {down_trees};# visible trees {bottom_scenic_score}")
            #print(f"\tTree scenic score: {tree_scenic_score}")

            if tree_scenic_score > max_scenic_score:
                max_scenic_score = tree_scenic_score
                best_tree_coords = (row, col)


    # print number of visible trees and total
    print("SUMMARY".center(30, '*'))
    print(f"Forest size is {forest_rows} x {forest_cols}")
    print(f"Best Tree is at: {best_tree_coords}")
    print(f"Max scenic score: {max_scenic_score}")
