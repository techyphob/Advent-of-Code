import re
a = []
with open('3.txt', 'r') as input_file:
    for line in input_file:
        a += re.findall('mul\(\d{1,3},\d{1,3}\)', line)
total = 0
for m in a:
    nums = re.findall('\d{1,3}', m)
    total += (int(nums[0]) * int(nums[1]))
print (total)
              


            
