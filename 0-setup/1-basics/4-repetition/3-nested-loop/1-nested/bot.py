#Ask user how many rows to have and saves at the interger variable 'rows'
print("How many rows should I have?")
rows = int(input())

#Ask user how many columns to have and saves as the interger 'columns' (and add a clear line after the user input)
print("\nHow many columns should I have?")
columns = int(input())

#Insert the line 'Here I go:' after the last user input with a clear line before and after
print("\nHere I go:\n")

# nested loop with outer dealing with the number of rows and an inner loop dealing with the number of columns, suppressing the lf/cr inherited from the print statement
for count in range(0,rows,1):
    for count in range(0,columns,1):
        print(":-) ",end="")
    print()

#Once all loops have completed, display 'Done!' (with a clear line after the printed smileys)
print("\nDone!")

