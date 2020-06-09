import math
from graphics import *

class Turtle(object):
    def __init__(self,window,position,length,width,angle=math.pi/2):
        self.window = window
        self.position = position
        self.length = length
        self.width = width
        self.angle = angle

    def rotate(self,delta_angle):
        self.angle += delta_angle

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
        return Turtle(self.window,
                      [self.position[0],self.position[1]],
                      self.length,
                      self.width,
                      self.angle)
