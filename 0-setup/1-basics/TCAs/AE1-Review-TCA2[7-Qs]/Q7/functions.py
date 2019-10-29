#Define the modeules for use in the main program:

#Define line under module
def line_under(word):
    print(word)
    print("*" * (len(word)))

#Define line over module
def line_over(word):
    print("*" * (len(word)))
    print(word)

#define line both over and under module
def line_both(word):
    print("*" * (len(word)))
    print(word)
    print("*" * (len(word)))

#Define grid module
def grid(word, rows, columns):
    printed_columns = columns
    while (printed_columns > 0):
        print("*" * len(word), "   ", end = "")
        printed_columns = printed_columns - 1
    printed_columns = columns
    print("\n")
    while (printed_columns > 0):
        print(word, "|", " ", end = "")
        printed_columns = printed_columns - 1
    printed_columns = columns
    while (printed_columns > 0):
        print("*" * len(word), "   ")
        printed_columns = printed_columns - 1

