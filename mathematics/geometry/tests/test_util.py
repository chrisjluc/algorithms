from mathematics.geometry import util
import unittest

class TestUtil(unittest.TestCase):

    def test_dist_same_point(self):
        a = (5, 9)
        b = (5, 9)
        self.assertEqual(util.dist_squared(a, b), 0)

    def test_dist_case_1(self):
        a = (7, 2)
        b = (81, 19)
        expected = 5765
        self.assertEqual(util.dist_squared(a, b), expected)

    def test_dist_case_2(self):
        a = (99, 9)
        b = (1027, -12)
        expected = 861625
        self.assertEqual(util.dist_squared(a, b), expected)

    def test_dist_3d(self):
        a = (1, 8, -2)
        b = (-12, 3, -1)
        expected = 195
        self.assertEqual(util.dist_squared(a, b), expected)
