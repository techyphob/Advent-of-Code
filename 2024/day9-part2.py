# example = 2858
# live = 
import re

filesystem = ''
file_lengths = {}
spaces = {}

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day9-example.txt"
#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day9.txt"

def create_file_map(fs):
    my_map = []
    is_file = True
    count = 0
    for i in range(len(fs)):
        if is_file:
            file_lengths[count] = int(fs[i])
            for j in range(int(fs[i])):
                my_map.append(str(count))
            count += 1
        else:
            spaces[i] = int(fs[i])
            for j in range(int(fs[i])):
                my_map.append(('.'))
        is_file = not(is_file)    
    return my_map

def compact_filesystem(fs_map):
    for i in sorted(file_lengths.keys(), reverse = True):
        file_len = file_lengths[i]
        if file_len in spaces.keys():
            space_start = list(spaces.values()).index(file_len)
            for x in range(len(fs_map)):
                if fs_map[x] == i:
                    fs_map[i] ='.'
            for j in range(file_len):
                fs_map[space_start+ j] = i
    print(fs_map)
def checksum(fs_map):
    cs = 0
    for i in range(len(fs_map)):
        if fs_map[i] != '.':
            cs += (i * int(fs_map[i]))
    return cs

with open(input_file, 'r') as inf:
    filesystem = inf.readline()

file_map = create_file_map(filesystem)

print(compact_filesystem(file_map))
print(file_lengths)
print(spaces)
#print(checksum(compact_filesystem(file_map)))

