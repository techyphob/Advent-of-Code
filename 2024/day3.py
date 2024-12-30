# example = 161
# live = 173529487

import re
muls = []
total = 0

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day3-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day3.txt"

inf = open(input_file, 'r')
stuff = inf.readlines()

content = ''.join(stuff)
muls += re.findall('mul\(\d{1,3},\d{1,3}\)', content)

for m in muls:
    nums = re.findall('\d{1,3}', m)
    total += (int(nums[0]) * int(nums[1]))
print (total)
              


            
