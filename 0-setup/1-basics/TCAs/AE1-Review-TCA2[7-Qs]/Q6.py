#Define a function with 2 parameters
def is_league_united(first_hero,second_hero):
    if (first_hero == "Superman" and second_hero == "Wonder Woman") or (first_hero == "Wonder Woman" and second_hero == "Superman"):
        return True
    else:
        return False

def decide_plan(first_hero,second_hero):
    united = is_league_united(first_hero,second_hero) #I need to assign a variable to the result of calling the function (otherwise I will lose the results!)
    if united == True:
        print("Time to save the world!")
    else:
        print("We must unite the league!")

def run():
    print("Please enter your 1st hero's name")
    first_hero = input()
    print("Please enter your 2nd hero's name.")
    second_hero = input()

    print("do you want 'league' or 'plan'?")
    league_or_plan = input()

    if (league_or_plan == "league"):
        result = is_league_united(first_hero,second_hero)
        print(result)
    elif (league_or_plan == "plan"):
        decide_plan(first_hero,second_hero)
    else:
        print("Invalid command. Please try again")

run()