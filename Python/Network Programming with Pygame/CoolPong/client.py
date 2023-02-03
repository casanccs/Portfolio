import socket
import pygame as pg
from random import randint
from math import sin,cos, asin,radians,degrees
from sys import exit
import threading

def quitGame():
    sock.send("quit".encode())
    run = False
    pg.quit()
    exit()


class Balls(pg.sprite.Sprite):

    def __init__(self,id):
        super().__init__()
        bs = 50 #ball size
        self.image = pg.Surface((bs,bs))
        self.image.set_colorkey('black')
        pg.draw.circle(self.image,'white',(bs//2,bs//2),bs//2)
        self.rect = self.image.get_rect(center = (900,900)) #Spawns at center of SPACE ALWAYS
        self.id = id


class Player(pg.sprite.Sprite):

    def __init__(self,color, side): #Spawn positions and directions depend on what side they spawn
        super().__init__()
        self.side = side
        self.speed = 5
        self.vel = [0,0]
        #Setup for the block
        if side == 0: #Bottom part of the SPACE
            self.image = pg.Surface((75,25))
            self.rect = self.image.get_rect(center = (900, 1800-50)) #Center of SPACEx, and slightly up from bottom
            #self.rect = self.image.get_rect(center = (100,100))
        if side == 1: #Top part of the SPACE
            self.image = pg.Surface((75,25))
            self.rect = self.image.get_rect(center = (900, 50)) #Center of SPACEx, and slightly down from top
        if side == 2: #Left part of the SPACE
            self.image = pg.Surface((25,75))
            self.rect = self.image.get_rect(center = (50, 900)) #Center of SPACEy, and slightly right from left
        if side == 3: #Right part of the SPACE
            self.image = pg.Surface((25,75))
            self.rect = self.image.get_rect(center = (1800-50, 900)) #Center of SPACEy, and slight left from right
        self.image.fill(color)

    def update(self):
        self.rect.move_ip(self.vel[0],self.vel[1])
        if pg.key.get_pressed()[pg.K_RIGHT]:
            if self.side == 0:
                self.vel[0] = self.speed
            if self.side == 1:
                self.vel[0] = -self.speed
            if self.side == 2:
                self.vel[1] = self.speed
            if self.side == 3:
                self.vel[1] = -self.speed
        elif pg.key.get_pressed()[pg.K_LEFT]:
            if self.side == 0:
                self.vel[0] = -self.speed
            if self.side == 1:
                self.vel[0] = self.speed
            if self.side == 2:
                self.vel[1] = -self.speed
            if self.side == 3:
                self.vel[1] = self.speed
        else:
            self.vel = [0,0]
        if side == 0 or side == 1:
            if self.rect.left < 625:
                self.rect.left = 625
            if self.rect.right > 1175:
                self.rect.right = 1175
        if side == 2 or side == 3:
            if self.rect.top < 625:
                self.rect.top = 625
            if self.rect.bottom > 1175:
                self.rect.bottom = 1175

class Walls(pg.sprite.Sprite): #Do this so we can have a group of walls
    def __init__(self,width,height,cx,cy):
        super().__init__()
        self.image = pg.Surface((width,height))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = (cx,cy))

pg.init()


while True:
    try:
        color = input("What color do you want to be? (yellow, purple, red, blue, green, pink, brown): ")
        break
    except:
        print("Wrong color")
#THERE IS A REASON WE MUST ASK FOR THE COLOR BEFORE WE CONNECT
addr1 = socket.gethostbyname(socket.gethostname())
addr2 = 'something'
sock = socket.socket()
#sock = socket.socket(family = socket.AF_INET6)
sock.connect((addr1,3500))
side = int(sock.recv(9000)) #This will be the side the player is at
sock.send(color.encode())
#As soon as we connected, ask for the side/id and send the color we inputed

clock = pg.time.Clock()

SCREEN = pg.display.set_mode((600,600))
SPACE = pg.Surface((600*3,600*3))
SPACE.fill('black')
"""
Example of the SPACE:

   ---
   | |
   | |
---   ---
|       |
---   ---
   | |
   | |
   ---

Each players space is 600x600
Even the middle is 600x600
This means that the ENTIRE space is 1800x1800
"""

"""
For this online game, we can make the illusion of it being multiplayer by having the client
blit ball position and their own players' position, but the server will take in all players'
positions, and handle the collision with the ball and send the ball position to all
of the players.
"""
# if side == 0:
#     print("Connected...You are on the bottom of the screen")
#     rSPACE = SPACE.get_rect(centerx = 300, bottom = 600) #This will move the SPACE surface to be in the correct position
# if side == 1:
#     print("Connected...You are on the top of the screen")
#     rSPACE = SPACE.get_rect(centerx = 300, top = 0)
# if side == 2:
#     print("Connected....You are on the left of the screen")
#     rSPACE = SPACE.get_rect(centery = 300, left = 0)
# if side == 3:
#     print("Connected...You are on the right of the screen")
#     rSPACE = SPACE.get_rect(centery = 300, right = 600)

#I will try a different idea
#Since I have to rotate the image anyways, i will make sure the side you control is always
    #at the bottom of the screen, so the rectangle will be at the bottom
if side == 0:
    print("Connected...You are on the bottom of the screen")
    #don't need to rotate SPACE
if side == 1:
    print("Connected...You are on the top of the screen")
    SPACE = pg.transform.rotate(SPACE, 180)
if side == 2:
    print("Connected....You are on the left of the screen")
    SPACE = pg.transform.rotate(SPACE, 90)
if side == 3:
    print("Connected...You are on the right of the screen")
    SPACE = pg.transform.rotate(SPACE, 270)
rSPACE = SPACE.get_rect(centerx = 300, bottom = 600) #This will move the SPACE surface to be in the correct position
#rSPACE = SPACE.get_rect(center = (300,300))
print("Waiting for the other players...")
print(sock.recv(100).decode()) #Once this prints, the game starts



walls = pg.sprite.Group(Walls(50,600,600,1500) , Walls(50,600,1200,1500) ,
                        Walls(50,600,600,300) , Walls(50,600,1200,300) ,
                        Walls(600,50,300,600) , Walls(600,50,300,1200) ,
                        Walls(600,50,1500,600) , Walls(600,50,1500,1200)
        )



player = Player(color,side)
players = pg.sprite.Group(player)
balls = pg.sprite.Group()

def send():
    while True:
        msg = f"{player.side} {player.rect.centerx} {player.rect.centery}"
        sock.send(msg.encode())
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            break
        sock.recv(1)



threading.Thread(target=send).start()

run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quitGame()

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        quitGame()
    players.update()
    walls.draw(SPACE)
    players.draw(SPACE)
    balls.draw(SPACE)
    if side == 0:
        #don't need to rotate SPACE
        SPACE2 = SPACE.copy()
    if side == 1:
        SPACE2 = pg.transform.rotate(SPACE, 180)
    if side == 2:
        SPACE2 = pg.transform.rotate(SPACE, 90)
    if side == 3:
        SPACE2 = pg.transform.rotate(SPACE, 270)
    SCREEN.blit(SPACE2, rSPACE)
    pg.display.flip()
    SPACE.fill('black')

