# variables : A B
# constants : none
# axiom : A
# rules : (A → AB), (B → A)
class Plant(object):
# axiom is a string, variables are a list of strings,
# rules are a dictionary
    def __init__(self,axiom,**rules):
        self.instructions = axiom
        self.rules = rules

    def generate(self,iterations=1):
        for iter in range(iterations):
            new_instructions = ""
            for i in self.instructions:
                if i in self.rules.keys():
                    new_instructions += self.rules[i]
                else:
                    new_instructions += i

            self.instructions = new_instructions


test_plant = Plant('A',A='AB',B='A')
test_plant.generate(5)
