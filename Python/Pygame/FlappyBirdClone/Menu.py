import pygame as pg


class Menu:

    
    def makeText(self, text, color, location):
        f = pg.font.SysFont("arial", 25)
        sText = f.render(text, True, color)
        rText = sText.get_rect(centerx = location[0], centery = location[1])
        return sText, rText
    
    def __init__(self):
        black = (0,0,0)
        self.choice = 0
        #Title stays the same
        self.title = self.makeText("Flappy Clone", black, (400,100))
        self.pressed = True

    def update(self,surf):
        red = (255,0,0)
        black = (0,0,0)

        #EASY MEDIUM AND HARD CHANGES
        easy = self.makeText("EASY", black, (400,300))
        medium = self.makeText("MEDIUM", black, (400, 500))
        hard = self.makeText("HARD", black, (400, 700))
        if self.choice == 0: #EASY SHOULD BE RED
            easy = self.makeText("EASY",red, (400, 300))
        if self.choice == 1: #MEDIUM SHOULD BE RED
            medium = self.makeText("MEDIUM", red, (400, 500))
        if self.choice == 2: #HARD SHOULD BE RED
            hard = self.makeText("HARD", red, (400, 700))
        if self.pressed: #IF YOU PRESS 
            if pg.key.get_pressed()[pg.K_DOWN]:
                self.choice += 1
                if self.choice > 2:
                    self.choice = 0
                self.pressed = False
            if pg.key.get_pressed()[pg.K_UP]:
                self.choice -= 1
                if self.choice < 0:
                    self.choice = 2
                self.pressed = False
        else:
            if not pg.key.get_pressed()[pg.K_DOWN] and not pg.key.get_pressed()[pg.K_UP]:
                self.pressed = True
                
        surf.blits(((self.title[0],self.title[1]),(easy[0],easy[1]),(medium[0],medium[1]),(hard[0],hard[1])))
        if pg.key.get_pressed()[pg.K_RETURN]:
            return True
        else:
            return False