import re
a = []
def find_muls(my_string):
    return re.findall("mul\(\d{1,3},\d{1,3}\)", my_string)

input_file = open('E:\OneDrive\Learning\Advent of Code\\3.txt', 'r')
stuff = input_file.readlines()

content = ''.join(stuff)

do = content.find("do()")
dont = content.find("don't()")

a = find_muls(content[0:dont])
print(do, dont, sep= "\t")

while dont > -1:
    do = content.find("do()",dont)
    dont = content.find("don't()",do)
    a += find_muls(content[do:dont])
    print(do, dont, sep= "\t")

#a += find_muls(content[do::])

total = 0
for m in a:
    nums = re.findall('\d{1,3}', m)
    total += (int(nums[0]) * int(nums[1]))
print (total)
              


            
