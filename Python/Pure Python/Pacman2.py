from random import randint
from os import system
from time import time,sleep
import keyboard

def cc():
    system('cls')

#Pacman is a 18x18 board
def printBoard(board):
    print("██"*20)
    for i in range(17):
        print("██" + "".join(board[i]) + "██")
    print("██"*20)

board = [list(i) for i in """        ##        
 ## ### ## ### ## 
                  
 ## # ###### # ## 
    #   ##   #    
### ### ## ### ###
### #        # ###
      ##  ##      
### # #    # # ###
### # ###### # ###
                  
 ## ## #### ## ## 
  #            #  
# # # ###### # # #
    #   ##   #    
 ###### ## ###### 
                  """.split('\n')] #2d list of the level

for i in board:
    for j in range(len(i)):
        if i[j] == " ":
            i[j] = "  "
        if i[j] == "#":
            i[j] = "██"

cc()
printBoard(board)
#[8,8] is "center"               
clear = [[i for i in j] for j in board]

class Entity():
    def __init__(self,character, location,direction):
        self.char = character
        self.pos = location
        self.dir = direction
        self.dirL = [[0,-1],[0,1],[1,0],[-1,0]]
        self.open = [False,False,False,False]
        self.check(board) #Will be the form: [True,True,True,True], open[0] is up, open[1] is down, open[2] is right, open[3] is left
    def move(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]
    
    def check(self,board): #checks for the applicable open spots to change direction
        #board[self.pos[1]][self.pos[0]] is the current position of the instance, "self"
        #open[0] is up, open[1] is down, open[2] is right, open[3] is left
        if self.pos[1] > 0:
            self.open[0] = board[self.pos[1]-1][self.pos[0]] == "  "
        else:
            self.open[0] = False
        if self.pos[1] < 16: #if you are moving up, you cannot move down
            self.open[1] = board[self.pos[1]+1][self.pos[0]] == "  "
        else:
            self.open[1] = False
        if self.pos[0] < 17:
            self.open[2] = board[self.pos[1]][self.pos[0]+1] == "  "
        else:
            self.open[2] = False
        if self.pos[0] > 0:
            self.open[3] = board[self.pos[1]][self.pos[0]-1] == "  "
        else:
            self.open[3] = False
        if self.dir != [0,0]:
            id = self.dirL.index(self.dir)
            if id % 2 == 0: id += 1
            else: id -= 1
            self.open[id] = False #Makes it so the opposite direction will be False
        #problem: if they are in the square, they will eventually run into a wall
        

    def newDirection(self): #This method will choose a random new direction
        while True:
            id = randint(0,3)
            if self.open[id]:
                self.dir = self.dirL[id].copy() #AAAGHGHSDJKFALKFJAKJEFJO
                break
        
    def update(self,board):
        #Move first in the direction you are assigned (must be assigned a "True" direction)
        self.move() #move first
        #Draw on the board where the character moved
        try:
            board[self.pos[1]][self.pos[0]] = self.char
        except:
            ""
        #Update the self.open
        self.check(board) #I move THEN I check
        #If the character has more than 1 direction to travel, then set a newDirection
        if sum(self.open) > 0:
            self.newDirection()
        if sum(self.open) == 0:
            self.dir[0] = -self.dir[0]
            self.dir[1] = -self.dir[1]

class Pacman(Entity):     
    def __init__(self):
        
        self.chars = ["vv","ʌʌ","<<",">>"]
        Entity.__init__(self,self.chars[3],[8,16],[0,0]) #has self.pos, self.char, self.dir, self.dirL,self.open
    #Inherit Everything, but override "newDirection" method
    def newDirection(self):
        if self.open[0]:
            if keyboard.is_pressed('up arrow'):
                self.dir = self.dirL[0].copy()
                self.char = self.chars[0]
        if self.open[1]:
            if keyboard.is_pressed('down arrow'):
                self.dir = self.dirL[1].copy()
                self.char = self.chars[1]
        if self.open[2]:
            if keyboard.is_pressed('right arrow'):
                self.dir = self.dirL[2].copy()
                self.char = self.chars[2]
        if self.open[3]:
            if keyboard.is_pressed('left arrow'):
                self.dir = self.dirL[3].copy()
                self.char = self.chars[3]
        if self.dir != [0,0]:
            id = self.dirL.index(self.dir) #current direction you are going
            if not self.open[id]: #if the current direction you are going is not open
                self.dir = [0,0]


if __name__ == "__main__":
    entList = [Entity("@@",[8,8],[1,0])]
    pac = Pacman()
    start = time()
    Score = 1
    LOST = False
    while not LOST:
        cc()
        for i in entList:
            i.update(board)
        pac.update(board)
        printBoard(board) #print the board
        print(f"Score: {Score}")
        board = [[i for i in j] for j in clear]
        sleep(0.10)
        if time() - start > 7:
            entList.append(Entity("@@",[8,8],[1,0]))
            start = time()
            Score += 1
        for i in entList:
            if i.pos == pac.pos:
                print("You Lost!")
                sleep(5)
                LOST = True
                break

#Current Glitches:
    #1. Because the Entities only move to " ", and Pacman inherits from Entity, they MAY avoid each other