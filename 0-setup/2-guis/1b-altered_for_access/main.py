from Bot import bot
from SuperBot import SuperBot
from FlyingBot import FlyingBot

#An object of SuperBot class [this object is superbot1]
superbot1 = SuperBot("Dale", 47, 100, 200, 300)

#An object of bot class [this object is bot1]
bot1 = bot("Ross", 53, 10, 20)

#An object of SuperBot class [this object is superbot1]
flyingbot1 = FlyingBot("Martin", 60, 250, 35000, 400, 80)

#Set of commands to test the workings of my code
bot1.display_name()
superbot1.display_name()
flyingbot1.display_name()
bot1.display_age()
superbot1.display_age()
flyingbot1.display_age()
bot1.display_energy()
superbot1.display_energy()
bot1.display_shield()
superbot1.display_shield()
bot1.display_summary()
superbot1.display_summary()
flyingbot1.display_summary()
#print(bot1)
#print(superbot1)
#superbot1.get_super_power_level()
#print(super_power_level)
print(superbot1.get_super_power_level())
print(flyingbot1.get_hover_distance())
bot1.decrement_energy()
bot1.display_energy()
bot1.decrement_shield()
bot1.display_shield()
bot1.increment_energy()
bot1.display_energy()
bot1.increment_shield()
bot1.display_shield()
bot1.increment_age()
bot1.display_age()
print(bot1.get_age())
print(superbot1.get_age())
print(flyingbot1.get_age())
print(bot1.get_name())
print(superbot1.get_name())
print(flyingbot1.get_name())
print(bot1.get_energy())
print(superbot1.get_energy())
print(flyingbot1.get_energy())
print(bot1.get_shield())
print(superbot1.get_shield())
print(flyingbot1.get_shield())