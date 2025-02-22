#   example = 55312
#   live = 191690

#   rules
#
#   stone = 0 replace with stone = 1
#   if even number of digits replace with 2 stones 
#   if neither new stone x2024
#
from functools import cache
from math import log10
#input = "125 17"
input = "30 71441 3784 580926 2 8122942 0 291"

stones  = list(map(int,input.split()))
number_of_stones = 0

@cache
def blink(stone, iteration = 0, max_iteration = 75):
    if iteration == max_iteration:
        return 1

    iteration += 1
    if stone == 0:
        return blink(1, iteration, max_iteration)

    l = int(log10(stone)) + 1
    if l%2 == 0:
        return blink(int(stone//(pow(10,l/2))), iteration, max_iteration) + blink(int(stone%(pow(10,l/2))), iteration, max_iteration)

    return blink(stone * 2024, iteration, max_iteration)

for stone in stones:
    number_of_stones += blink(stone)
    
print(number_of_stones)




#for i in range (75):
#    temp = []
#    temp += [1] * stones.count(0)
#    stones = [s for s in stones if s != 0]
    #temp += [2024] * stones.count(1)
    #stones = [s for s in stones if s != 1]
    #temp += [2] * stones.count(20)
    #temp += [0] * stones.count(20)
    #stones = [s for s in stones if s != 20]
    #temp += [2] * stones.count(24)
    #temp += [4] * stones.count(24)
    #stones = [s for s in stones if s != 24]
