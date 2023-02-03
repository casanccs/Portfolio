import pygame as pg


class HostMenu:
    
    def __init__ (self):


      
       
       self.green = (0,255,0)
       self.f = pg.font.SysFont('arial', 80)
       self.f2 = pg.font.SysFont('arial', 40)
       self.f3 = pg.font.SysFont('arial', 30)
       self.rMos = pg.Rect(0,0,5,5)
       self.selection = 0
       self.sSelection = 0

       self.sTitle = self.f.render("| - | Host Menu | - |", True, self.green)
       self.sPlay = self.f2.render("| - | BEGIN MATCH | - |", True, self.green)
       self.sSetting = self.f2.render("| - | MATCH SETTINGS | - |", True, self.green)

       # Settings Text

       self.sPNUM = self.f3.render("PLAYERS: ", True, self.green)
       self.sZNUM = self.f3.render("ZOMBIES: ", True, self.green) 
       self.sPWRUPS = self.f3.render("POWERUPS: ", True, self.green)
      

       self.rTitle = self.sTitle.get_rect(center = (350, 200))
      
       self.rPlay = self.sPlay.get_rect(center = (300,300))
       self.rSettings = self.sSetting.get_rect(center = (350,450))
       self.rPNUM = self.sPNUM.get_rect(center = (350,500))
       self.rZNUM = self.sZNUM.get_rect(center = (350,550))
       self.rPWRUPS = self.sPWRUPS.get_rect(center = (350,600)) 


    def update(self, surf, PNUM, ZNUM, PWRNUM):

        mPos = pg.mouse.get_pos()
        self.rMos.center = mPos
        
        # Play Screen

        if self.rMos.colliderect(self.rPlay):
            self.sPlay = self.f2.render("| - | BEGIN MATCH | - |", True, 'yellow')
        else:
            self.sPlay = self.f2.render("| - | BEGIN MATCH | - |", True, self.green)

        # Main Click Detection

        if self.rMos.colliderect(self.rPlay) and pg.mouse.get_pressed()[0]:
            self.sSelection = 4            

        # Text Type Values

        if self.rMos.colliderect(self.rPNUM):
            self.sPNUM = self.f3.render("PLAYERS: " + PNUM, True, 'yellow')
        else:
            self.sPNUM = self.f3.render("PLAYERS: " + PNUM, True, self.green)

        if self.rMos.colliderect(self.rZNUM):
             self.sZNUM = self.f3.render("ZOMBIES: " + ZNUM, True, 'yellow') 
        else:
             self.sZNUM = self.f3.render("ZOMBIES: " + ZNUM,True, self.green) 

        if self.rMos.colliderect(self.rPWRUPS):
             self.sPWRUPS = self.f3.render("POWERUPS: " + PWRNUM, True, 'yellow') 
        else:
             self.sPWRUPS = self.f3.render("POWERUPS: " + PWRNUM, True, self.green) 


        

        # Click Detection Per each

        # Player Text

        if self.rMos.colliderect(self.rPNUM) and pg.mouse.get_pressed()[0]:
            self.sSelection = 1
            self.sPWRUPS = self.f3.render("PLAYER: ", True, 'yellow') 
        else:
             self.sPWRUPS = self.f3.render("PLAYER: ", True, self.green) 

        # Zombie Text

        if self.rMos.colliderect(self.rZNUM) and pg.mouse.get_pressed()[0]:
            self.sSelection = 2
            self.sPWRUPS = self.f3.render("ZOMBIES: ", True, 'yellow') 
        else:
             self.sPWRUPS = self.f3.render("ZOMBIES: ", True, self.green) 

        # Power Up Text

        if self.rMos.colliderect(self.rPWRUPS) and pg.mouse.get_pressed()[0]:
            self.sSelection = 3
            self.sPWRUPS = self.f3.render("POWERUPS: ", True, 'yellow') 
        else:
             self.sPWRUPS = self.f3.render("POWERUPS: ", True, self.green) 
        
        
        
        
       

        # Settings Screen
            


        
        surf.blit(self.sTitle, self.rTitle)
        surf.blit(self.sPlay, self.rPlay)
        surf.blit(self.sSetting, self.rSettings)
        surf.blit(self.sPNUM, self.rPNUM)
        surf.blit(self.sZNUM, self.rZNUM)
        surf.blit(self.sPWRUPS, self.rPWRUPS)
        


"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠻⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⣀⣀⠀⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠻⣿⣿⣿⠅⠛⠋⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢼⣿⣿⣿⣃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣛⣫⡄⠀⢸⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡆⠸⣿⣿⣿⡷⠂⠨⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⡇⢀⣿⡿⠋⠁⢀⡶⠪⣉⢸⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿⣷⣿⣿⣷⣦⡙⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""