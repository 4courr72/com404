#Ask a question and store the user's response as a whole number in a variable
print("How many zones must I cross?")
zones = int(input())

#Display an initial message
print("Crossing zones...")

#Display zones crossed as a countdown
while (zones > 0):
    print("...crossed zone", zones)
    zones = zones - 1

print("Crossed all zones. Jumanji!")
