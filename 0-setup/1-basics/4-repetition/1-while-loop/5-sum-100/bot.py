#Display explaining what this program is doing....
print("Calculating the sum of the first 100 numbers...")

#1st variable, set to 1 (for the first number in the series) for tracking the total we are at as we increment and add up
current_total = 0


#control variable, set to 0 and used to keep a track of how many times we have gone round the loop
count = 0

#the while loop to add numbers from 1 to 100 together but also use it to supply the actual number to add
while count < 101: #Set at 101 so we include the final number '100' in our count
    current_total = current_total + count
    count = count + 1

print("...Done! The answer is", current_total)
