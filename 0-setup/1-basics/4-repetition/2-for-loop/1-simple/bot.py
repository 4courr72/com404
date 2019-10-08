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