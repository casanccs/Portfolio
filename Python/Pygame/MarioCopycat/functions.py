import pygame as pg

def move(player,walls): 
    # move the player and does logic with the tiles 
    # it collides with.
    # This also returns a dictionary
    colDir = {'up': False, 'down': False, 'left': False, 'right': False} # Tell us what directions we are colliding with
    player.rect.move_ip(player.vel[0], 0)
    hitList = detect(walls,player.rect)
    for tile in hitList:
        if player.vel[0] > 0:
            # We are moving right
            # We are colliding right a tile to our right
            player.rect.right = tile.left
            colDir['right'] = True
        if player.vel[0] < 0:
            player.rect.left = tile.right
            colDir['left'] = True
    player.rect.move_ip(0, player.vel[1])
    hitList = detect(walls,player.rect)
    for tile in hitList:
        if player.vel[1] > 0:
            # We are moving down
            # We are colliding right a tile to our right
            player.rect.bottom = tile.top
            colDir['down'] = True
        if player.vel[1] < 0:
            player.rect.top = tile.bottom
            colDir['up'] = True

    return colDir



def detect(walls,pRect): 
    # walls is a list of rectangles
    # pRect is a rectangle
    # return the rectangles that the player collides with
    hitList = []
    for wall in walls:
        if wall.colliderect(pRect):
            hitList.append(wall)
    return hitList

def quitGame():
    pg.event.post(pg.event.Event(pg.QUIT, {}))