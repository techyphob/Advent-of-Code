# example = 36
# live = 

#0 = north
#1 = east
#2 = south
#3 = west

#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day10-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day10.txt"

my_map = []
rows = 0
columns = 0
trail_heads = []

def get_trail_heads():
    for i in range(rows):
        if 0 in my_map[i]:
            for j in range(columns):
                if my_map[i][j] == 0:
                    trail_heads.append((i,j))

def next_step(path, next_value):
    paths = []
    for p in path:
        current_loc = p[-1]
        y = current_loc[0]
        x = current_loc[1]
        if y > 0:
            if my_map[y-1][x] == next_value:
                n_path = p[:]
                n_path.append((y-1,x))
                paths.append(n_path)
        if y < rows-1:
            if my_map[y+1][x] == next_value:
                s_path = p[:]
                s_path.append((y+1,x))
                paths.append(s_path)
        if x > 0:
            if my_map[y][x-1] == next_value:
                w_path = p[:]
                w_path.append((y,x-1))
                paths.append(w_path)
        if x < columns-1:
            if my_map[y][x+1] == next_value:
                e_path = p[:]
                e_path.append((y,x+1))
                paths.append(e_path)
    return paths

def follow_path(path):
    paths = []
    current_loc = path[-1]
    y = current_loc[0]
    x = current_loc[1]
    next_value = str(int(my_map[y][x]) + 1)

    if y > 0:
        if my_map[y-1][x] == next_value:
            n_path = path[:]
            n_path.append((y-1,x))
            if len(n_path) < 10:
                paths.append(follow_path(n_path))
            else:
                paths.append(n_path)
    if y < rows-1:
        if my_map[y+1][x] == next_value:
            s_path = path[:]
            s_path.append((y+1,x))
            if len(s_path) < 10:
                paths.append(follow_path(s_path))
            else:
                paths.append(s_path)
    if x > 0:
        if my_map[y][x-1] == next_value:
            w_path = path[:]
            w_path.append((y,x-1))
            if len(w_path) < 10:
                paths.append(follow_path(w_path))
            else:
                paths.append(w_path)

    if x < columns-1:
        if my_map[y][x+1] == next_value:
            e_path = path[:]
            e_path.append((y,x+1))
            if len(e_path) < 10:
                paths.append(follow_path(e_path))
            else:
                paths.append(e_path)
    return paths

with open(input_file, 'r') as inf:
    for line in inf:
        my_map.append(list(map(int,line.rstrip())))
total = 0
rows = len(my_map)
columns = len(my_map[0])
get_trail_heads()

for p in trail_heads:
    p1 = [[p]]
    for i in range(1,10):
        p1 = next_step(p1,i)
    total += len(set([str(x[-1]) for x in p1]))

print(total)


#for  k in trail_heads:
#    next_step([k])
