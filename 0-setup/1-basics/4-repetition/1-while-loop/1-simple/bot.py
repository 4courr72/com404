#Asks user how many cables to remove
print("How many cables should I remove?")

#At stores the answer in the variable 'cables'
cables = int(input())

#Set a count variable ('removed_cables') to zero (Prins calls this a control variable)
removed_cables = 0

#While loop that functions whilst the number of cables removed is less than the total of cables to be removed
while (removed_cables < cables):
    removed_cables = removed_cables + 1 #Increments the cables_removed variable by one for each time round the loop
    print("Removed cable.")
#Comment 15/10/19: Answers published - same solution but I put print of removed cable after the increment line (line 12)

