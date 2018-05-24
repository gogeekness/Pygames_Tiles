# Tile class
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


class Tile(pygame.sprite.Sprite):
    image = None

    # Construct the tiles
    def __init__(self, pos, tcolor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = load_image('Tiles_01_', (tcolor + '.png'))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        angle = (random.random() * 2 * math.pi)
        self.speedx = (math.cos(angle) * config.speed)
        self.speedy = (math.sin(angle) * config.speed)


    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        # if hit edge reverse direction
        if self.rect.left < 0 or self.rect.right > config.width:
            self.speedx = -self.speedx
            self.rect.x += self.speedx
        if self.rect.top < 0 or self.rect.bottom > config.height:
            self.speedy = -self.speedy
            self.rect.y += self.speedy

    # shift up

    # shift down

    # shift left

    # shift right