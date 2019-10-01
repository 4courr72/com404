#Ask user for input on paint direction
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()

#If input is "up"
if (direction == "up"):
    print("I am painting in the upward direction!")

#If imput is "down"
elif (direction == "down"):
    print("I am painting in the downward direction!")

#If input is "left"
elif (direction == "left"):
    print("I am painting in the left direction!")

#The only input left (sorry :-) is "right"
else:
    print("I am painting in the right direction!")