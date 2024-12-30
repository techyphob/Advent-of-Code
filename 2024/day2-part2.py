# example = 4
# live = 

errors = 0
safe = 0
report_list = []

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day2-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day2.txt"

def diff_check(n):
    for i in n:
        if abs(i) > 3 or abs(i) < 1:
            return False
    return True

def safe_test(n):
    global errors
    if errors > 1:
        return False
    if n[1] - n[0] > 0:
        ascending = True
    else:
        ascending = False
        
    for i in range(0, len(n) - 1):
        if n[i] - n[i+1] >= 1 and n[i] - n[i+1] <= 3 and not ascending:
            continue
        elif (n[i] - n[i+1]) * -1 >= 1 and (n[i] - n[i+1]) * -1 <= 3 and ascending:
            continue
        else:
            if i == 0 and abs(n[0] - n[1]) <= 3:
                print(n[0], n[1], n[2])
            if i+2 == len(n):
                del(n[i+1])
                errors += 1
                return safe_test(n)
            else:
                if n[i] - n[i+2] >= 1 and n[i] - n[i+2] <= 3 and not ascending:
                    del(n[i+1])
                    errors += 1
                    return safe_test(n)
                elif (n[i] - n[i+2]) * -1 >= 1 and (n[i] - n[i+2]) * -1 <= 3 and ascending:
                    del(n[i+1])
                    errors += 1
                    return safe_test(n)
                else:
                    return False
    return True

with open(input_file) as inf:
    for line in inf:
        report_list.append(list(map(int, line.split())))

for report in report_list:
    if report == sorted(report) or report == sorted(report, reverse=True):
        safe += diff_check([abs(x-y) for x,y in zip(report, report[1::])])

print ('Safe:\t', safe)


#692
#698
#716
#705
#687
#694
#697
#704
#692
#698
#697 ???
#716







