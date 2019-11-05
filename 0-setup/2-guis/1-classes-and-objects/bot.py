#Setup a class for bot
class bot:
    def __init__(self, name, age, energy, shield_level):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield_level = shield_level

    def display_name(self):
        print("*" * len(self.name) + "**")
        print("*" + self.name + "*")
        print("*" * len(self.name) + "**")

    def display_age(self):
        print(self.age)
        print("     $  $")
        print("     |  |")
        print("   ********")
        print("  **********")
        print(" {  You are }")
        print(" {   ", self.age, "   }")
        print("  **********")
        print("    I    I")
        print("----------------")

    def display_energy(self):
        print("█" * self.energy)

    def display_shield(self):
        print("__________")
        print("| Shield:|")
        print("|   ", self.shield_level, " |")
        print(" \      /")
        print("  \    /")
        print("   \  /")
        print("    VV")

    def display_summary(self):
        bot1.display_name()
        bot1.display_energy()
        bot1.display_shield()

    def __str__(self):
        return("name="+self.name), ("age="+str(self.age))
        #return("age="+str(self.age))
        #return("energy="+str(self.energy))


bot1 = bot("Ross", 53, 10, 20)
#bot1.display_name()
#bot1.display_age()
#bot1.display_energy()
#bot1.display_shield()
#bot1.display_summary()
print(bot1)
