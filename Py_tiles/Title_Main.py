#!/usr/bin/env python3
# Multi Bonce Ball

import os
import pygame
import random
import sys
import Tile_Config as config
from Tile_classes import Tile
from pygame.locals import *

# ----------------------------------------------------------------------------------------------------


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

    for i in range(0, 5):
        for tcolor in config.tilecolor:
            tileset.append(Tile((random.random() * 700 + 50, random.random() * 500 + 50), tcolor))

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
