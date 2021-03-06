import lsystem as ls
import plant, turtleSystem
import math
import graphics

win = graphics.GraphWin("Test", 400, 800)

lsystem = ls.LSystem('X',X=' F+[[X]-X]-F[-FX]+X',F='FF')
print(lsystem.get_instructions(1))
test_plant = plant.Plant(80,0.5,2,math.pi/6,lsystem,5)

test_ts = turtleSystem.TurtleSystem(test_plant,win)
test_ts.draw()

win.getMouse()
