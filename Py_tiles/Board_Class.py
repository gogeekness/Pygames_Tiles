# GameBoard class

import os, pygame, random, math
import Tile_Config as config


# The main class that the other classes will work from.
# From this the graphics will pull status information and color type.
# The other get there info from this gameboard

class Gameboard:

    # create a 2d array with the inital information for the gameboard
    # Sets status for the board as "init"
    def __init__(self):
        self.array = [[{"color": config.tilecolor[random.randint(1, 5)], "status": "init"} \
                       for x in range(config.gamesize[0])] for y in range(config.gamesize[1])]
        for i in range (0, config.gamesize[1]):
            for j in range (0, config.gamessize[0]):
                gameboard.find_3(array[i,j], (i, j))


    # to set the gameboard so there are no 3/4/5 tile groups on the gameboard at the start
    def find_3(self, pos):
        print(self.pos[0],pos[1])
        # config.gamesize[0]
        # config.gamesize[1]






