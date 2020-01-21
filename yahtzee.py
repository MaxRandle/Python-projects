import random
def yahtzee():
    """returns the number of rolls before a yahtzee is thrown"""
    count = 0
    yahtzee = False
    while yahtzee == False:
        count += 1
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        roll3 = random.randint(1,6)
        roll4 = random.randint(1,6)
        roll5 = random.randint(1,6)
        roll6 = random.randint(1,6)
        if roll1 == roll2 == roll3 == roll4 == roll5 == roll6:
            yahtzee = True
    return count

def mad_dice(number_of_dice, number_of_rolls):
    totals = {}
    for number in range(1*number_of_dice, 6*number_of_dice+1):
        totals[number] = 0
        
    for x in range(0, number_of_rolls):
        total = 0
        for number in range(0, number_of_dice):
            total += random.randint(1,6)
        totals[total] += 1

    for number in range(1*number_of_dice, 6*number_of_dice+1):
        print("The value", number, "occurred", totals[number], "times.")
    maximum_number = 0
    maximum_value = 0
    for x in range(1*number_of_dice, 6*number_of_dice+1):
        if totals[x] > maximum_number:
                   maximum_number = totals[x]
                   maximum_value = x
    print("The most commonly occurring total was", maximum_value, "occurring", maximum_number, "times.")
