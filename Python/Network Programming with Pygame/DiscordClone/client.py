import socket
import threading
import pygame as pg


#Thread that gets ran every frame
def receive(sock, messages):
    while True:
        msg = sock.recv(9000).decode()
        print(msg)
        messages.insert(0,msg)
        
        



addr1 = socket.gethostbyname(socket.gethostname()) #IPv4
addr2 = '2600:1700:4be0:1a40:455c:9d7e:d566:4c7b' #IPv6


#sock = socket.socket(family = socket.AF_INET6)
sock = socket.socket()
sock.connect((addr1, 3550))
print("Connected")
print(sock.recv(9000).decode())
name = input("What is your name?: ")
sock.send(name.encode())

#Forced to wait until everyone else sends their names
print(sock.recv(9000).decode())

pg.init()
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)
SCREEN = pg.display.set_mode((600,600))
SCREEN.fill(black)

#MESSAGES SCREEN
MSCREEN = pg.Surface((600,500))
MSCREEN.fill('white')
msr = MSCREEN.get_rect()

mfont = pg.font.SysFont('arial',25)
msgs = []


#TYPE SCREEN
TSCREEN = pg.Surface((600,100))
TSCREEN.fill('black')
tsr = TSCREEN.get_rect(topleft = (0,500))

text = ""
font = pg.font.SysFont('comic sans', 25)
tsurf = font.render("Type here: " + text, True, 'white')
trect = tsurf.get_rect(topleft = (0, 10))


rthread = threading.Thread(target = receive, args = (sock, msgs)).start()



run = True
while run:
    clock.tick(60)
    
    for i,msg in enumerate(msgs):
        ts = mfont.render(msg, True, 'black')
        tr = ts.get_rect(bottomleft = (0, 500 + -i*50))
        MSCREEN.blit(ts,tr)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pg.K_RETURN:
                sock.send(text.encode())
                text = ""
            else:
                text += event.unicode
            tsurf = font.render("Type here: " + text, True, 'white')
        

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False

    TSCREEN.blit(tsurf,trect)
    SCREEN.blit(MSCREEN,msr)
    SCREEN.blit(TSCREEN,tsr)
    pg.display.update()

    MSCREEN.fill('gray')
    TSCREEN.fill('black')
    SCREEN.fill(black)