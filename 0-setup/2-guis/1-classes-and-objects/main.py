from Bot import bot
from SuperBot import SuperBot
from FlyingBot import FlyingBot

#An object of SuperBot class [this object is superbot1]
superbot1 = SuperBot("Dale", 47, 100, 200, 300)

#An object of bot class [this object is bot1]
bot1 = bot("Ross", 53, 10, 20)

#An object of SuperBot class [this object is superbot1]
flyingbot1 = FlyingBot("Martin", 60, 250, 35000, 400, 60)

#Set of commands to test the workings of my code
bot1.display_name()
superbot1.display_name()
bot1.display_age()
superbot1.display_age()
bot1.display_energy()
superbot1.display_energy()
#bot1.display_shield()
#bot1.display_summary()
#print(bot1)
#print(superbot1)
#superbot1.get_super_power_level()
#print(super_power_level)
print(superbot1.get_super_power_level())
print(flyingbot1.get_hover_distance())
