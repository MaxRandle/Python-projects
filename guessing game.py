import random

def play():
    print("Welcome to the guessing game!\nIn this game you will try to guess a number between 1 and 128.")
    print("Type a your first guess:")
    x = random.randrange(1,128+1)
    guess = 0
    guessCount = 0
    while guess != x:
        guess = int(input())
        if guess > x:
            guessCount += 1
            print ("Too high, guess lower.")
        elif guess < x:
            guessCount += 1
            print ("Too low, guess higher.")
        else:
            guessCount += 1
            print ("Congratulations! you guessed the right number in {} tries!".format(guessCount))
    
play()
