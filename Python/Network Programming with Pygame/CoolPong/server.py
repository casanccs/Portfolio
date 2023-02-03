import socket
import pygame as pg
from random import randint
from math import sin,cos, asin,radians,degrees
from sys import exit
import threading

def sta(group,msg):
    for el in group:
        el.sock.send(msg.encode())

def quitGame():
    run = False
    pg.quit()
    exit()

class Ball(pg.sprite.Sprite):

    def __init__(self,pratio,id):
        super().__init__()
        self.id = id
        bs = 50*pratio #ball size
        self.image = pg.Surface((bs,bs))
        self.image.set_colorkey('black')
        pg.draw.circle(self.image,'white',(bs//2*pratio,bs//2*pratio),bs//2*pratio)
        self.rect = self.image.get_rect(center = (900*pratio,900*pratio)) #Spawns at center of SPACE ALWAYS
        self.speed = 5
        self.angle = radians(randint(0,360))
        self.vel = [self.speed*cos(self.angle)*pratio, -self.speed*sin(self.angle)*pratio]
        
        
    def update(self):
        self.rect.move_ip(self.vel[0], self.vel[1])
        if self.rect.right < 0 or self.rect.left > 1800*pratio or self.rect.top > 1800*pratio or self.rect.bottom < 0:
            self.rect.center = (900*pratio,900*pratio)
            self.angle = radians(randint(0,360))
            self.vel = [self.speed*cos(self.angle)*pratio, -self.speed*sin(self.angle)*pratio]
        

                
            

class Player(pg.sprite.Sprite):

    def __init__(self,pratio,color, side,sock):
        super().__init__()
        self.id = side
        if side == 0: #Bottom part of the SPACE
            self.image = pg.Surface((75*pratio,25*pratio))
            self.rect = self.image.get_rect(center = (900*pratio, 1750*pratio)) #Center of SPACEx, and slightly up from bottom
            #self.rect = self.image.get_rect(center = (100,100))
        if side == 1: #Top part of the SPACE
            self.image = pg.Surface((75*pratio,25*pratio))
            self.rect = self.image.get_rect(center = (900*pratio, 50*pratio)) #Center of SPACEx, and slightly down from top
        if side == 2: #Left part of the SPACE
            self.image = pg.Surface((25*pratio,75*pratio))
            self.rect = self.image.get_rect(center = (50*pratio, 900*pratio)) #Center of SPACEy, and slightly right from left
        if side == 3: #Right part of the SPACE
            self.image = pg.Surface((25*pratio,75*pratio))
            self.rect = self.image.get_rect(center = (1750*pratio, 900*pratio)) #Center of SPACEy, and slight left from right
        self.image.fill(color)
        self.sock = sock
        self.run = True
    
    

class Walls(pg.sprite.Sprite): #Do this so we can have a group of walls
    def __init__(self,pratio,width,height,cx,cy):
        super().__init__()
        self.image = pg.Surface((width*pratio,height*pratio))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = (cx*pratio,cy*pratio))

pg.init()

addr1 = socket.gethostbyname(socket.gethostname())
print(addr1)
addr2 = 'something'

sock = socket.socket()
#sock = socket.socket(family = socket.AF_INET6)
sock.bind((addr1,3500))
sock.listen()




dinfo = pg.display.Info() #Gets information about our display
psize = [dinfo.current_w, dinfo.current_h]
#Because the height of your screen is usually smaller than the width:
psize[0] = psize[1] #just incase, .copy()
"""
Big note:
In the original, I did all of the sizes, positions, and speeds, based off of:
1. Screen size of 600x600
2. Play Space of 1800x1800
But our screen sizes are not all 600x600
And showing the ENTIRE Play space of 1800x1800 is not possible since most screens are 1080 pixels high
We must scale everything accordingly
"""
pratio = psize[0]/1800
players = pg.sprite.Group()
n = int(input("How many people will there be? (Up to 4): "))
for i in range(n):
    new = sock.accept()[0]
    new.send(str(i).encode())
    color = new.recv(100).decode()
    players.add(Player(pratio,color,i,new))
sta(players,"Done with all players!")
# If our screen was only 900 pixels tall, we would have to shrink everything by half
# sratio would be 0.5, showing that this is correct
walls = pg.sprite.Group(Walls(pratio,50,600,600,1500) , Walls(pratio,50,600,1200,1500) ,
                        Walls(pratio,50,600,600,300) , Walls(pratio,50,600,1200,300) ,
                        Walls(pratio,600,50,300,600) , Walls(pratio,600,50,300,1200) ,
                        Walls(pratio,600,50,1500,600) , Walls(pratio,600,50,1500,1200)
        )
if n == 2:
    walls.add(Walls(pratio,50,600,600,900), Walls(pratio,50,600,1200,900))
if n == 3:
    walls.add(Walls(pratio,50,600,1200,900))


SCREEN = pg.display.set_mode()
SCREEN.fill('white')
SPACE = pg.Surface(psize)
SPACE.fill('black')
rSPACE = SPACE.get_rect(center = (SCREEN.get_width()//2, SCREEN.get_height()//2))

#There will only be 4 balls throughout the game, but when someone dies, the ball will get "recentered"
balls = pg.sprite.Group(Ball(pratio,"0"), Ball(pratio,"1"), Ball(pratio,"2"), Ball(pratio, "3"))

run = True
def updatePlayer(player):
    while player.run:
        msg = player.sock.recv(1000).decode()
        if msg == "quit":
            player.run = False
        #msg -> 'id x y'
        msg = msg.split()
        if len(msg) == 3:
            player.rect.center = (int(msg[1])*pratio,int(msg[2])*pratio)
        player.sock.send("a".encode())

def sendBalls():
    while run:
        for ball in balls:  
            player.sock.send(f"{ball.id} {ball.left} {ball.top}".encode())

for player in players:
    threading.Thread(target = updatePlayer, args=(player,)).start()

clock = pg.time.Clock()

font = pg.font.SysFont('comic sans',20)
fps = str(int(clock.get_fps()))
texts = font.render(fps, True, 'black')
textr = texts.get_rect()

while run:
    clock.tick(60)
    fps = str(int(clock.get_fps()))
    texts = font.render(fps, True, 'black')
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            quitGame()

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        quitGame()
    
        

    players.draw(SPACE)
    balls.update()
    balls.draw(SPACE)
    walls.draw(SPACE)
    SCREEN.blit(texts,textr)
    SCREEN.blit(SPACE,rSPACE)
    pg.display.flip()
    SPACE.fill('black')
    SCREEN.fill('white')
