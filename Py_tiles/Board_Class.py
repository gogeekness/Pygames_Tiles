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
        # Create a blank init game field that includes a buffer region around the game region
        self.array = [[{"color": config.tilecolor[0], "status": config.tilestatus[0]}
            for x in range(config.fullboardsize[0])] for y in range(config.fullboardsize[1])]
        #
        # Now create the tiles for the game board in the center of the play field
        for i in range(config.boardbuffer, config.boardsize[1] + config.boardbuffer):
            for j in range(config.boardbuffer, config.boardsize[0] + config.boardbuffer):
                self.find_start(self.array[i][j], i, j)


    # to help indexing the board
    # ---
    def __getitem__(self, tup):
        x, y = tup
        return self.array[x][y]

    def __setitem__(self, tup, value):
        x, y = tup
        self.array[x][y] = value
    # ---


    def checkequal(self, pos_list, tile_color, x, y):
        checklist = []
        for i, j in pos_list:
            checklist.append(config.tilecolor.index(self.array[i+x][j+y]['color']))
        #print("Chceklist:", checklist)
        return False if checklist.count(tile_color) < len(pos_list) else True


    # to set the gameboard so there are no winning tile groups on the gameboard at the start
    def find_start(self, status, x, y):
        # checksum the 3 right-horizontal, and 3-vertical, and 4-square
        # Then see if the tile needs to be changed
        checksumh, checksumv, checksums = 0, 0, 0
        three = True
        # while the modula is == 0 then repeat
        while three:
            tilecolor = random.randint(1, 4)
            self.array[x][y]['color'] = config.tilecolor[tilecolor]
            #print("Tile color for xy", config.tilecolor[tilecolor])
            checksumh = self.checkequal(config.pattern3l[0], tilecolor, x, y)
            checksums = self.checkequal(config.pattern4s[2], tilecolor, x, y)
            checksumv = self.checkequal(config.pattern3l[3], tilecolor, x, y)
            if not checksumh and not checksumv and not checksums:
                # If the sum don't match then break out of the loop and
                #print(">== New Tile Cords: ", x, y, "Value: ", self.array[x][y]['color'])
                three = False








