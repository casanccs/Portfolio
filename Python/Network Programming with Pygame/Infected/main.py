
# Add them to the group that they belong to (humans, zombies, etc.)
# Mines dont explode on the other people's screen if you touch it
# Collisions from one group to another probably won't register as well

import pygame as pg
from mainmenu import *
from Host import*
from tilemap import *
from game import *
from charactersel import *
import socket
import threading
from random import randint, sample

def stringList_to_list(stringList,n): #m is number of rows, n is number of columns, only works when the numbers are 0 <= i <= 9, and all rows have same number of columns
    newList = []
    temp = []
    j = 0 #iterator for current index of column
    for k, el in enumerate(stringList):
        if el in ['0','1','2','3','4','5','6','7','8','9']:
            temp.append(int(el))
            j += 1
            if j == n: #this means we need to start adding to the next row
                j = 0
                newList.append(temp)
                temp = []
    return newList

def acceptPlayers():
    global nplayers
    while run:
        new = sock.accept()[0] # This freezes this thread, so if i try to exit, sock.accept() will still keep this thread active.
        print("Accepted someone!")
        nplayers += 1
        allsockets.append(new)

def assignment(types, zNum):
    n = len(types)
    #pull (zNum) amount of random numbers, all must be unique
    indices = []
    while len(indices) < zNum:
        index = randint(0,n-1)
        if index in indices:
            continue
        indices.append(index)
    for i in range(zNum):
        types[indices[i]] = 1
    #Assign a random person to be a mine, given certain conditions
    if n - zNum > 2: #Then there can be a mine player
        while True:
            index = randint(0,n-1)
            if types[index] == 0:
                types[index] = 2
                break
    print(types)
    return types

def sendMessage():
    while run:
        if listen:
            print("in send")
            msg = f"{gameScreen.cPlayer.rect.x} {gameScreen.cPlayer.rect.y} " #needs to be his own position at first
            for psock in allsockets:
                msg += psock.recv(9000).decode()
            for psock in allsockets:
                psock.send(msg.encode())
            print("original:", msg)
            # for i in range(nplayers):
            #     if i != 0:
            #         self.players.sprites()[i].topleft = (int(msg[i*2]), int(msg[i*2 + 1]))
            print('sent!')
        SCREEN.fill('black')
        gameScreen.update(SCREEN, events,PLAYS,PLAYR, msg)
        pg.display.update()




sock = socket.socket()
addr = socket.gethostbyname(socket.gethostname()) #When the tilemap creator is show, have the address on the screen
nplayers = 1
run = True

allsockets = [] #This will not include the host socket
characters = []
types = []


pg.init()
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)
SCREEN = pg.display.set_mode((700,700))
pg.display.set_caption('Infected')
SCREEN.fill(black)
PLAYS = pg.Surface((2000,2000))
PLAYR = PLAYS.get_rect()


Hplay = False
Jplay = False
Tplay = False
CharPlay = False
Mplay = True
play = False


menu = MainMenu()
hmenu = HostMenu()
charSelscreen = CharacterSelection()
pscreen = tilemap()


