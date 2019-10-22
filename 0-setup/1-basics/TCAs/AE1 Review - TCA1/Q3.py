#Asking user for miles to secret HQ (as a whole number)
print("How many miles must I travel before I reach the secret base?")
distance = int(input())

#Set up a variable to use as a counter
print("I will count the miles...")
print()
while distance > 0:
    print("I have", distance, "miles to go before I reach the base.")
    distance = distance - 1
print("""
I have arrived at the secret headquarters of the MIB!
It is time to sneak in.""")