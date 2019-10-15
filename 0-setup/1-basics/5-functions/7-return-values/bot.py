#Define a function 'sum_weights' with 2 parameters for weight of each bot
def sum_weights(bop_weight, beep_weight):
    total_weight = (bop_weight + beep_weight)
    return total_weight

#define a function 'calc_avg_weight with 2 parameters for weight of each bot (so use same parameters as before?)
def calc_avg_weight(bop_weight, beep_weight):
    ave_weights = (sum_weights(bop_weight, beep_weight)/2)
    return ave_weights

#Define a function 'run' with no parameters but asks for the weights of each bot and whether to sum or average those weights
def run():
    print("What is the weight of Beep?")
    beep_weight = int(input())

    print("\nWhat is the weight of Bop?")
    bop_weight = int(input())

    print("What would you like to calculate (sum or average)?")
    sum_or_average = input()

    if sum_or_average == "sum":
        print("The sum of Beep and Bop's weight is", sum_weights(beep_weight, bop_weight))
    elif sum_or_average == "average":
        print("The average of Beep and Bop's weight is", calc_avg_weight(beep_weight, bop_weight))

run()
