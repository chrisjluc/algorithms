from graphs.shortest_paths import *
from graphs import util
import unittest

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

shortestPathsFrom0 = {
	0: 0, 
	1: 4, 
	2: 12, 
	3: 19, 
	4: 21, 
	5: 11, 
	6: 9, 
	7: 8, 
	8: 14
}

class TestDijkstrasAlgorithm(unittest.TestCase):
	def setUp(self):
		self.graph = util.convertAdjToGraph(adjGraph)

	def test_lengths(self):
		(lengths, prev) = dijkstra(self.graph, 0)
		self.assertEqual(lengths, shortestPathsFrom0)

	def test_path(self):
		(lengths, prev) = dijkstra(self.graph, 0)
		self.assertEqual(util.getPathFromPrev(prev, 8), [0, 1, 2])

class TestBellmanFord(unittest.TestCase):
	def setUp(self):
		self.graph = util.convertAdjToGraph(adjGraph)

	def test_lengths(self):
		(lengths, prev) = bellmanFord(self.graph, 0)
		self.assertEqual(lengths, shortestPathsFrom0)

	def test_path(self):
		(lengths, prev) = bellmanFord(self.graph, 0)
		self.assertEqual(util.getPathFromPrev(prev, 8), [0, 1, 2])

class TestFloydWarshall(unittest.TestCase):
	def setUp(self):
		self.graph = util.convertAdjToGraph(adjGraph)

	def test_lengths(self):
		lengths = floydWarshall(self.graph)
		l0 = {i: lengths[0][i] for i in range(9)}
		self.assertEqual(l0, shortestPathsFrom0)