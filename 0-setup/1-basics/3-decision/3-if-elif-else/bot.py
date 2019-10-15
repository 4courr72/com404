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

#Comments 08-10-19: There are no further solutions posted on SOL at this time (checked 10:40 08/10/19) and is the case across th rest of the activities this week.
#[Comments 15-10-19: Solutions there now - I note Prins's use of the \n to through a new line, also that he has one comment covering all the 4 directions statments. Otherwise pretty much the same ]