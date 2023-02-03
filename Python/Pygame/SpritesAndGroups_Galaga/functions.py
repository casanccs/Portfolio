import pygame as pg


def makeText(font, size, text, location, color):
    f = pg.font.SysFont(font, size)
    s = f.render(text, True, color)
    r = s.get_rect(topleft = location)
    return s, r