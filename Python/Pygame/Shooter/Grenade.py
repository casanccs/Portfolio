from settings import *

class Grenade(pg.sprite.Sprite):

    def __init__(self,angle,ppos):
        pg.sprite.Sprite.__init__(self)


        self.image = pg.Surface((50,50))
        self.image.fill((0,150,0))
        self.rect = self.image.get_rect(center = ppos)
        self.speed = 10 #speed of the bullet
        self.angle = angle
        self.vel = [self.speed*cos(radians(angle)),self.speed*sin(radians(angle*-1))]#Velocity
        self.toExplode = False


    def update(self):
        self.speed -= 0.5
        self.vel = [self.speed*cos(radians(self.angle)),self.speed*sin(radians(self.angle*-1))]#Velocity
        if self.speed <= 0:
            self.toExplode = True
            self.explode()
        self.rect.move_ip(self.vel)

        if self.rect.right < 0:
            self.kill()
        
        
    def explode(self):
        self.image = pg.Surface((200,200))
        self.image.fill((200,200,0))
        self.rect = self.image.get_rect(center = self.rect.center)
        