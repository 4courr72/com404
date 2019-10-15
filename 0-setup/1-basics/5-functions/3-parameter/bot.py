#define a function 'escape_by' with a parameter 'plan'
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

#Call the function three times with different values for the parameter 'plan'
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")