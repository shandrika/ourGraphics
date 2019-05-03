from graphics import *
from random import *

def draw_rect(rX, rY, rColor, sizeX, sizeY, win):

    square = Rectangle(Point(rX, rY),
                       Point(rX + sizeX, rY + sizeY))
    square.setFill(rColor)
    square.setOutline(rColor)
    square.draw(win)
    
def draw_sky(sX, sY, sizeX, sizeY, win):
    draw_rect(sX, sY, "sky blue", sizeX, sizeY, win)
    
def draw_be(bX, bY, sizeX, sizeY, win):
    draw_rect(bX, bY, "light yellow", sizeX, sizeY, win)
    
def draw_h20(wX, wY, sizeX, sizeY, win):
    draw_rect(wX, wY, "blue", sizeX, sizeY, win)
    
def draw_cir(cX, cY, radius, cColor1, cColor2, win):
    circle = Circle(Point(cX, cY), radius)
    circle.setFill(cColor1)
    circle.setOutline(cColor2)
    circle.draw(win)

def draw_puff(pX, pY, radius, pColor, win):
    puff = Circle(Point(pX, pY), radius)
    puff.setFill(pColor)
    puff.setOutline(pColor)
    puff.draw(win)

def draw_cloud(clX, clY, pMin, pMax, clColor, win):
    puffs = randint(pMin, pMax)
    for i in range(puffs):
        pX = randint(clX - 50, clX + 50)
        pY = randint(clY - 20, clY + 20)
        pSz = randint(5, 35)
        draw_puff(pX, pY, pSz, clColor, win)

def draw_clouds(sX, sY, clNum, clBumpX, clBumpY, clColor, win):
    for j in range(clNum):
        sY2 = sY + randint(-clBumpY, clBumpY)
        draw_cloud(sX + j * clBumpX, sY2, 10, 18, clColor, win)
        
def draw_waves(winSzX, wY, wRad, wColor1, wColor2, win):
    waves = int(winSz / wRad * 2)
    for r in range(1):
        for i in range(waves):
                draw_cir(wRad + i * wRad * 2, wY + r * wRad * 2, wRad, wColor1, wColor2, win)
    
     
winSz = 1000

win = GraphWin("Let's Play Volleyball!", winSz, winSz)
win.setCoords(0,0, winSz, winSz)

#Called Funcs
draw_h20(0,0, winSz, winSz * .7, win) #water
draw_be(0,0, winSz, winSz * .4, win) #beach 
draw_sky(0,winSz/2 + 100, winSz, winSz * .5, win) #sky
draw_waves(winSz,winSz/2 + 100, 15, "sky blue", "sky blue", win) #waves
draw_cir(winSz/2, winSz/1.17, 125, "yellow","yellow", win) #Sun
draw_clouds(100, 930, 6, 150, 100, "white", win) #Clouds

# Creation of Sand Spots
for s in range(1000):
    saX = randint(10,1000)
    saY = randint(10,490)
    saSz = randint(1,2)
    draw_cir(saX, saY, saSz, "burlywood1","burlywood1", win)

    

#draw_cir(winSz/2, winSz/5, 34, "white", "black", win) #Volleyball



