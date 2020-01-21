#test the best way to stake in RS
""""the aim is to see how many stakes each strategy takes to double your money
or become bankrupt"""
#Wins double money

import random


winRate = 0.5

def betWin():
    if random.randint(0, 1) > winRate:
        return True
    return False

#double up
"""each time you lose, you put in double your last bet"""

#Pros:
#each win covers ALL previous consecutive losses

#cons:
#slow at making money.
#can get streaked log2(n) times to become bankrupt.
#increasing the bet also decreaces the size of a loss streak to bankrupt

def doubleUp():
    cash = 1024
    bet = 1
    #print("bet 0:", cash)
    betCount = 1
    while (cash < 2048) and (cash > bet):
        if betWin() == True:
            cash += bet
            #print("bet {}:".format(betCount), cash, "won {}".format(bet))
            bet = 1
        else:
            cash -= bet
            #print("bet {}:".format(betCount), cash, "lost {}".format(bet))
            bet *= 2
        betCount += 1
    return cash


def doubleUpTest(x):
    win = 0
    loss = 0
    for i in range(0, x):
        if doubleUp() == 2048:
            win += 1
        else:
            loss += 1
    print("Wins: {}, Losses: {}, ratio: {}".format(win, loss, win/(win+loss)))

#half up
"""You always bet half your cash pool"""

#Pros:
#Fast at making money on win streaks.
#Will never go bankrupt.

#Cons:
#Need to win 1.5 times to recoup a loss.

def halfUp():
    cash = 1024
    #print(cash)
    while (cash < 2048) and (cash > 0.1):
        bet = cash/2
        if betWin() == True:
            cash += bet
        else:
            cash -= bet
        #print(round(cash, 3))
    return cash

def halfUpTest(x):
    wins = 0
    losses = 0
    for i in range(0, x):
        if halfUp() >= 2048:
            wins += 1
        else:
            losses += 1
    print("Wins: {}, Losses: {}, ratio: {}".format(wins, losses, wins/(wins+losses)))
    


#3 and 3

def threeThree():
    cash = 1024
    consecWins = 0
    consecLosses = 0
    bet = 10
    while (cash > bet) and (cash < 1998):
        if betWin() == True:
            cash += bet
            consecLosses = 0
            consecWins += 1
        else:
            cash -= bet
            consecWins = 0
            consecLosses += 1
        if consecWins == 3:
            bet = 100
        if consecLosses == 3:
            bet = 10
    return cash

def threeThreeTest(x):
    wins = 0
    losses = 0
    for i in range(0, x):
        if threeThree() >= 1998:
            wins += 1
        else:
            losses += 1
    print("Wins: {}, Losses: {}, ratio: {}".format(wins, losses, wins/(wins+losses)))
    

#constant bet
"""Bet the same amount each time"""


