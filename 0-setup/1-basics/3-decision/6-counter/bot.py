#A program to count how many odd and evn numbers out of a list of three
print("Please enter the first whole number.")
first_number = int(input())

print("Please enter the second whole number.")
second_number = int(input())

print("Please enter the third whole number.")
third_number = int(input())

#Setting up a counter for odd and even numbers, set them to zero
odd_counter = 0
even_counter = 0

if (first_number % 2 != 0):
    odd_counter = odd_counter + 1
else:
    even_counter = even_counter + 1

if (second_number % 2 != 0):
    odd_counter = odd_counter + 1
else:
    even_counter = even_counter + 1

if (third_number % 2 != 0):
    odd_counter = odd_counter + 1
else:
    even_counter = even_counter + 1

#Used whilst testing: print(odd_counter)
#Used whilst testing: print(even_counter)

print("There were " + str(even_counter) + " even and " + str(odd_counter) + " odd numbers.")