# Text Variabels
pNumTxt = ""
zNumTxt = ""
pwrNumTxt = ""
pg.mixer.music.load("assets/music1.wav")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.25)
accepting = threading.Thread(target = acceptPlayers)
listen = False # Used to see if you are hosting, so we can properly exit
while run:
    clock.tick(60)
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                if hmenu.sSelection == 1:
                    pNumTxt = pNumTxt[:-1]

                if hmenu.sSelection == 2:
                    zNumTxt = zNumTxt[:-1]

                if hmenu.sSelection == 3:
                    pwrNumTxt = pwrNumTxt[:-1]  
           
            else:
                if hmenu.sSelection == 1 and event.unicode in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    pNumTxt += event.unicode

                if hmenu.sSelection == 2 and event.unicode in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    zNumTxt += event.unicode

                if hmenu.sSelection == 3 and event.unicode in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    pwrNumTxt += event.unicode
            if event.key == pg.K_RETURN and Tplay:
                for i in range(10):
                    x = randint(0,39)
                    y = randint(0,39)
                    while pscreen.tilemap[y][x] != 0:
                        x = randint(0,39)
                        y = randint(0,39)
                    pscreen.tilemap[y][x] = 4
                Tplay = False
                hmenu.sSelection = 5

                play = True
                #We need to send the tilemap to the other players WITHIN the creation of the game instance
                characters.append(charSelscreen.sSelection)
                #all_sockets.send(str(pscreen.tilemap))
                for i , psock in enumerate(allsockets):
                    psock.send(str(nplayers).encode()) #This will be n
                    psock.recv(100)
                    psock.send(str(i+1).encode()) #First they need their id
                    psock.recv(100)
                    psock.send(str(pscreen.tilemap).encode()) #Send that player the tilemap
                    #We then need to send the player the correct sprite that the player's chose
                    selection = int(psock.recv(100).decode()) #Gets that player's character
                    characters.append(selection)
                types = [0]*nplayers
                types = assignment(types, int(zNumTxt))
                for psock in allsockets:
                    psock.send(str(characters).encode()) #Sending the character list to all players
                    psock.recv(100)
                    print(str(types))
                    psock.send(str(types).encode())

                gameScreen = Game(pscreen.tilemap, '0', sock,characters, nplayers, types)
                threading.Thread(target = sendMessage).start()
                print(characters)
                    



    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False
        #sock.close() # This throws an error, but its ok
        if listen: socket.socket().connect((addr, 3550))



    

    # Host a match

    if menu.selection == 1:
        if menu.justSwitched: # We want this part to be ran only once
            menu.justSwitched = False
            sock.bind((addr, 3550)) # You will be the host
            sock.listen()
            listen = True
            accepting.start() # Need code to stop accepting
            # nplayers will also be their "id", but the host is "0"
        Hplay = True
        Mplay = False
    else:
        Hplay = False

    # Join a match

    if menu.selection == 2:
        if menu.justSwitched: # We want this part to be ran only once
            menu.justSwitched = False
            #addr2 = input("Input Ip")
            # if addr2 == "":
            #  sock.connect((addr, 3550))
            # else:
            #     sock.connect((addr2, 3550)) # We need to allow the user to type
            sock.connect((addr,3550))
            
        Jplay = True
        Mplay = False
    else:
        Jplay = False

    if menu.selection == 3:
        CharPlay = True
        Mplay = False
    else:
        CharPlay = False

    if hmenu.sSelection == 4:
        Tplay = True
        Hplay = False
        Jplay = False
        Mplay = False
    else:
        Tplay = False   

    if Hplay: # host screen
        hmenu.update(SCREEN, pNumTxt, zNumTxt, pwrNumTxt)

    if Tplay: # tilemap
        pscreen.update(SCREEN,PLAYS,PLAYR, nplayers)

    if play: # actual game
        SCREEN.fill("black")
        if not listen:
            gameScreen.update(SCREEN, events,PLAYS,PLAYR, "")  

    if CharPlay:
        if charSelscreen.update(SCREEN):
            CharPlay = False
            Mplay = True

    if Mplay:
        menu.update(SCREEN, events)  

    if Jplay: #The user is now WAITING on the host to start the match
        n = int(sock.recv(100).decode())
        sock.send('n got'.encode())
        id = sock.recv(100).decode() #id will be a string
        #after id, that means the match will start
        sock.send('id received'.encode())
        print(id)
        #we need to recieve and parse the tilemap
        pscreen.tilemap = stringList_to_list(sock.recv(20000).decode(), len(pscreen.tilemap[0]))
        print(pscreen.tilemap)
        sock.send(str(charSelscreen.sSelection).encode()) #Send the character that the player chose to the host
        chars = sock.recv(9000).decode().strip('][').split(', ') #Get the list of characters
        sock.send("test".encode())
        types = sock.recv(9000).decode().strip('][').split(', ') #Get the list of types everyone is
        chars = [int(x) for x in chars.copy()]
        types = [int(x) for x in types.copy()]
        print(id , chars)
        gameScreen = Game(pscreen.tilemap, id, sock, chars, n, types)
        Jplay = False
        play = True
        menu.selection = 0


    

    if not listen or not play:
        pg.display.update()
        SCREEN.fill(black)
    


