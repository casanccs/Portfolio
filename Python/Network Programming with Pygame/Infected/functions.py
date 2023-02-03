import pygame as pg
import socket
import threading
from random import randint
from math import sin, cos, asin, radians, degrees

def detect1(obj, sprites):
    hitlist = []
    for sprite in sprites:
        if obj.rect.colliderect(sprite.rect):
            hitlist.append(sprite)
    return hitlist

def detect2(obj, rects): 
    hitlist = []
    for rect in rects:
        if obj.rect.colliderect(rect):
            hitlist.append(rect)
    return hitlist

def objmove1(obj, sprites): #For Sprites
    coldir = {"top": False, "bottom": False, "left": False, "right": False}
    obj.rect.move_ip(obj.vel[0], 0)
    hitlist = detect1(obj, sprites)
    for hit in hitlist:
        if obj.vel[0] > 0:
            obj.rect.right = hit.rect.left
            coldir["right"] = True

        elif obj.vel[0] < 0:
            obj.rect.left = hit.rect.right
            coldir["left"] = True


    obj.rect.move_ip(0, obj.vel[1])
    hitlist = detect1(obj, sprites)
    for hit in hitlist:
        if obj.vel[1] > 0:
            obj.rect.bottom = hit.rect.top
            coldir["bottom"] = True

        elif obj.vel[1] < 0:
            obj.rect.top = hit.rect.bottom
            coldir["top"] = True

    return coldir 
    
def objmove2(obj, rects): #For Rectangles
    coldir = {"top": False, "bottom": False, "left": False, "right": False}
    obj.rect.move_ip(obj.vel[0], 0)
    hitlist = detect2(obj, rects)
    for hit in hitlist:
        if obj.vel[0] > 0:
            obj.rect.right = hit.left
            coldir["right"] = True

        elif obj.vel[0] < 0:
            obj.rect.left = hit.right
            coldir["left"] = True


    obj.rect.move_ip(0, obj.vel[1])
    hitlist = detect2(obj, rects)
    for hit in hitlist:
        if obj.vel[1] > 0:
            obj.rect.bottom = hit.top
            coldir["bottom"] = True

        elif obj.vel[1] < 0:
            obj.rect.top = hit.bottom
            coldir["top"] = True

    return coldir 