def e2():
    #finds the sum of all even fibonacci numbers not exceeding 4,000,000
    l = [1, 1]
    s = 0
    while (l[-1] < 4000000):
        if (l[-1]%2 == 0):
            s += l[-1]
        l += [l[-1] + l[-2]]
    return s
