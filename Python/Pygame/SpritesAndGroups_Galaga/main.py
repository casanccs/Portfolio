import pygame as pg
from Ship import *
from Alien import *
from time import time
from Bullet import *
from functions import *

pg.init()
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)
SCREEN = pg.display.set_mode((0,0))
SCREEN.fill(black)

ship = Ship()
shipGroup = pg.sprite.Group(ship)

a = Alien()
alienGroup = pg.sprite.Group(a)

bulletGroup = pg.sprite.Group()

start = time()
space = 1
start2 = time()
run = True

curScore = 0
myFile = open('SpritesAndGroups_Galaga/HighScore.txt', 'r')
highScore = int(myFile.read())
myFile.close()

#surface and rectangle for the current score
sC, rC = makeText('arial', 50, "Score: " + str(curScore), (0,0), white)
sH, rH = makeText('arial', 50, "High Score: " + str(highScore), rC.bottomleft, white)

while run:
    clock.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            bulletGroup.add(Bullet(ship.rect))
        if event.type == pg.KEYDOWN:
            bulletGroup.add(Bullet(ship.rect))

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False

    if time() - start > space:
        alienGroup.add(Alien())
        start = time()
    if time() - start2 > 1:
        space -= 0.1
        if space < 0.1:
            space = 0.1
        start2 = time()
    if len(pg.sprite.groupcollide(shipGroup, alienGroup, True, True)) > 0: #The player is touching an alien
        run = False

    if len(pg.sprite.groupcollide(bulletGroup, alienGroup, True, True)) > 0:
        curScore += 1
        sC, rC = makeText('arial', 50, "Score: " + str(curScore), (0,0), white)
        if curScore > highScore:
            highScore = curScore
            sH, rH = makeText('arial', 50, "High Score: " + str(highScore), rC.bottomleft, white)
            myFile = open("SpritesAndGroups_Galaga/HighScore.txt", 'w')
            myFile.write(str(highScore))
            myFile.close()

    
    bulletGroup.update()
    bulletGroup.draw(SCREEN)
    shipGroup.update()
    shipGroup.draw(SCREEN)
    alienGroup.update()
    alienGroup.draw(SCREEN)
    SCREEN.blit(sC, rC)
    SCREEN.blit(sH, rH)

    pg.display.update()
    SCREEN.fill(black)