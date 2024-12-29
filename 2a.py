errors = 0
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

safe = 0

with open('2a.txt', 'r') as input_file:
    for line in input_file:
        errors = 0
        number_list = list(map(int, line.split()))
        if safe_test(number_list):
            safe += 1
print ('Safe:\t', safe)

#692
#698
#697 ???
#716







