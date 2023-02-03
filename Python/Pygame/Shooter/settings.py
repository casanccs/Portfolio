import pygame as pg
from time import time
from random import randint, choice
from math import sin, cos, atan, radians, degrees

pg.init()
clock = pg.time.Clock()
colors = {'black': (0,0,0), 'white' : (255,255,255), 'orange' : (150,80,0)}


SCREEN = pg.display.set_mode((800,800))
SCREEN.fill(colors['orange'])
ssize = [SCREEN.get_width(),SCREEN.get_height()]

