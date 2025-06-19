from snake_settings import *
from random import randint
from pygame.math import Vector2

class FRUIT:
    def __init__(self, snake_pos, fruit_pos = []):
        self.fruit_pos = fruit_pos
        self.randomize(snake_pos)

    def randomize(self, snake_pos):
        self.x = randint(0, CELL_NUMBER - 1)
        self.y = randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        if (self.pos in snake_pos or self.pos in self.fruit_pos) :
            self.randomize(snake_pos)

    def draw_fruit(self):
        fruite_rect = py.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        py.draw.rect(screen, FOOD_COLOR , fruite_rect)

