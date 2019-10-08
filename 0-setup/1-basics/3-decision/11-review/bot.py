#Task combining what learnt this week into a self designed program
#As of 12:20 08-10-19, very much a work in progress
print("Do you have a project Brief? (yes/no)")
brief = input()
if brief == ("No") or brief == ("no"):
    print("Do you have a statement of what the project is about?(yes/no)")
    statement = input()
    if statement == ("No") or statement == ("no"):
        print("Is there a project Sponsor? (yes/no)")
    sponsor = input()
else:
    if brief == ("Yes") or brief == ("yes"):
        print("Is it clear what the project is about? (yes/no)")
        clear = input()
    elif clear == ("no") or clear == ("No"):
        print("Contact the PMO and ask for further guidance.")
    else:
        Print("You can start the project.")



print("See head of PMO to get a Project Sponsor allocated")
print("Go to the next item on your 'ToDo' list.")


