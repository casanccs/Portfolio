import pygame
from settings import *
from functions import *
from HighScore import *
class GameOver():
    def __init__(self):
        self.titleS, self.titleR = makeText(text = "Dodge.",location = (P_WIDTH_H,P_HEIGHT_H))
        self.exitS, self.exitR = makeText(text ="Press the Escape Key to Exit Game", location = (P_WIDTH_H,32))
        self.playS, self.playR = makeText(text = "Press the Spacebar to Play Game", location = (P_WIDTH_H, PLAY_R.h -30))

    def update(self,menuCursor,scoreArray,colorArray,currentHigh,check):
        
        if check:
            newH = makeText(text = "You placed a new high score!", location = (P_WIDTH_H,P_HEIGHT_H + 90))
        else:
            newH = makeText(text = "High Score: " + str(currentHigh).strip(), location = (P_WIDTH_H,P_HEIGHT_H + 90))
        PLAY.fill(color["Black"])
        scoreS, scoreR = makeText(text = "Final Score is: " + str(max(scoreArray)), location = (P_WIDTH_H, P_HEIGHT_H - 30))
        if menuCursor > 1:
            for i in range(menuCursor):
                if scoreArray[i] == max(scoreArray):
                    winS,winR = makeText(text = "Winner is: " + str(reversed_color[colorArray[i]]), location = (P_WIDTH_H, P_HEIGHT_H + 30))
            PLAY.blit(winS,winR)
        self.playR.centery = 80
        PLAY.blits(((self.exitS,self.exitR),(self.playS,self.playR),(scoreS, scoreR),(newH[0],newH[1])))