import pygame as py

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 50
BODY_PART = 3
SNAKE_COLOR = "#3393ff"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
CELL_SIZE = 40
CELL_NUMBER = 20
SCREEN_UPDATE = py.USEREVENT

py.init()
screen = py.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = py.time.Clock()
py.time.set_timer(SCREEN_UPDATE, 150)
