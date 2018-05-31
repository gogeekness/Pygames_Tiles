# Graphics Tile class
# To display the tiles on the screen
# To shift the tiles on the screen while indicating the underlying board status

import os, pygame, random, math
import Tile_Config as config

# define where data directory is located
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data_dir")


def load_image(subfile, tcolor):
    try:
        image = pygame.image.load(os.path.join(data_dir, (subfile + tcolor)))
    except pygame.error:
        raise SystemExit('Could not load tile image.', os.path.join(data_dir, (subfile + tcolor)))
    return image

class