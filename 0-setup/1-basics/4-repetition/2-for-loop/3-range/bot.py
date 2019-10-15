#Request user input for brightness level and store it in a variable
print("What level of brightness is required?")
brightness = int(input())

#
print("Adjusting brightness...")

#
for number in range (2, brightness + 1, 2):
    print("Beep's brightness level:", "*" * number)
    print("Bop's brightness level:", "*" * number)
    print() #..to put a lf/cr in between paired statements

print("Adjustments complete!")
#Commment 15/10/19: Answers published - essentially the same, I used the less descriptive local (to the 'for' statement) variable 'number'
#Prins's answer slightly easier to follow as he used 'brightness' for the local variable.

