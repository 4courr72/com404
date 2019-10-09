#Ask the user for the phrase and save it n a variable 'phrase'
print("What phrase do you see?")
phrase = input()

#Then display 'Reversing...' with an empty line below and above
print("\nReversing...\n")

#The start the line of the reversed test, display 'The phrase is' and suppress the lf/cr
print("The phrase is: ",end="")

#FOR loop to display the inputted phrase backwards - supress lf/cr so each letter is displayed next to each on the same line
for position in range(len(phrase)-1, -1, -1):
    print(phrase[position], end="")

#Once FOR loop complete, display 'Done!' with a clear line before. An additional new line to cope with the suppression of lf/cr from FOR loop
print("\n\nDone!")
