from dp import strings
import unittest

class TestLongestCommonSubstring(unittest.TestCase):
    def testEmptyStrings(self):
        actual = strings.longest_common_substring('','')
        self.assertEqual(actual, set())

    def test1(self):
        actual = strings.longest_common_substring('abab', 'baba')
        self.assertEqual(actual, set(['aba', 'bab']))

    def test2(self):
        actual = strings.longest_common_substring('xmjyaux', 'mzjawxu')
        self.assertEqual(actual, set(['x', 'm', 'j', 'a', 'u']))

    def test3(self):
        actual = strings.longest_common_substring('cacbacabc', 'ccbacabdadca')
        self.assertEqual(actual, set(['cbacab']))

class TestLongestCommonSubsequence(unittest.TestCase):
    def testEmptyStrings(self):
        actual = strings.longest_common_subsequence('','')
        self.assertEqual(actual, set())

    def test1(self):
        actual = strings.longest_common_subsequence('abab', 'baba')
        self.assertEqual(actual, set(['aba', 'bab']))

    def test2(self):
        actual = strings.longest_common_subsequence('xmjyaux', 'mzjawxu')
        self.assertEqual(actual, set(['mjau', 'mjax']))

    def test3(self):
        actual = strings.longest_common_subsequence('cacbacabc', 'ccbacabdadc')
        self.assertEqual(actual, set(['ccbacabc']))
