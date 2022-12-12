import os
folder = os.path.dirname(os.path.realpath(__file__))
import string
alphabet = list(string.ascii_lowercase)
weights = dict(zip(alphabet, range(len(alphabet))))
from collections import defaultdict

def load_graph(inp, one_start=True):
    graph = {}
    starts = []
    for i, row in enumerate(inp):
        row = list(row.strip())
        for j, el in enumerate(row):
            current_key = (i, j)
            
            if el == 'S':
                height = weights['a']
                if one_start is True:
                    starts.append(current_key)
            elif el == 'E':
                height = weights['z']
                end = current_key
            else:
                height = weights[el]
                
            if height == 0 and one_start is False:
                starts.append(current_key)
                
            current_node = {'value': el, 'height': height, 'neighbours': []}
            graph[current_key] = current_node
            current_neighbours = current_node['neighbours']
            
            if j != 0:
                current_neighbours.append((i, j - 1))
                graph[(i, j - 1)]['neighbours'].append(current_key)
            if i != 0:
                current_neighbours.append((i-1, j))
                graph[(i-1, j)]['neighbours'].append(current_key)
                
    return graph, starts, end
 
def shortest_path(graph, start, reverse=False):
    all_nodes = set(graph.keys())
    start_height = graph[start]['height']
    max_val = 9999999
    distances = defaultdict(lambda: max_val)
    
    source_node = start
    distances[source_node] = 0
    while all_nodes:
        min_distance = max_val
        
        for node in all_nodes: 
            if distances[node] <= min_distance:
                source_node = node
                min_distance = distances[node]
                start_height = graph[node]['height']
        
        all_nodes.remove(source_node)
        for node_key in graph[source_node]['neighbours']:
            node = graph[node_key]
            if reverse is True:
                condition = (start_height - node['height']) == 1 or (node['height'] >= start_height)
                stop_condition = node['value'] == 'a'
            else:
                condition = (node['height'] - start_height) == 1 or (node['height'] <= start_height)
                stop_condition = node['value'] == 'E'
            if condition:
                new_distance = distances[source_node] + 1
                if new_distance < distances[node_key]:
                    distances[node_key] = new_distance
                
                if stop_condition:
                    all_nodes = set()
                    break
    return distances
 
    
def part1(inp, one_start=True):
    graph, starts, end = load_graph(inp, one_start)
    distances = shortest_path(graph, starts[0])
    return distances[end]

def part2(inp):
    graph, starts, end = load_graph(inp, one_start=False)
    distances = shortest_path(graph, end, reverse=True)
    min_d = 99999999
    for node in starts:
        if distances[node] <= min_d:
            min_d = distances[node]
    return min_d
    
print('~~Part 1~~')
print(f"Test: {part1(open(f'{folder}/test.txt', 'r'))}")
print(f"Final: {part1(open(f'{folder}/input.txt', 'r'))}")

print('~~Part 2~~')
print(f"Test: {part2(open(f'{folder}/test.txt', 'r'))}")
print(f"Final: {part2(open(f'{folder}/input.txt', 'r'))}")
