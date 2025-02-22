#   example = 55312
#   live = 191690

#   rules
#
#   stone = 0 replace with stome = 1
#   if even number of digits replace with 2 stones 
#   if neither new stone x2024
#

#input = "125 17"
input = "30 71441 3784 580926 2 8122942 0 291"

for i in range (25):
    temp = ""
    for stone in input.split():
        l = len(stone)
        if stone == '0':
            temp += ' 1'
        elif l%2 == 0:
            temp += ' ' + str(int(stone[0:l//2]))
            temp += ' ' + str(int(stone[l//2:]))
        else:
            temp += ' '  + str(int(stone)*2024)
    input = temp

print(len(input.split()))
