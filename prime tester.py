def isprime(number):
    """
Prime numbers are only divisible by themselves and 1.
0 and 1 are not considered prime numbers.
Every non prime number can be written as a unique
combination of prime factors.
test cases
#test
>>> isprime(1)
False
>>> isprime(2)
True
>>> isprime(3)
True
>>> isprime(29)
True
>>> isprime(345)
False
>>> isprime(999979)
True
>>> isprime(999981)
False
>>> isprime(49)
False
>>> isprime(95)
False
"""
    n = abs(int(number))
    if n == 2:
        return True
    elif n < 3:
        return False
    for x in range(3, int(n/2 +1), 1):
        if n % x == 0:
            return False
    return True

import doctest
doctest.testmod()
