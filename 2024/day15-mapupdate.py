import os

with open(os.path.join('2024', 'input', 'day15-example-first.txt')) as input_file:
    old = input_file.read()

print(old)
old_grid, directions  = old.split('\n\n')

new_grid = ''
for tile in old_grid:
    match tile:
        case 'O':
            new_grid += '[]'
        case '#':
            new_grid += '##'
        case '.':
            new_grid += '..'
        case '@':
            new_grid += '@.'
        case '\n':
            new_grid += '\n'

with open(os.path.join('2024', 'input', 'day15-example.txt'), 'w+') as output_file:
    output_file.write(new_grid + '\n\n' + directions)
