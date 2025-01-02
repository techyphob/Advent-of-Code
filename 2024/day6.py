# example = 41
# live = 4454

#0 = north
#1 = east
#2 = south
#3 = west

#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day6-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day6.txt"

my_map = []
count = 0
direction = 0
rows = 0
columns = 0
current_pos = []
path = set()

def get_start_pos():
    for i in range(rows):
        if '^' in my_map[i]:
            for j in range(columns):
                if my_map[i][j] == '^':
                    #my_map[i][j] = '.'
                    return [i,j]    

def direction_change():
    global direction
    direction = (direction + 1)%4
    move()
    
def move():
    global direction
    global current_pos
    
    i = current_pos[0]
    j = current_pos[1]
    match direction:
        case 0:
            if i-1 >= 0:
                if my_map[i-1][j] != '#':
                    current_pos = [i-1,j]
                else:
                    direction_change()
            else:
                current_pos = [-1,-1]
        case 1:
            if j+1 < columns:
                if my_map[i][j+1] != '#':
                    current_pos = [i,j+1]
                else:
                    direction_change()
            else:
                current_pos = [-1,-1]
        case 2:
            if i+1 < rows:
                if my_map[i+1][j] != '#':
                    current_pos = [i+1,j]
                else:
                    direction_change()
            else:
                current_pos = [-1,-1]
        case 3:
            if j-1 >= 0:
                if my_map[i][j-1] != '#':
                    current_pos = [i,j-1]
                else:
                    direction_change()
            else:
                current_pos = [-1,-1]
    
with open(input_file, 'r') as inf:
    for line in inf:
        my_map.append(list(map(str,line.rstrip())))

rows = len(my_map)
columns = len(my_map[0])
current_pos = get_start_pos()
path.add(str(current_pos))

while current_pos != [-1,-1]:
    count += 1
    move()
    path.add(str(current_pos))
print(len(path)-1)
