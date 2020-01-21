#Fermats theorem
import math
def fermat():
    for a in range(100, 1000):
        for b in range(100, 1000):
            c = round((a**2 + b**3)**(1/3), 7)
            x = math.floor(c)
            if c-x == 0.0 and c < 1000:
                print("a={} b={} c={}".format(a, b, c))
    return



