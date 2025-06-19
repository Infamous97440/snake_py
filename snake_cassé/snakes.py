from snake_settings import *
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_body(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = py.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            py.draw.rect(screen, SNAKE_COLOR, block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def handle_input(self, event):
        if event.key == py.K_UP:
            self.direction = Vector2(0, 1) if self.direction != Vector2(0, 1) else self.direction
        if event.key == py.K_LEFT:
            self.direction = Vector2(1, 0) if self.direction != Vector2(1, 0) else self.direction
        # The snake only moves left and up ???

