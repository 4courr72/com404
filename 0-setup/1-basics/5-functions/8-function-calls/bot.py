#Define a function to display the user's inputted word in an ascii art box

def ascii_art_box(word):
    print("Performing the ascii art box function") #Inserted whilst testing
    length = len(word)
    print("*" * (length + 4))
    print("*", word, "*")
    print("*" * (length + 4))
    #print(length) - used this during testing

def lower_case_word(word):
#    print(lower(word)) - my origianl statement that didnt work
    print(word.lower())

def upper_case_word(word):
    print(word.upper())

def mirrored_word(word):
    print(word, "| Need to write this bit")

def repeat_word(word):
    print("How many times would you like to print your word?")
    times_to_repeat = int(input())
    print(word * times_to_repeat)

def run():
    print("What is your word?")
    word = input()
    print("""
    Which option would you like? The options are:

    1) Display in a Box
    2) Display in Lower-case
    3) Display in Upper-case
    4) Display your word and then with it mirrored
    5) Repeat your word (you will be asked how many times) - they will be displayed in alternate upper and lower case

    Please type the number corresponding to your selection.""")
    selection = int(input())
    print(selection) #Put in for testing
    if selection == 1:
        print("We are going to option 1")
        ascii_art_box(word)
    elif selection == 2:
        print("We are going to option 2")
        lower_case_word(word)
    elif selection == 3:
        print("We are going to option 3")
        upper_case_word(word)
    elif selection == 4:
        print("We are going to option 4")
        mirrored_word(word)
    elif selection == 5:
        print("We are going to option 5")
        repeat_word(word)
    else:
        print("end of test") #Used whilst building to test functionality

run()

