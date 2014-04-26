from strings.search import *
import unittest

class TestNaiveSearch(unittest.TestCase):
    def test_noOccurance(self):
        self.assertEqual(naive_search('assdf ajdsfksldjf', '123'), [])

    def test_oneOccurance(self):
        self.assertEqual(naive_search('asdf12345', '123'), [4])

    def test_multipleOccurances(self):
        self.assertEqual(naive_search('asdf asdf asdf asdf', 'df'), [2, 7, 12, 17])

class TestRabinKarp(unittest.TestCase):
    def test_noOccurance(self):
        self.assertEqual(rabin_karp('assdf ajdsfksldjf', '123'), [])

    def test_oneOccurance(self):
        self.assertEqual(rabin_karp('asdf12345', '123'), [4])

    def test_multipleOccurances(self):
        self.assertEqual(rabin_karp('asdf asdf asdf asdf', 'df'), [2, 7, 12, 17])

class TestKMP(unittest.TestCase):
    def test_noOccurance(self):
        self.assertEqual(knuth_morris_pratt('assdf ajdsfksldjf', '123'), [])

    def test_oneOccurance(self):
        self.assertEqual(knuth_morris_pratt('asdf12345', '123'), [4])

    def test_multipleOccurances(self):
        self.assertEqual(knuth_morris_pratt('asdf asdf asdf asdf', 'df'), [2, 7, 12, 17])