# example = 6
# live = 

#0 = north
#1 = east
#2 = south
#3 = west

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day6-example.txt"
#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day6.txt"

my_map = []
direction = 0
rows = 0
columns = 0
start_pos = []
current_pos = []
obs_list = []
obs_path = []
obs_path_2 = []
free_space = []
new_possibles = set()


def direction_change():
    global direction
    direction = (direction + 1)%4
    move()
    
def move(my_pos):    
    i = my_pos[0]
    j = my_pos[1]
    match direction:
        case 0:
            if i-1 >= 0:
                if my_map[i-1][j] != '#':
                    current_pos = [i-1,j]
                else:
                    obs_path.append([[i-1,j], direction])
                    obs_path_2.append([i-1,j])
                    direction_change()
            else:
                current_pos = [-1,-1]
        case 1:
            if j+1 < columns:
                if my_map[i][j+1] != '#':
                    current_pos = [i,j+1]
                else:
                    obs_path.append([[i,j+1], direction])
                    obs_path_2.append([i,j+1])
                    direction_change()
            else:
                current_pos = [-1,-1]
        case 2:
            if i+1 < rows:
                if my_map[i+1][j] != '#':
                    current_pos = [i+1,j]
                else:
                    obs_path.append([[i+1,j], direction])
                    obs_path_2.append([i+1,j])
                    direction_change()
            else:
                current_pos = [-1,-1]
        case 3:
            if j-1 >= 0:
                if my_map[i][j-1] != '#':
                    current_pos = [i,j-1]
                else:
                    obs_path.append([[i,j-1], direction])
                    obs_path_2.append([i,j-1])
                    direction_change()
            else:
                current_pos = [-1,-1]

def check_square(pos1, pos2, pos3, direction, i):
    match direction:
        case 0:
            if pos1[1]-1 >=0:
                pos4 = [pos3[0]-1,pos1[1]-1]
                if obstruction_check(pos3, pos4, 3, i) and obstruction_check(pos4, pos1, 0, i) and pos4 != start_pos: 
                    return pos4
                else:
                    return [-1,-1]
            else:
                return [-1,-1]
        case 1:
            if pos1[0]-1 >=0:
                pos4 = [pos1[0]-1,pos3[1]+1]
                if obstruction_check(pos3, pos4, 0, i) and obstruction_check(pos4, pos1, 1, i) and pos4 != start_pos:
                    return pos4
                else:
                    return [-1,-1]
            else:
                return [-1,-1]
        case 2:
            if pos1[1]+1 <= columns:
                pos4 = [pos3[0]-1,pos1[1]+1]
                if obstruction_check(pos3, pos4, 0, i) and obstruction_check(pos4, pos1, 1, i) and pos4 != start_pos:
                    return pos4
                else:
                    return [-1,-1]
            else:
                return [-1,-1]
        case 3:
            if pos1[0]+1 <= rows:
                pos4 = [pos1[0]+1,pos3[1]-1]
                if obstruction_check(pos3, pos4, 0, i) and obstruction_check(pos4, pos1, 1, i) and pos4 != start_pos:
                    return pos4
                else:
                    return [-1,-1]
            else:
                return [-1,-1]

def check_new_path(pos, direction,i):
    pass

def obs_to_path_check(pos, direction, i):
    if pos not in obs_path_2:
        print("New Obstruction:\t{}".format(pos))
    else:
        if [pos, direction] in obs_path[:i]:
            return True
            print("We hit this the right way:\t{0}".format(pos))
        else:
            return False
            print("We hit this late:\t{0}".format(pos))
    return False

def obstruction_check(pos1, pos2, direction, path_index):
    match direction:
        case 0:
            for i in range (pos1[0],pos2[0],-1):
                my_pos = [i,pos2[1]]
                if my_pos in obs_list:
                    return obs_to_path_check(my_pos, direction, path_index)
            return True
        case 1:
            for i in range (pos1[1],pos2[1]):
                my_pos = [pos2[0],i]
                if my_pos in obs_list:
                    return obs_to_path_check(my_pos, direction, path_index)
            return True
        case 2:
            for i in range (pos1[0],pos2[0]):
                my_pos = [i,pos2[1]]
                if my_pos in obs_list:
                    return obs_to_path_check(my_pos, direction, path_index)
            return True
        case 3:
            for i in range (pos1[1],pos2[1],-1):
                my_pos = [pos2[0],i]
                if my_pos in obs_list:
                    return obs_to_path_check(my_pos, direction, path_index)
            return True
        
def get_obstructions():
    for i in range(rows):
        for j in range(columns):
            if my_map[i][j] != '.' and my_map[i][j] != '^':
                obs_list.append([i,j])
            else:
                free_space.append([i,j])

def get_start_pos():
    for i in range(rows):
        if '^' in my_map[i]:
            for j in range(columns):
                if my_map[i][j] == '^':
                    my_map[i][j] = '.'
                    return [i,j]    

with open(input_file, 'r') as inf:
    for line in inf:
        my_map.append(list(map(str,line.rstrip())))

rows = len(my_map)
columns = len(my_map[0])
current_pos = get_start_pos()
start_pos = current_pos
get_obstructions()

while current_pos != [-1,-1]:
    move(current_pos)

print("Obstructions:\t{0}\nEncountered:\t{1}\nFree Space:\t{2}".format(len(obs_list),len(obs_path),len(free_space)))

#
#   Test if a square can be create for every three obstructions returning the guard to the same path
#   Then test if guard gets to square position without encountering an obstruction,
#   that there are no other obstructions on the path back to the first
#
count = 0
for i in range(len(obs_path)-2):
    new_possibles.add(str(check_square(obs_path[i][0],obs_path[i+1][0],obs_path[i+2][0], obs_path[i][1], i+2)))

new_possibles.remove("[-1, -1]")
print(len(new_possibles))






