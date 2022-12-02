from pathlib import Path
from itertools import groupby

input_data = Path('../data/input.txt').read_text()

if __name__ == "__main__":
    cal_data = input_data.splitlines()
    #print(cal_data)
    inventory_list = [  sum([int(x) for x in g]) for k,g in groupby(cal_data, key=lambda s: s!="") if k ]
    inventory_list.sort(reverse=True)
    print(sum(inventory_list[:3]))