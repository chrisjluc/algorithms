from graphs.topological_sort import *
from graphs import util
from graphs.graph import Graph
import unittest

graph1 = Graph()
for v in [0, 1, 2, 3, 4, 5]:
    graph1.add_node(v)
graph1.add_edge(5, 2)
graph1.add_edge(5, 0)
graph1.add_edge(4, 0)
graph1.add_edge(4, 1)
graph1.add_edge(2, 3)
graph1.add_edge(3, 1)

graph2 = Graph()
for v in [5, 7, 3, 11, 8, 2, 9, 10]:
    graph2.add_node(v)
graph2.add_edge(3, 8)
graph2.add_edge(3, 10)
graph2.add_edge(5, 11)
graph2.add_edge(7, 8)
graph2.add_edge(7, 11)
graph2.add_edge(8, 9)
graph2.add_edge(11, 2)
graph2.add_edge(11, 9)
graph2.add_edge(11, 10)

class TestTopsort(unittest.TestCase):

    def test_dfs_topsort(self):
        expected1 = [5, 4, 2, 3, 1, 0]
        expected2 = [7, 5, 11, 3, 10, 8, 9, 2]

        self.assertEqual(expected1, topsort_dfs(graph1))
        self.assertEqual(expected2, topsort_dfs(graph2))
