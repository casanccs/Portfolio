import pygame
from settings import *
import random
from Enemy import *

selFont = "arial"

def makeText(text, location):
    tT = pygame.font.SysFont("arial", 40)
    tS = tT.render(str(text), True, color["White"])
    tR = tS.get_rect()
    tR.center = location
    return tS, tR

def makeText2(text, location, color):
    tT = pygame.font.SysFont(selFont, 30)
    tS = tT.render(str(text), True, color)
    tR = tS.get_rect()
    tR.center = location
    return tS, tR

def makeText3(text, location, color, size):
    tT = pygame.font.SysFont(selFont, size)
    tS = tT.render(str(text), True, color)
    tR = tS.get_rect()
    tR.center = location
    return tS, tR

def exitGame():
    LOOPS["MAIN"] = False
    LOOPS["MENU"] = False
    LOOPS["PLAY"] = False
    LOOPS["OVER"] = False

def changeLoop(fObj , tObj):
    global LOOPS
    LOOPS[fObj] = False
    LOOPS[tObj] = True

def spawnEnemy():
    dir = random.randint(0,3)
    if dir == 0:
        en2 = Enemy("#FF0000", "up")
    if dir == 1:
        en2 = Enemy("#FF0000", "down")
    if dir == 2:
        en2 = Enemy("#FF0000", "right")
    if dir == 3:
        en2 = Enemy("#FF0000", "left")
    return en2

def updateText(array, numPlayers,colorArray):
    #Update text will update all of the scores and final score. This function needs to be able to be used for ALL 1-4 Player Game Modes
    temp = []
    temp.append(makeText2(array[0], (P_WIDTH_H,P_HEIGHT*7/16), colorArray[0]))
    if numPlayers > 1:
        temp.append(makeText2(array[1], (P_WIDTH_H,P_HEIGHT*9/16), colorArray[1]))
    if numPlayers > 2:
        temp.append(makeText2(array[2], (P_WIDTH*7/16,P_HEIGHT_H), colorArray[2]))
    if numPlayers > 3:
        temp.append(makeText2(array[3], (P_WIDTH*9/16,P_HEIGHT_H), colorArray[3]))
    for i in range(numPlayers):
        PLAY.blit(temp[i][0],temp[i][1])