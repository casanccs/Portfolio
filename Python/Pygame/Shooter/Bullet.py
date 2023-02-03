from settings import *

class Bullet(pg.sprite.Sprite):

    def __init__(self,angle,ppos):
        pg.sprite.Sprite.__init__(self)


        self.og = pg.image.load('Shooter/Bullet.png')
        self.og = pg.transform.scale(self.og,(50,20))
        self.ogr = self.og.get_rect(center = ppos)
        self.image = pg.transform.rotate(self.og,angle)
        self.rect = self.image.get_rect(center = self.ogr.center)
        self.speed = 20 #speed of the bullet
        self.vel = [self.speed*cos(radians(angle)),self.speed*sin(radians(angle*-1))]#Velocity
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        
        self.rect.move_ip(self.vel)

        if self.rect.right < 0:
            self.kill()