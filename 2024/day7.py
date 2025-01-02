# example = 3749
# live = 12553187650171

equations = []
total = 0

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day7-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day7.txt"

def calculate_equation(nums, symb):
    equ = nums[0]
    bin_num = format(symb, '#018b')
    for i in range(1,len(nums)):
        if int(bin_num[-i]) == 1:
            equ *= nums[i]
        else:
            equ += nums[i]
    return equ

def calculate_all(e):
    possible_answers = []
    req_symbs = pow(2,len(e[1])-1)
    for i in range(req_symbs):
        possible_answers.append(calculate_equation(e[1],i))
    if int(e[0]) in possible_answers:
        return int(e[0])
    else:
        return 0

with open(input_file, 'r') as inf:
    for line in inf:
        split_line = line.split(':')
        equations.append([int(split_line[0]),list(map(int,split_line[1].split()))])

for e in equations:
    total += calculate_all(e)

print(total)