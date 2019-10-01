#activity 8 code - beep is looking for his book!
#initial user question about where to look
print("Where should I look?")
where_to_look = input()

#decide whether looking in bedroom or not - if yes, ask a further question
if (where_to_look == "in the bedroom"):
    print("Where in the bedroom should I look?")
    where_in_bedroom = input()
elif (where_in_bedroom == "under the bed"):
        print("Found some shoes but no battery")

#gets here if anything other than 'in the bedroom'
#decide whether looking in bathroom or not - if yes, ask further question
else:
    if (where_to_look == "in the bathroom"):
        print("Where in the bathroom should I look?")
        where_in_bathroom = input()
    elif (where_in_bathroom == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")


    print("Found some mess but no battery.")
