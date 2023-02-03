import pygame as pg

pg.init()
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)
SCREEN = pg.display.set_mode((600,600))
SCREEN.fill(black)
run = True

tilemap = [[0,0,0],[0,0,0],[0,0,0]]
box1 = pg.Surface((200,200))
boxR = box1.get_rect()
box1.fill("red")

turn = 1

x = pg.image.load('PygameTicTacToe/x.png')
x = pg.transform.scale(x,(200,200))
o = pg.image.load('PygameTicTacToe/o.png')
o = pg.transform.scale(o,(200,170))

xTiles = []
oTiles = []

def checkWin(tiles):
    win1 = [[0,0],[1,0],[2,0]]
    win2 = [[0,1],[1,1],[2,1]]
    win3 = [[0,2],[1,2],[2,2]]
    win4 = [[0,0],[0,1],[0,2]]
    win5 = [[1,0],[1,1],[1,2]]
    win6 = [[2,0],[2,1],[2,2]]
    win7 = [[0,0],[1,1],[2,2]]
    win8 = [[0,2],[1,1],[2,0]]

    if win1[0] in tiles and win1[1] in tiles and win1[2] in tiles:
        return True
    elif win2[0] in tiles and win2[1] in tiles and win2[2]  in tiles:
        return True
    elif win3[0] in tiles and win3[1] in tiles and win3[2]  in tiles:
        return True
    elif win4[0] in tiles and win4[1] in tiles and win4[2] in tiles:
        return True
    elif win5[0] in tiles and win5[1] in tiles and win5[2] in tiles:
        return True
    elif win6[0] in tiles and win6[1] in tiles and win6[2] in tiles:
        return True
    elif win7[0] in tiles and win7[1] in tiles and win7[2] in tiles:
        return True
    elif win8[0] in tiles and win8[1] in tiles and win8[2] in tiles:
        return True
    else:
        return False
    

while run:
    clock.tick(60)
    boxR.center = pg.mouse.get_pos()

    mpos = pg.mouse.get_pos()
    tileposX = mpos[0]//200
    tileposY = mpos[1]//200

    
    if checkWin(oTiles):
        print("o won")
        run = False
    elif checkWin(xTiles):
        print("x won")
        run = False

    boxR.topleft = (tileposX*200,tileposY*200)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if  tilemap[tileposY][tileposX] == 0 :
                tilemap[tileposY][tileposX] = turn
                if turn == 1:
                    turn = 2
                    xTiles.append([tileposX,tileposY])
                elif turn == 2:
                    turn = 1
                    oTiles.append([tileposX,tileposY])

            
            print(tilemap)

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False

    for X in range(3): #Blits tiles onto the screen
        for Y in range(3):
            if tilemap[Y][X] == 1:
                SCREEN.blit(x,(X*200,Y*200))
            if tilemap[Y][X] == 2:
                SCREEN.blit(o,(X*200,Y*200))


    SCREEN.blit(box1, boxR)

    pg.display.update()

    SCREEN.fill(white)