from setting import *
from Menu import *
from Create import *
from Inventory import *
from os import listdir

# Minor Fix
    # Zooming in/out gets slower as I make the bigger/smaller
    # This is because I change the scale by 0.1 each time, so as a the scale increases, the rate of change decreases

while MAIN:

    menuWindow = Menu()
    while MENU:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_RETURN:
                    if menuWindow.numTilesX != "0" and menuWindow.numTilesY != '0':
                        MENU = False
                        CREATE = True

        menuWindow.update(SCREEN,events)

    textures = [pg.image.load('TileMapCreator/textures/dirt.png'),pg.image.load('TileMapCreator/textures/grass.png')]
    textures = list(map(pg.image.load,['TileMapCreator/textures/' + string for string in listdir('TileMapCreator/textures')]))
    print(textures)
    createWindow = Create(int(menuWindow.numTilesX),int(menuWindow.numTilesY),textures)
    inventoryWindow = Inventory(textures)
    selection = textures.copy()

    while CREATE:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_RETURN:
                    MENU = True
                    CREATE = False

        createWindow.update(SCREEN,events)
        selection = inventoryWindow.update(SCREEN,events)
        pg.display.flip()
        createWindow.play.fill('white')
        inventoryWindow.screen.fill('brown')
        inventoryWindow.screen2.fill('orange')
        SCREEN.fill('gray')