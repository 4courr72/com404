#import the Bot class from the relevant file
from SuperBot import SuperBot

#Setup the subclass 'FlyingBot'
class FlyingBot(SuperBot):
    def __init__(self, name, age, energy, shield_level, super_power_level, hover):
        super().__init__(name, age, energy, shield_level, super_power_level)
        self.hover = hover

    def get_hover_distance(self):
        return self.hover

    def set_hover_distance(self, hover):
        self.hover = hover

