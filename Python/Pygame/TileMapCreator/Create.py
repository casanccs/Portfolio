from setting import *



class Create():

    def __init__(self,tilesX,tilesY,textures):
        self.temp = textures
        self.textures = []
        for texture in self.temp:
            self.textures.append(pg.transform.scale(texture,(sSize[1]*.1,sSize[1]*.1)))
        self.tx = tilesX
        self.ty = tilesY
        if self.tx > self.ty: #if there are more tiles in the x direction, 
            self.tSize = sSize[1]//self.tx
        else:
            self.tSize = sSize[1]//self.ty
        self.ogtSize = self.tSize
        self.playSize = (self.tSize*self.tx, self.tSize*self.ty)
        self.playScale = 1
        self.play = pg.Surface(self.playSize)
        self.playr = self.play.get_rect()
        self.play.fill('gray')

        self.mprev = pg.mouse.get_pos()

        self.tilemap = [[0 for i in range(self.tx)].copy() for j in range(self.ty)]
        self.cur = (0,0)

        self.block = pg.Surface((self.tSize-2,self.tSize-2))
        self.block.fill('black')
        self.wblock = pg.Surface((self.tSize,self.tSize))
        self.wblock.fill('white')
        self.rblock = self.wblock.copy()
        self.rblock.fill('red')
        self.mouseOffset = [0,0]
        
        self.choice = 1
        


    def update(self,surf,events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.unicode in [str(i) for i in range(10)]:
                    if int(event.unicode) <= len(self.textures):
                        self.choice = int(event.unicode)
                    
            if event.type == pg.MOUSEWHEEL:
                self.playScale += 0.05*event.y
                if self.playScale < 0.1:
                    self.playScale = 0.1
                self.tSize = self.ogtSize*self.playScale
                self.playSize = int(self.tSize*self.tx),int(self.tSize*self.ty)
                self.block = pg.Surface((self.tSize-2,self.tSize-2))
                self.block.fill('black')
                self.wblock = pg.Surface((self.tSize,self.tSize))
                self.wblock.fill('white')
                self.play = pg.Surface(self.playSize)
                self.playr = self.play.get_rect(topleft = self.playr.topleft)
                self.play.fill('white')
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pg.quit()
                    sys.exit()
                if event.button == 1: #update the tilemap
                    if self.cur != None:
                        self.tilemap[self.cur[1]][self.cur[0]] = self.choice

        if pg.mouse.get_pressed()[0]: #change the position of the play rectangle
            mcur = pg.mouse.get_pos()
            self.playr.move_ip(mcur[0] - self.mprev[0], mcur[1] - self.mprev[1])
            self.mouseOffset = list(self.playr.topleft)

        touched = False
        for row, rowel in enumerate(self.tilemap): #places the black blocks onto the white surface
            for col, colel in enumerate(rowel):
                rect = pg.Rect(col*self.tSize+1,row*self.tSize+1,self.tSize-2,self.tSize-2)
                if colel > 0:
                    texture = pg.transform.scale(self.textures[colel-1],(self.tSize+1,self.tSize+1))
                    self.play.blit(texture,rect)
                else:
                    self.play.blit(self.block,rect)
                mpos = pg.mouse.get_pos()
                if rect.collidepoint((mpos[0] - self.mouseOffset[0], mpos[1] - self.mouseOffset[1])):
                    rect.topleft = (rect.left-2,rect.top-2)
                    self.play.blit(self.wblock,rect)
                    self.cur = (col,row)
                    touched = True
        if not touched:
            self.cur = None
                    


        
        surf.blit(self.play,self.playr)
        self.mprev = pg.mouse.get_pos()