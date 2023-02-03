import pygame as pg
import socket
import sys
from os import system
import threading

"""
This section denotes the online portion
"""
def cc():
    system('cls')
cc()

name = input("What is your name?: ")
color = input("What color do you want to be? (options: white, orange, blue, green, red, purple, pink, brown): ")
print("Trying to connect...")
sock = socket.socket()
sock.connect((socket.gethostbyname(socket.gethostname()), 3950))
sock.send(name.encode())
sock.recv(9000)
sock.send(color.encode())
print(sock.recv(9000).decode())

sock.send("Random".encode())

pg.init()

clock = pg.time.Clock()
SCREEN = pg.display.set_mode((800,800))
SSIZE = SCREEN.get_size()


class Player(pg.sprite.Sprite):

    def __init__(self,color, id):
        super().__init__()
        self.image = pg.Surface((100,100))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = [i//2 for i in SSIZE])
        self.vel = [0,0]
        self.id = id
    
    def update(self):
        self.rect.move_ip(self.vel)
        if pg.key.get_pressed()[pg.K_UP]:
            self.vel = [0,-5]
        elif pg.key.get_pressed()[pg.K_RIGHT]:
            self.vel = [5,0]
        elif pg.key.get_pressed()[pg.K_DOWN]:
            self.vel = [0,5]
        elif pg.key.get_pressed()[pg.K_LEFT]:
            self.vel = [-5,0]
        else:
            self.vel = [0,0]
        sock.send(f"{self.rect.left} {self.rect.top} {self.id}".encode())
        #sends string in form of "500 200" with "x y"

class Other(pg.sprite.Sprite):

    def __init__(self,color,id):
        super().__init__()
        self.image = pg.Surface((100,100))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = [i//2 for i in SSIZE])
        self.id = id
        self.thread = threading.Thread(target = self.update)
        self.thread.start()


    

    def update(self): #This part needs to be threaded, DOES NOT GET CALLED IN GAME LOOP, GETS CALLED IN THE INIT
        pg.time.wait(2000) #THIS WAS IT!!!!!
        """
        How did I get to this conclusion?
        in the for loop:
        for i in range(n-1): #because the self is already counted
            msg = sock.recv(9000).decode().split()
            sock.send("done".encode())
            #msg is in form: ["color", "id"]
            other = Other(msg[0],int(msg[1]))
            others.add(other)
        You can see that I recv() the other players info, i.e. "white 2", on the first inner line.
        But when I instantiate an "Other" instance, it creates a thread RIGHT AFTER.
        In this thread, in the update of the class, I am SUPPOSED to recv() the other players' position and id, i.e. "300 500 2"
        BUT INSTEAD, the send() from the server side is still sending me this info, "white 2", NOT positional info, which has to happen
            during gameplay AFTER the setup.
        So when I create an "Other" object, I immediately active the update method, which should only play during gameplay.
        "Other" object creations occur BEFORE gameplay, so I must tell each thread to wait for the setup.
        """
        while True:
            msg = sock.recv(9000).decode().split()
            
            #NOTE msg is in form, ["300","500", "id"]
            print(msg)
            if int(msg[2]) == self.id:
                self.rect.top = int(msg[1])
                self.rect.left = int(msg[0])

print(sock.recv(9000).decode()) #Causes program to wait until the server sends the FIRST thing, which happens when all players are in
sock.send("Done connecting players".encode())
msg = sock.recv(9000).decode().split()
print(msg)
#msg is in form: ["color", "id"]
self = Player(msg[0], int(msg[1]))
players = pg.sprite.Group(self)
sock.send("Done sending info for a player".encode())
n = int(sock.recv(9000).decode())
sock.send("Done sending n".encode())
print("Your info has been created! Players: ", n)

print(sock.recv(9000).decode())
sock.send("Done setting self up".encode())

others = pg.sprite.Group()


for i in range(n-1): #because the self is already counted
    msg = sock.recv(9000).decode().split()
    sock.send("done".encode())
    #msg is in form: ["color", "id"]
    other = Other(msg[0],int(msg[1]))
    others.add(other)
    #sock.send("done".encode())

print("Other players are done!")
#Big caution: they players must not enter this code UNTIL the server starts working

RUN = True
while RUN:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
    
    if pg.key.get_pressed()[pg.K_ESCAPE]:
        pg.event.post(pg.event.Event(pg.QUIT))

    players.update()
    players.draw(SCREEN)
    others.draw(SCREEN)
    pg.display.flip()
    SCREEN.fill('black')
    clock.tick(60)