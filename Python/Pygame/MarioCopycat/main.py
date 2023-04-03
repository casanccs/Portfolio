import pygame as pg
from Player import *
from Enemy import *
from functions import *
from random import randint
pg.init()
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)
SCREEN = pg.display.set_mode((800,800))
SCREEN.fill(black)
run = True


tilemap =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 8, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 8, 0, 0, 9, 0, 0, 0, 0, 0, 9, 0, 0, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2]]

tsize = (800//15,800//15) #Tells us how big each tile should be
dirt = pg.image.load('dirt.png')
dirt = pg.transform.scale(dirt, tsize)
grass = pg.image.load('grass.png')
grass = pg.transform.scale(grass, tsize)

tRect = pg.Rect(0,0,*tsize)

PLAY = pg.Surface((tsize[0]*40, tsize[1]*15))
PLAYR = PLAY.get_rect() #We want PLAY to start at the left
follow = False #If the camera will follow the player or not

walls = []

player = Player()
pgroup = pg.sprite.Group(player)


egroup = pg.sprite.Group()

jump9 = []
jump8 = []

SPAWN = pg.event.custom_type()

for X in range(40):
        for Y in range(15):
            tRect.topleft = (X*tsize[0],Y*tsize[1])
            if tilemap[Y][X] == 9: #If the tile's value is 1, grass block
                jump9.append(tRect.copy())
            if tilemap[Y][X] == 8:
                jump8.append(tRect.copy())
                
pg.time.set_timer(SPAWN, 3000)

while run:
    clock.tick(60)
    
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN:
            egroup.add(Enemy((randint(0,PLAY.get_width()),0)))

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False

    if 400 < player.rect.centerx < 1720:
        follow = True
    else:
        follow = False

    if follow:
        PLAYR.left = -(player.rect.centerx-400)


    #Blit the tiles onto PLAY
    for X in range(40):
        for Y in range(15):
            tRect.topleft = (X*tsize[0],Y*tsize[1])
            if tilemap[Y][X] == 1: #If the tile's value is 1, grass block
                PLAY.blit(grass,(X*tsize[0],Y*tsize[1]))
                walls.append(tRect.copy())
            if tilemap[Y][X] == 2:
                PLAY.blit(dirt,(X*tsize[0],Y*tsize[1])) 
                walls.append(tRect.copy())

    if len(pg.sprite.groupcollide(pgroup, egroup, True, False)):
        quitGame()

    pgroup.update(walls, events, PLAY)
    pgroup.draw(PLAY)

    egroup.update(walls, events, PLAY, player.rect, jump9, jump8)
    egroup.draw(PLAY)
    #Blit the PLAY onto SCREEN
    SCREEN.blit(PLAY,PLAYR)
    pg.display.update()

    SCREEN.fill(black)
    PLAY.fill(black)
    walls = []