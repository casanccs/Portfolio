import pygame as pg

class Bullet(pg.sprite.Sprite):

    def __init__(self, pRec):
        
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((20,55))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect(center = pRec.center)

    def update(self):
        
        self.rect.move_ip(0,-15)

        if self.rect.bottom < 0:
            self.kill()

