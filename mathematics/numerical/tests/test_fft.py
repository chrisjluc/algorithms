import unittest
from mathematics.numerical.fft import dft, cooley_tukey_fft
from random import random
from numpy import fft


class TestDFT(unittest.TestCase):

    def setUp(self):
        self.success = lambda x, y: sum(
            (x[i] - y[i]) ** 2 for i in xrange(len(x)))
        self.test = [random() for _ in xrange(256)]

    def test_loops_dft(self):
        ans = dft(self.test)
        compare = fft.fft(self.test)
        self.assertLess(self.success(ans, compare), 10 ** -7)


class TestArrays(unittest.TestCase):
x
    def setUp(self):
        self.success = lambda x, y: sum(
            (x[i] - y[i]) ** 2 for i in xrange(len(x)))
        self.test = [random() for _ in xrange(256)]

    def test_loops_dft(self):
        ans = cooley_tukey_fft(self.test)
        compare = fft.fft(self.test)
        self.assertLess(self.success(ans, compare), 10 ** -7)
