""" This module contrains the following algorithms for generating primes:
    - Sieves of Eratosthenes (Optimized)
    - Sieve of Atkins
"""
from math import sqrt

def sieve_of_eratosthenes(lim=100):
    """Implements a Genuine Sieve of Eratosthenes for primes < lim
    this will easily generate primes less than 10M in around 2.5 seconds

    returns: list of primes < lim
    """

    is_prime = [True]*(lim+1)
    sqrtn = int(round(sqrt(lim)))

    for i in xrange(2, sqrtn+1):
        if is_prime[i]:
            for j in xrange(i**2, lim+1, i):
                is_prime[j] = False

    return [i for i in xrange(len(is_prime)) if is_prime[i] and i >= 2]

def sieve_of_atkins(lim=100):
    """Implements a lighty optimized Sieve of Atkins for primes < lim
    This implimentation is about 3.5x slower than the sieve_of_eratosthenes.
    More optimization is needed to solve the quatratic forms and
    to enforce tighter limits on loops.

    returns: list of primes < lim"""

    is_prime = [False]*(lim+1)
    sqrtn = int(round(sqrt(lim)))
    for i in xrange(sqrtn+1):
        # The following three lines are to reduce repeated calculations of x^2
        xsq = i**2
        x4 = 4*xsq
        x3 = 3*xsq
        # More work can be done to set tighter bound on loops
        for j in xrange(sqrtn+1):
            ysq = j**2
            # n = 4x^2 + y^2
            n = x4 + ysq
            if (n<=lim) and ((n%12==1) or (n%12==5)):
                is_prime[n] = True
            # n = 3x^2 + y^2
            n = x3 + ysq
            if (n<=lim) and (n%12==7):
                is_prime[n] = True
            # n = 3x^2 - y^2
            n = x3 - ysq
            if (i>j) and (n<=lim) and (n%12==11):
                is_prime[n] = True

    for n in xrange(5, int(round(lim))):
        if is_prime[n]:
            kn = n**2
            for k in [i*kn for i in range(1,(lim/n**2+1))]:
                is_prime[k] = False

    return [2, 3]+[i for i in xrange(len(is_prime)) if is_prime[i] and i>=5]

def main():
    import time
    n = 1000000
    start = time.time()
    sieve_of_eratosthenes(lim=n)
    print "Sieve of Eratosthenese: ", time.time()-start

    start = time.time()
    sieve_of_atkins(n)
    print "Sieve of Atkins: ", time.time()-start

if __name__ == "__main__":
    import sys
    sys.exit(main())
