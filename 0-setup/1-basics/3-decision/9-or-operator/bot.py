#Beep goes on an adventure :-)
#Asking what type of route to take
print("What type of adventure should I have?")
adventure = input()

#Checking whether route is scary or short...if yes then display comment 1
if ((adventure == "scary") or (adventure =="short")):
    print("Entering the dark forest!.")

#Then checking to see if safe or long...if yes then display comment 2
else:
    if ((adventure == "safe") or (adventure == "long")):
        print("Taking the safe route!.")

    #For any other input display comment 3
    else:
        print("Not sure which route to take." )