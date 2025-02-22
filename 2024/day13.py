# example   480
# live      34393

from lib.utils import read_input
from numpy import array
import re

YEAR = '2024'
example = False
map_type = str
day = 13

class claw_machine(object):
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        # part 1
        #self.prize = prize
        #part 2
        self.prize = 10000000000000 + prize
    
    def cost_to_prize(self):
        b_presses = ((self.a[0]*self.prize[1])-(self.a[1]*self.prize[0]))/((self.a[0]*self.b[1])-(self.a[1]*self.b[0]))
        a_presses = (self.prize[0]-(b_presses*self.b[0]))/self.a[0]
        if b_presses == int(b_presses) and a_presses == int(a_presses):
            return int(a_presses * 3 + b_presses)
        else:
            return 0
        
def split_line(input_line, sep):
    s = re.search("X\\" + sep + "+(\d*).+Y\\" + sep + "(\d*)", input_line)
    return array([int(s[1]),int(s[2])])

input = read_input(YEAR, day, map_type, example)
machines = []
for i in range(0, len(input), 4):
    machines.append(claw_machine(split_line(input[i], '+'), split_line(input[i+1], '+'), split_line(input[i+2], '=')))

cost = 0
for m in machines:
    cost += m.cost_to_prize()
print(cost)