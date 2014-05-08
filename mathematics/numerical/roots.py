"""This module contains the following root-finding algorithms. These are
algorithms that find c on [a...b] for a function f such that f(c) = 0.
    - Newton-Raphson Method
    - Bisection Method
    - Brent's Method

This module is concerned with finding scalar, real roots approximated as
floating point numbers.

Finding a root of f(x) - g(x) = 0 is the same as solving the equation
f(x) = g(x). So equation solving is the same thing as computing (or finding)
a root of a function.

References:

http://en.wikipedia.org/wiki/Root-finding_algorithm
http://en.wikipedia.org/wiki/Brent's_method"""


def newton(a, b, f, TOL=10 ** -6, NMAX=1000):
    """Newton's method assumes the function f to have a continuous derivative.
    Newton's method may not converge if started too far away from a root.
    However, when it does converge, it is faster than the bisection method,
    and is usually quadratic

    @param a - lower bound
    @param b - upper bound
    @param f - function
    @param TOL - tolerance
    @param NMAX - maximum iterations"""

    N = 0

    c = (a + b) / 2.0
    fc = f(c)

    while N <= NMAX:
        N += 1

        c = c - fc / ((f(c + TOL) - f(c)) / TOL)
        fc = f(c)

        if abs(fc) <= TOL:
            return c
    return c


def bisection(a, b, f, TOL=10 ** -6, NMAX=1000):
    """Repeatedly bisects an interval and then selects a subinterval
    in which a root must lie for further processing. It is a very
    simple and robust method.

    @param a - lower bound
    @param b - upper bound
    @param f - function
    @param TOL - tolerance
    @param NMAX - maximum iterations"""

    N = 0
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print "Function is not bracketed"
        return None

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    while N <= NMAX:
        N += 1
        c = (a + b) / 2.
        fc = f(c)

        if abs(b - a) / 2 ** N < TOL:
            return c

        if fa * fc > 0:
            a = c
            fa = fc
        else:
            b = c
            fb = fc
    return c


def brentq(a, b, f, TOL=10 ** -6, NMAX=1000):
    """Popular root-finding algorithm combining the bisection method, the
    secant method and inverse quadratic interpolation. It has the reliability
    of bisection but it can be as quick as some of the less reliable methods.

    @param a - lower bound
    @param b - upper bound
    @param f - function
    @param TOL - tolerance
    @param NMAX - maximum iterations"""

    N = 0
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print "Function is not bracketed"
        return None

    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa

    c = a
    fc = fa
    mflag = True
    s = float()
    fs = float()

    while N <= NMAX:
        N += 1

        if fa != fc and fb != fc:
            s = a * fb * fc / (fa - fb) / (fa - fc) + \
                b * fa * fc / (fb - fa) / (fb - fc) + \
                c * fa * fb / (fc - fa) / (fc - fb)
        else:
            s = b - fb * (b - a) / (fb - fa)
        t = (3 * a + b) / 4

        cond1 = (t > s and s < b) or (b > s and s < t)
        cond2 = mflag and abs(s - b) >= abs(b - c) * 0.5
        cond3 = not mflag and abs(s - b) >= abs(c - d) * 0.5
        cond4 = mflag and abs(b - c) < TOL
        cond5 = not mflag and abs(c - d) < TOL

        if not cond1 or cond2 or cond3 or cond4 or cond5:
            s = (a + b) * 0.5
            mflag = True
        else:
            mflag = False

        fs = f(s)
        d = c
        c = b
        fc = fb

        if fa * fs < 0:
            b = s
            fb = fs
        else:
            a = s
            fa = fs

        if abs(f(a)) < abs(f(b)):
            a, b = b, a
            fa, fb = fb, fa

        if abs(b - a) < TOL:
            return s
    return s
