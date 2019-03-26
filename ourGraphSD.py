from graphics import *

def draw_rect(rX, rY, color, sizeX, sizeY, win):
    square = Rectangle(Point(rX, rY),
                       Point(rX + sizeX, rY + sizeY))
    square.setFill(color)
    square.draw(win)

sqSz = 100

win = GraphWin("Let's Play Volleyball!", sqSz * 10, sqSz * 10)
win.setCoords(0,0, sqSz * 10, sqSz * 10)

draw_rect(sqSz * 0, sqSz * 0, "sky blue", sqSz * 10, sqSz * 10, win)

