import pygame as pg

pg.init()
clock = pg.time.Clock()

from math import sqrt


def h(start , end):
    return sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

def getNeighbor(node,grid):
    neighbor = []
    if node.x + 1 < len(grid[0]) and not grid[node.y][node.x + 1].wall: #Right node
        neighbor.append(grid[node.y][node.x + 1])
    if node.x - 1 > 0 and not grid[node.y][node.x - 1].wall: #Left node
        neighbor.append(grid[node.y][node.x - 1])
    if node.y + 1 < len(grid) and not grid[node.y + 1][node.x].wall: #Bottom node
        neighbor.append(grid[node.y + 1][node.x])
    if node.y - 1 > 0 and not grid[node.y - 1][node.x].wall: #Top node
        neighbor.append(grid[node.y - 1][node.x])
    if node.x + 1 < len(grid[0]) and node.y + 1 < len(grid): #Bottom right node
        if not grid[node.y][node.x + 1].wall and not grid[node.y + 1][node.x].wall:
            if not grid[node.y + 1][node.x + 1].wall:
                neighbor.append(grid[node.y + 1][node.x + 1])
    if node.x + 1 < len(grid[0]) and node.y - 1 > 0: #Top right node
        if not grid[node.y][node.x + 1].wall and not grid[node.y - 1][node.x].wall:
            if not grid[node.y - 1][node.x + 1].wall:
                neighbor.append(grid[node.y - 1][node.x + 1])
    if node.x - 1 > 0 and node.y - 1 > 0: #Top left node
        if not grid[node.y][node.x - 1].wall and not grid[node.y - 1][node.x].wall:
            if not grid[node.y - 1][node.x - 1].wall:
                neighbor.append(grid[node.y - 1][node.x - 1])
    if node.x - 1 > 0 and node.y + 1 < len(grid): #Bottom left node
        if not grid[node.y][node.x - 1].wall and not grid[node.y + 1][node.x].wall:
            if not grid[node.y + 1][node.x - 1].wall:
                neighbor.append(grid[node.y + 1][node.x - 1])
    return neighbor

def makePath(current):
    path = [(current.x,current.y)]
    while current.ppos != None:
        current = current.ppos
        path.append((current.x,current.y))
    path.reverse()
    return path

def findPath(matrix, start, end, surf):
    inf = float('inf')
    openSet = [] #The open set will be the set of discovered nodes that will be processed
    closedSet = []
    class Node:
        #Each node will have:
        def __init__(self,x,y):
            # The position
            self.x = x
            self.y = y
            # The cost
            self.f = inf
            self.g = inf
            self.h = inf

            self.neighbors = []
            self.ppos = None
            self.wall = False


    grid = [[Node(x,y) for x in range(len(matrix[0]))].copy() for y in range(len(matrix))]

    grid[start[1]][start[0]].g = 0
    grid[start[1]][start[0]].f = h(start, end)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <= 0:
                grid[i][j].wall = True
    
    openSet.append(grid[start[1]][start[0]])

    while openSet:
        current = min([node.f for node in openSet])
        current = [node for node in openSet if node.f == current][0]
        if current.x == end[0] and current.y == end[1]: #Won't work because current is not a node
            print("Done")
            return makePath(current)


        openSet.remove(current)
        closedSet.append(current)
        tilemap.update(AREA)
        SCREEN.blit(AREA,(0,0))
        for point in closedSet:
            x = point.x*tileSize[0]
            y = point.y*tileSize[1]
            pg.draw.rect(surf, (0,255,0),pg.Rect(x,y,tileSize[0],tileSize[1]))
        for point in openSet:
            x = point.x*tileSize[0]
            y = point.y*tileSize[1]
            pg.draw.rect(surf, (255,0,0),pg.Rect(x,y,tileSize[0],tileSize[1]))
        for point in makePath(current): #draw blue circles for the current path
            x = point[0]*tileSize[0] + tileSize[1]//2
            y = point[1]*tileSize[1] + tileSize[1]//2
            pg.draw.circle(surf, (0,0,255),(x,y),ss[1]//54//2)

        pg.display.update()
        AREA.fill((194, 178, 128))
        SCREEN.fill(black)
        #pg.time.wait(50)
        current.neighbors = getNeighbor(current, grid)
        print(current.neighbors)
        for neighbor in current.neighbors:
            currentG = current.g + 1
            if currentG < neighbor.g:
                neighbor.ppos = current
                neighbor.g = currentG
                neighbor.f = currentG + h((neighbor.x,neighbor.y), end)
                if neighbor not in openSet:
                    openSet.append(neighbor)
    print("Failed to Find Path.")
    return []



black = (0,0,0)
white = (255,255,255)
SCREEN = pg.display.set_mode((0,0))
SCREEN.fill(black)
ss = SCREEN.get_size()

AREA = pg.Surface(ss)
AREA.fill((194, 178, 128))

class Tilemap(pg.sprite.Sprite):
    def __init__(self,matrix, dict,w,h):
        super().__init__()
        self.rT = pg.Rect(0,0,w,h)
        self.matrix = matrix
        self.dict = dict
        self.w = w
        self.h = h


    def update(self,surf):
        tarray = []
        mpos = pg.mouse.get_pos()
        wb = pg.Surface((self.w,self.h))
        wb.fill(white)
        surf.blit(wb,(mpos[0]//self.w*self.w,mpos[1]//self.h*self.h))
        y = 0
        for row in self.matrix:
            x = 0
            for rc in row:
                if rc == 0:
                    self.rT.topleft = (x*self.w, y*self.h)
                    surf.blit(self.dict[rc], self.rT)
                    tarray.append(self.rT.copy())
                x += 1
            y += 1
        return tarray

    def addWall(self,pos):
        self.matrix[pos[1]][pos[0]] = 0
    
    def deleteWall(self,pos):
        self.matrix[pos[1]][pos[0]] = 1

class Pathfinder:

    def __init__(self, matrix, start, end,surf):
        self.path = findPath(matrix,start,end,surf)

    def update(self,surf):
        for point in self.path:
            x = point[0]*tileSize[0] + tileSize[1]//2
            y = point[1]*tileSize[1] + tileSize[1]//2
            pg.draw.circle(surf, (0,0,255),(x,y),ss[1]//54//2)


matrix = [[1 for _ in range(96)].copy() for _ in range(54)]
tileSize = ss[0]//96, ss[1]//54
wall = pg.Surface(tileSize)
wall.fill(black)

tilemap = Tilemap(matrix, {0: wall}, *tileSize)

pf = []
run = True
while run:
    clock.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mpos = pg.mouse.get_pos()
            tilemap.addWall((mpos[0]//tileSize[0], mpos[1]//tileSize[1]))
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                mpos = pg.mouse.get_pos()
                pf = Pathfinder(tilemap.matrix, (0,0), (mpos[0]//tileSize[0], mpos[1]//tileSize[1]),SCREEN)
    
    if pg.mouse.get_pressed()[0]:
        mpos = pg.mouse.get_pos()
        tilemap.addWall((mpos[0]//tileSize[0], mpos[1]//tileSize[1]))
    
    if pg.key.get_pressed()[pg.K_BACKSPACE]:
        mpos = pg.mouse.get_pos()
        tilemap.deleteWall((mpos[0]//tileSize[0], mpos[1]//tileSize[1]))

    if pg.key.get_pressed()[pg.K_ESCAPE]:
        run = False



    tilemap.update(AREA)
    if pf: pf.update(AREA)
    SCREEN.blit(AREA,(0,0))
    pg.display.update()
    AREA.fill((194, 178, 128))
    SCREEN.fill(black)