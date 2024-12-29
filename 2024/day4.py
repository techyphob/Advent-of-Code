# example = 18
# line = 2578
puzzle = []
count = 0

input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day4-example.txt"
input_file = "E:\\OneDrive\\Learning\\Advent of Code\\2024\\input\\day4.txt"

def check_letter(i, j, position, letter, step):
    global count
    global puzzle

#012
#3x4
#567    
    match position:
        case 0:
            if i-step >= 0 and j-step >= 0:
                i -= step
                j -= step
            else:
                return False
        case 1:
            if i-step >= 0:
                i -= step
            else:
                return False
        case 2:
            if i-step >= 0 and j+step < len(puzzle[i]):
                i -= step
                j += step
            else:
                return False
        case 3:
            if j-step >= 0:
                j -= step
            else:
                return False
        case 4:
            if j+step < len(puzzle[i]):
                j += step
            else:
                return False
        case 5:
            if i+step < len(puzzle) and j-step >= 0:
                i += step
                j -= step
            else:
                return False
        case 6:
            if i+step < len(puzzle):
                i += step
            else:
                return False
        case 7:
            if i+step < len(puzzle) and j+step < len(puzzle[i]):
                i += step
                j += step
            else:
                return False
            
    if puzzle[i][j] == letter:
        return True
    else:
        return False

with open(input_file, 'r') as inf:
    for line in inf:
        puzzle += line.rstrip().split()

for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == 'X':
            for n in range(8):
                if check_letter(i, j, n, "M", 1):
                    if check_letter(i, j, n, "A", 2):
                        if check_letter(i, j, n, "S", 3):
                            count += 1
            

print(count)
