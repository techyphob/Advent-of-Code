import os
import sys

def read_input(year, day, map_type=str, example=False): 
    try:
        if example:
            filename = f'day{day}-example.txt'
        else:
            filename = f'day{day}.txt'
        with open(os.path.join(year, 'input', filename)) as input_file:
            return [map_type(line.strip()) for line in input_file]
    
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
