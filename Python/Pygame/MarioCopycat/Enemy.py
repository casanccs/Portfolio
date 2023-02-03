import pygame as pg
from functions import *

class Enemy(pg.sprite.Sprite):

    def __init__(self, spawn):
        super().__init__()
        self.image = pg.Surface((800//15,800//15))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = spawn)
        self.vel = [0,0]
        self.grav = 0.4
        self.toJump = False

    def update(self, walls, events, PLAY: pg.Surface, pRect , jump9, jump8):
        #self.rect.move_ip(self.vel)
        colDir = move(self, walls)

        if len(detect(jump9,self.rect)) and self.toJump:
            self.vel[1] = -15
            self.toJump = False
        if len(detect(jump8, self.rect)) and self.toJump:
            self.vel[1] = -8
            self.toJump = False

        if colDir['down'] or colDir['up']:
            self.vel[1] = 0

        if colDir['down']:
            self.toJump = True

        # for event in events:
        #     if event.type == pg.KEYDOWN:
        #         if event.key == pg.K_SPACE and self.toJump:
        #             self.vel[1] = -15
        #             self.toJump = False
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > PLAY.get_size()[0]:
            self.rect.right = PLAY.get_size()[0]

        # Dying
        if self.rect.top > PLAY.get_size()[1]:
            self.kill()

        if pRect.center > self.rect.center:
            self.vel[0] = 4
        elif pRect.center < self.rect.center:
            self.vel[0] = -4
        else:
            self.vel[0] = 0
        
        self.vel[1] += self.grav