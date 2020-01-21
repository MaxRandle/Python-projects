#test death rolls

import random

def game():
    x = 0
    limit = 100
    while limit != 1:
        limit = random.randint(1, limit)
        x += 1
    return x

def test(numberOfTrials):
    first = 0
    second = 0
    for i in range(0, numberOfTrials):
        if game() % 2 == 0:
            second += 1
        else:
            first += 1
    return first, second
