import os
import sys
from collections import namedtuple

coord = namedtuple("coord", ["x", "y"])
grid_size = namedtuple('grid',['width','height'])

def read_input(year, day, map_type=str, example=False): 
    try:
        if example:
            filename = f'day{day}-example.txt'
        else:
            filename = f'day{day}.txt'
        with open(os.path.join(year, 'input', filename)) as input_file:
            return [map_type(line.strip()) for line in input_file]
    
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

def read_input_str(year, day, example=False): 
    try:
        if example:
            filename = f'day{day}-example.txt'
        else:
            filename = f'day{day}.txt'
        with open(os.path.join(year, 'input', filename)) as input_file:
            return input_file.read()
    
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

def create_grid(inputs):
    grid = {}
    for y, row in enumerate(inputs):
        for x, cell in enumerate(row):
            grid[coord(x, y)] = cell
    return grid

def get_grid_size(grid):
    max_x = max(coord.x for coord in grid.keys())
    max_y = max(coord.y for coord in grid.keys())
    return grid_size(max_x, max_y)

def find_position(grid, char):
    for coord, val in grid.items():
        if val == char:
            return coord
            
def print_grid(grid):
    grid_output = ''
    grid_size = get_grid_size(grid)
    for y in range(grid_size[1]+1):
        for x in range(grid_size[0]+1):
            grid_output += grid[coord(x, y)]
        grid_output += "\n"
    with open('debug_grid.txt', 'w') as outf:
        outf.writelines(grid_output)
