import pygame as pg
from random import randint

class Pipes:
    
    def __init__(self, space): #set distance 140
        self.surf = pg.Surface((100,5000))
        self.surf.fill((0,255,0))
        #rect1 is top pipe
        self.rect1 = self.surf.get_rect(left = 800, bottom = randint(10,800 - space - 10))
        self.rect2 = self.surf.get_rect(left = 800, top = self.rect1.bottom + space)
        self.v = [-10,0]


    def update(self, surf):
        
        self.rect1.move_ip(self.v)
        self.rect2.move_ip(self.v)
        
        surf.blits([(self.surf, self.rect1),(self.surf, self.rect2)])