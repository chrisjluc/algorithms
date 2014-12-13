import unittest
from sorts.sorts import *

class TestSorts(unittest.TestCase):
    def setUp(self):
        self.test = [1, 3, 2, 16, 5, 4, 10,
                       100, 11, 12, 1000, 6, 
                       90, 4, 33, 5, 88]
        self.sorted = [1, 2, 3, 4, 4, 5, 5, 6,
                       10, 11, 12, 16, 33, 88,
                       90, 100, 1000]

    def test_heap_sort_lazy(self):
        self.assertEqual(heap_sort_lazy(self.test), self.sorted)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.test, 0, len(self.test)-1), self.sorted)

    def test_merge_sort_recursive(self):
        self.assertEqual(merge_sort_recursive(self.test), self.sorted)

    def test_merge_sort_iterative(self):
        self.assertEqual(merge_sort_iterative(self.test), self.sorted)
