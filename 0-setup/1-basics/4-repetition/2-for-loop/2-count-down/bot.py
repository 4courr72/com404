#Request user input for distance from the cave and store in a variable
print("How far are we from the cave?")
distance = int(input())

#and create a variable to use as a check
steps_to_go = distance

#Put in a new line for spacing
print()

#Now a for loop to display and count down the steps - did this to preserve the origanl input
for count in range (distance):
    print(steps_to_go, "steps remaining")
    steps_to_go = steps_to_go - 1

print()
print("We have reached the cave!")
#Commment 15/10/19: Answers published - I did it a long winded way and should have used the 'for count in range(distance, 0, -1):' statement
#to make it slicker.  ended up using a decrement statement (line 14) to acheive the same effect.