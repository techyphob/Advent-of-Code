#012
#3x4
#567

puzzle = []
count = 0
def check_letter(i, j, position, letter, step):
    global count
    global puzzle
    
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


with open("E:\OneDrive\Learning\Advent of Code\\4a.txt", 'r') as input_file:
    for line in input_file:
        puzzle += line.rstrip().split()

for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):  #assume puzzle is square
        if puzzle[i][j] == 'X':         #i = row, j = col
            for n in range(8):
                if check_letter(i, j, n, "M", 1):
                    if check_letter(i, j, n, "A", 2):
                        if check_letter(i, j, n, "S", 3):
                            count += 1
            

print(count)

