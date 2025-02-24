# example   12
# live      215987200

from lib.utils import read_input
from collections import Counter
from math import prod

YEAR = '2024'
example = False
map_type = str
day = 14
day = 14
if example:
    grid_size = (11,7)
else:
    grid_size = (101,103)

class robot(object):
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def patrol(self, time):
        for i in range(0,time):
            self.position[0] = (self.position[0] + self.velocity[0]) % grid_size[0]
            self.position[1] = (self.position[1] + self.velocity[1]) % grid_size[1]
    
    def in_quadrant(self):
        q_width = grid_size[0]//2
        q_height = grid_size[1]//2
        if self.position[0] in range(0,q_width) and self.position[1] in range(0,q_height):
            return 1
        elif self.position[0] in range(q_width + 1, grid_size[0]) and self.position[1] in range(0,q_height):
            return 2
        elif self.position[0] in range(0,q_width) and self.position[1] in range(q_height + 1, grid_size[1]):
            return 3
        elif self.position[0] in range(q_width + 1, grid_size[0]) and self.position[1] in range(q_height + 1, grid_size[1]):
            return 4
        else:
            return 0

def split_line(input_line):
    return list(map(int,input_line[2:].split(',')))

def print_map(num, r_positions):
    grid = ''
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if [x,y] in r_positions:
                grid += "R"
            else:
                grid += "."
        grid += "\n"
    if 'R'*8 in grid:
        with open(str(num) + '.txt', 'w') as outf:
            outf.writelines(grid)

robots = []
input = read_input(YEAR, day, map_type, example)
for l in input:
    pv = l.split()
    robots.append(robot(split_line(pv[0]), split_line(pv[1])))

for m in range (200*200):
    for r in robots:
        r.patrol(1) 
    
    r_positions = [r.position for r in robots]

    xs = Counter([x[0] for x in r_positions])
    for v in xs.values():
        if v > 31:
            print_map(m, r_positions)
            break