#Asking user for how many bars to be charged
print("How many bars should be charged?")
bars_full_charge = int(input())

#Setup control variable and set to 0
bars_current_charge = 0

#Setup while loop to display bars whilst charging up to required level
while bars_current_charge < bars_full_charge:
    bars_current_charge = bars_current_charge + 1
    print("Charging:","█" * int(bars_current_charge))

print("The battery is fully charged")
#Comment 15/10/19: Answers published - same but I note I did not put line 9 in brackets after the 'while' - still worked though.