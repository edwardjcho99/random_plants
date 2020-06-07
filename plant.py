# variables : A B
# constants : none
# axiom : A
# rules : (A → AB), (B → A)
class Plant(object):
# axiom is a string, variables are a list of strings,
# rules are a dictionary
    def __init__(self,axiom,**rules):
        self.axiom = axiom
        self.rules = rules

    def generate_instructions(self,iterations=1):
        instructions = self.axiom
        for iter in range(iterations):
            new_instructions = ""
            for i in instructions:
                if i in self.rules.keys():
                    new_instructions += self.rules[i]
                else:
                    new_instructions += i

            instructions = new_instructions
        return instructions


test_plant = Plant('X',X='F+[[X]-X]-F[-FX]+X',F='FF')
print(test_plant.generate_instructions(2))
