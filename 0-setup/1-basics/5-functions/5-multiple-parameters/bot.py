#Define a function called climb_ladder with two parameters (for steps remaining and steps crossed)
def climb_ladder(steps_remaining,steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We made it!")

#Call the function with differing parameter values
climb_ladder(5,2)
climb_ladder(5,5)

#Note: Pointed out to Prins the numbers 2 and 5 should be other way round to get the listed display - he agreed and changed the text on the session