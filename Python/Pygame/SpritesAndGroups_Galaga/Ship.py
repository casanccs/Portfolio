import pygame as pg

class Ship(pg.sprite.Sprite):

    def __init__(self):
        
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((100,100))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(bottom = 1030, centerx = 800)

    def update(self):
        
        self.rect.centerx = pg.mouse.get_pos()[0]


