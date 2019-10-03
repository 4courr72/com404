#User input about what was heard
print("What did I hear?")
hear = input()

#User input about what was seen
print("What did I see?")
see = input()

#Check inputs to see if the combination of 'grrr' and 'two red eyes' was used
if (hear == "grrr") and (see == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")
