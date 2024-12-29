rules = []
updates = []
count = 0

def get_rule(value):
    global rules
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
    
with open("E:\OneDrive\Learning\Advent of Code\i5.txt", 'r') as input_file:
    for line in input_file:
        if '|' in line:
            rules += [list(map(int, line.rstrip().split("|")))]
        elif ',' in line:
            updates += [list(map(int,line.rstrip().split(",")))]

for update in updates:
    count += check_update(update)

print(count)
