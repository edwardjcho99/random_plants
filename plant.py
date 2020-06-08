import math
import turtleSystem as ts
import turtle as t

class Plant(object):
    # axiom is a string
    # rules is a dictionary
    def __init__(self,axiom,window,**rules):
        self.axiom = axiom
        self.instructions = axiom
        self.rules = rules
        self.window = window

    # sets the set of instructions to draw the plant.
    # input: n = number of iterations in the L-System algorithm.
    def generate(self,n=None):
        if n is None:
            new_instructions = ""
            for i in self.instructions:
                if i in self.rules.keys():
                    new_instructions += self.rules[i]
                else:
                    new_instructions += i

            self.instructions = new_instructions
            return

        instructions = self.axiom
        for iter in range(n):
            new_instructions = ""
            for i in instructions:
                if i in self.rules.keys():
                    new_instructions += self.rules[i]
                else:
                    new_instructions += i

            instructions = new_instructions
        self.instructions = instructions

    # draws the plant using its set of instructions.
    # input: n = number of iterations in the L-System algorithm.
    def draw(self,n=None,angle=math.pi/6):
        if n is not None:
            self.generate(n)

        # create a turtle instance to draw plant
        turtleSystem = ts.TurtleSystem(t.Turtle([200,0],math.pi/2,self.window))

        for i in self.instructions:
            if i == "+":
                turtleSystem.rotate(angle)
            elif i == "-":
                turtleSystem.rotate(-angle)
            elif i == "F":
                turtleSystem.move_forward(20)
            elif i == "[":
                turtleSystem.push()
            elif i == "]":
                turtleSystem.current = turtleSystem.pop()
