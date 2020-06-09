import turtle

class TurtleSystem(object):
    # current is an instance of a Turtle
    def __init__(self,position,length,angle,window):
        self.current = turtle.Turtle(position,length,angle,window)
        self.turtle_stack = []

    def push(self):
        self.turtle_stack.append(self.current.copy_turtle())

    def pop(self):
        return self.turtle_stack.pop()

    def move_forward(self):
        self.current.move_forward()

    def rotate(self,angle):
        self.current.rotate(angle)
