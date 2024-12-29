# example = 143
# line = 7074

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
obs_list = []

def obstruction_check():
    test_pos = current_pos
    test_direction = (direction+1)%4
    print("--------------{0}{1}------------".format(current_pos,direction))
    while test_direction != direction:
        match test_direction:
            case 0:
                for i in range(test_pos[0], -1, -1):
                    if [i, test_pos[1]] in obs_list:
                        test_pos = [i+1, test_pos[1]]
                        print(test_pos, test_direction)
                #desire_vector = [current_pos[0],0]
            case 1:
                for j in range(test_pos[1], columns):
                    if [test_pos[0], j] in obs_list:
                        test_pos = [test_pos[0], j-1]
                        print(test_pos, test_direction)
                #desire_vector = [current_pos[1],1]
            case 2:
                for i in range(test_pos[0], rows):
                    if [i, test_pos[1]] in obs_list:
                        test_pos = [i-1, test_pos[1]]
                        print(test_pos, test_direction)
                #desire_vector = [current_pos[0],2]
            case 3:
                for j in range(test_pos[1], -1, -1):
                    if [test_pos[0], j] in obs_list:
                        test_pos = [test_pos[0], j+1]
                        print(test_pos, test_direction)
                #desire_vector = [current_pos[1],3]    
        test_direction = (test_direction+1)%4

def get_obstructions():
    global obs_list
    for i in range(rows):
        for j in range(columns):
            if my_map[i][j] != '.' and my_map[i][j] != '^':
                obs_list += [list([i,j])]
    
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
start_pos = get_start_pos()
get_obstructions()

