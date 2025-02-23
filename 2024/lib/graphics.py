import pygame

class Sprite(object):
    def __init__(self, x, y, colour, size, image = 'circle'):
        self.__colour = colour
        self.__size = size
        self._image = image
        self.__x = x
        self.__y = y
        self.__position = [self.__x, self.__y]

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        self.__position = pos

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    def move_left(self):
        self.x -= 1
    
    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1
    
    def move_down(self):
        self.y += 1

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.position = [x, y]

    def delete(self):
       self.set_position(-1, -1)
 
    def draw(self, surface):
        if self.image == 'circle':
            pygame.draw.circle(surface, self.colour, ((self.x+.5)*self.size, ( \
            self.y+.5)*self.size), self.size/2)
        elif self.image == 'rectangle':
            pygame.draw.rect(surface, self.colour, pygame.Rect((self.x*self.size, self.y*self.size), (self.size, self.size)))