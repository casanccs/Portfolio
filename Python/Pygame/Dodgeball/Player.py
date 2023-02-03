import pygame
from settings import *
from functions import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color,control):
        pygame.sprite.Sprite.__init__(self)
        self.control = control #Answers are: "Arrows","WASD", "IJKL", "TFGH,"Joy1", "Joy2"
        if self.control == "Arrows":
            self.controls = [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP]
        elif self.control == "WASD":
            self.controls = [pygame.K_d,pygame.K_a,pygame.K_s,pygame.K_w]
        elif self.control == "IJKL":
            self.controls = [pygame.K_l,pygame.K_j,pygame.K_k,pygame.K_i]
        elif self.control == "TFGH":
            self.controls = [pygame.K_h,pygame.K_f,pygame.K_g,pygame.K_t]
        if self.control == "lstick":
            self.controls = [pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP]
        elif self.control == "rstick":
            self.controls = [pygame.K_d,pygame.K_a,pygame.K_s,pygame.K_w]
        elif self.control == "lbutton":
            self.controls = [pygame.K_l,pygame.K_j,pygame.K_k,pygame.K_i]
        elif self.control == "rbutton":
            self.controls = [pygame.K_h,pygame.K_f,pygame.K_g,pygame.K_t]
        self.image = pygame.Surface((si.current_h/25,si.current_h/25))
        self.rect = pygame.draw.rect(self.image, color ,self.image.get_rect())
        self.rect.center = (PLAY_R.w/2,PLAY_R.h/2)
        self.speed = [0,0]
        self.rate = 5

    def update(self):
        self.rect = self.rect.move(self.speed)
        if pygame.key.get_pressed()[self.controls[0]]:
            self.speed[0] = self.rate
        elif pygame.key.get_pressed()[self.controls[1]]:
            self.speed[0] = -self.rate
        else:
            self.speed[0] = 0
        if pygame.key.get_pressed()[self.controls[2]]:
            self.speed[1] = self.rate
        elif pygame.key.get_pressed()[self.controls[3]]:
            self.speed[1] = -self.rate
        else:
            self.speed[1] = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > PLAY_R.w:
            self.rect.right = PLAY_R.w
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > PLAY_R.h:
            self.rect.bottom = PLAY_R.h
        PLAY.blit(self.image,self.rect)