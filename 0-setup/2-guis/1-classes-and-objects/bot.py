#Setup a class for bot
class bot:
    def __init__(self, name, age, energy, shield_level):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield_level = shield_level

    def display_name(self):
        print("*" * len(name))
        print("*" + name + "*")
        print("*" * len(name))

bot1 = bot(Ross, 53, 10, 20)
display_name(bot1)