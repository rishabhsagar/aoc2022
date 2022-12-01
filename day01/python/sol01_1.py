from pathlib import Path
from itertools import groupby

input_data = Path('../data/input.txt').read_text()

if __name__ == "__main__":
    cal_data = input_data.splitlines()
    #print(cal_data)
    inventory_list = [  sum([int(x) for x in g]) for k,g in groupby(cal_data, key=lambda s: s!="") if k ]
    print(max(inventory_list))