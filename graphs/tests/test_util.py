import unittest
from collections import defaultdict
from graphs import util

adjGraph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 0, 10, 0, 2, 0, 0],
    [0, 0, 0, 14, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

class TestConvertAdjToGraph(unittest.TestCase):
    def setUp(self):
        self.graph = util.convertAdjToGraph(adjGraph)

    def test_nodes(self):
        L = len(self.graph.nodes)
        self.assertEqual(L, 9)
        self.assertEqual(self.graph.nodes, set([0, 1, 2, 3, 4, 5, 6, 7, 8]))

    def test_adjNodes(self):
        dd = defaultdict(list)
        dd[0] = [1, 7]
        dd[1] = [0, 2, 7]
        dd[2] = [1, 3, 5, 8]
        dd[3] = [2, 4, 5]
        dd[4] = [3, 5]
        dd[5] = [2, 4, 6]
        dd[6] = [3, 5, 7, 8]
        dd[7] = [0, 1, 6, 8]
        dd[8] = [2, 6, 7]
        self.assertEqual(self.graph.adjNodes, dd)

    def test_weights(self):
        L = len(self.graph.nodes)
        self.assertEqual(len(self.graph.weights), 28)
        for i in range(L):
            for j in range(L):
                if adjGraph[i][j] != 0:
                    self.assertEqual(adjGraph[i][j], self.graph.weights[(i, j)])

class TestGetEdgeListFromPath(unittest.TestCase):
    def test_singleNodePath(self):
        path = ['a']
        self.assertEqual(util.getEdgeListFromPath(path), [])

    def test_multiNodePath(self):
        path = ['a', 'b', 'c', 'd', 'e']
        edgeList = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
        self.assertEqual(util.getEdgeListFromPath(path), edgeList)