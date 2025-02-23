# example   12
# live      

from lib.utils import read_input
from numpy import array
import pygame
from lib.graphics import Sprite

BLOCK_SIZE = 4
SCR_X = 101
SCR_Y = 103

SCR_SIZE = (BLOCK_SIZE * SCR_X, BLOCK_SIZE * SCR_Y)
DSP_SIZE = (BLOCK_SIZE * (SCR_X + 2), BLOCK_SIZE * (SCR_Y + 3))

pygame.init()

display = pygame.display.set_mode(DSP_SIZE)
scr = pygame.surface.Surface((SCR_SIZE))
display.fill((32, 82, 2))
scr.fill((83, 132, 84))

YEAR = '2024'
example = False
map_type = str
day = 14
grid_size = (101,103)

class robot(Sprite):
    def __init__(self, position, velocity):
        super().__init__(position[0], position[1], (15, 252, 3), BLOCK_SIZE)
        self.dx = velocity[0]
        self.dy = velocity[1]
    
    def patrol(self, time):
        self.x = (self.x + self.dx) % grid_size[0]
        self.y = (self.y + self.dy) % grid_size[1]
        
    def draw(self, surface):
        super().draw(surface)

def split_line(input_line):
    return array(list(map(int,input_line[2:].split(','))))

def start():
    alive = True
    clock = pygame.time.Clock()

    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    alive = False

            display.fill((32, 82, 2))
            scr.fill((83, 132, 84))
            for r in robots:
                r.patrol(1)
                r.draw(scr)
            display.blit(scr,(BLOCK_SIZE,BLOCK_SIZE*2))          
            pygame.display.update()
            clock.tick(10)

robots = []
input = read_input(YEAR, day, map_type, example)
for l in input:
    pv = l.split()
    robots.append(robot(split_line(pv[0]), split_line(pv[1])))

start()