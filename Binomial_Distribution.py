#binomial distribution
#X~B(n,p) P(x) = nCx * p^x * (1-p)^(n-x)



def binrange(n, p, xlow, xhigh):
    xsum = 0
    for i in range(xlow, xhigh+1):
        xsum += binomial(n, p, i)
    return xsum

def binomial(n, p, x):
    return c(n, x) * p**x * (1-p)**(n-x)

def c(n, r):
    #combination
    return f(n)/(f(n-r)*f(r))

def f(n):
    #factorial
    x = 1;
    for i in range(2, n+1):
        x *= i
    return x

def e(n, p):
    #expected
    return n*p

def sd(n, p):
    #standard deviation
    return (n*p*(1-p))**0.5
