#Set a variable for health at an initial value of 100%
health = int(100)

#Display this initial health value within a statement
print("Your health is 100%. Escape is in progress...\n")

for count in range (0,5,1):
    print("...Oh dear, who is that?")
    response = (input())
    if (response == "Smiler's Bot"):
        health = health - 20
        print("Time to jam out of here!\n")
    elif (response == "Hacker"):
        health = health + 20
        print("Yay! better follow this one!\n")
    else:
        print("Phew, just another emoji!\n")

print("Escaped! Health is", health)

