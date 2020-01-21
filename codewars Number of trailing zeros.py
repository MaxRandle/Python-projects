def zeros(n):
    num5s = 0
    num2s = 0
    for i in range(1, n+1):
        num5s += n5(i, 0)
        num2s += n2(i, 0)
        
    return min(num5s, num2s)
    
def n5(n, c):
    #reutrns the number of 5's that appear in the prime factors of n
    if n % 5 != 0:
        return c
    if n % 5 == 0:
        return n5(n/5, c+1)
        
def n2(n, c):
    #reutrns the number of 2's that appear in the prime factors of n
    if n % 2 != 0:
        return c
    if n % 2 == 0:
        return n2(n/2, c+1)
