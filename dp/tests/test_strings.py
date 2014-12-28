from dp import strings
import unittest

class TestLongestCommonSubsequence(unittest.TestCase):
    def testEmptyStrings(self):
        actual = strings.longest_common_subsequence('','')
        self.assertEqual(actual, 0)

    def test1(self):
        actual = strings.longest_common_subsequence('abab','baba')
        self.assertEqual(actual, 3)

    def test2(self):
        actual = strings.longest_common_subsequence('xmjyaux','mzjawxu')
        self.assertEqual(actual, 4)

    def test3(self):
        actual = strings.longest_common_subsequence('cacbacabc','ccbacabdadcacba')
        self.assertEqual(actual, 8)

class TestLongestCommonSubstring(unittest.TestCase):
    def testEmptyStrings(self):
        actual = strings.longest_common_substring('','')
        self.assertEqual(actual, 0)

    def test1(self):
        actual = strings.longest_common_substring('abab','baba')
        self.assertEqual(actual, 3)

    def test2(self):
        actual = strings.longest_common_substring('xmjyaux','mzjawxu')
        self.assertEqual(actual, 1)

    def test3(self):
        actual = strings.longest_common_substring('cacbacabc','ccbacabdadcacba')
        self.assertEqual(actual, 6)
