#Using what I have learnt in this session...
print("""Ahhh, hello earthling,
I am a new life force sent to your planet to save you from yourselves.
Do you want to help me? - Yes or No""")
help_reply = input() #Capturing this as a variable so I can do some conditional tests at a later date
print(help_reply) #Put in whilst testing
print("""To be fair, I don't care what you put,
your going to help me anyway""")
print()
print("...so I had better know your name. What is it?")
name = input()
print("Hello " + name + ", not exactly a heros name is it!")
input()
print("""Good, you're still awake and you have some functioning grey matter left.
Now, what would you like to use as your special power; invisability (use the letter 'I') or a waspish tounque and quick wittedness? (use the letter W)""")
special_power = input()
print(special_power) #Put in whilst testing
print("""How much of this power do you want? Now, remember every unit of power decreases your lifespan.
At 10 units you will live to 100, fo every unit above or below this, you will lose or gain 10 years (e.g. at 18 units you will die at 20 years old""")
power_units_initial = input()
print(power_units_initial)
print("\t\t\t\tThe current level of your special power is " + special_power * int(power_units_initial))
print()
print("Let the games begin!")
print()
print("       /")
print("      /")
print(" \   /")
print("  \ /")
print('                                .,od88888888888bo,.')
print('                             .d88888888888888888888888b.')
print('                          .d88888888888888888888888888888b.')
print('                        .d888888888888888888888888888888888b.')
print('                      .d8888888888888888888888888888888888888b.')
print('                     d88888888888888888888888888888888888888888b')
print('                    d8888888888888888888888888888888888888888888b')
print('                   d888888888888888888888888888888888888888888888')
print('                   8888888888888888888888888888888888888888888888')
print('                   8888888888888888888888888888888888888888888888')
print('                   8888888888888888888888888888888888888888888888')
print('                   Y88888888888888888888888888888888888888888888P')
print('                   "8888888888P    "Y8888888888P"    "Y888888888"')
print('                    88888888P        Y88888888P        Y88888888')
print('                    Y8888888          ]888888P          8888888P')
print('                     Y888888          d888888b          888888P')
print('                      Y88888b        d88888888b        d88888P')
print('                       Y888888b.   .d88888888888b.   .d888888')
print('                        Y8888888888888888P Y8888888888888888')
print('                         888888888888888P   Y88888888888888')
print('                         "8888888888888[     ]888888888888"')
print('                            "Y888888888888888888888888P"')
print('                                 "Y88888888888888P"')
print('                              888b  Y8888888888P  d888')
print('                              "888b              d888"')
print('                               Y888bo.        .od888P')
print('                                Y888888888888888888P')
print('                                 "Y88888888888888P"')
print('                                   "Y8888888888P"')
print('           d8888bo.                  "Y888888P"                  .od888b')
print('          888888888bo.                  """"                  .od8888888')
print('          "88888888888b.                                   .od888888888[')
print('          d8888888888888bo.                              .od888888888888')
print('        d88888888888888888888bo.                     .od8888888888888888b')
print('        ]888888888888888888888888bo.            .od8888888888888888888888b=')
print('        888888888P" "Y888888888888888bo.     .od88888888888888P" "Y888888P=')
print('         Y8888P"           "Y888888888888bd888888888888P"            "Y8P')
print('           ""                   "Y8888888888888888P"')
print('                                  .od8888888888bo.')
print('                              .od888888888888888888bo.')
print('                          .od8888888888P"  "Y8888888888bo.')
print('                       .od8888888888P"        "Y8888888888bo.')
print('                   .od88888888888P"              "Y88888888888bo.')
print('         .od888888888888888888P"                    "Y8888888888888888bo.')
print('        Y8888888888888888888P"                         "Y8888888888888888b=')
print('        888888888888888888P"                            "Y8888888888888888=')
print('         "Y888888888888888       Thomas E. Davis         "Y88888888888888P=')
print('              ""Y8888888P                                  "Y888888P"')
print('                 "Y8888P                                     Y888P"')
print('                    ""                                        """')
#Thanks to Thomas E. Davis - from the website http://ascii.co.uk/art/skull
print()
#Trying again with the triple quotes ....
print("""          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '""")
#Thanks to Unknown - from the website http://ascii.co.uk/art/skull
print()
print("""...but to make you feel at home on your planet, I will take £5 from you and triple your initial power.

...you don't have any choice in the matter by the way.""")
input()
print("""Still awake, well done!
You humans aren't as puny as you look.

Cheers for the fiver, your new power level is.....

""")
print(special_power * (int(power_units_initial + power_units_initial))) #This is not functioning as expected - did start with *3 but seems to deliver power_units_initial to the power of 3
