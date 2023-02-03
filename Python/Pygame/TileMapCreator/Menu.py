from setting import *

class Menu(pg.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()

        self.font = pg.font.SysFont('arial',titleSize)
        self.title = self.font.render('Tilemap Creator',True, 'white')
        self.rtitle = self.title.get_rect(midtop = (sSize[0]//2, int(sSize[1]*.10)))
        self.numTilesX = "10"
        self.numTilesY = "10"
        self.tx = self.font.render("# tiles in a row: " + str(self.numTilesX),True,'white')
        self.rtx = self.tx.get_rect(midtop = (sSize[0]//2, int(sSize[1]*.45)))
        self.ty = self.font.render("# tiles in a column: " + str(self.numTilesY),True,'white')
        self.rty = self.ty.get_rect(midtop = (sSize[0]//2, int(sSize[1]*.65)))
        self.choice = 0

    def update(self,surf,events):
        if self.rtx.collidepoint(pg.mouse.get_pos()):
            self.choice = 0
        if self.rty.collidepoint(pg.mouse.get_pos()):
            self.choice = 1

        for event in events:
            if event.type == pg.KEYDOWN:
                if event.unicode in [str(i) for i in range(10)]:
                    if self.choice == 0:
                        self.numTilesX += event.unicode
                    if self.choice == 1:
                        self.numTilesY += event.unicode
                if event.key == pg.K_BACKSPACE:
                    if self.choice == 0:
                        self.numTilesX = self.numTilesX[0:-1]
                    if self.choice == 1:
                        self.numTilesY = self.numTilesY[0:-1]
                

        
        if self.choice == 0:
            self.tx = self.font.render("# tiles in a row: " + str(self.numTilesX),True,'yellow')
            self.ty = self.font.render("# tiles in a column: " + str(self.numTilesY),True,'white')
        if self.choice == 1:
            self.tx = self.font.render("# tiles in a row: " + str(self.numTilesX),True,'white')
            self.ty = self.font.render("# tiles in a column: " + str(self.numTilesY),True,'yellow')
        self.rtx = self.tx.get_rect(midtop = (sSize[0]//2, int(sSize[1]*.45)))
        self.rty = self.ty.get_rect(midtop = (sSize[0]//2, int(sSize[1]*.55)))
        

        surf.blits(([self.title,self.rtitle],[self.tx,self.rtx],[self.ty,self.rty]))
        pg.display.flip()
        surf.fill('black')