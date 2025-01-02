# example = 6
# live = 

#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day6-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day6.txt"

class TestMap():
    def __init__(self, layout):
        self.__map = layout
        self.__start_pos = []
        self.__direction = 0
        self.i = -1
        self.j = -1
        self.__obs = []
        self.__obs_path = []
        self.__space = []
        self.__unique_moves = set()
        self.__moves = 0

        self.rows = len(layout)
        self.cols = len(layout[0])
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.__map[i][j] != '.' and self.__map[i][j] != '^':
                    self.__obs.append([i,j])
                elif self.__map[i][j] == '^':
                    self.start_pos = [i, j]
                    self.__space.append([i,j])
                else:
                    self.__space.append([i,j])

    def get_current_pos(self):
        return [self.i, self.j]
    
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self):
        self.__direction = 0

    def direction_change(self):
        self.__direction = (self.__direction + 1)%4
        self.move()

    @property
    def obs_path(self):
        return self.__obs_path

    @property
    def obs(self):
            return self.__obs
    
    @obs.setter
    def setter(self, my_obs):
        self.__obs = my_obs

    @property
    def space(self):
        return self.__space
    
    @space.setter
    def space(self, my_space):
        self.__space = my_space

    @property
    def start_pos(self):
        return self.__start_pos
    
    @start_pos.setter
    def start_pos(self, pos):
        self.__start_pos = pos
        self.i = pos[0]
        self.j = pos[1]
        self.__unique_moves.add(str(pos))

    @property
    def unique_moves(self):
        return len(self.__unique_moves)
    
    @property
    def moves(self):
        return self.__moves
    
    @moves.setter
    def setter(self, move_count):
        self.__moves = move_count

    def check_space(self, i, j):
        return self.__map[i][j] != '#'
    
    def move(self):
        #0 = north
        #1 = east
        #2 = south
        #3 = west

        if self.i == -1 and self.j == -1:
            return False
        else:
            match self.__direction:
                case 0:
                    if self.i-1 >= 0:
                        if self.check_space(self.i-1,self.j):
                            self.i = self.i-1
                        else:
                            self.__obs_path.append([[self.i-1,self.j], self.direction])
                            #obs_path_2.append([self.i-1,self.j])
                            self.direction_change()
                    else:
                        self.i, self.j = (-1,-1)
                case 1:
                    if self.j+1 < self.cols:
                        if self.check_space(self.i,self.j+1):
                            self.j = self.j+1
                        else:
                            self.__obs_path.append([[self.i,self.j+1], self.direction])
                            #obs_path_2.append([i,j+1])
                            self.direction_change()
                    else:
                        self.i, self.j = (-1,-1)
                case 2:
                    if self.i+1 < self.rows:
                        if self.check_space(self.i+1,self.j):
                            self.i = self.i+1
                        else:
                            self.__obs_path.append([[self.i+1,self.j], self.direction])
                            #obs_path_2.append([i+1,j])
                            self.direction_change()
                    else:
                        self.i, self.j = (-1,-1)
                case 3:
                    if self.j-1 >= 0:
                        if self.check_space(self.i,self.j-1):
                            self.j = self.j-1
                        else:
                            self.__obs_path.append([[self.i,self.j-1], self.direction])
                            #obs_path_2.append([i,j-1])
                            self.direction_change()
                    else:
                        self.i, self.j = (-1,-1)
            if self.i != -1:
                self.__unique_moves.add(str([self.i,self.j]))
                self.__moves += 1
            return True

    def reset(self, new_pos, new_driection):
        self.__moves = 0
        self.__direction = new_driection
        self.__unique_moves = set()
        self.start_pos = new_pos


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

start_map = []
with open(input_file, 'r') as inf:
    for line in inf:
        start_map.append(list(map(str,line.rstrip())))

a_map = TestMap(start_map)

print("Obstructions:\t\t{0}\nFree Space:\t\t{1}\nStart Position:\t\t{2}\nStart Direction:\t{3}".format(len(a_map.obs),len(a_map.space),a_map.start_pos, a_map.direction))
while a_map.move():
    pass    
print("Unique Positions:\t{0}\nMoves:\t\t\t{1}\nObs Encountered:\t{2}".format(a_map.unique_moves, a_map.moves,len(a_map.obs_path),))
#print(a_map.obs_path)
#print([x[0] for x in a_map.obs_path])

#   Test if a square can be create for every three obstructions returning the guard to the same path
#   Then test if guard gets to square position without encountering an obstruction,
#   that there are no other obstructions on the path back to the first
#
#count = 0
#for i in range(len(obs_path)-2):
#    new_possibles.add(str(check_square(obs_path[i][0],obs_path[i+1][0],obs_path[i+2][0], obs_path[i][1], i+2)))##
#
#new_possibles.remove("[-1, -1]")
#print(len(new_possibles))
