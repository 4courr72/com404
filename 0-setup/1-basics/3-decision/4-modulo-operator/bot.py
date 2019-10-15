#Asking for user input (an integer!)
print("Please enter a whole number.")
number = int( input() ) #To force saved input as an integer - think of it as gets input first (so inside brackets) then turns it into an integer

#Modulo 2 to see if odd or even
if (number % 2 != 0):
    print("The number " + str(number) + " is an odd number")
else:
    print("The number " + str(number) + " is an even number")
#[Comments 15-10-19: Solutions there now - I note Prins has used '== 0' and I used '!= 0' and have switched the print statements - this gives the same result
