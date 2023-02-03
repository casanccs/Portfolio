import pygame as pg
from functions import *

class Player(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.Surface((800//15,800//15))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = (30,800//30))
        self.vel = [0,0]
        self.grav = 0.4
        self.toJump = False

    def update(self, walls, events, PLAY: pg.Surface):
        #self.rect.move_ip(self.vel)
        colDir = move(self, walls)

        if colDir['down'] or colDir['up']:
            self.vel[1] = 0

        if colDir['down']:
            self.toJump = True

        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and self.toJump:
                    self.vel[1] = -15
                    self.toJump = False
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > PLAY.get_size()[0]:
            self.rect.right = PLAY.get_size()[0]

        # Dying
        if self.rect.top > PLAY.get_size()[1]:
            pg.event.post(pg.event.Event(pg.QUIT, {}))

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.vel[0] = 7
        elif pg.key.get_pressed()[pg.K_LEFT]:
            self.vel[0] = -7
        else:
            self.vel[0] = 0
        
        self.vel[1] += self.grav