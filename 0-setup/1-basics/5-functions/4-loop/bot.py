#Define a function 'cross_bridge' with a parameter for the distance of the bridge crossed in steps (I will call this 'steps')
def cross_bridge(steps):
    steps_to_go = steps

    #Print a message for each step
    for count in range (steps):
        print("Crossed step.")
        count = count - 1

    #Check whether steps is more than 5 so a warning message can be displayed first, if less a different message is displayed
    if steps > 5:
        print("The bridge is collapsig!")
    else:
        print("We must keep going!")

#Call the function with parameters eaither side of the 5 step mark
cross_bridge(3)
cross_bridge(6)


