import math
def e3(x):
    #calculates the largest prime factor of a number
    l = getfactors(x)
    for i in l:
        if isprime(i) == True:
            return i

def getfactors(x):
    la = []
    lb = []
    for i in range(1, math.ceil(math.sqrt(x)) + 1):
        if (x%i == 0):
            la += [x/i]
            lb += [i]
    return la + lb[::-1]

def isprime(n):
    if n == 2:
        return True
    elif n < 3:
        return False
    for x in range(3, int(n/2 +1), 1):
        if n % x == 0:
            return False
    return True
