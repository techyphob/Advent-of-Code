# example = 14
# live = 367

import itertools

#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day8-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day8.txt"

my_map = []
antennas = {}
anti_nodes= set()

def get_content(i,j):
    return my_map[i][j]

def calc_antinodes(pair):
    diff = [pair[0][0]- pair[1][0],pair[0][1]- pair[1][1]]
    pos = [pair[0][0] + diff[0], pair[0][1] + diff[1]]
    if in_map(pos):
        anti_nodes.add(str(pos))
    pos = [pair[1][0] - diff[0], pair[1][1] - diff[1]]
    if in_map(pos):
        anti_nodes.add(str(pos))

def in_map(pos):
    if pos[0] >= 0 and pos [0] < COLS and pos[1] >= 0 and pos[1] < ROWS:
        return True
    else:
        return False

with open(input_file, 'r') as inf:
    for line in inf:
        my_map.append(list(map(str,line.rstrip())))

ROWS = len(my_map)
COLS = len(my_map[0])

for i in range(ROWS):
    for j in range(COLS):
        this_pos = my_map[i][j]
        if  this_pos != '.':
            if this_pos not in antennas:
                antennas[this_pos]= [[i,j]]
            else:
                antennas[this_pos].append([i,j])
for k in antennas:
    pairs = list(itertools.combinations(antennas[k], 2))
    for pair in pairs:
        calc_antinodes(pair)
print(len(anti_nodes))