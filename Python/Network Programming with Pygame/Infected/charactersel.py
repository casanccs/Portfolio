import pygame as pg
from player_client import *


class CharacterSelection:
    def __init__(self):
        self.sel = 0
        self.rMos = pg.Rect(0,0,5,5)

        self.sSelection = 4

        #Character Selection Surfaces
        self.sChar0 = pg.Surface((40,40))
        self.sChar1 = pg.Surface((40,40))
        self.sChar2 = pg.Surface((40,40))
        self.sChar3 = pg.Surface((40,40))
        self.sChar4 = pg.Surface((40,40))
        self.sChar5 = pg.Surface((40,40))
        self.sChar6 = pg.Surface((40,40))
        self.sChar7 = pg.Surface((40,40))
        self.sChar8 = pg.Surface((40,40))
        self.sChar9 = pg.Surface((40,40))
        self.sChar10 = pg.Surface((40,40))
        self.sChar11 = pg.Surface((40,40))
        self.sChar12 = pg.Surface((40,40))
        self.sChar13 = pg.Surface((40,40))
        self.sChar14 = pg.Surface((40,40))
        self.sChar14 = pg.Surface((40,40))
        self.sChar15 = pg.Surface((40,40))
        self.sChar16 = pg.Surface((40,40))

        #Character Surface Filling
        self.sChar1.fill('green')
        self.sChar2.fill('blue')
        self.sChar3.fill('red')
        self.sChar4.fill('yellow')

        self.sChar5.fill('green')
        self.sChar6.fill('blue')
        self.sChar7.fill('red')
        self.sChar8.fill('yellow')

        self.sChar9.fill('green')
        self.sChar10.fill('blue')
        self.sChar11.fill('red')
        self.sChar12.fill('yellow')

        self.sChar13.fill('green')
        self.sChar14.fill('blue')
        self.sChar15.fill('red')
        self.sChar16.fill('yellow')

        self.sChar0 = pg.image.load('assets/Characters/n0.png')
        self.sChar0 = pg.transform.scale(self.sChar0, (40,40))

        #self.sChar1 = pg.image.load('assets/Characters/n1.png')
        #self.sChar1 = pg.transform.scale(self.sChar1, (40,40))
        
        self.sChar2 = pg.image.load('assets/Characters/n2.png')
        self.sChar2 = pg.transform.scale(self.sChar2, (40,40))

        self.sChar3 = pg.image.load('assets/Characters/n3.png')
        self.sChar3 = pg.transform.scale(self.sChar3, (40,40))
        
        self.sChar4 = pg.image.load('assets/Characters/n4.png')
        self.sChar4 = pg.transform.scale(self.sChar4, (40,40))

        # self.sChar5 = pg.image.load('assets/Characters/n5.png')
        # self.sChar5 = pg.transform.scale(self.sChar5, (40,40))
        
        # self.sChar6 = pg.image.load('assets/Characters/n6.png')
        # self.sChar6 = pg.transform.scale(self.sChar6, (40,40))

        # self.sChar7 = pg.image.load('assets/Characters/n7.png')
        # self.sChar7 = pg.transform.scale(self.sChar7, (40,40))
        
        # self.sChar8 = pg.image.load('assets/Characters/n8.png')
        # self.sChar8 = pg.transform.scale(self.sChar8, (40,40))

        # self.sChar9 = pg.image.load('assets/Characters/n9.png')
        # self.sChar9 = pg.transform.scale(self.sChar9, (40,40))
        
        # self.sChar10 = pg.image.load('assets/Characters/n10.png')
        # self.sChar10 = pg.transform.scale(self.sChar10, (40,40))

        # self.sChar11 = pg.image.load('assets/Characters/n11.png')
        # self.sChar11 = pg.transform.scale(self.sChar11, (40,40))
        
        # self.sChar12 = pg.image.load('assets/Characters/n12.png')
        # self.sChar12 = pg.transform.scale(self.sChar12, (40,40))

        # self.sChar13 = pg.image.load('assets/Characters/n13.png')
        # self.sChar13 = pg.transform.scale(self.sChar13, (40,40))
        
        # self.sChar14 = pg.image.load('assets/Characters/n14.png')
        # self.sChar14 = pg.transform.scale(self.sChar14, (40,40))

        # self.sChar15 = pg.image.load('assets/Characters/n15.png')
        # self.sChar15 = pg.transform.scale(self.sChar15, (40,40))
        
        # self.sChar16 = pg.image.load('assets/Characters/n16.png')
        # self.sChar16 = pg.transform.scale(self.sChar16, (40,40))



        #Character Selection Rectangles

        self.rChar0 = self.sChar0.get_rect(center = (260, 250))
        self.rChar1 = self.sChar1.get_rect(center = (320, 250))
        self.rChar2 = self.sChar2.get_rect(center = (380, 250))
        self.rChar3 = self.sChar3.get_rect(center = (440, 250))

        self.rChar4 = self.sChar4.get_rect(center = (260, 350))
        self.rChar5 = self.sChar5.get_rect(center = (320, 350))
        self.rChar6 = self.sChar6.get_rect(center = (380, 350))
        self.rChar7 = self.sChar7.get_rect(center = (440, 350))

        self.rChar8 = self.sChar8.get_rect(center = (260, 450))
        self.rChar9 = self.sChar9.get_rect(center = (320, 450))
        self.rChar10 = self.sChar10.get_rect(center = (380, 450))
        self.rChar11 = self.sChar11.get_rect(center = (440, 450))

        self.rChar12 = self.sChar12.get_rect(center = (260, 550))
        self.rChar13 = self.sChar13.get_rect(center = (320, 550))
        self.rChar14 = self.sChar14.get_rect(center = (380,550))
        self.rChar15 = self.sChar15.get_rect(center = (440, 550))



        


    def update(self, surf):
        mPos = pg.mouse.get_pos()
        self.rMos.center = mPos
        
        

        
        surf.blit(self.sChar1, self.rChar1)
        surf.blit(self.sChar2, self.rChar2)
        surf.blit(self.sChar3, self.rChar3)
        surf.blit(self.sChar4, self.rChar4)
        surf.blit(self.sChar5, self.rChar5)
        surf.blit(self.sChar6, self.rChar6)
        surf.blit(self.sChar7, self.rChar7)
        surf.blit(self.sChar8, self.rChar8)
        surf.blit(self.sChar9, self.rChar9)
        surf.blit(self.sChar10, self.rChar10)
        surf.blit(self.sChar11, self.rChar11)

        surf.blit(self.sChar12, self.rChar12)
        surf.blit(self.sChar13, self.rChar13)
        surf.blit(self.sChar14, self.rChar14)
        surf.blit(self.sChar15, self.rChar15)
        surf.blit(self.sChar16, self.rChar16)

        if self.rMos.colliderect(self.rChar1) and pg.mouse.get_pressed()[0]:
            self.sSelection = 1
            return True
        if self.rMos.colliderect(self.rChar2) and pg.mouse.get_pressed()[0]:
            self.sSelection = 2
            return True
        if self.rMos.colliderect(self.rChar3) and pg.mouse.get_pressed()[0]:
            self.sSelection = 3
            return True
        if self.rMos.colliderect(self.rChar4) and pg.mouse.get_pressed()[0]:
            self.sSelection = 4
            return True
        if self.rMos.colliderect(self.rChar5) and pg.mouse.get_pressed()[0]:
            self.sSelection = 5
            return True
        if self.rMos.colliderect(self.rChar6) and pg.mouse.get_pressed()[0]:
            self.sSelection = 6  
            return True                
        if self.rMos.colliderect(self.rChar7) and pg.mouse.get_pressed()[0]:
            self.sSelection = 7
            return True
        if self.rMos.colliderect(self.rChar8) and pg.mouse.get_pressed()[0]:
            self.sSelection = 8
            return True
        if self.rMos.colliderect(self.rChar9) and pg.mouse.get_pressed()[0]:
            self.sSelection = 9
            return True
        if self.rMos.colliderect(self.rChar10) and pg.mouse.get_pressed()[0]:
            self.sSelection = 10
            return True
        if self.rMos.colliderect(self.rChar11) and pg.mouse.get_pressed()[0]:
            self.sSelection = 11
            return True
        if self.rMos.colliderect(self.rChar12) and pg.mouse.get_pressed()[0]:
            self.sSelection = 12
            return True
        if self.rMos.colliderect(self.rChar13) and pg.mouse.get_pressed()[0]:
            self.sSelection = 13
            return True
        if self.rMos.colliderect(self.rChar14) and pg.mouse.get_pressed()[0]:
            self.sSelection = 14
            return True
        if self.rMos.colliderect(self.rChar15) and pg.mouse.get_pressed()[0]:
            self.sSelection = 15
            return True
        if self.rMos.colliderect(self.rChar16) and pg.mouse.get_pressed()[0]:
            self.sSelection = 16
            return True                                       
     
        
    