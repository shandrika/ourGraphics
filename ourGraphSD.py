from graphics import *
from random import*

def draw_rect(rX, rY, rColor, sizeX, sizeY, win):
    square = Rectangle(Point(rX, rY),
                       Point(rX + sizeX, rY + sizeY))
    square.setFill(rColor)
    square.setOutline(rColor)
    square.draw(win)
    
def draw_sky(sX, sY, sizeX, sizeY, win):
    draw_rect(sX, sY, "sky blue", sizeX, sizeY, win)
    
def draw_be(bX, bY, sizeX, sizeY, win):
    draw_rect(bX, bY, "bisque1", sizeX, sizeY, win)
    
def draw_h20(wX, wY, sizeX, sizeY, win):
    draw_rect(wX, wY, "blue", sizeX, sizeY, win)
    
def draw_cir(cX, cY, radius, cColor1, cColor2, win):
    circle = Circle(Point(cX, cY), radius)
    circle.setFill(cColor1)
    circle.setOutline(cColor2)
    circle.draw(win)
    
winSz = 1000

win = GraphWin("Let's Play Volleyball!", winSz, winSz)
win.setCoords(0,0, winSz, winSz)

draw_sky(0,0, winSz, winSz, win)
draw_h20(0,0, winSz, winSz * .7, win)
draw_be(0,0, winSz, winSz * .5, win)
draw_cir(winSz/2, winSz/4, 34, "white","black", win)

# Creation of Sand Spots
for s in range(1000):
    saX = randint(10,1000)
    saY = randint(10,490)
    saSz = randint(1,2)
    draw_cir(saX, saY, saSz, "burlywood1","burlywood1", win)
