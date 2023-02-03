import pygame as pg
from functions import *
from random import randint

class Player(pg.sprite.Sprite):


    def __init__(self,walls, id, sock, char, type):
        super().__init__()
        self.id = id #Be used to identify which character they are
        self.sock = sock
        self.type = type
        if self.type == 0:
            if char == 0:
                self.image = pg.image.load('assets/Characters/n0.png')
            if char == 1:
                self.image = pg.image.load('assets/Characters/n1.png') 
            if char == 2:
                self.image = pg.image.load('assets/Characters/n2.png') 
            if char == 4:
                self.image = pg.image.load('assets/Characters/n4.png') 
        if self.type == 1:
            if char == 0:
                self.image = pg.image.load('assets/Characters/z0.png')
            if char == 1:
                self.image = pg.image.load('assets/Characters/z1.png') 
            if char == 2:
                self.image = pg.image.load('assets/Characters/z2.png') 
            if char == 4:
                self.image = pg.image.load('assets/Characters/z4.png') 
        if self.type == 2:
            self.image = pg.image.load('assets/landmine.png')
       
        self.image = pg.transform.scale(self.image, (50,50))

        #spawning
        if self.type == 1: #ZOMBIE SPAWNING
            self.rect = self.image.get_rect(bottomright = (2000,2000))

        if self.type == 0: 
            self.rect = self.image.get_rect(topleft = (0,0))

        self.vel = [0,0]
        self.speed = 10
        self.walls = walls

        self.stamina = 300
        self.maxStamina = 300


        self.MineAmount = 3
        
        

    def update(self, events, id):
        coldir = objmove2(self, self.walls)

        if self.type == 1: # if the type is a zombie
            self.speed = 21.1

        
        if id == self.id:
            if pg.key.get_pressed()[pg.K_w]:
                self.vel[1] = -self.speed

            elif pg.key.get_pressed()[pg.K_s]:
                self.vel[1] = self.speed  
            else:
                self.vel[1] = 0    

            if pg.key.get_pressed()[pg.K_a]:
                self.vel[0] = -self.speed
                    
            elif pg.key.get_pressed()[pg.K_d]:
                self.vel[0] = self.speed
            else:
                self.vel[0] = 0  

        if self.type == 2 and (self.vel[0] != 0 or self.vel[1] != 0):
            #change to legs
            self.image = pg.image.load('assets/landmine2.png')
        elif self.type == 2:
            #change to normal
            self.image = pg.image.load('assets/landmine.png')

        if self.type == 0:
            
            #Stamina

            if pg.key.get_pressed()[pg.K_LSHIFT] and self.stamina > 1 and (self.vel[0] != 0 or self.vel[1] != 0):
                self.speed = 30
                self.stamina -= 7
            elif self.vel[0] == 0 and self.vel[1] == 0:
                self.stamina += 5
            else:
                self.speed = 10    
                self.stamina += 2.5
            if self.stamina > self.maxStamina:
                self.stamina = self.maxStamina 
            
            if self.stamina < 0:
                self.stamina = 0
                

            
        if self.rect.x < 0:
            self.rect.x = 0    
        if self.rect.right > 2000:
            self.rect.right = 2000
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > 2000:
            self.rect.bottom = 2000
    

            




