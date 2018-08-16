'''
Mouse Class
#
# This will setup the needed methods that are needed for mouse control
#
# It will track location (x,y), Tile location (Tx, Ty), and movement
#
# --------------------------------------------------------
'''


import pygame, os
import Tile_Config as config
from pygame.locals import *
from Gtiles_Class import Tile
from Board_Class import Gameboard



class Gamemouse:
    '''create a class Gamemouse to indecate direction of the pointer and position.
    Then take that pointer and convert to tile position.
    With direction and tile-pos then shift the needed tiles. '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call sprite initializer
        self.pos = (0, 0)
        self.mousedir = config.mousedir
        try:
            self.image = pygame.image.load(os.path.join(config.data_dir, "Tile-cursor.png"))
        except pygame.error:
            raise SystemExit('Could not load tile image.', os.path.join(config.data_dir, "Tile-cursor.png"))
        self.image = self.image.convert()
        self.rect = self.image
        self.select = 0  # Is button pressed
        self.shift = 0  # Is shifting tiles

    def update(self):
        "move the fist based on the mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.select:
            self.rect.move_ip(5, 10)

    def mouse_press(self, event):
        # mouse button handling
        if pygame.mouse.get_pressed()[0]:
            try:
                self.pos = pygame.mouse.get_pos()
                return self.pos
            except AttributeError:
                pass


    def mouse_direction(self, pos):
        # relative direction for the pointer.
        if pos is not None:
            mouserel = pygame.mouse.get_rel()
            if mouserel[0] > 0:
                return self.mousedir[1] # East
            elif mouserel[0] < 0:
                return self.mousedir[3] # West
            # Due the Y inversion on the s
            # creen the outputs are swapped.
            elif mouserel[1] < 0:
                return self.mousedir[0] # South
            elif mouserel[1] > 0:
                return self.mousedir[2] # North
            else:
                return self.mousedir[4] # Still


    def which_tile(self, pos):
        # Convert to tile location
        # Send info back to Main to setup shifting
        # if on tile, then mouse.select = 1
        pass
