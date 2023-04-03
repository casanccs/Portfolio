from setting import *

class Inventory():

    def __init__(self,textures):
        self.textures = textures
        self.screen = pg.Surface((sSize[0]//15,sSize[1]//3))
        self.screenSize = self.screen.get_size()
        self.screenr = self.screen.get_rect(topright = (sSize[0],0))
        #self.screenr = self.screen.get_rect(topleft = (0,0))

        self.screen.fill('brown')
        #self.screen.set_alpha(150)
        self.arrowup = pg.transform.scale(pg.image.load('arrow.png'),(int(self.screenSize[0]*.2),int(self.screenSize[1]*.1)))
        self.arrowupr = self.arrowup.get_rect(centerx = (self.screenSize[0]//2), top = (self.screenSize[1]//30))
        self.arrowdown = pg.transform.rotate(self.arrowup,180)
        self.arrowdownr = self.arrowdown.get_rect(centerx = (self.screenSize[0]//2), bottom = int(29*self.screenSize[1]/30))

        self.group = 0
        self.ngroup = (len(self.textures)-1)//4 #Maximum number of groups
        print("self.ngroup " + str(self.ngroup))
        self.selection = [self.textures[i] for i in range(len(textures)) if self.group*4 <= i < self.group*4 + 4] #Which texures should be shown

        #Text
        self.font = pg.font.SysFont('arial',self.screenSize[0]//3)
        self.one = self.font.render(str(self.group*4 + 1),True, 'white')
        self.oner = self.one.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,0*self.screenSize[0]//4 + 0*self.screenSize[1]//10 + 4*self.screenSize[1]//28))
        self.two = self.font.render(str(self.group*4 + 2),True, 'white')
        self.twor = self.two.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,1*self.screenSize[0]//4 + 1*self.screenSize[1]//10 + 4*self.screenSize[1]//28))
        self.three = self.font.render(str(self.group*4 + 3),True, 'white')
        self.threer = self.three.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,2*self.screenSize[0]//4 + 2*self.screenSize[1]//10 + 4*self.screenSize[1]//28))
        self.four = self.font.render(str(self.group*4 + 4),True, 'white')
        self.fourr = self.four.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,3*self.screenSize[0]//4 + 3*self.screenSize[1]//10 + 4*self.screenSize[1]//28))

        self.screen2 = pg.Surface((sSize[0]//15,sSize[0]//15))
        self.screen2.fill('orange')
        self.screen2r = self.screen2.get_rect(topleft = self.screenr.bottomleft)
        self.font2 = pg.font.SysFont('arial',self.screenSize[0]//3//2)
        self.tileT = self.font2.render("Current tile: ",True, 'black')
        self.tileTr = self.tileT.get_rect(top = 10, centerx = self.screen2.get_size()[0]//2)

        self.choice = 0
        self.choiceT = self.font.render(str(self.choice+1), True, 'black')
        self.choiceTr = self.choiceT.get_rect(centery = self.screen2r.height//2, right = self.screen2r.width - 10)

        self.tile = pg.transform.scale(self.textures[self.choice], ( self.screen2r.width//3,self.screen2r.height//3))
        self.tileR = self.tile.get_rect(left = self.screen2r.width//6,centery = self.screen2r.height//2)
    def update(self,surf: pg.Surface,events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                mpos = list(pg.mouse.get_pos())
                mpos[0] -= sSize[0]-sSize[0]//15
                if self.arrowdownr.collidepoint(mpos): #If i click down on the down arrow
                    if self.group+1 <= self.ngroup: #If I am not on the final group
                        self.group += 1
                if self.arrowupr.collidepoint(mpos): #If i click down on the down arrow
                    if self.group-1 >= 0: #If I am not on the first group
                        self.group -= 1
                
            if event.type == pg.KEYDOWN:
                if event.unicode in [str(i) for i in range(10)]:
                    if int(event.unicode) <= len(self.textures):
                        self.choice = int(event.unicode)
                        if self.choice != 0:
                            self.tile = pg.transform.scale(self.textures[self.choice-1], ( self.screen2r.width//3,self.screen2r.height//3))
                        else:
                            self.tile = pg.Surface((0,0))
                        self.choiceT = self.font.render(str(self.choice), True, 'black')
            self.one = self.font.render(str(self.group*4 + 1),True, 'white')
            self.oner = self.one.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,0*self.screenSize[0]//4 + 0*self.screenSize[1]//10 + 4*self.screenSize[1]//28))
            self.two = self.font.render(str(self.group*4 + 2),True, 'white')
            self.twor = self.two.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,1*self.screenSize[0]//4 + 1*self.screenSize[1]//10 + 4*self.screenSize[1]//28))
            self.three = self.font.render(str(self.group*4 + 3),True, 'white')
            self.threer = self.three.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,2*self.screenSize[0]//4 + 2*self.screenSize[1]//10 + 4*self.screenSize[1]//28))
            self.four = self.font.render(str(self.group*4 + 4),True, 'white')
            self.fourr = self.four.get_rect(topleft = (self.screenSize[0] - self.screenSize[0]//3,3*self.screenSize[0]//4 + 3*self.screenSize[1]//10 + 4*self.screenSize[1]//28))
            self.selection = [self.textures[i] for i in range(len(self.textures)) if self.group*4 <= i < self.group*4 + 4] #Which texures should be shown

                
        for i, el in enumerate(self.selection):
            #We know that up arrow takes up screenSize[1]//30 + screenSize[1]//10 = 4*screenSize[1]//30
            cur = pg.transform.scale(el,(self.screenSize[0]//4,self.screenSize[0]//4))
            rect = pg.Rect(self.screenSize[0]//5,i*self.screenSize[0]//4 + i*self.screenSize[1]//10 + 5*self.screenSize[1]//30, self.screenSize[0]//4,self.screenSize[0]//4)
            self.screen.blit(cur,rect)

        self.screen.blit(self.one,self.oner)
        self.screen.blit(self.two,self.twor)
        self.screen.blit(self.three,self.threer)
        self.screen.blit(self.four,self.fourr)
        self.screen.blit(self.arrowup,self.arrowupr)
        self.screen.blit(self.arrowdown,self.arrowdownr)
        

        self.screen2.blit(self.choiceT,self.choiceTr)
        self.screen2.blit(self.tileT, self.tileTr)
        self.screen2.blit(self.tile, self.tileR)
        surf.blit(self.screen2, self.screen2r)
        surf.blit(self.screen,self.screenr)