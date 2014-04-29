"""This module contains the following Discrete Fourier Transform algorithms:
    - DTF (Loops) - O(N^2)
    - Cooley-Tukey - O(NlogN)

    A Fourier Transform converts the sampled function from its original domain
    (often time or position along a line) to the frequency domain.

    References:

    http://en.wikipedia.org/wiki/Discrete_Fourier_transform#Spectral_analysis
    http://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/"""


from cmath import exp, pi


def dft(x):
    """Discrete Fourier Transform

    @params x - signal"""

    N = len(x)
    result = [complex()] * (N)
    for k in xrange(N):
        Xk = complex()
        for n in xrange(N):
            Xk += x[n] * exp(-2j * pi * n * k / N)
        result[k] = Xk
    return result


def cooley_tukey_FFT(x):
    """Implements the Cooley-Tukey Fast Fourier Transform

    @params x - signal with length that is a power of two"""
    
    N = len(x)
    if N % 2 > 0:
        print "x must be a power of 2"
    elif N <= 8:
        return dft(x)
    else:
        X_even = cooley_tukey_FFT(x[::2])
        X_odd = cooley_tukey_FFT(x[1::2])
        X = [0] * N
        for k in xrange(N / 2):
            twiddle = exp(-2j * pi * k / N)
            X[k] = X_even[k] + twiddle * X_odd[k]
            X[k + N / 2] = X_even[k] - twiddle * X_odd[k]
        return X
