import unittest
from graphs.maximum_flow import *
from graphs import util

# Graph from http://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm.
graph1 = Graph()
for v in "sopqrt":
    graph1.add_node(v)
graph1.add_edge('s', 'o', 3)
graph1.add_edge('s', 'p', 3)
graph1.add_edge('o', 'p', 2)
graph1.add_edge('o', 'q', 3)
graph1.add_edge('p', 'r', 2)
graph1.add_edge('r', 't', 3)
graph1.add_edge('q', 'r', 4)
graph1.add_edge('q', 't', 2)

# Graph from https://community.topcoder.com/tc?module=Static&d1=tutorials&d2=maxFlow.
graph2 = Graph()
for v in "xabcdey":
    graph2.add_node(v)
graph2.add_edge('x', 'a', 3)
graph2.add_edge('x', 'b', 1)
graph2.add_edge('a', 'c', 3)
graph2.add_edge('b', 'c', 5)
graph2.add_edge('b', 'd', 4)
graph2.add_edge('d', 'e', 2)
graph2.add_edge('e', 'y', 3)
graph2.add_edge('c', 'y', 2)

# No path from source to sink (a -> e), so there should be 0 flow.
noPathGraph = Graph()
for v in "abcde":
    noPathGraph.add_node(v)
noPathGraph.add_edge('a', 'b', 2)
noPathGraph.add_edge('b', 'c', 4)

class TestFordFulkerson(unittest.TestCase):
    def testGraph1(self):
        maxFlow = ford_fulkerson(graph1, 's', 't')
        self.assertEqual(maxFlow, 5)

    def testGraph2(self):
        maxFlow = ford_fulkerson(graph2, 'x', 'y')
        self.assertEqual(maxFlow, 3)

    def testNoPath(self):
        maxFlow = ford_fulkerson(noPathGraph, 'a', 'e')
        self.assertEqual(maxFlow, 0)