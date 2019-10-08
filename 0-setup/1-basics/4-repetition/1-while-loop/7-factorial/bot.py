#Requesting user input for a number to factorialise (is that a word?)
print("Please enter a number:")
number = int(input())

#set a variable to be one - we will use this to provide the first number of the factorial and to check when we have reached the inputted number
start = 1

#Set another variable for a running total and set at zero
total = 0

#then a final variable as a tempory location for each interation factor result
result = 1

#a while loop to factor the nubers up to the inputted number
while start < number:
    result = result * (start + 1)
    start = start + 1
    total = total + result

print("The facorial is", result)