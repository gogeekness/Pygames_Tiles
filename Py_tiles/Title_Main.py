#!/usr/bin/env python3
# Multi Bonce Ball

import os
import pygame
import random
import sys
import Tile_Config as config
from Tile_classes import Tile
from Board_Class import Gameboard
from pygame.locals import *

# ----------------------------------------------------------------------------------------------------

''' Notes:
 3 across will be a normal but the the fill-side as the direction of the last shift
 4 across will be like a normal but the whole board shifts as with the direction of the last shift
 4 square will be spiral shift of 4 lines
 5 across will be like a normal but the whole board shifts as with the direction of the last shift'''



def main():# define where data directory is located
    pygame.init()
    tileset = []

    # make a background
    backscreen = pygame.display.set_mode(config.size)
    backscreen.fill(config.black)
    backscreen.blit(backscreen, (0, 0))

    # load_image("ball.png")
    tiles = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    Tile.containers = tiles, all

    tileboard = Gameboard


    for i in range(0, 7):
        for j in range(0, 7):
            tileset.append(Tile((50 + (j * 100), 50 + (i * 100)), config.tilecolor[random.randint(1, 4)]))

    # keep track of time
    clock = pygame.time.Clock()
    # game loop
    while 1:
        # get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) \
                    or (event.type == KEYDOWN and event.key == K_q):
                sys.exit()

        # clear sprites
        backscreen.fill(config.black)

        # update sprites
        all.update()

        # update display
        dirty = all.draw(backscreen)
        pygame.display.update(dirty)

        pygame.display.flip()

        # timer set for 30 frames
        clock.tick(30)


# This is the main_init
if __name__ == '__main__':
    main()
