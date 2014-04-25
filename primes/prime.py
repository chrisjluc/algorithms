""" This module contains the following algorithms for generating primes:
    - Sieves of Eratosthenes (Optimized)
    - Sieve of Atkins
"""
from math import sqrt, ceil


def eratosthenes(lim=100):
    """Implements a Genuine Sieve of Eratosthenes for primes < lim

    returns: list of primes < lim
    """

    is_prime = [True] * (lim + 1)
    sqrtn = int(round(sqrt(lim)))

    for i in xrange(2, sqrtn + 1):
        if is_prime[i]:
            for j in xrange(i ** 2, lim + 1, i):
                is_prime[j] = False

    return [i for i in xrange(len(is_prime)) if is_prime[i] and i >= 2]


def atkins(lim=100):
    """Implements a lighty optimized Sieve of Atkins for primes < lim
    This implimentation is about 3.5x slower than the sieve_of_eratosthenes.
    More optimization is needed to solve the quatratic forms and
    to enforce tighter limits on loops.

    returns: list of primes < lim"""

    is_prime = [False] * (lim + 1)
    sqrtn = int(round(sqrt(lim)))
    for i in xrange(sqrtn):
        # The following three lines are to reduce repeated calculations of x^2
        xsq = i ** 2
        x4 = 4 * xsq
        x3 = 3 * xsq
        # More work can be done to set tighter bound on loops
        for j in xrange(sqrtn):
            ysq = j ** 2
            # n = 4x^2 + y^2
            n = x4 + ysq
            if (n <= lim) and ((n % 12 == 1 or n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            # n = 3x^2 + y^2
            n = x3 + ysq
            if (n <= lim) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            # n = 3x^2 - y^2
            n = x3 - ysq
            if  (n <= lim) and (i > j) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in xrange(5, sqrtn):
        if is_prime[n]:
            kn = n ** 2
            for k in [i for i in xrange(kn, lim, kn)]:
                is_prime[k] = False

    return [2, 3] + [i for i in xrange(len(is_prime)) if is_prime[i] and i >= 5]
