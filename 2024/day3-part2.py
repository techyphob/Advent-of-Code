# example = 48
# line = 99532691

import re
muls = []
total = 0

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day3-part2-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day3.txt"

def find_muls(my_string):
    return re.findall("mul\(\d{1,3},\d{1,3}\)", my_string)

inf = open(input_file, 'r')
stuff = inf.readlines()
content = ''.join(stuff)

do = content.find("do()")
dont = content.find("don't()")

muls += find_muls(content[0:dont])

while dont > -1:
    do = content.find("do()",dont)
    dont = content.find("don't()",do)
    muls += find_muls(content[do:dont])

for m in muls:
    nums = re.findall('\d{1,3}', m)
    total += (int(nums[0]) * int(nums[1]))
print (total)
              


            
