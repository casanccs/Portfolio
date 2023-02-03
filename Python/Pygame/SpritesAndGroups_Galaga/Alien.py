import pygame as pg
from random import randint

class Alien(pg.sprite.Sprite):

    def __init__(self):
        
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((100,100))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(left = randint(0, 1820), bottom = -100)

    def update(self):
        #move
        self.rect.move_ip(0, 5)

        if self.rect.top > 1080:
            self.kill()

