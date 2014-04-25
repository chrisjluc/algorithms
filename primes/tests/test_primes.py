import unittest
from primes.prime import eratosthenes, atkins

class TestEratosthenes(unittest.TestCase):
    def setUp(self):
        """Source : http://www.miniwebtool.com/list-of-prime-numbers/?to=100"""
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                       31, 37, 41, 43, 47, 53, 59, 61, 67,
                       71, 73, 79, 83, 89, 97]

    def test_primes(self):
        self.assertEqual(eratosthenes(100), self.primes)

class TestAtkins(unittest.TestCase):
    def setUp(self):
        """Source : http://www.miniwebtool.com/list-of-prime-numbers/?to=100"""
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                       31, 37, 41, 43, 47, 53, 59, 61, 67,
                       71, 73, 79, 83, 89, 97]

    def test_primes(self):
        self.assertEqual(atkins(100), self.primes)
