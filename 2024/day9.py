# example = 1928
# live = 6301895872542
import re

filesystem = ''

#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day9-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day9.txt"

def create_file_map(fs):
    my_map = []
    is_file = True
    count = 0
    for i in range(len(fs)):
        if is_file:
            for j in range(int(fs[i])):
                my_map.append(str(count))
            count += 1
        else:
            for j in range(int(fs[i])):
                my_map.append(('.'))
        is_file = not(is_file)    
    return my_map
    
def compact_filesystem(fs_map):
    for i in range (len(fs_map)-1, -1, -1):
        if fs_map[i].isdigit() and i > fs_map.index('.'):
            fs_map[fs_map.index('.')] = fs_map[i]
            fs_map[i] = '.'
    return fs_map

def checksum(fs_map):
    cs = 0
    for i in range(len(fs_map)):
        if fs_map[i] != '.':
            cs += (i * int(fs_map[i]))
    return cs

with open(input_file, 'r') as inf:
    filesystem = inf.readline()

file_map = create_file_map(filesystem)

print(checksum(compact_filesystem(file_map)))

