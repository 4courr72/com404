#A program to compare two numbers and see which is the biggest/smallest
#Asking user for the first number
print("Please enter the first number.")
first_number = int(input())

#Asking user for the second number
print("Please enter the second number.")
second_number = int(input())

#Comparing and displaying results
if (first_number < second_number):
    print("the first number is the smallest")
elif (second_number < first_number):
    print("the second number is the smallest")
else:
    print("Both are equal!")