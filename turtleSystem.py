import turtle

class TurtleSystem(object):
    def __init__(self,plant,window):
        self.plant = plant
        self.current = turtle.Turtle(window,[200,0],plant.stalk_length,plant.thickness)
        self.turtle_stack = []

    def push(self):
        self.turtle_stack.append(self.current.copy_turtle())

    def pop(self):
        return self.turtle_stack.pop()

    def draw(self):
        for i in self.plant.get_formula():
            if i == "+":
                self.current.rotate(self.plant.delta_angle)
            elif i == "-":
                self.current.rotate(-self.plant.delta_angle)
            elif i == "F":
                self.current.move_forward()
            elif i == "[":
                self.push()
            elif i == "]":
                self.current = self.pop()
