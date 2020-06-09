import math
from graphics import *

class Turtle(object):
    def __init__(self,position,length,angle,window):
        # position is an array [x,y]
        self.position = position
        # length of base stalk as int
        self.length = length
        # float in radians
        self.angle = angle

        self.window = window

    def rotate(self,angle):
        self.angle += angle

    def move_forward(self):
        old_x = self.position[0]
        old_y = self.position[1]
        # set x
        self.position[0] += int(self.length * math.cos(self.angle))
        # set y
        self.position[1] += int(self.length * math.sin(self.angle))

        line = Line(Point(old_x,old_y),
                    Point(self.position[0],self.position[1]))
        line.draw(self.window)

    # make a deep copy of the turtle
    def copy_turtle(self):
        return Turtle([self.position[0],self.position[1]],
                      self.length,
                      self.angle,
                      self.window)
