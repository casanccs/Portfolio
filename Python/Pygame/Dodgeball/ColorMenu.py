import pygame
from settings import *
from functions import *

class ColorMenu():
    def __init__(self,menuCursor):
        #global self.colorArray
        self.colorArray = [] #Array of colors in use by players
        self.options = color #self.options will be the color dictionary defined in settings
        self.num = menuCursor
        self.location = []
        self.taken = []
        for i in range(16):
            self.taken.append(False)
        for i in range(4):
            for j in range(4):
                self.location.append((P_HEIGHT*(1/4 + 1/20 + j/10 + j/30), P_HEIGHT*(1/4 + 1/20 + i/10 + i/30)))
        
        self.matrix = []
        self.crow = []
        #There are 16 colors in the options dictionary
        for i in range(4):
            for j in range(4):
                Surf = pygame.Surface((P_HEIGHT/10,P_HEIGHT/10))
                Rect = pygame.draw.rect(Surf, colorL[4*i + j],Surf.get_rect())
                Rect.topleft = (P_HEIGHT*1/4 + P_HEIGHT*j/10 + P_HEIGHT*j/30, P_HEIGHT*1/4 + P_HEIGHT*i/10 + P_HEIGHT*i/30)
                pair = [Surf,Rect]
                self.crow.append(pair)
            self.matrix.append(self.crow)
            self.crow = []
        self.p1T = makeText(text = "Player 1 color:",location = (P_HEIGHT/8, P_HEIGHT/16)) 
        self.p1Choice = 0 #The number of the choice will dictate where the Text will end up being
        self.p1CT = makeText3("Player 1", self.location[self.p1Choice], color["Black"],20)
        self.p1Press = True
        if menuCursor > 1:
            self.p2T = makeText(text = "Player 2 color:",location = (P_HEIGHT*7/8, P_HEIGHT/16))
            self.p2Choice = 1 #The number of the choice will dictate where the Text will end up being
            self.p2CT = makeText3("Player 2", self.location[self.p2Choice], color["Black"],20)
            self.p2Press = True
        if menuCursor > 2:
            self.p3T = makeText(text = "Player 3 color:",location = (P_HEIGHT/8, P_HEIGHT*7/8))
            self.p3Choice = 2 #The number of the choice will dictate where the Text will end up being
            self.p3CT = makeText3("Player 3", self.location[self.p3Choice], color["Black"],20)
            self.p3Press = True
        if menuCursor > 3:
            self.p4T = makeText(text = "Player 4 color:",location = (P_HEIGHT*7/8, P_HEIGHT*7/8))
            self.p4Choice = 3 #The number of the choice will dictate where the Text will end up being
            self.p4CT = makeText3("Player 4", self.location[self.p4Choice], color["Black"],20)
            self.p4Press = True
        self.spaceP = False
            
    def update(self):
        self.taken[self.p1Choice] = True
        if self.num > 1:
            self.taken[self.p2Choice] = True
        if self.num > 2:
            self.taken[self.p3Choice] = True
        if self.num > 3:
            self.taken[self.p4Choice] = True
        if self.p1Press:
            if pygame.key.get_pressed()[pygame.K_UP]:
                temp = self.p1Choice
                while True:
                    self.p1Choice += -4
                    if self.p1Choice < 0:
                        self.p1Choice += 16
                    if self.taken[self.p1Choice] == False:
                        break
                    if self.p1Choice == temp:
                        break
                self.p1Press = False
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                temp = self.p1Choice
                while True:
                    self.p1Choice += 4
                    if self.p1Choice > 15:
                        self.p1Choice += -16
                    if self.taken[self.p1Choice] == False:
                        break
                    if self.p1Choice == temp:
                        break
                self.p1Press = False

            elif pygame.key.get_pressed()[pygame.K_LEFT]:
                temp = self.p1Choice
                while True:
                    self.p1Choice += -1
                    if self.p1Choice == -1 or self.p1Choice == 3 or self.p1Choice == 7 or self.p1Choice == 11:
                        self.p1Choice += 4
                    if self.taken[self.p1Choice] == False:
                        break
                    if self.p1Choice == temp:
                        break
                self.p1Press = False

            elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                temp = self.p1Choice
                while True:
                    self.p1Choice += 1
                    if self.p1Choice == 4 or self.p1Choice == 8 or self.p1Choice == 12 or self.p1Choice == 16:
                        self.p1Choice += -4
                    if self.taken[self.p1Choice] == False:
                        break
                    if self.p1Choice == temp:
                        break
                self.p1Press = False
        if not self.p1Press:
            if not (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]):
                self.p1Press = True
        for i in range(4):
            for j in range(4):
                PLAY.blit(self.matrix[i][j][0],self.matrix[i][j][1])

        if self.spaceP:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.colorArray.append(colorL[self.p1Choice])
                if self.num > 1:
                    self.colorArray.append(colorL[self.p2Choice])
                if self.num > 2:
                    self.colorArray.append(colorL[self.p3Choice])
                if self.num > 3:
                    self.colorArray.append(colorL[self.p4Choice])
                self.colorArray.append("#FFFFFF")
                self.colorArray.append("#FFFFFF")
                self.colorArray.append("#FFFFFF")

                print(self.colorArray)
                changeLoop("ColorMenu","PLAY")
        if not pygame.key.get_pressed()[pygame.K_SPACE]:
            self.spaceP = True
        self.p1CT[1].center = self.location[self.p1Choice]
        self.p1S = pygame.Surface((si.current_h/25,si.current_h/25)) 
        self.p1R = pygame.draw.rect(self.p1S, colorL[self.p1Choice],self.p1S.get_rect())
        self.p1R.center = (P_HEIGHT/8,P_HEIGHT*2/16)
        PLAY.blits(((self.p1T[0],self.p1T[1]),(self.p1S,self.p1R)))
        PLAY.blit(self.p1CT[0],self.p1CT[1])
        if self.num > 1:
            if self.p2Press:
                if pygame.key.get_pressed()[pygame.K_w]:
                    temp = self.p2Choice
                    while True:
                        self.p2Choice += -4
                        if self.p2Choice < 0:
                            self.p2Choice += 16
                        if self.taken[self.p2Choice] == False:
                            break
                        if self.p2Choice == temp:
                            break
                    self.p2Press = False
                elif pygame.key.get_pressed()[pygame.K_s]:
                    temp = self.p2Choice
                    while True:
                        self.p2Choice += 4
                        if self.p2Choice > 15:
                            self.p2Choice += -16
                        if self.taken[self.p2Choice] == False:
                            break
                        if self.p2Choice == temp:
                            break
                    self.p2Press = False

                elif pygame.key.get_pressed()[pygame.K_a]:
                    temp = self.p2Choice
                    while True:
                        self.p2Choice += -1
                        if self.p2Choice == -1 or self.p2Choice == 3 or self.p2Choice == 7 or self.p2Choice == 11:
                            self.p2Choice += 4
                        if self.taken[self.p2Choice] == False:
                            break
                        if self.p2Choice == temp:
                            break
                    self.p2Press = False

                elif pygame.key.get_pressed()[pygame.K_d]:
                    temp = self.p2Choice
                    while True:
                        self.p2Choice += 1
                        if self.p2Choice == 4 or self.p2Choice == 8 or self.p2Choice == 12 or self.p2Choice == 16:
                            self.p2Choice += -4
                        if self.taken[self.p2Choice] == False:
                            break
                        if self.p2Choice == temp:
                            break
                    self.p2Press = False
            if not self.p2Press:
                if not (pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d]):
                    self.p2Press = True
            self.p2CT[1].center = self.location[self.p2Choice]
            self.p2S = pygame.Surface((si.current_h/25,si.current_h/25))
            self.p2R = pygame.draw.rect(self.p2S, colorL[self.p2Choice] ,self.p2S.get_rect())
            self.p2R.center = (P_HEIGHT*7/8,P_HEIGHT*2/16)
            self.p2CT[1].center = self.location[self.p2Choice]
            PLAY.blits(((self.p2T[0],self.p2T[1]),(self.p2S,self.p2R)))
            PLAY.blit(self.p2CT[0],self.p2CT[1])
        if self.num > 2:
            if self.p3Press:
                if pygame.key.get_pressed()[pygame.K_i]:
                    temp = self.p3Choice
                    while True:
                        self.p3Choice += -4
                        if self.p3Choice < 0:
                            self.p3Choice += 16
                        if self.taken[self.p3Choice] == False:
                            break
                        if self.p3Choice == temp:
                            break
                    self.p3Press = False
                elif pygame.key.get_pressed()[pygame.K_k]:
                    temp = self.p3Choice
                    while True:
                        self.p3Choice += 4
                        if self.p3Choice > 15:
                            self.p3Choice += -16
                        if self.taken[self.p3Choice] == False:
                            break
                        if self.p3Choice == temp:
                            break
                    self.p3Press = False

                elif pygame.key.get_pressed()[pygame.K_j]:
                    temp = self.p3Choice
                    while True:
                        self.p3Choice += -1
                        if self.p3Choice == -1 or self.p3Choice == 3 or self.p3Choice == 7 or self.p3Choice == 11:
                            self.p3Choice += 4
                        if self.taken[self.p3Choice] == False:
                            break
                        if self.p3Choice == temp:
                            break
                    self.p3Press = False

                elif pygame.key.get_pressed()[pygame.K_l]:
                    temp = self.p3Choice
                    while True:
                        self.p3Choice += 1
                        if self.p3Choice == 4 or self.p3Choice == 8 or self.p3Choice == 12 or self.p1Choice == 16:
                            self.p3Choice += -4
                        if self.taken[self.p3Choice] == False:
                            break
                        if self.p3Choice == temp:
                            break
                    self.p3Press = False
            if not self.p3Press:
                if not (pygame.key.get_pressed()[pygame.K_i] or pygame.key.get_pressed()[pygame.K_k] or pygame.key.get_pressed()[pygame.K_j] or pygame.key.get_pressed()[pygame.K_l]):
                    self.p3Press = True
            self.p3CT[1].center = self.location[self.p3Choice]
            self.p3S = pygame.Surface((si.current_h/25,si.current_h/25))
            self.p3R = pygame.draw.rect(self.p3S, colorL[self.p3Choice] ,self.p3S.get_rect())
            self.p3R.center = (P_HEIGHT/8,P_HEIGHT*15/16)
            self.p3CT[1].center = self.location[self.p3Choice]
            PLAY.blits(((self.p3T[0],self.p3T[1]),(self.p3S,self.p3R)))
            PLAY.blit(self.p3CT[0],self.p3CT[1])
        if self.num > 3:
            if self.p4Press:
                if pygame.key.get_pressed()[pygame.K_t]:
                    temp = self.p4Choice
                    while True:
                        self.p4Choice += -4
                        if self.p4Choice < 0:
                            self.p4Choice += 16
                        if self.taken[self.p4Choice] == False:
                            break
                        if self.p4Choice == temp:
                            break
                    self.p4Press = False
                elif pygame.key.get_pressed()[pygame.K_g]:
                    temp = self.p4Choice
                    while True:
                        self.p4Choice += 4
                        if self.p4Choice > 15:
                            self.p4Choice += -16
                        if self.taken[self.p4Choice] == False:
                            break
                        if self.p4Choice == temp:
                            break
                    self.p4Press = False

                elif pygame.key.get_pressed()[pygame.K_f]:
                    temp = self.p1Choice
                    while True:
                        self.p4Choice += -1
                        if self.p4Choice == -1 or self.p4Choice == 3 or self.p4Choice == 7 or self.p4Choice == 11:
                            self.p4Choice += 4
                        if self.taken[self.p4Choice] == False:
                            break
                        if self.p4Choice == temp:
                            break
                    self.p4Press = False

                elif pygame.key.get_pressed()[pygame.K_h]:
                    temp = self.p4Choice
                    while True:
                        self.p4Choice += 1
                        if self.p1Choice == 4 or self.p4Choice == 8 or self.p4Choice == 12 or self.p4Choice == 16:
                            self.p4Choice += -4
                        if self.taken[self.p4Choice] == False:
                            break
                        if self.p4Choice == temp:
                            break
                    self.p4Press = False
            if not self.p4Press:
                if not (pygame.key.get_pressed()[pygame.K_t] or pygame.key.get_pressed()[pygame.K_g] or pygame.key.get_pressed()[pygame.K_f] or pygame.key.get_pressed()[pygame.K_h]):
                    self.p4Press = True
            self.p4CT[1].center = self.location[self.p4Choice]
            self.p4S = pygame.Surface((si.current_h/25,si.current_h/25))
            self.p4R = pygame.draw.rect(self.p4S, colorL[self.p4Choice] ,self.p4S.get_rect())
            self.p4R.center = (P_HEIGHT*7/8,P_HEIGHT*15/16)
            self.p4CT[1].center = self.location[self.p4Choice]
            PLAY.blits(((self.p4T[0],self.p4T[1]),(self.p4S,self.p4R)))
            PLAY.blit(self.p4CT[0],self.p4CT[1])
        self.taken = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]