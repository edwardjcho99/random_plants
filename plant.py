class Plant(object):
    def __init__(self,stalk_length,stalk_multiplier,thickness,delta_angle,lsystem,iterations):
        self.stalk_length = stalk_length
        self.stalk_multiplier = stalk_multiplier
        self.thickness = thickness
        self.delta_angle = delta_angle
        self.lsystem = lsystem
        self.iterations = iterations

        self.stalk_length *= 0.5**self.iterations

    def get_formula(self):
        return self.lsystem.get_instructions(self.iterations)
