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
        self.array = [[{"color": config.tilecolor[0], "status": "init"} \
                       for x in range(config.fullboardsize[0])] for y in range(config.fullboardsize[1])]
        for i in range(config.boardbuffer, config.boardsize[1] + config.boardbuffer):
            for j in range(config.boardbuffer, config.boardsize[0] + config.boardbuffer):
                self.find_start(self.array[i][j], i, j)

    def __getitem__(self, tup):
        x, y = tup
        return self.array[x][y]

    def __setitem__(self, tup, value):
        x, y = tup
        self.array[x][y] = value


    # to set the gameboard so there are no winning tile groups on the gameboard at the start
    def find_start(self, status, x, y):
        self.array[x][y]['color'] = config.tilecolor[random.randint(1, 4)]
        print("Cords:", x, y, "Color", self.array[x][y]['color'])

        # config.gamesize[0]
        # config.gamesize[1]








