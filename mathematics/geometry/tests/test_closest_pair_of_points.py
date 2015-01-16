from mathematics.geometry import closest_pair_of_points
import unittest

class TestClosestPairOfPoints(unittest.TestCase):

    def test_2_points(self):
        P = [(0, 1), (2, 0)]
        actual = closest_pair_of_points.closest_pair_of_points(P)
        self.assertTrue((0, 1) in actual)
        self.assertTrue((2, 0) in actual)

    def test_3_points(self):
        P = [(0, 1), (2, 0), (1, 1)]
        actual = closest_pair_of_points.closest_pair_of_points(P)
        self.assertTrue((0, 1) in actual)
        self.assertTrue((1, 1) in actual)

    def test_vertical_points(self):
        P = [(0, 1), (0, 7), (0, 0), (0, 4), (0, 9)]
        actual = closest_pair_of_points.closest_pair_of_points(P)
        self.assertTrue((0, 0) in actual)
        self.assertTrue((0, 1) in actual)

    def test_vertical_points(self):
        P = [(1, 0), (7, 0), (0, 0), (4, 0), (9, 0)]
        actual = closest_pair_of_points.closest_pair_of_points(P)
        self.assertTrue((1, 0) in actual)
        self.assertTrue((0, 0) in actual)


    def test_alot_of_points(self):
        P = [(5, 0), (0, 1), (2, 0), (1, 1), (-1, 3), (0, 4), (4, 6), (4, 4), (4, 8), (3, 3), (-1, 7)]
        actual = closest_pair_of_points.closest_pair_of_points(P)
        self.assertTrue((0, 1) in actual)
        self.assertTrue((1, 1) in actual)
