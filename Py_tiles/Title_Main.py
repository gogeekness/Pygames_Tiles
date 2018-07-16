#!/usr/bin/env python3
# This is a tile puzzle game
# The idea is to have rows & colnums shift as a move
# When there is a 3-row, 4-row, 5-row, and 4 square then remove them from play
# Play ends if there are no 3,4,5 rows or 4 squares

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
    backscreen = pygame.display.set_mode(config.displaysize)
    backscreen.fill(config.black)
    backscreen.blit(backscreen, (0, 0))

    # load_image("ball.png")
    tiles = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    Tile.containers = tiles, all

    tileboard = Gameboard()

    buffervar = config.boardbuffer
    for i in range(buffervar, config.boardsize[1] + buffervar):
        for j in range(buffervar, config.boardsize[0] + buffervar):
            # print("Cords:", i, j, " color: -> ", tileboard[(i, j)]['color'])
            tileset.append(Tile((50 + ((j - buffervar) * 100), 50 + ((i - buffervar) * 100)), tileboard[(i, j)]['color']))

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
