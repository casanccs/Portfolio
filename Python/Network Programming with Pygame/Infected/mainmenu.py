import pygame as pg


class MainMenu:
    
    def __init__ (self):

      
       
       self.green = (0,255,0)
       self.f = pg.font.SysFont('arial', 80)
       self.f2 = pg.font.SysFont('arial', 40)
       self.n = 1
       self.toPress = True
       self.rMos = pg.Rect(0,0,5,5)
       self.selection = 0
        

       self.sTitle = pg.image.load("assets/infectedlogo.png")
       self.sTitle = pg.transform.scale(self.sTitle,(500,200))
       self.sPlay = self.f2.render("| - | HOST A MATCH | - |", True, self.green)
       self.sSetting = self.f2.render("| - | JOIN A MATCH | - |", True, self.green)

       self.sCharSel = self.f2.render("| - | Character Selection | - |", True, self.green)
       self.rCharSel = self.sCharSel.get_rect(center = (350, 550))
      

       self.rTitle = self.sTitle.get_rect(center = (350, 200))
      
       self.rPlay = self.sPlay.get_rect(center = (350,350))
       self.rSettings = self.sSetting.get_rect(center = (350,450))
       self.isclicked = False

       self.justSwitched = True # This will be used to tell if the user JUST changed menus, used when we want to only run a code ONCE


    def update(self, surf, events):

       

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rMos.colliderect(self.rSettings):
                    self.selection = 2
                    self.justSwitched = True
                elif self.rMos.colliderect(self.rPlay):
                    self.selection = 1
                    self.justSwitched = True
                elif self.rMos.colliderect(self.rCharSel):
                    self.selection = 3
                    self.justSwitched = True
            

        mPos = pg.mouse.get_pos()
        self.rMos.center = mPos
        
        # Play Screen

        if self.rMos.colliderect(self.rPlay):
            self.sPlay = self.f2.render("| - | HOST A MATCH | - |", True, 'yellow')
        else:
            self.sPlay = self.f2.render("| - | HOST A MATCH | - |", True, self.green)    
        
        # Character Selection Screen

        if self.rMos.colliderect(self.rCharSel):
            self.sCharSel = self.f2.render("| - | Character Selection | - |", True, 'yellow')
        else:
            self.sCharSel = self.f2.render("| - | Character Selection | - |", True, self.green)
      

        # Settings Screen

        if self.rMos.colliderect(self.rSettings):
            self.sSetting = self.f2.render("| - | JOIN A MATCH | - |", True, "yellow")
            
        else:
            self.sSetting = self.f2.render("| - | JOIN A MATCH | - |", True, self.green) 

     

             

        
            
        surf.blit(self.sTitle, self.rTitle)
        surf.blit(self.sPlay, self.rPlay)
        surf.blit(self.sCharSel, self.rCharSel)
        surf.blit(self.sSetting, self.rSettings)

        

