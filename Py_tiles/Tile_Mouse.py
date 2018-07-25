#!/usr/bin/env python3

import pygame
from pygame.locals import *
from Gtiles_Class import Tile
from Board_Class import Gameboard


def mouse_press(event):

    # mouse button handling
    if event.type == pygame.MOUSEBUTTONDOWN or mouselatch:
        print("Mouse Location", pygame.mouse.get_pos())
        mouselatch = True

    if event.type == pygame.MOUSEBUTTONUP:
        mouselatch = False

    