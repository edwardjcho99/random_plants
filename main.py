from graphics import *
import plant
win = GraphWin("My Plant", 400, 400)

test_plant = plant.Plant('X',win,X='F+[[X]-X]-F[-FX]+X',F='FF')
test_plant.draw(n=3)

win.getMouse()
