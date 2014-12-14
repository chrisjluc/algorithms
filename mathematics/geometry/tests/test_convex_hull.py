from mathematics.geometry import convex_hull
import unittest

class TestConvexHull(unittest.TestCase):
    def setUp(self):
        self.input_2d = []
        self.expected_2d = []

        with open('mathematics/geometry/tests/test_convex_hull_2d.input', 'r') as fin:
            for l in fin:
                pt = tuple(map(float, l.split()))
                self.input_2d.append(pt)

        with open('mathematics/geometry/tests/test_convex_hull_2d.expected', 'r') as fin:
            for l in fin:
                pt = tuple(map(float, l.split()))
                self.expected_2d.append(pt)

    def test_gift_wrapping_2d_empty(self):
        output = convex_hull.gift_wrapping_2d([]);
        self.assertEqual(output, [])

    def test_gift_wrapping_2d_single(self):
        output = convex_hull.gift_wrapping_2d([(0, 0)]);
        self.assertEqual(output, [(0, 0)])

    def test_gift_wrapping_2d(self):
        output = convex_hull.gift_wrapping_2d(self.input_2d)
        self.assertEqual(sorted(output), sorted(self.expected_2d))