import pygame
from settings import *
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self,color,direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.rate = random.randint(4,8)
        self.image = pygame.Surface((SCREEN_H/30,SCREEN_H/30))
        self.rect = pygame.draw.circle(self.image, color, (SCREEN_H/60,SCREEN_H/60),int(SCREEN_H/60))
        self.speed = [0,0]
        self.cw = int(self.rect.w/2)
        self.rand = random.randint(self.cw,P_WIDTH - self.cw)
        if direction == "right":
            self.rect.center = (-100,self.rand)
            self.speed = [self.rate,0]
        if direction == "up":
            self.rect.center = (self.rand,P_HEIGHT + 100)
            self.speed = [0,-self.rate]
        if direction == "left":
            self.rect.center = (P_HEIGHT + 100,self.rand)
            self.speed = [-self.rate,0]
        if direction == "down":
            self.rect.center = (self.rand,-100)
            self.speed = [0,self.rate]
        self.spawn = self.rect.center
    def update(self):
        self.rect = self.rect.move(self.speed)
        #This will check if the enemy is outside a range
        if (self.direction == "right" and self.rect.right > P_WIDTH + 200) or (self.direction == "left" and self.rect.left < -200):
            self.rect.center = self.spawn
            self.rect.centery = random.randint(self.cw,P_WIDTH - self.cw)
        if ((self.direction == "up" and self.rect.top < -200) or (self.direction == "down" and self.rect.bottom > P_WIDTH + 200)):
            self.rect.center = self.spawn
            self.rect.centerx = random.randint(self.cw,P_WIDTH - self.cw)
        PLAY.blit(self.image,self.rect)