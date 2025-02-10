class Quack:
    def make_sound(self):
        return "Quaack"

class Squeak:
    def make_sound(self):
        return "Squeak!"

class Duck:
    def __init__(self, name, sound_made):
        self.name = name
        self.quack_behavior = sound_made

    def make_sound(self):
        return self.quack_behavior.make_sound()
