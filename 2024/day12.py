#
#   This solution is taken from https://hamatti.org/adventofcode/2024/solutions/day-12 while looking for a better way to  
#   navigate grids/maps than that which I have previously used. 
#

# example = 1930
# live =    1431440

from lib.utils import read_input
from collections import namedtuple

YEAR = '2024'
example = False
map_type = str
day = 12

Coordinate = namedtuple("Coordinate", ["x", "y"]) 
 
def create_grid(inputs):
    grid = {}
    for y, row in enumerate(inputs):
        for x, cell in enumerate(row):
            grid[Coordinate(x, y)] = cell
    return grid

def get_neighbours(pos):
    return (
        Coordinate(pos.x + 1, pos.y),
        Coordinate(pos.x - 1, pos.y),
        Coordinate(pos.x, pos.y + 1),
        Coordinate(pos.x, pos.y - 1),
    )

def find_plot(pos, grid, visited):
    visited.add(pos)
    new_neighbours = [
        n
        for n in get_neighbours(pos)
        if n not in visited and grid.get(n) == grid.get(pos)
    ]
    if not new_neighbours:
        return visited
    for neighbour in new_neighbours:
        visited.update(find_plot(neighbour, grid, visited))
    return visited

def find_perimeter(position, grid):
    perimeter = 0
    value = grid.get(position)
    for neighbour in get_neighbours(position):
        if grid.get(neighbour) != value:
            perimeter += 1
    return perimeter

def find_plots(grid):
    plots = []
    processed = set()
    for position in grid:
        if position in processed:
            continue
        plot = find_plot(position, grid, set())
        processed.update(plot)
        plots.append(plot)
    return plots


my_grid = create_grid(read_input(YEAR, day, map_type, example))
plots = find_plots(my_grid)

cost = 0
for plot in plots:
    area = len(plot)
    perimeter = sum(find_perimeter(pos, my_grid) for pos in plot)
    cost += area * perimeter
 
print(f"Part 1: {cost}")
