import unittest
from graphs.maximum_flow import *
from graphs import util

# Graph from http://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm.
graph1 = Graph()
for v in "sopqrt":
    graph1.addNode(v)
graph1.addEdge('s', 'o', 3)
graph1.addEdge('s', 'p', 3)
graph1.addEdge('o', 'p', 2)
graph1.addEdge('o', 'q', 3)
graph1.addEdge('p', 'r', 2)
graph1.addEdge('r', 't', 3)
graph1.addEdge('q', 'r', 4)
graph1.addEdge('q', 't', 2)

# Graph from https://community.topcoder.com/tc?module=Static&d1=tutorials&d2=maxFlow.
graph2 = Graph()
for v in "xabcdey":
    graph2.addNode(v)
graph2.addEdge('x', 'a', 3)
graph2.addEdge('x', 'b', 1)
graph2.addEdge('a', 'c', 3)
graph2.addEdge('b', 'c', 5)
graph2.addEdge('b', 'd', 4)
graph2.addEdge('d', 'e', 2)
graph2.addEdge('e', 'y', 3)
graph2.addEdge('c', 'y', 2)

# No path from source to sink (a -> e), so there should be 0 flow.
noPathGraph = Graph()
for v in "abcde":
    noPathGraph.addNode(v)
noPathGraph.addEdge('a', 'b', 2)
noPathGraph.addEdge('b', 'c', 4)

class TestFordFulkerson(unittest.TestCase):
    def testGraph1(self):
        maxFlow = fordFulkerson(graph1, 's', 't')
        self.assertEqual(maxFlow, 5)

    def testGraph2(self):
        maxFlow = fordFulkerson(graph2, 'x', 'y')
        self.assertEqual(maxFlow, 3)

    def testNoPath(self):
        maxFlow = fordFulkerson(noPathGraph, 'a', 'e')
        self.assertEqual(maxFlow, 0)