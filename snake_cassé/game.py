import pygame as py
import sys
from snake_settings import *
from fruit import FRUIT
from snakes import Snake

class MAIN:
    def __init__(self, n = 10) -> None:
        self.snake = Snake() # Calls the __init__() from 'snakes' file
        self.fruit = []
        self.score = 0
        for i in range(0):
            self.fruit.append(FRUIT(self.snake.body, self.fruit))

    def draw(self):
        self.draw_grass()
        self.snake.draw_body()
        for fruit in self.fruit:
            fruit.draw_fruit()

    def update(self):
        self.snake.move_snake()

    def game_over(self):
        if False: # The snake can quit the screen borders...
            py.quit()
            sys.exit()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                py.quit()
                sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = py.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        py.draw.rect(screen, grass_color, grass_rect)

    def poll_event(self, event):
        self.snake.handle_input(event)

    def check_collision(self):
        for fruit in self.fruit:
            if self.snake.body[0] == fruit.pos:
                # Is something missing ? What does the snake should do when eating a fruit ?
                self.score += 1
                fruit.randomize([]) # Would be better if the fruit was unable to spawn on the snake's body

