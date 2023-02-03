import pygame
pygame.init()
si = pygame.display.Info()

LOOPS = {"MAIN": True, "MENU": True, "ColorMenu" : False, "PLAY": False, "OVER": False, "RulesScreen": False}

color = {"White": "#FFFFFF", "Grey": "#777777", "Green": "#00FF00", "Blue": "#0000FF", "Pink": "#F1948A", "Purple": "#8E44AD", "Yellow": "#FFFF00", "Orange": "#FFA500", "Brown": "#8B4513", "Cyan": "#00FFFF", "Red": "#FF0000", "Dark Green": "#013220", "Gold": "#DAA520", "Beige": "#F0E68C", "Olive" : "#808000", "Navy" : "#000070","Black": "#000000"}
reversed_color = {value : key for (key, value) in color.items()}
colorL = list(iter(color.values()))

scoreArray = [0,0,0,0]
#Main Screen
SCREEN = pygame.display.set_mode((si.current_w,si.current_h))
SCREEN_W = si.current_w
SCREEN_H = si.current_h
SCREEN_W_H = SCREEN_W/2
SCREEN_H_H = SCREEN_H/2

PowerPoints = 2 #Amount of points you get for each power

#Play Screen
PLAY = pygame.Surface((si.current_h, si.current_h))
PLAY.fill(color["Black"])
PLAY_R = PLAY.get_rect()
PLAY_R.center = (si.current_w/2,si.current_h/2)

P_WIDTH = PLAY_R.w
P_HEIGHT = PLAY_R.h

P_WIDTH_H = PLAY_R.w/2
P_HEIGHT_H = PLAY_R.h/2
MIDDLE = (P_WIDTH_H,P_HEIGHT_H)


toPause = False
menuCursor = 1