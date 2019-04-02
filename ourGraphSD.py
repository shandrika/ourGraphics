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


winSz = 1000

win = GraphWin("Let's Play Volleyball!", winSz, winSz)
win.setCoords(0,0, winSz, winSz)

draw_sky(0,0, winSz, winSz, win)
draw_h20(0,0, winSz, winSz * .7, win)
draw_be(0,0, winSz, winSz * .5, win)
draw_cir(winSz/2, winSz/4, 34, "white", "black", win) # Volleyball

puffs = randint(10, 18)
for i in range(puffs):
        pX = randint(100, 200)
        pY = randint(910, 950)
        pSz = randint(1, 35)
        draw_puff(pX, pY, pSz, "white", win)



