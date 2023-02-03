import pickle
import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self, color, sock, id):
        super().__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (300,300))
        self.vel = [0,0]
        self.speed = 5
        self.sock = sock
        self.id = id

    def update(self):
        if pg.key.get_pressed()[pg.K_UP]:
            self.vel[1] = -self.speed
        if pg.key.get_pressed()[pg.K_DOWN]:
            self.vel[1] = self.speed
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.vel[0] = self.speed
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.vel[0] = -self.speed
        self.rect.move_ip(*self.vel)
        self.vel = [0,0]