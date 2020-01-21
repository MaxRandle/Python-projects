import math
def e1():
    #calculates the sum of all multiples of 3 and 5 below 1000
    s = 0
    for i in range(0, math.ceil(1000/5)):
        s += i*5
    for i in range(0, math.ceil(1000/3)):
        if (i*3)%5 != 0:
            s += i*3
    return s

#alternative
def a1(r, a, b, c):
    """how many numbers from 1 to r are divisible by a, b, or c?"""
    #|AuBuC| = |A| + |A| + |C| - |AnB| - |AnC| - |BnC| + |AnBnC|
    A = []
    B = []
    C = []
    AnB = []
    AnC = []
    BnC = []
    AnBnC = []
    for i in range(1, r+1):
        if i%a == 0:
            A += [i]
        if i%b == 0:
            B += [i]
        if i%c == 0:
            C += [i]
        if i%(a*b) == 0:
            AnB += [i]
        if i%(a*c) == 0:
            AnC += [i]
        if i%(b*c) == 0:
            BnC += [i]
        if i%(a*b*c) == 0:
            AnBnC += [i]
    return len(A) + len(B) + len(C) - len(AnB) - len(AnC) - len(BnC) + len(AnBnC)
            
