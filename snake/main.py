import random
from re import VERBOSE
import pygame as py
import sys
from pygame.math import Vector2
from snake_settings import *

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
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
            main_game.snake.direction = Vector2(0, -1) if main_game.snake.direction != Vector2(0, 1) else main_game.snake.direction
        if event.key == py.K_DOWN:
            main_game.snake.direction = Vector2(0, 1) if main_game.snake.direction != Vector2(0, -1) else main_game.snake.direction 
        if event.key == py.K_LEFT:
            main_game.snake.direction = Vector2(-1, 0) if main_game.snake.direction != Vector2(1, 0) else main_game.snake.direction
        if event.key == py.K_RIGHT:
            main_game.snake.direction = Vector2(1, 0) if main_game.snake.direction != Vector2(-1, 0) else main_game.snake.direction

class FRUIT:
    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruite_rect = py.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        py.draw.rect(screen, FOOD_COLOR , fruite_rect)

class MAIN:
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = FRUIT()

    def draw(self):
        self.snake.draw_body()
        self.fruit.draw_fruit()

    def update(self):
        self.snake.move_snake()

    def poll_event(self, event):
        self.snake.handle_input(event)

    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.randomize()
            self.snake.add_block()

py.init()
screen = py.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = py.time.Clock()
main_game = MAIN()
py.time.set_timer(SCREEN_UPDATE, 150)
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == py.KEYDOWN:
            main_game.poll_event(event)
    screen.fill((175, 215, 70))
    main_game.check_collision()
    main_game.draw()
    py.display.update()
    clock.tick(60)

