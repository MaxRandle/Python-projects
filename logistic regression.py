#initial conditions
import random

def generateTestData(n):
    vmin = -4
    vmax = 4
    m = 1.5
    b = 5
    xmin = 2
    xmax = 100
    d = []
    for i in range(0, n):
        x = random.randrange(xmin, xmax)
        d += [[x, x*m + b + random.randrange(vmin, vmax)]]
    return d
        


def gd():
    dataset = generateTestData(10000)
    L = 0.0001
    m = 0
    b = 0
    for data in dataset:
        x = data[0]
        y = data[1]
        p = m * x + b
        e = y - p
        m = m + e*x*L
        b = b + e*L*10
    return "y = {}x + {}".format(round(m, 3), round(b, 3))


        
