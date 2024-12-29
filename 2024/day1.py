# part 1
# example = 11
# live = 1722302
# part 2
# example = 31
# live = 20373490

distance = 0
similarity = 0
list_1 = []
list_2 = []

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day1-example.txt"
#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day1.txt"

with open(input_file) as inf:
    for line in inf:
        value = line.rstrip().split()
        list_1.append(int(value[0]))
        list_2.append(int(value[1]))

list_1.sort()
list_2.sort()

for i in range(len(list_1)):
    distance += abs(list_1[i] - list_2[i])
    similarity += list_1[i] * list_2.count(list_1[i])
print('Distance:', distance, sep='\t')
print('Similarity:', similarity, sep='\t')
