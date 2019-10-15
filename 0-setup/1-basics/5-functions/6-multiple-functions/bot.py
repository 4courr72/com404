#Define function 'display_ladder' with one parameter 'steps' - this discplays a rung for every value of the parameter 'steps'
def display_ladder(steps):
    print("""| |
***
""" * steps)

#Define function 'create_ladder' with no parameters
def create_ladder():
    print("How many steps remain?")
    steps_remain = int(input())
    print()
    display_ladder(steps_remain)

create_ladder()

