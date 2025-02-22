# example = 2858
# live = 
# 48765332710 too low

import re

filesystem = '.'
file_lengths = {}
spaces = {}

#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day9-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day9.txt"
def find_spaces(fs_map):
    dots = 0
    last_index = 0
    spaces = {}
    for i in range(len(fs_map)):
        if fs_map[i] == '.' and i > last_index:
            for j in range(i, len(fs_map)):
                if fs_map[j] == '.': 
                    dots += 1
                else:
                    spaces[i] = dots
                    dots = 0
                    last_index = j + dots
                    break
    return spaces

def find_index(fs_map, value):
    for i in range(len(fs_map)):
        if fs_map[i] == str(value):
            return i
    return i

def find_space_index(spaces, required_len):
    for i in sorted(spaces):
        if spaces[i] >= required_len:
            spaces[i + required_len] = spaces[i] - required_len
            spaces[i] = 0
            return i
    return -1
    
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
            for j in range(int(fs[i])):
                my_map.append(('.'))
        is_file = not(is_file)
    return my_map

def compact_filesystem(fs_map):
    for i in sorted(file_lengths.keys(), reverse = True):
        print(i)
        file_len = file_lengths[i]
        space_index = find_space_index(spaces, file_len)
        if space_index > 0 and space_index < find_index(fs_map,i):
            for j in range(len(fs_map)):
                    if fs_map[j] == str(i):
                        fs_map[j] = '.'
            for k in range(file_len):
                    fs_map[space_index + k] = str(i)
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
spaces = find_spaces(file_map)
#print(compact_filesystem(file_map))
print(checksum(compact_filesystem(file_map)))

