from random import randint, choices
from os import system
from time import time, sleep


def cc():
    system('cls')
    print("Leave entry blank to go back a screen.\n")

def clear():
    system('cls')

#impementing custom decorator
def inputIntTest(low,high): #low and high are included
    def onDecorate(func):
        def onCall(*args):
            while True:
                out = func(*args)
                if low <= out <= high: #valid
                    return out
                else: #invalid
                    print("Invalid input!")
        return onCall
    return onDecorate

def inputStrTest(*args,failMessage):
    def onDecorate(func):
        def onCall(*fargs):
            while True:
                out = func(*fargs)
                if out in args:
                    return out, True
                elif out == "":
                    return out, False
                else: #invalid
                    print(failMessage)
        return onCall
    return onDecorate

def avoidInputStrTest(*args,failMessage):
    def onDecorate(func):
        def onCall(*fargs):
            while True:
                out = func(*fargs)
                if out in args:
                    print(failMessage)
                elif out == "":
                    return out, False #False is to "Go back"
                else:
                    return out, True #True is to "Go forward"
        return onCall
    return onDecorate

@inputIntTest(1,5)
def askN():
    n = int(input("How many players will be in the match? (Up to 5): "))
    return n

@inputStrTest("y","n", failMessage = "You didn't type y or n!")
def yn(question):
    n = input(question)
    return n

@inputIntTest(1,3)
def askRow(inst):
    n = int(input(f'{inst.name}, which row will you bet on?: '))
    inst.choice = n
    return n

def printInfo(playerList):
    sn = ""
    sm = ""
    sb = ""
    sc = ""
    sh = ""
    ss = ""
    s = [""]*4
    for i in playerList:
        for j in range(len(s)):
            s[j] += "|"
        s[0] += "{:^34}".format("Choice: " + str(i.choice))
        s[1] += "{:^34}".format("Bet: " + str(i.bet))
        s[2] += "{:^34}".format("Money: " + str(i.money))
        s[3] += "{:^34}".format(str(i.name))
    for j in range(len(s)):
        s[j] += "|"
        print('{:^176}'.format(s[j]))

class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.bet = 0
        self.choice = 0
    
class Slots:

    def __init__(self):
        self.items = [ "🍒", "🍋", "💎"]
        self.board = [["  " for i in range(3)] for j in range(3)]
    
    def spin(self):
        for i in range(3):
            self.board[i] = choices(self.items, k = 3)

        return [(i[0] == i[1] == i[2]) for i in self.board] #returns a list saying True if that row won or not.

def printBoard(slots,playerList,MiddleMessage):

    """
    Maximum 5 players
    """
    #Slots is 5 characters long, which means the "o" in slots must be in the 13th spot 
    print('{:^176}'.format("Slots"))
    print('{:^176}\n'.format("‾"*9)) #8 + 9 + 8 = 25 which is correct
    #Middle Part (6 spaces)
    print('{:^176}'.format(" "*8 + "_"*16))
    for i in range(3):
        print('{:^173}'.format(f'Row: {i+1} | {slots[i][0]} | {slots[i][1]} | {slots[i][2]} |')) #176-3 because of emojis
    print('{:^176}\n'.format(" "*8 + "‾"*16))
    #Message part
    print("{:^176}".format(MiddleMessage))
    #After
    print('\n\n')
    #Player space (3 spaces before)
    printInfo(playerList)



def printBoard2(playerList):
    time = 3
    for i in range(3):
        print('{:^176}'.format("Slots"))
        print('{:^176}\n'.format("‾"*9)) #8 + 9 + 8 = 25 which is correct
        #Middle Part ()
        print()
        print('{:^176}'.format("Starting in..."))
        print('{:^176}'.format(time))
        print()
        print('\n')
        #After
        print('\n\n\n')

        #Player Space
        printInfo(playerList)
        sleep(1)
        clear()
        time -= 1
    


if __name__ == "__main__":
    cc()
    print("WARNING! This game works on consoles that support unicode with emojis!")
    print(f"Test to see if your console supports: 🍒, 🍌, 🍇")
    sleep(2)
    cc()
    try:
        file = open('CoolSlots.txt', 'r')
        saved = file.readlines() #looks like: ["Cristian 5000", "Someone 1000", ...]
        saved = [[i.split()[0], int(i.split()[1])] for i in saved] #looks like: [["Cristian", 5000], ["Someone", 1000], ...]

        @inputStrTest(*[i[0] for i in saved], failMessage = "Person not in database!")
        def savedPerson(question):
            n = input(question)
            return n

        @avoidInputStrTest(*[i[0] for i in saved], failMessage = "Person is already in database!")
        def newPerson(question):
            n = input(question)
            return n

        nplayers = askN() #Enforce decorator
        cc()
        playerList = []
        for i in range(nplayers): #Current issue is that people can choose the same name
            while True:
                cc()
                print(f"Player {i+1}: ")
                inFile = yn("Do you have a saved person? (y/n): ") #Enforce decorator
                if inFile[0] == "y":
                    name = savedPerson("What is your name?: ") #Enforce decorator
                    if name[1]:
                        money = [i[1] for i in saved if i[0] == name[0]][0] #should only be 1 element
                        clear()
                        break
                else:
                    name = newPerson("What is your name?: ")
                    if name[1]:
                        money = 5000
                        clear()
                        break
                    
            playerList.append(Person(name[0],money))
        while True:    
            #While loop will probably occur here
            betFunctions = []
            for i in range(len(playerList)): #This is insane
                @inputIntTest(0,playerList[i].money)
                def checkInput():
                    n = int(input(f"{playerList[i].name}, what is your bet?: "))
                    return n
                betFunctions.append(checkInput)
            machine = Slots()
            printBoard(machine.board,playerList,"")

            #Ask for bets and row
            for i in range(len(playerList)):
                playerList[i].bet = betFunctions[i]()
                askRow(playerList[i])
            clear()
            printBoard2(playerList)
            wtime = 0.01
            while wtime < 0.3:
                rows = machine.spin()
                printBoard(machine.board, playerList, "Spinning...")
                sleep(wtime)
                wtime += 0.01
                clear()
        
            if rows[0] == rows[1] and rows[1]== rows[2]: #If all rows won or lost, everyone wins
                for i in range(len(playerList)):
                    playerList[i].money += playerList[i].bet
                printBoard(machine.board, playerList, "Everyone Won!")

            else: 
                winList = []
                for i in range(len(playerList)):
                    if rows[playerList[i].choice - 1]:
                        playerList[i].money += playerList[i].bet
                    else:
                        playerList[i].money -= playerList[i].bet
                printBoard(machine.board, playerList, "Updated Money!")
            if input("Want to play again? (y/n): ") != "y":
                break
            clear()
    
    finally:
        file.close()
    print("Saving...")
    file = open('CoolSlots.txt', 'w')
    for i in playerList:
        for j in saved:
            if i.name == j[0]:
                j[1] = i.money
                break
        else:
            saved.append([i.name, i.money]) #If they are a new player
    for i in saved:
        file.write(f'{i[0]} {i[1]}\n')
    print("Saved.")
    