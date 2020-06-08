import turtle

class TurtleSystem(object):
    # current is an instance of a Turtle
    def __init__(self,current):
        self.current = current
        self.turtle_stack = []

    def push(self):
        self.turtle_stack.append(self.current.copy_turtle())

    def pop(self):
        return self.turtle_stack.pop()

    def move_forward(self,distance):
        self.current.move_forward(distance)

    def rotate(self,angle):
        self.current.rotate(angle)
