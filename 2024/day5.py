# example = 143
# line = 7074

rules = []
updates = []
count = 0

#input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day5-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day5.txt"

def get_rule(value):
    return_list = []
    for r in rules:
        if r[0] == value:
            return_list.append(r[1])
    return return_list

def check_update(udate):
    len_u = len(udate)
    for i in range(len_u):
        future_pages = get_rule(udate[i])
        for p in future_pages:
            if p in udate[0:i]:
                return 0
    return int(udate[len_u//2])
    
with open(input_file, 'r') as inf:
    for line in inf:
        if '|' in line:
            rules.append(list(map(int, line.rstrip().split("|"))))
        elif ',' in line:
            updates.append(list(map(int,line.rstrip().split(","))))

for update in updates:
    count += check_update(update)

print(count)
