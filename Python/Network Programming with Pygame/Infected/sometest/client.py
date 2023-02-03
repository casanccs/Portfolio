import pickle
import pygame as pg
import sys
from player import *
import socket
import threading

addr = socket.gethostbyname(socket.gethostname())
sock = socket.socket()
sock.connect((addr, 3550))
color = input("What color will you be?: ")
sock.send(color.encode())
player = pickle.loads(sock.recv(9000))
print(player.id)

sock.recv(100) # all players would have joined after this line


pg.init()
clock = pg.time.Clock()
SCREEN = pg.display.set_mode((600,600))



while run:
    clock.tick(60)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False
        pg.quit()
        sys.exit()


   
    pg.display.flip()
    SCREEN.fill('black')
