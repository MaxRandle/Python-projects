def zeros(n):
    num5s = 0

    for i in range(1, n+1):
        num5s += n5(i, 0)

    return num5s
    
def n5(n, c):
    #reutrns the number of 5's that appear in the prime factors of n
    if n % 5 != 0:
        return c
    if n % 5 == 0:
        return n5(n/5, c+1)
        

