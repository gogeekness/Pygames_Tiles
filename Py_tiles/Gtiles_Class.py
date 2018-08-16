# Tile class
# This will setup the graphical displaying of the tiles
#
# It will pull the color and status from teh board class
#
# --------------------------------------------------------

import os, pygame, random, math
import Tile_Config as config
# import Board_Class as board


def load_image(subfile, tcolor):
    try:
        # this code loads the specific color for the tile.
        image = pygame.image.load(os.path.join(config.data_dir, (subfile + tcolor)))
    except pygame.error:
        raise SystemExit('Could not load tile image.', os.path.join(config.data_dir, (subfile + tcolor)))
    return image


# constructor for class Tile
class Tile(pygame.sprite.Sprite):
    image = None

    # Construct the tiles
    def __init__(self, pos, tcolor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = load_image('Tiles_01_', (tcolor + '.png'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speedx = config.speed
        self.speedy = config.speed


    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        # if hit edge reverse direction
        if self.rect.left < 0 or self.rect.right > config.width:
            self.speedx = -self.speedx
            self.rect.x += self.speedx
        if self.rect.top < 0 or self.rect.bottom > config.height:
            self.speedy = -self.speedy
            self.rect.y += self.speedy

    #follow cursor

    # shift up

    # shift down

    # shift left

    # shift right