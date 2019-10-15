#Requesting user input for a phrase or word
print("Please enter a phrase.")
phrase = input()

#create a variable to hold the results of a len against the user input
char_count = len(phrase)

#Test line whilst writing code to display current value of char_count - rem out when not needed
#print(char_count)

#Setup a control variable
char_printed_so_far = 0

while char_printed_so_far < char_count:
    print("Bop ", end="")
    char_printed_so_far = char_printed_so_far + 1

#and put a CR to get to next line at the end
print("")
#Comment 15/10/19: Answers published - although mechanics of answer is the same, I did not need to set a variable to store the les(phrase)
#I could have just tested against a lens(phrase) statement directly and got the same recult. Prins answer was thus shorter and more efficient code (i.e. used less lines and less memory?)