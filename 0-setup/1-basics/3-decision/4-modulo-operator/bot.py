#Asking for user input (an integer!)
print("Please enter a whole number.")
number = int( input() )
if (number % 2 != 0):
    print("The number " + str(number) + " is an odd number")
else:
    print("The number " + str(number) + " is an even number")

