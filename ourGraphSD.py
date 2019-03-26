from graphics import *

def draw_rect(rX, rY, rColor, sizeX, sizeY, win):
    square = Rectangle(Point(rX, rY),
                       Point(rX + sizeX, rY + sizeY))
    square.setFill(rColor)
    square.setOutline(rColor)
    square.draw(win)
    
def draw_sky(sX, sY, sizeX, sizeY, win):
    draw_rect(sX, sY, "sky blue", sizeX, sizeY, win)
    
def draw_be(bX, bY, sizeX, sizeY, win):
    draw_rect(bX, bY, "yellow", sizeX, sizeY, win)
    
def draw_h20(wX, wY, sizeX, sizeY, win):
    draw_rect(wX, wY, "blue", sizeX, sizeY, win)
    
def draw_cir(cX, cY, radius, cColor, win):
    circle = Circle(Point(cX, cY), radius)
    circle. setFill(cColor)
    circle.draw(win)
    
sqSz = 100

win = GraphWin("Let's Play Volleyball!", sqSz * 10, sqSz * 10)
win.setCoords(0,0, sqSz * 10, sqSz * 10)

draw_sky(0,0, sqSz * 10, sqSz * 10, win)
draw_h20(0,0, sqSz * 10, sqSz * 7, win)
draw_be(0,0, sqSz * 10, sqSz * 5, win)
draw_cir(sqSz/2, sqSz/4, 34, "white", win)


