import pygame
from settings import *
from functions import *

class MainMenu():
    #Static Text
    def __init__(self):
        self.titleS, self.titleR = makeText3(text = "DodgeBall™",location = (P_WIDTH_H,P_HEIGHT_H/2), color = color["Grey"], size = 60)
        self.exitS, self.exitR = makeText(text ="Press the Escape Key to Exit Game", location = (P_WIDTH_H,32))
        self.playS, self.playR = makeText(text = "Press the Spacebar to Play Game", location = (P_WIDTH_H, PLAY_R.h -30))
        self.makerS, self.makerR = makeText(text = "Made by: Cristian", location = (P_HEIGHT_H,P_HEIGHT_H*5/8))
        self.maker2S, self.maker2R = makeText(text = "Assisted by: Preston", location = (P_HEIGHT_H,P_HEIGHT_H*3/4))

    def update(self,menuCursor, high,high2):
        newH = makeText(text = "High Score for 1 and 2 Player: " + str(high).strip(), location = (P_WIDTH_H,P_HEIGHT*8/16))
        newH2 = makeText(text = "High Score for 3 and 4 Player: " + str(high2).strip(), location = (P_WIDTH_H,P_HEIGHT*9/16))
        if menuCursor == 1: #this means the player is on selecting "1 - PLAYER"
                onePS, onePR = makeText2(text = "1 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*10/16)), color = color["Red"])
        else:
            onePS, onePR = makeText2(text = "1 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*10/16)), color = color["Yellow"])
        if menuCursor == 2: #this means the player is on selecting "1 - PLAYER"
            twoPS, twoPR = makeText2(text = "2 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*11/16)), color = color["Red"])
        else:
            twoPS, twoPR = makeText2(text = "2 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*11/16)), color = color["Yellow"])
        if menuCursor == 3: #this means the player is on selecting "1 - PLAYER"
            threePS, threePR = makeText2(text = "3 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*12/16)), color = color["Red"])
        else:
            threePS, threePR = makeText2(text = "3 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*12/16)), color = color["Yellow"])
        if menuCursor == 4: #this means the player is on selecting "1 - PLAYER"
            fourPS, fourPR = makeText2(text = "4 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*13/16)), color = color["Red"])
        else:
            fourPS, fourPR = makeText2(text = "4 - PLAYER", location = (P_WIDTH_H, int(P_HEIGHT*13/16)), color = color["Yellow"])
            
        PLAY.blits(((self.titleS,self.titleR),(self.exitS,self.exitR),(self.playS,self.playR),(self.makerS,self.makerR),(self.maker2S,self.maker2R),(onePS,onePR),(twoPS,twoPR),(threePS,threePR),(fourPS,fourPR),(newH[0],newH[1]),(newH2[0],newH2[1])))