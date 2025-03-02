# example   10092
# live      

from lib.utils import read_input_str
from collections import namedtuple

YEAR = '2024'
example = False
map_type = str
day = 15

coord = namedtuple('coord',['x','y'])
grid = namedtuple('grid',['width','height'])

def create_grid(g_string):
    grid = {}
    for y, row in enumerate(g_string):
        for x, cell in enumerate(row):
            grid[coord(x, y)] = cell
    return grid

def print_grid():
    grid_output = ''
    for y in range(grid_size.height):
        for x in range(grid_size.width):
            grid_output += my_grid[coord(x, y)]
        grid_output += "\n"
    with open('debug_grid.txt', 'w') as outf:
        outf.writelines(grid_output)

def calcuate_gps_total():
    gps_total = 0
    for y in range(grid_size.height):
        for x in range(grid_size.width):
            if my_grid[coord(x, y)] == 'O':
                gps_total += 100 * y + x
    return gps_total

def find_robot():
    for y in range(grid_size.height):
        for x in range(grid_size.width):
            if my_grid[coord(x, y)] == '@':
                return coord(x,y)

def update_grid(slice):
    count = 0
    for c in slice[0]:
        my_grid[c] = slice[1][count]
        count += 1

def in_grid(pos):
    if (pos.x >= 0 and pos.x < grid_size.width) and (pos.y >= 0 and pos.y < grid_size.height):
        return True
    else:
        return False 

def move_robot(r_pos, direction):
    slice = [[], []]
    slice[0].append(r_pos)
    slice[1].append(my_grid[r_pos])

    match direction:
        case '^':
            delta = coord(0,-1)
        case '>':
            delta = coord(1,0)
        case 'v':
            delta = coord(0,1)
        case '<':
            delta = coord(-1,0)

    slicer = coord(r_pos.x + delta.x, r_pos.y + delta.y)
    while in_grid(slicer):
        if my_grid[slicer] == '.':
            slice[0].append(slicer)
            slice[1].append(my_grid[slicer])
            slicer = coord(slicer.x + delta.x, slicer.y + delta.y)
            break
        else:
            slice[0].append(slicer)
            slice[1].append(my_grid[slicer])
            slicer = coord(slicer.x + delta.x, slicer.y + delta.y)

    if slice[1][1] == '#' or slice[1][-1] == '#':
        return r_pos
    else:
        if '#' in slice[1]:
            return r_pos
        else:
            slice[1].insert(0, slice[1].pop())
            update_grid(slice)
            return slice[0][1]

input = read_input_str(YEAR, day, example)
grid_string, directions = input.split("\n\n")
grid_string = grid_string.split()
directions  = ''.join(directions.split())

grid_size = grid(len(grid_string[0]), len(grid_string))

my_grid = create_grid(grid_string)
robot_position = find_robot()

for d in directions:
    robot_position = move_robot(robot_position, d)

print_grid()
print(calcuate_gps_total())
