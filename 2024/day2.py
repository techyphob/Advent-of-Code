# example = 2
# line = 680

safe = 0
report_list = []

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day2-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day2.txt"

def diff_check(n):
    for i in n:
        if abs(i) > 3 or abs(i) < 1:
            return 0
    return 1

with open(input_file) as inf:
    for line in inf:
        report_list.append(list(map(int, line.split())))

for report in report_list:
    if report == sorted(report) or report == sorted(report, reverse=True):
        safe += diff_check([abs(x-y) for x,y in zip(report, report[1::])])

print ('Safe:\t', safe)
