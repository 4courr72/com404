#Ask user for the number of mountains to display
print("How many mountains should I display?")

#...and save the input inot a variable
no_of_mountains = int(input())

print("Displaying...")

#Then our for loop to display the required number of mountains
for count in range (no_of_mountains):
    print("           __")
    print("          /  \_")
    print("         /^    \ ")
    print("        /  ^    \_ ")
    print("      _/ ^ ^     ^\ ")
    print("     /  ^     ^    \ ")
print()
print("Done!")
#Comment 15/10/19: Answers published - similar but Prins used the triple "
#makes code much cleaner and then I don't need my print statement at the front of each row for the ascii art!"