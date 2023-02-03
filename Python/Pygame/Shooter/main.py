from functions import *
from Player import *
from Bullet import *
from Enemy import *
from Grenade import *

SPAWN = pg.event.custom_type()
pg.time.set_timer(SPAWN, 1000)

p1 = Player()
pGroup = pg.sprite.Group(p1)
bGroup = pg.sprite.Group()
zGroup = pg.sprite.Group()
gGroup = pg.sprite.Group()
run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            bGroup.add(Bullet(p1.angle,p1.rect.center))
        if event.type == SPAWN:
            zGroup.add(Enemy())
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_g:
                gGroup.add(Grenade(p1.angle,p1.rect.center))

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False
        
    #bzDict = pg.sprite.groupcollide(zGroup, bGroup, False, True)
    bzDict = pg.sprite.groupcollide(zGroup,bGroup, False, True, collided = pg.sprite.collide_mask)
    #One zombie is shot: {zombie1 : bullet, zombie2 : bullet, zombie3 : bullet}
    if len(bzDict) > 0:
        zombies = list(bzDict.keys())
        #zombies are all of the zombies that got shot in the current frame
        for zombie in zombies:
            zombie.hp -= 5
            if zombie.hp <= 0:
                zombie.kill()

    gzDict = pg.sprite.groupcollide(zGroup, gGroup, False, False)
    if len(gzDict) > 0: #If a grendade is touching a zombie
        for grenade in list(gzDict.values()):
            if grenade[0].toExplode: #If a grenade exploded
                zombies = list(gzDict.keys())
                #zombies are all of the zombies that got shot in the current frame
                for zombie in zombies: #If a grenade exploded and is colliding with the grenade
                    zombie.hp -= 15
                    if zombie.hp <= 0:
                        zombie.kill()
                
    for grenade in gGroup:
        if grenade.toExplode:
            grenade.kill()


    pGroup.update()
    bGroup.update()
    zGroup.update(p1.rect.center)
    gGroup.update()
    bGroup.draw(SCREEN)
    pGroup.draw(SCREEN)
    zGroup.draw(SCREEN)
    gGroup.draw(SCREEN)
    pg.display.update()
    SCREEN.fill(colors['orange'])