#define a function for items in a suitcase
def item_from_suitcase(item):
    print("I wonder what is in my suitcase...")
    if (item == "toothbrush"):
        print("A toothbrush. Well, got to have clean teeth!\n")
    elif (item == "spidey suit"):
        print("My Spidey suit! Won't be needing this. I am on holiday.\n")
    else:

        print("An unexpected item! It could be useful.\n")

item_from_suitcase("toothbrush")
item_from_suitcase("belt")
item_from_suitcase("spidey suit")
