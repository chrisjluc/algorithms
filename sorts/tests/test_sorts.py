import unittest
from sorts.sorts import *

class TestSorts(unittest.TestCase):
    def setUp(self):
        self.testOne = [1]
        self.sortedOne = [1]

        self.testSame = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.sortedSame = [1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.testMany = [1, 3, 2, 16, 5, 4, 10,
                       100, 11, 12, 1000, 6, 
                       90, 4, 33, 5, 88]
        self.sortedMany = [1, 2, 3, 4, 4, 5, 5, 6,
                       10, 11, 12, 16, 33, 88,
                       90, 100, 1000]

    def test_heap_sort_lazy(self):
        self.assertEqual(heap_sort_lazy(self.testMany), self.sortedMany)
        self.assertEqual(heap_sort_lazy(self.testSame), self.sortedSame)
        self.assertEqual(heap_sort_lazy(self.testOne), self.sortedOne)
        self.assertEqual(heap_sort_lazy([]), [])


    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.testMany, 0, len(self.testMany)-1), self.sortedMany)
        self.assertEqual(quick_sort(self.testSame, 0, len(self.testSame)-1), self.sortedSame)
        self.assertEqual(quick_sort(self.testOne, 0, len(self.testOne)-1), self.sortedOne)
        self.assertEqual(quick_sort([], 0, 0), [])


    def test_merge_sort_recursive(self):
        self.assertEqual(merge_sort_recursive(self.testMany), self.sortedMany)
        self.assertEqual(merge_sort_recursive(self.testSame), self.sortedSame)
        self.assertEqual(merge_sort_recursive(self.testOne), self.sortedOne)
        self.assertEqual(merge_sort_recursive([]), [])


    def test_merge_sort_iterative(self):
        self.assertEqual(merge_sort_iterative(self.testMany), self.sortedMany)
        self.assertEqual(merge_sort_iterative(self.testSame), self.sortedSame)
        self.assertEqual(merge_sort_iterative(self.testOne), self.sortedOne)
        self.assertEqual(merge_sort_iterative([]), [])

