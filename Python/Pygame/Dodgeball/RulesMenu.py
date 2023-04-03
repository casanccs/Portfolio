import pygame
from settings import *
from functions import *

class RulesMenu():
    def __init__(self, menuCursor):
        self.player1 = self.pControl(1, "↑", "↓", "←", "→", (P_HEIGHT/8,P_HEIGHT/8))
        if menuCursor > 1:    
            self.player2 = self.pControl(2, "w", "s", "a", "d",(P_HEIGHT*3/8,P_HEIGHT/8))
        if menuCursor > 2:
            self.player3 = self.pControl(3, "i", "k", "j", "l", (P_HEIGHT*5/8,P_HEIGHT/8))
        if menuCursor > 3:
            self.player4 = self.pControl(4, "t", "g", "f", "h",(P_HEIGHT*7/8,P_HEIGHT/8))

        self.normRulesText = makeText3(text = "Avoid the red balls and grab the stars!", location = (P_HEIGHT_H,P_HEIGHT*6/8), color = color["White"], size = 50)
            
    def pControl(self, playerNum, Up, Down, Left, Right, textLocation):
        pN = makeText3(text = "Player " + str(playerNum) + " Controls:", location = textLocation, color = color["White"], size = 40)
        pU = makeText3(text = str(Up) + " to move Up", location = (textLocation[0], textLocation[1] + P_HEIGHT/20), color = color["White"], size = 20)
        pD = makeText3(text = str(Down) + " to move Down", location = (textLocation[0], textLocation[1] + P_HEIGHT*2/20), color = color["White"], size = 20)
        pL = makeText3(text = str(Left) + " to move Left", location = (textLocation[0], textLocation[1] + P_HEIGHT*3/20), color = color["White"], size = 20)
        pR = makeText3(text = str(Right) + " to move Right", location = (textLocation[0], textLocation[1] + P_HEIGHT*4/20), color = color["White"], size = 20)

        return pN,pU,pD,pL,pR
        """
        ExamRight
        Player X Controls:
        W to move Up
        S to move Down
        A to move Left
        D to move Right

        ↑ ↓ ← → 
        """
    #self.player1 == (pN,pU,pD,pL,pR)
    #self.player1[0] == pN == pN[0]
    def update(self, menuCursor):
        PLAY.blits(((self.player1[0][0], self.player1[0][1]),(self.player1[1][0],self.player1[1][1]),(self.player1[2][0],self.player1[2][1]),(self.player1[3][0],self.player1[3][1]),(self.player1[4][0],self.player1[4][1])))
        if menuCursor > 1:
            PLAY.blits(((self.player2[0][0], self.player2[0][1]),(self.player2[1][0],self.player2[1][1]),(self.player2[2][0],self.player2[2][1]),(self.player2[3][0],self.player2[3][1]),(self.player2[4][0],self.player2[4][1])))
        if menuCursor > 2:
            PLAY.blits(((self.player3[0][0], self.player3[0][1]),(self.player3[1][0],self.player3[1][1]),(self.player3[2][0],self.player3[2][1]),(self.player3[3][0],self.player3[3][1]),(self.player3[4][0],self.player3[4][1])))
        if menuCursor > 3:
            PLAY.blits(((self.player4[0][0], self.player4[0][1]),(self.player4[1][0],self.player4[1][1]),(self.player4[2][0],self.player4[2][1]),(self.player4[3][0],self.player4[3][1]),(self.player4[4][0],self.player4[4][1])))
        PLAY.blit(self.normRulesText[0],self.normRulesText[1])