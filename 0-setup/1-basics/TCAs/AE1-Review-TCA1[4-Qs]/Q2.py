#Ask the user a question about location of Forky and save response in a variable
print("Where is Forky?")
location = (input())

#Out depending on the user's response
if (location == "With Bonnie"):
    print("Phew! Bonnie will be happy.")

elif (location == "Running away"):
    print("Oh no! Bonnie will be upset!")

#All other responses get a seperate message
else:
    print("Ah! I better look for him")


