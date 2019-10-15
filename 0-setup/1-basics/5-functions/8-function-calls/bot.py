#Define a function to display the user's inputted word inan ascii art box

def ascii_art_box(word):
    print("Performing the ascii art box function")
    #print("*" * (len(word))
    #print("*" word "*")
    #print("*" * (len(word))

def lower_case_word(word):
    print(lower(word))

def upper_case_word(word):
    print(upper(word))

def mirrored_word(word):
    print(word, "| Need to write this bit")

def repeat_word(word):
    print("How many times would you like to display your word?")
    time_repeat = int(input())

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
    if selection == "1":
        ascii_art_box(word)
    elif selection == "2":
        lower_case_word(word)
    else:
        print("end of test")

run()

