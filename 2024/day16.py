# example   7036
# example2  11048
# live      0

import lib.utils as util
from collections import namedtuple

YEAR = '2024'
example = True
map_type = str
day = 16

coord = namedtuple('coord',['x','y'])
move = namedtuple('move',['next','direction'])

input = util.read_input(YEAR, day, map_type, example)
my_grid = util.create_grid(input)
start_pos = util.find_position(my_grid, 'S')
target_pos = util.find_position(my_grid, 'E')
grid_size = util.get_grid_size(my_grid)

class path(object):
    def __init__(self, path, grid, direction, target_pos, cost=0):
        self.grid = grid
        self.direction = direction
        self.path = path
        self.target_pos = target_pos
        self.branches = []
        self.cost = cost

    def get_valid_moves(self):
        moves = []
        position = self.path[-1]
        if position.x > 0 and self.direction != 'right':
            if self.grid[coord(position.x-1, position.y)] != '#':
                moves.append(move(coord(position.x-1, position.y), 'left'))
        if position.x < grid_size.width-1 and self.direction != 'left':
            if self.grid[coord(position.x+1, position.y)] != '#':
                moves.append(move(coord(position.x+1, position.y), 'right'))
        if position.y > 0 and self.direction != 'down':
            if self.grid[coord(position.x, position.y-1)] != '#':
                moves.append(move(coord(position.x, position.y-1), 'up'))
        if position.y < grid_size.height-1 and self.direction != 'up':
            if self.grid[coord(position.x, position.y+1)] != '#':
                moves.append(move(coord(position.x, position.y+1), 'down'))
        return moves    

    def move_cost(self,move):
        if move.direction == self.direction:
            return 1
        else:
            return 1000

    def get_branches(self):
        moves = self.get_valid_moves()
        for move in moves:
            if move.next in self.path:
                continue
            elif move.next == self.target_pos:
                yield self.cost + self.move_cost(move)
            else:
                new_path = self.path.copy()
                new_path.append(move.next) 
                new_direction = move.direction
                move_cost = self.cost + self.move_cost(move)
                self.branches.append(path(new_path, self.grid, new_direction, self.target_pos, move_cost))
        for branch in self.branches:
            yield from branch.get_branches()  

    def step(self):
        moves = self.get_valid_moves()
        for move in moves:
            if move.next in self.path:
                continue
            elif move.next == self.target_pos:
                pass
            else:
                new_path = self.path.copy()
                new_path.append(move.next) 
                new_direction = move.direction
                yield path(new_path, self.grid, new_direction, self.target_pos)
            
def worse_cost():
    cost = 0
    for y in range(start_pos.y, target_pos.y, int((target_pos.y - start_pos.y)/abs(target_pos.y - start_pos.y))):
        for x in range(start_pos.x, target_pos.x, int((target_pos.x - start_pos.x)/abs(target_pos.x - start_pos.x))):
            cost += 1
        cost += 1000
    return cost

def best_cost():
    if start_pos.x == target_pos.x:
        cost = abs(target_pos.x - start_pos.x)
    elif start_pos.y == target_pos.y:
        cost = abs(target_pos.y - start_pos.y)
    else:
        cost = abs(target_pos.x - start_pos.x) + abs(target_pos.y - start_pos.y) + 1000
    return cost
    
wc = worse_cost()
bc = best_cost()

costs = []
root = path([start_pos], my_grid, 'right', target_pos)
costs = root.get_branches()
print(min(costs))
#for c in costs:
#    print(c)
