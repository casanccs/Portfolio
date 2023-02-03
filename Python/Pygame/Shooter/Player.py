from settings import *

class Player(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.og = pg.image.load('Shooter/topPlayer.png')
        self.og = pg.transform.scale(self.og, (100,100))
        self.ogr = self.og.get_rect(center = (400,400))

        self.image = self.og
        self.rect = self.ogr
        self.offset = pg.math.Vector2((30,0))
        self.speed = 10
        self.angle = 0

    def update(self):
        mpos = pg.mouse.get_pos()
        #To know how far in the x direction the mouse is from the player
        xdist = mpos[0] - self.rect.centerx
        #y direction
        ydist = mpos[1] - self.rect.centery

        
        if pg.key.get_pressed()[pg.K_w]:
            self.ogr.move_ip(0,-self.speed)
        if pg.key.get_pressed()[pg.K_d]:
            self.ogr = self.ogr.move(self.speed,0)
        if pg.key.get_pressed()[pg.K_a]:
            self.ogr.move_ip(-self.speed,0)
        if pg.key.get_pressed()[pg.K_s]:
            self.ogr.move_ip(0,self.speed)
            
        # if pg.key.get_pressed()[pg.K_w]:
        #     self.ogr.move_ip(self.speed*cos(radians(self.angle))  ,  -self.speed*sin(radians(self.angle)))
        # if pg.key.get_pressed()[pg.K_d]:
        #     self.ogr.move_ip(self.speed*cos(radians(self.angle - 90))  ,  -self.speed*sin(radians(self.angle - 90)))
        # if pg.key.get_pressed()[pg.K_a]:
        #     self.ogr.move_ip(self.speed*cos(radians(self.angle + 90))  ,  -self.speed*sin(radians(self.angle + 90)))
        # if pg.key.get_pressed()[pg.K_s]:
        #     self.ogr.move_ip(-self.speed*cos(radians(self.angle))  ,  self.speed*sin(radians(self.angle)))
        
        if xdist != 0:
            self.angle = -degrees(atan(ydist/xdist))
        if xdist < 0:
            self.angle += 180
        
        self.image = pg.transform.rotate(self.og, self.angle)
        newoff = self.offset.rotate(-self.angle)
        self.rect = self.image.get_rect(center = self.ogr.center + newoff)
