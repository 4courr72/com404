#Request user to type in the markings seen and save them to the variable 'markings'
print("What strange markings do you see?")
markings = input()

#Display the message 'Indentifing...' with a blank line before and after
print("\nIndentifing...\n")

#For loop to display each charactoer and the position in the list
for position in range(0, len(markings), 1):
    print("index", position, markings[position])

#Display a 'Done!' message once complete
print("\nDone!")