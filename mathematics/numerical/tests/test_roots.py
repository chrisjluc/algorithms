import unittest
from math import cos
from mathematics.numerical.roots import newton, bisection, brentq


class TestNewton(unittest.TestCase):

    def setUp(self):
        self.f = lambda x:(x+2)*(x-6)
        self.f2 = lambda x:cos(x) -x**2
        self.TOL = 10*-5

    def test_root_2(self):
        ans = newton(-3., -1., self.f, self.TOL)
        diff = -2. - ans
        self.assertTrue(diff < self.TOL)

    def test_root_6(self):
        ans = newton(5., 7., self.f, self.TOL)
        diff = 6. - ans
        self.assertTrue(diff < self.TOL)

    def test_cosx(self):
        ans = newton(0., 1., self.f2, self.TOL)
        diff = 0.824132 - ans
        self.assertTrue(diff < self.TOL)


class TestBisect(unittest.TestCase):

    def setUp(self):
        self.f = lambda x:(x+2)*(x-6)
        self.f2 = lambda x:cos(x)-x**2
        self.TOL = 10**-5

    def test_root_2(self):
        ans = bisection(-4., -1., self.f, self.TOL)
        diff = -2. - ans
        self.assertTrue(diff < self.TOL)

    def test_root_6(self):
        ans = bisection(3., 8., self.f, self.TOL)
        diff = 6. - ans
        self.assertTrue(diff < self.TOL)

    def test_cosx(self):
        ans = bisection(0., 1., self.f2, self.TOL)
        diff = 0.824132 - ans
        self.assertTrue(diff < self.TOL)


class TestBrentq(unittest.TestCase):

    def setUp(self):
        self.f = lambda x:(x+2)*(x-6)
        self.f2 = lambda x:cos(x)-x**2
        self.TOL = 10**-5

    def test_root_2(self):
        ans = brentq(-3., -1., self.f, self.TOL)
        diff = -2. - ans
        self.assertTrue(diff < self.TOL)

    def test_root_6(self):
        ans = brentq(5., 10., self.f, self.TOL)
        diff = 6. - ans
        self.assertTrue(diff < self.TOL)

    def test_cosx(self):
        ans = brentq(0., 1., self.f2, self.TOL)
        diff = 0.824132 - ans
        self.assertTrue(diff < self.TOL)
