#Import the functions from the functions.py program
from functions import *

#Define a run module
def run():
    #Ask user for a word as save as a variable
    print("Please enter a word.")
    word = input()

    #Ask user which option they would like
    print("""
    Please select from the following options:
    1 - Display your word with a line below it
    2 - Display your word with a line above it
    3 - Display your word between two lines
    4 - Display your word in a grid of lines""")
    option = int(input())
    #For testing phase of writing the code:
    #print("Word is", word)
    #print("Option chosen is", option)
    if option == 4:
        print("How manys rows would you like?")
        rows = int(input())
        print("How many columns would you like?")
        columns = int(input())
        #For testing purposes:
        print(rows)
        print(columns)
    if option == 1:
        line_under(word)
    elif option == 2:
        line_over(word)
    elif option == 3:
        line_both(word)
    elif option == 4:
        grid(word, rows, columns)
    else:
        print("Not a valid option - please start again!")



#Run the program
run()