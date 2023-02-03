import pygame as pg

class Bird:
    
    def __init__(self, controls):

        self.controls = controls
        self.js = [0,-12]
        self.v = [0,0]
        self.surf = pg.image.load('slime.png')
        self.surf = pg.transform.scale(self.surf, (55,55))
        self.rect = self.surf.get_rect(center = (100,400))
        self.angle = 0


    def setAngle(self,targetAngle): #SAVE THIS METHOD
        diff = targetAngle - self.angle
        self.angle = targetAngle
        return pg.transform.rotate(self.surf, diff)

    def update(self,surf): #Return True if you die
        #controls
        
        #gravity
        self.v[1] += 0.7
        """
        if self.angle > 0:
            self.surf = pg.transform.rotate(self.surf, -1)
            self.angle += -1
        """
        #controls
        
        if self.v[1] < 0: #going upwards
            self.surf = self.setAngle(45)
        else:
            self.surf = self.setAngle(-45)
        
        
        
        
        if pg.key.get_pressed()[self.controls]:
            self.v = self.js.copy()

        #update position of Bird
        self.rect.move_ip(self.v)

        #if you touch the ground you die
        if self.rect.bottom >= surf.get_height():
            return False

        #Blit
        surf.blit(self.surf, self.rect)

        return True