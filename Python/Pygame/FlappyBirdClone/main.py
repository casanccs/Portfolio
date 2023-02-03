import pygame as pg
from time import time
from Bird import *
from Pipes import *
from Menu import *
pg.init()
clock = pg.time.Clock()

f = pg.font.SysFont("arial", 25)
def makeText(text, color, location):
    sText = f.render(text, True, color)
    rText = sText.get_rect(x = location[0], centery = location[1])
    return sText, rText

#COLORS
white = (255,255,255)
black = (0,0,0)
cyan = (150,150,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)

SCREEN = pg.display.set_mode((800,800))
SCREEN.fill(cyan)

play = False



#MENU
mInst = Menu()
menu = True
while menu:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False
            menu = False
    if mInst.update(SCREEN):
        play = True
        menu = False
    pg.display.update()
    

#PLAY
spaces = [330, 280, 230]
player = Bird(pg.K_SPACE)
pipeList = []
score = 0
Scores = makeText(str(score), black, (10,20))
start = time()
while play:

    clock.tick(60)

    if time() - start >= 1: #if more than a second pass
        pipeList.append(Pipes(spaces[mInst.choice]))
        start = time()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False
            menu = False
    
    if not player.update(SCREEN):
        play = False

    for pipe in pipeList:
        pipe.update(SCREEN)

        if pipe.rect1.right < 0: #removes the pipes from the level if they go to the right
            pipeList.remove(pipe)
            score += 1
            Scores = makeText(str(score), black, (10,20))
        if pipe.rect1.colliderect(player.rect) or pipe.rect2.colliderect(player.rect):
            play = False
    SCREEN.blit(Scores[0], Scores[1])
    pg.display.update()
    

    
    SCREEN.fill(cyan)

pg.time.wait(2000)