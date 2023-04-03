import pygame
import os as fileI

class HighScore():
    def __init__(self,score,numOfP):
        self.check = False
        fileString = "Highscore.txt"
        self.file = open(fileString,"r+")
        self.currentH = self.file.readline()
        self.currentH2 = self.file.readline()
        self.file.seek(0,0)
        if int(score) > int(self.currentH) and (numOfP == 1 or numOfP == 2):
            self.currentH = score
            self.check = True
            print(self.file.tell())
            self.file.write(str(self.currentH))
        self.file.readline()
        if int(score) > int(self.currentH2) and (numOfP == 3 or numOfP == 4):
            self.currentH2 = score
            self.check = True
            self.file.write(str(self.currentH2))
        self.file.close()

#There is a problem with the logic here: The way that it reaches the second line depends on the seek, which depends on the number of characters for the first record