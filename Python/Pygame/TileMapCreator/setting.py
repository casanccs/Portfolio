import pygame as pg
import sys

pg.init()

SCREEN = pg.display.set_mode((0,0))
sSize = SCREEN.get_size()

titleSize = int(sSize[1]*.05)

MAIN = True
MENU = True
CREATE = False