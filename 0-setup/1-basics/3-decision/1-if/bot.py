#First exercise of week 2
print("What type of book is this?")
book = input() #default is str, would use int() or float() if want a different variable
ad_book = "adventure"
print()
if (book == ad_book): #a single = assigns something to a variable, == compares
    print("I like " + book + " books!")
print()
print ("Finished reading book.")
#or I could write as:
#print("What type of book is this?")
#book = input()
#print()
#if (book == "adventure"):
#    print("I like " + book + " books!")
#print()
#print ("Finished reading book.")