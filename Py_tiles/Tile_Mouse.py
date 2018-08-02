# Mouse Class
#
# This will setup the needed methods that are needed for mouse control
#
# It will track location (x,y), Tile location (Tx, Ty), and movement
#
# --------------------------------------------------------



import pygame
import Tile_Config as config

from pygame.locals import *
from Gtiles_Class import Tile
from Board_Class import Gameboard



class Gamemouse:
# create a class Gamemouse to indecate direction of the pointer and position.
# Then take that pointer and convert to tile position.
# With direction and tile-pos then shift the needed tiles.


    def __init__(self):
        self.posstack = [(0, 0), (0, 0), (0, 0)]
        self.mousedir = config.mousedir

    def mouse_press(self, event):
        # mouse button handling
        if pygame.mouse.get_pressed()[0]:
            try:
                return pygame.mouse.get_pos()
                # Convert to tile location
                # Send info back to Main to setup shifting
            except AttributeError:
                pass

    def mouse_direction(self, pos):
        if pos is not None:
            self.posstack.insert(0, pos)

            if len(self.posstack) > 2:
                # No need to retain the old positions
                print("arry size", len(self.posstack))
                nul = self.posstack.pop()
            # Test the difference with new position from the old.
            if self.posstack[0][0] > self.posstack[1][0]:
                return self.mousedir[1] # East
            elif self.posstack[0][0] < self.posstack[1][0]:
                return self.mousedir[3] # West
            # Due the Y inversion on the screen the outputs are swapped.
            elif self.posstack[0][1] < self.posstack[1][1]:
                return self.mousedir[0] # South
            elif self.posstack[0][1] > self.posstack[1][1]:
                return self.mousedir[2] # North
            else:
                return self.mousedir[4] # Still

    def which_tile(selfself, pos):
        pass
