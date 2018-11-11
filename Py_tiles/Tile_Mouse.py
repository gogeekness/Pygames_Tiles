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


class Gamemouse(pygame.sprite.Sprite):
    '''create a class Gamemouse to indecate direction of the pointer and position.
    Then take that pointer and convert to tile position.
    With direction and tile-pos then shift the needed tiles. '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.pos = (0, 0)
        self.mousedir = config.mousedir
        try:
            self.image = pygame.image.load(os.path.join(config.data_dir, "Tile-cursor.png"))
        except pygame.error:
            raise SystemExit('Could not load tile image.', os.path.join(config.data_dir, "Tile-cursor.png"))
        self.rect = self.image.get_rect()
        #self.layer = pygame.sprite.LayeredUpdates()
        self.select = 0  # Is button pressed
        self.shift = 0  # Is shifting tiles

    def update(self):
        # move the fist based on the mouse position
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
        if self.select:
            self.rect.move_ip(5, 10)


    def mouse_press(self, event):
        # mouse button handling
        if pygame.mouse.get_pressed()[0]:
            try:
                self.pos = pygame.mouse.get_pos()
                self.select = True
                return self.pos
            except AttributeError:
                pass

    def mouse_collide(self, spritegroup):
        # Is teh mouse/cursor on a tile
        collide = None
        if self.select:
            collide = pygame.sprite.spritecollide(self, spritegroup, False)
        return collide

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
