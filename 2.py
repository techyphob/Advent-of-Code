errors = 0
safe = 0

def diff_error(n):
    diff_error_cnt = 0
    for i in n:
        if abs(i) > 3 or abs(i) < 1:
            diff_error_cnt += 1
    return diff_error_cnt

def direction_check(n):
    pos = 0
    neg = 0
    for i in n:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
    return len(n) - abs(neg - pos)


with open('2a.txt', 'r') as input_file:
    for line in input_file:
        errors = 0
        num_list = list(map(int, line.split()))
        diff_list = [x-y for x,y in zip(num_list, num_list[1::])]
        diff_errors = diff_error(diff_list)
        direction_changes = direction_check(diff_list)
        if diff_errors == 0 and direction_changes <= 2:
            safe += 1
        elif diff_errors == 1 and direction_changes == 0:
            safe += 1
            print(num_list, diff_list, direction_changes, sep = '\t')
        #remove 1 for first check
            
print ('Safe:\t', safe)

#692
#698
#716
#705
#687
#694
#697
#704







