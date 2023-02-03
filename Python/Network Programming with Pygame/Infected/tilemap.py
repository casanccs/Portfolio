import pygame as pg
import socket


class tilemap:
    
    def __init__ (self):
        self.tilemap = [[0 for i in range(40)].copy() for i in range(40)]
        self.textures = [pg.transform.scale(pg.image.load("assets/floor.png"), (50,50)),pg.transform.scale(pg.image.load("assets/wall.png"), (50,50))
        ,pg.transform.scale(pg.image.load("assets/door.png"), (50,50)),pg.transform.scale(pg.image.load("assets/window.png"), (50,50)) ]
        self.image = pg.transform.scale(self.textures[0], (50, 50))
        self.rect = self.image.get_rect(center = (350,350))
        self.tilemap[2][2] = 1
        self.cur = self.textures[1]
        self.choice = 1
        self.offset = [0,0]
        self.ip = socket.gethostbyname(socket.gethostname())

        #IP DISPLAY FOR HACKERS TO USE!!!?!1111111?!?!?!?!?1111___111
        self.fDeez = pg.font.SysFont('Impact', 38)

        self.sIP = self.fDeez.render(self.ip, True, 'green')
        self.rIP = self.sIP.get_rect(topright = (700,0))

        
        

        

    def update(self, surf,plays,playr, nplayers):

        self.nPlayers = nplayers

        self.nPlayerS = self.fDeez.render("PLRS:" + str(self.nPlayers), True, 'red')
        self.nPlayerR = self.nPlayerS.get_rect(center = (350, 20))


        #when child labor exitss for no reason
        self.cur = self.textures[self.choice]
        mpos = list(pg.mouse.get_pos())
        mpos[0] -= playr.x
        mpos[1] -= playr.y

        for x in range(40):
            for y in range(40):
                self.rect.topleft = (x*50,y*50)
                plays.blit(self.textures[self.tilemap[y][x]], self.rect)
        
        plays.blit(self.cur, (mpos[0]//50*50,mpos[1]//50*50))
        if pg.key.get_pressed()[pg.K_0]:
            self.choice = 0
        if pg.key.get_pressed()[pg.K_1]:
            self.choice = 1
        if pg.key.get_pressed()[pg.K_2]:
            self.choice = 2
        if pg.key.get_pressed()[pg.K_3]:
            self.choice = 3
        if  pg.key.get_pressed()[pg.K_RIGHT]:
            playr.move_ip(-15, 0)
        if  pg.key.get_pressed()[pg.K_LEFT]:
            playr.move_ip(15, 0)
        if  pg.key.get_pressed()[pg.K_UP]:
            playr.move_ip(0, 15)
        if  pg.key.get_pressed()[pg.K_DOWN]:
            playr.move_ip(0, -15)
        
        if pg.mouse.get_pressed()[0]:
            self.tilemap[mpos[1]//50][mpos[0]//50] = self.choice
        #deez 
        surf.blit(plays,playr)
        surf.blit(self.sIP, self.rIP) 
        surf.blit(self.nPlayerS, self.nPlayerR)
    