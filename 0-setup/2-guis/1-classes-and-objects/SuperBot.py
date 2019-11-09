#import the Bot class from the relevant file
from Bot import bot

#Setup the subclass 'Superbot'
class SuperBot(bot):
    def __init__(self, name, age, energy, shield_level, super_power_level):
        super().__init__(name, age, energy, shield_level)
        self.super_power_level = super_power_level

    def get_super_power_level(self):
        return self.super_power_level

#Unsure how you would use the set method - ask Prins
    def set_super_power_level(self, super_power_level):
        self.super_power_level = super_power_level


#bot1 = SuperBot("Ross", 53, 10, 20) - part of my testing