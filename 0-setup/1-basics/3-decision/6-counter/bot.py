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
#Comment 15/10/19: Answers there now - again, method very similar but Prins uses '== 0' and I use '!= 0' with cooresponding odd and even statements switched round.
#I also note Prins uses  "There were", even_numbers, "even and", .....etc whilst I used "there were " + . I prefer Prins use of the comma as it gives a space in the output and is cleaner.