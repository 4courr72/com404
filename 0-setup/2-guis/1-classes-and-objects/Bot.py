#Setup a class for bot
class bot:
    #Setup the Contructor
    def __init__(self, name, age, energy, shield_level): #attributes - they are only in the brackets if they are expected to be supplied each time
        self.name = name
        self.age = age
        self.energy = energy #Could set a number here, e.g. 'self.energy = 100'
        self.shield_level = shield_level
# I could have declared a couple of constants first, say 'MAX_ENERGY' and 'MAX_SHIELD' and then refer 'self.energy = MAX_ENERGY'. The constant would be declared after the 'class bot:' line but before the Constructor

    #Methods
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
        return("name="+self.name + ",age="+str(self.age))
        #("age="+str(self.age))
        #return("age="+str(self.age))
        #return("energy="+str(self.energy))

#An object of bot [this object is bot1]
#bot1 = bot("Ross", 53, 10, 20)


#bot1.display_name()
#bot1.display_age()
#bot1.display_energy()
#bot1.display_shield()
#bot1.display_summary()
#print(bot1)
