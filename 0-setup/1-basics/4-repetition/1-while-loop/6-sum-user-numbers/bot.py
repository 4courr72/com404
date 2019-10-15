#Request user input for the quantity of numbers a user wishes to add together - store as a variable
print("How many numbers should I add up?")
quantity = int(input())

#set a control variable as 0 - used to keep track of how many numbers we have asked for a number
asked_for_so_far = 0

#set a variable to store the total
total = 0

#A while loop to keep asking for a number the required number of times
while asked_for_so_far < quantity:
    asked_for_so_far = asked_for_so_far + 1
    print("please enter number", asked_for_so_far, "of", quantity)
    total = total + int(input())

print("The answer is", total)
#Comment 15/10/19: Answers published - very similar but Prins stores the inputted number into a variable called 'Number' where as I just use the direct input
#could argee the reverse of a comment on a previuos example where mine is more efficient because I am using less memory?

