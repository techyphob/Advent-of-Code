# example   12
# live      215987200

from lib.utils import read_input
from numpy import array
from collections import Counter
from math import prod

YEAR = '2024'
example = True
map_type = str
day = 14
if example:
    grid_size = array([11,7])
else:
    grid_size = array([101,103])

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
    return array(list(map(int,input_line[2:].split(','))))

robots = []
quads = []

input = read_input(YEAR, day, map_type, example)
for l in input:
    pv = l.split()
    robots.append(robot(split_line(pv[0]), split_line(pv[1])))

for r in robots:
    print(r.velocity)
    r.patrol(100)
    quads.append(r.in_quadrant())

counts = Counter(quads)
counts.pop(0)
print(prod(counts.values()))
