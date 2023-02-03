import pygame
import random

from pygame.display import update
import settings
from Enemy import *
from functions import *
from Player import *
from Power import *
from MainMenu import *
from GameOver import *
from RulesMenu import *
from HighScore import *
from ColorMenu import *

#https://www.pygame.org/docs/

pygame.init()
#Events
CLONE = pygame.USEREVENT + 1
some = pygame.time.set_timer(CLONE, 1500)

menuCursor = 1

#Entities
Enemy_Group = pygame.sprite.Group()
Player_Group = pygame.sprite.Group()
Power_Group = pygame.sprite.Group()
MAINMENU = MainMenu()
GAMEOVER = GameOver()
limit = 0 #Controls the game speed
     
while LOOPS["MAIN"]:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()

    if LOOPS["MENU"]:
        menuCursor = 1 #Controls which game mode the user selects
        scoreArray = [0,0,0,0]
        high = HighScore(max(scoreArray),0)

    while LOOPS["MENU"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitGame()
                if event.key == pygame.K_UP:
                    if menuCursor == 1:
                        menuCursor = 4
                    else:
                        menuCursor += -1
                if event.key == pygame.K_DOWN:
                    if menuCursor == 4:
                        menuCursor = 1
                    else:
                        menuCursor += 1
                if event.key == pygame.K_SPACE:
                    changeLoop("MENU", "RulesScreen")

        ###THIS IS IMPORTANT!^^ Every time we get to the menu loop, both groups need to be empty, and only when the user selects the game mode, will we add X amount of players to the group
        
        SCREEN.fill(color["Black"])
        PLAY.fill(color["Black"])
        MAINMENU.update(menuCursor,high.currentH,high.currentH2)
        SCREEN.blit(PLAY, PLAY_R)
        pygame.display.flip()

    ###We also need to make sure that when the player restarts the game from game over screen, it adds the same number of players

    if LOOPS["RulesScreen"]:
        high = HighScore(max(scoreArray),menuCursor)
        RULESSCREEN = RulesMenu(menuCursor)
    while LOOPS["RulesScreen"]:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    changeLoop("RulesScreen","MENU")
                if event.key == pygame.K_SPACE:
                    changeLoop("RulesScreen","ColorMenu")
        SCREEN.fill(color["White"])
        PLAY.fill(color["Black"])
        RULESSCREEN.update(menuCursor)
        SCREEN.blit(PLAY,PLAY_R)
        pygame.display.flip()

    if LOOPS["ColorMenu"]:
        CM = ColorMenu(menuCursor)

    while LOOPS["ColorMenu"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    changeLoop("ColorMenu","MENU")
        SCREEN.fill(color["White"])
        PLAY.fill(color["Black"])
        CM.update()
        SCREEN.blit(PLAY,PLAY_R)
        pygame.display.flip()

    if LOOPS["PLAY"]:
        p1 = Player(CM.colorArray[0], "Arrows")
        p2 = Player(CM.colorArray[1], "WASD")
        p3 = Player(CM.colorArray[2], "IJKL")
        p4 = Player(CM.colorArray[3], "TFGH")
        s1 = Power()
        s2 = Power()
        Player_Group.add(p1)
        Power_Group.add(s1)
        if menuCursor > 1:
            Player_Group.add(p2)
        if menuCursor > 2:
            Player_Group.add(p3)
            Power_Group.add(s2)
        if menuCursor > 3:
            Player_Group.add(p4)
        scoreArray = [0,0,0,0]
        updateText(scoreArray,menuCursor,CM.colorArray)
        SCREEN.blit(PLAY,PLAY_R)
    
    while LOOPS["PLAY"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()
            if event.type == CLONE:
                if Player_Group.has(p1):
                    scoreArray[0] += 1
                if Player_Group.has(p2):
                    scoreArray[1] += 1
                if Player_Group.has(p3):
                    scoreArray[2] += 1
                if Player_Group.has(p4):
                    scoreArray[3] += 1
                Enemy_Group.add(spawnEnemy())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    toPause = True
                    #This is important!!! It will read the line "if len(Player_Group) == 0" and run it
        while toPause:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        toPause = False
                    if event.key == pygame.K_SPACE:
                        changeLoop("PLAY","MENU")
                        toPause = False
                        Player_Group.empty()
                        Enemy_Group.empty()
                        Power_Group.empty()
                        CM.colorArray = []
            pauseS, pauseR = makeText2("PAUSED",(P_HEIGHT_H,P_WIDTH_H),color["White"])
            resS, resR = makeText2("Press ESCAPE to resume", (P_HEIGHT/2,P_HEIGHT/8),color["White"])
            exitS,exitR = makeText2("Press SPACEBAR to return to menu", (P_HEIGHT/2,P_HEIGHT*7/8),color["White"])
            PLAY.blits(((pauseS,pauseR),(resS,resR),(exitS,exitR)))
            SCREEN.blit(PLAY,PLAY_R)
            pygame.display.flip()
        limit += 1
        psC = pygame.sprite.groupcollide(Power_Group,Player_Group, True, False) #Logic of the collision of power to play
        if len(psC) > 0:
            psC = psC[list(iter(psC.keys()))[0]][0]
            if psC == p1:
                scoreArray[0] += PowerPoints
            elif psC == p2:
                scoreArray[1] += PowerPoints
            elif psC == p3:
                scoreArray[2] += PowerPoints
            elif psC == p4:
                scoreArray[3] += PowerPoints
            psC = Power()
            Power_Group.add(psC)
        pygame.sprite.groupcollide(Enemy_Group,Player_Group,True,True)
        if len(Player_Group) == 0 and len(Enemy_Group) != 0:
            changeLoop("PLAY","OVER")
            Enemy_Group.empty()
            Power_Group.empty()
        if limit > 5:
            limit = 0
            SCREEN.fill(color["White"])
            PLAY.fill(color["Black"])
            Enemy_Group.update()
            Player_Group.update()
            Power_Group.update()
            updateText(scoreArray,menuCursor,CM.colorArray)
            SCREEN.blit(PLAY,PLAY_R)
        pygame.display.flip()
    if LOOPS["OVER"]:
        high = HighScore(max(scoreArray),menuCursor)
    while LOOPS["OVER"]:
        SCREEN.fill(color["White"])
        if menuCursor == 1 or menuCursor == 2:
            GAMEOVER.update(menuCursor, scoreArray,CM.colorArray,high.currentH,high.check)
        elif menuCursor == 3 or menuCursor == 4:
            GAMEOVER.update(menuCursor, scoreArray,CM.colorArray,high.currentH2,high.check)            
        SCREEN.blit(PLAY,PLAY_R)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        changeLoop("OVER","PLAY")
                        #CM.colorArray = []
                    if event.key == pygame.K_ESCAPE:
                        changeLoop("OVER","MENU")
                        CM.colorArray = []

pygame.quit()