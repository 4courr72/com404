#Define the function 'identify' with no parameters
def identify():
    print("What lies before us?")
    what_we_see = input()

#Two screen outputs depending on the entered text
    if what_we_see == "a large boulder":
        print("It's time to run!")
    else:
        print("we will be fine")

#Call the function 'identify' with no parameters
identify()