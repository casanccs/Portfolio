import pygame as pg
from player_client import *
from paticles import *
from random import randint
import threading

class Game:
    def __init__(self, tilemap, id, sock, chars, nplayers, types):

        self.tilemap = tilemap
        self.textures = [pg.transform.scale(pg.image.load("assets/floor.png"), (50,50)),pg.transform.scale(pg.image.load("assets/wall.png"), (50,50))
        ,pg.transform.scale(pg.image.load("assets/door.png"), (50,50)),pg.transform.scale(pg.image.load("assets/window.png"), (50,50)), 
        pg.transform.scale(pg.image.load("assets/landmine.png"), (50,50))]
        self.image = pg.transform.scale(self.textures[0], (50, 50))
        self.explosion = pg.Surface((150,150))
        self.explosion.fill('Orange')
        self.gp = pg.sprite.Group()
        self.id = int(id)
        self.sock = sock
        self.chars = chars
        self.types = types
        self.n = nplayers
        
        #tilemap[randomy][randomx] = 4 #10 in tilemap is 
        self.rect = self.image.get_rect(center = (350,350))
        self.walls = []
        self.mine = []
        self.minepos = []
        for x in range(40):
            for y in range(40):
                self.rect.topleft = (x*50,y*50)
                if self.tilemap[y][x] != 0 and self.tilemap[y][x] != 4:  
                    self.walls.append(self.rect.copy())
        
        self.f4 = pg.font.SysFont('Courier New', 40)


        #Stamina

        self.sStaminaBg = pg.Surface((100, 40))
        self.sStaminaBg.fill('grey')
        self.rStaminaBg = self.sStaminaBg.get_rect(topleft = (15,15))
        
        self.sStamina = pg.Surface((90, 30))
        self.sStamina.fill('green')
        self.rStamina = self.sStamina.get_rect(topleft = (20,20)) 

        #Sprite Groups
        print(types, self.id)
        self.cPlayer = Player(self.walls, self.id, self.sock, chars[self.id], types[self.id]) #the playr needs to follow this self.cPlayer
        self.players = pg.sprite.Group()
        for i in range(nplayers): #Remember, player id == 1, means that they are the 
            if i == self.id:
                self.players.add(self.cPlayer)
            else:
                self.players.add(Player(self.walls, i, self.sock, chars[i], types[i]))
            

        self.humans = pg.sprite.Group(self.cPlayer) #pretend this is full of humans
        self.zombies = pg.sprite.Group() #pretend this is full of zombies
        self.run = True
        if self.id != 0:
            self.msgthread = threading.Thread(target = self.messages)
            self.msgthread.start()
                
    def update(self,surf,events,plays,playr, msg: str):
        
        if len(msg) > 3:
            msg = msg.split()
            print(msg)
            for i in range(self.n):
                    if i != self.id:
                        self.players.sprites()[i].rect.topleft = (int(msg[i*2]), int(msg[i*2 + 1]))

        hzcollision = pg.sprite.groupcollide(self.humans, self.zombies, False, False)
        if hzcollision: #turns humans into zombies
            hzcollision.keys()[0].type = 1

        self.mines = []
        MineX = self.cPlayer.rect.centerx//50 #Tile position x of player
        MineY = self.cPlayer.rect.centery//50 #Tile position y of player
        
        if self.cPlayer.type == 0:
            if pg.key.get_pressed()[pg.K_SPACE] and self.cPlayer.MineAmount >= 1 and self.cPlayer.stamina >= 80:
                if self.tilemap[MineY][MineX] != 4:
                    self.tilemap[MineY][MineX] = 4
                    self.cPlayer.MineAmount -= 1
                    self.cPlayer.stamina -= 75

        

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.run = False


        playr.x = 330 - self.cPlayer.rect.x
        playr.y = 330 - self.cPlayer.rect.y
        self.sStamina = pg.Surface(((self.cPlayer.stamina / self.cPlayer.maxStamina) * 90, 30))
        self.sStamina.fill('green')

        mpos = pg.mouse.get_pos()
        for x in range(40):
            for y in range(40):
                self.rect.topleft = (x*50,y*50)
                plays.blit(self.textures[self.tilemap[y][x]], self.rect)
                if self.tilemap[y][x] == 4:  
                    self.mines.append((self.rect.copy(), (x,y))) # dis is pretty useless because yes
                    

        for index,mine in enumerate(self.mines):
            if self.cPlayer.type == 1 and self.cPlayer.rect.colliderect(mine[0]):
                for i in range(100): #Makes it explode
                    self.gp.add(Particle(mine[0].center))   

                self.tilemap[self.mines[index][1][1]][self.mines[index][1][0]] = 0 #removes the mines


                #self.cPlayer.rect.topleft = (0,0)
                self.mines.pop(index)

            if self.cPlayer.type == 0 and self.cPlayer.rect.colliderect(mine[0]) and pg.key.get_pressed()[pg.K_e]:
                self.cPlayer.MineAmount += 1
                self.tilemap[self.mines[index][1][1]][self.mines[index][1][0]] = 0 #removes the mines
                self.mines.pop(index)

        self.gp.draw(plays)
        self.gp.update()        



                                                                                                   





        self.players.update(events, self.id)
        self.players.draw(plays)
        surf.blit(plays,playr)



        # Mines & Stamina Blitting
        if self.cPlayer.type == 0:
            self.sTextMine = self.f4.render("MINES: " + str(self.cPlayer.MineAmount), True, 'Red')
            self.rTextMine = self.sTextMine.get_rect(topleft = (20,75))
            surf.blit(self.sTextMine, self.rTextMine)
            surf.blit(self.sStaminaBg, self.rStaminaBg)
            surf.blit(self.sStamina, self.rStamina)


    def messages(self):
        while self.run:
            self.sock.send(f"{self.cPlayer.rect.x} {self.cPlayer.rect.y} ".encode())
            msg = self.sock.recv(9000).decode()
            print(msg)
            """
            msg looks like:
            "{0's x} {0's y} {1's x} {1's y} {2's x} {2's y}..."
            """
            msg = msg.split()
            """
            msg now looks like:
            [0's x, 0's y, 1's x, 1's y...]
            """
            #Don't forget to convert all elements to integers!!
            for i in range(self.n):
                if i != self.id:
                    print("updateing")
                    self.players.sprites()[i].rect.topleft = (int(msg[i*2]), int(msg[i*2 + 1]))