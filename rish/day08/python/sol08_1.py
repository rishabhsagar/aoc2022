from pathlib import Path

input_file = Path('../data/input.txt')

def print_tree(message, tree_map):
    print(message.center(len(tree_map[0]), '*'))
    for row_num, tree_row in enumerate(tree_map):
        print(f"{row_num}: {tree_row}")
    print(''.center(len(tree_map[0]), '*'))

if __name__ == "__main__":
    tree_map = list()
    with open(input_file) as file:
        while(tree_row := file.readline().rstrip()):
            tree_row = [int(x) for x in tree_row]
            tree_map.append(tree_row)

    #print_tree('Full Map', tree_map)

    #interior_trees = list()
    #for tree_row in tree_map[1:-1]:
        #interior_trees.append(tree_row[1:-1])

    #print_tree('Interior Trees', interior_trees)

    interior_rows = range(1, len(tree_map) -1)
    interior_cols = range(1, len(tree_map[0]) -1)
    
    forest_rows = len(tree_map)
    forest_cols = len(tree_map[0])

    exterior_trees = (len(tree_map) * 2) + ((len(tree_map[0]) - 2) * 2)

    interior_visible_trees = 0

    # count number of trees visible from inside
    for row in interior_rows:
        for col in interior_cols:
            current_tree = tree_map[row][col]
            print(f"scanning item location - {row}, {col} with tree height {current_tree}")
            left_trees = tree_map[row][0:col]
            is_visible_from_left = max(left_trees) < current_tree
            right_trees = tree_map[row][col+1:]
            is_visible_from_right = max(right_trees) < current_tree
            up_trees = [ x[col] for x in tree_map[0:row] ]
            is_visible_from_top = max(up_trees) < current_tree
            down_trees = [ x[col] for x in tree_map[row + 1:] ]
            is_visible_from_bottom = max(down_trees) < current_tree
            #print(f"\tLeft Trees: {left_trees}; Is visible from left? {is_visible_from_left}")
            #print(f"\tRight Trees: {right_trees}; Is visible from right? {is_visible_from_right}")
            #print(f"\tUp Trees: {up_trees}; Is visible from top? {is_visible_from_top}")
            #print(f"\tDown Trees: {down_trees}; Is visible from bottom? {is_visible_from_bottom}")
            if ( is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom ):
                interior_visible_trees = interior_visible_trees +1

    # print number of visible trees and total
    print("SUMMARY".center(30, '*'))
    print(f"Forest size is {forest_rows} x {forest_cols}")
    print(f"Number of exterior trees: {exterior_trees}")
    print(f"Number of interior visible trees: {interior_visible_trees}")
    total_visible_trees = interior_visible_trees + exterior_trees
    print(f"Total visible trees : {total_visible_trees}")
