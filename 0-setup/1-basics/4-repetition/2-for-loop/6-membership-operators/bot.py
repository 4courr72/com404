#Ask the user for the phrase and save it in a variable 'phrase'
print("What phrase do you see?")
phrase = input()

#Then display 'Reversing...' with an empty line below and above
print("\nReversing...\n")

#The start the line of the reversed test, display 'The phrase is' and suppress the lf/cr
print("The phrase is: ",end="")

#Completely stumped how to do this other than how I did it in previuos exercise
#Will perserver or look at answers if no success
#Had a cup of tea, a tab and 20 mins watching the telly......
#[My trying continues...]Starting with a simple statement using the 'in' membership operator to just print out the phrase as is....
#for x in phrase:
#    print(x,end="")
#print()
#...which works well. Now, how do I reverse the order......????????? [and I know it is looping coz if no end="", then I get each letter on a new line]
#'print(-x)' doesn't work - tried that (get an error).

#I'm still missing something. The example had it in brackets...
for (x in phrase):
    print(x)
#Mmmm, doesnt work at all. Time for bed me thinks

#Comment 15/10/19: Answerspublished.
########Prins's answer was:

# Ask user for phrase
#print("What phrase do you see?")
#phrase = input()

# Identify markings
#print("\nReversing...\nThe phrase is", end="")

#reversed = ""

#for letter in phrase:
#    reversed = "" + reversed

#print(reversed)

#Right, lets look at this.....
#