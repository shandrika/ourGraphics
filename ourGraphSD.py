from graphics import *

def draw_sky(sX, sY, color, size, win):
    square = Rectangle(Point(sX, sY),
                       Point(sX + size, sY + size))
    square.setFill(color)
    square.draw(win)

sqSz = 100

win = GraphWin("Beach", sqSz * 10, sqSz * 10)
win.setCoords(0,0, sqSz * 10, sqSz * 10)

draw_sky(sqSz, sqSz, "sky blue", sqSz * 10, win)

