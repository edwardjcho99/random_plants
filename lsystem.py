class LSystem(object):
    def __init__(self,axiom,**rules):
        self.axiom = axiom
        self.rules = rules

    def get_instructions(self,iterations):
        if iterations == 0:
            return self.axiom

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
