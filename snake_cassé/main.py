#!/usr/bin/python3

import pygame as py
import sys
from game import *
from snake_settings import *

main_game = MAIN()

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
    # Does the snake never dies ?
    py.display.update()
    clock.tick(60)
