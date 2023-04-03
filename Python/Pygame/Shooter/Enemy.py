from settings import *

class Enemy(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        type = randint(0,2)
        if type == 0: #normal zombie
            self.speed = 6
            self.hp = 10
            self.og = pg.image.load('normalZombie.png')
            self.og = pg.transform.scale(self.og, (100,100))
        elif type == 1: #fast zombie
            self.speed = 8
            self.hp = 5
            self.og = pg.image.load('fastZombie.png')
            self.og = pg.transform.scale(self.og, (75,75))
        else: #slow zombie
            self.speed = 3
            self.hp = 20
            self.og = pg.image.load('slowZombie.png')
            self.og = pg.transform.scale(self.og, (125,125))

        spawn = randint(0,3)
        if spawn == 0: #spawn at top
            spawnpoint = [randint(0,800),-300]
        elif spawn == 1: #spawn at bottom
            spawnpoint = [randint(0,800),1100]
        elif spawn == 2: #spawn at left
            spawnpoint = [-300,randint(0,800)]
        elif spawn == 3: #spawn at right
            spawnpoint = [1100,randint(0,800)]
        
        self.ogr = self.og.get_rect(center = spawnpoint)
        self.angle = 0
        self.image = pg.transform.rotate(self.og, self.angle)
        self.rect = self.image.get_rect(center = self.ogr.center)
        

    def update(self, ppos):
        
        #To know how far in the x direction the mouse is from the player
        xdist = ppos[0] - self.rect.centerx
        #y direction
        ydist = ppos[1] - self.rect.centery

        if xdist != 0:
            self.angle = -degrees(atan(ydist/xdist))
        if xdist < 0:
            self.angle += 180

        self.ogr.move_ip(self.speed*cos(radians(self.angle)),self.speed*sin(radians(self.angle*-1)))

        self.image = pg.transform.rotate(self.og, self.angle)
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = self.ogr.center)