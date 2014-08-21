import unittest
from graphs.spanning_trees import *
from graphs.graph import UndirectedGraph

graph1 = UndirectedGraph()
for v in 'abcdefghi':
    graph1.add_node(v)
graph1.add_edge('a', 'b', 4)
graph1.add_edge('b', 'c', 8)
graph1.add_edge('c', 'd', 7)
graph1.add_edge('d', 'e', 9)
graph1.add_edge('e', 'f', 10)
graph1.add_edge('f', 'g', 2)
graph1.add_edge('g', 'h', 1)
graph1.add_edge('h', 'a', 8)
graph1.add_edge('b', 'h', 11)
graph1.add_edge('c', 'i', 2)
graph1.add_edge('h', 'i', 7)
graph1.add_edge('i', 'g', 6)
graph1.add_edge('c', 'f', 4)
graph1.add_edge('d', 'f', 14)

graph2 = UndirectedGraph()
for v in 'abc':
    graph2.add_node(v)
graph2.add_edge('a', 'b', 4)
graph2.add_edge('a', 'c', 8)

class TestPrim(unittest.TestCase):
    def testGraph1(self):
        tree = prim(graph1)
        expected = set([
            ('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'),
            ('c', 'i'), ('c', 'f'), ('f', 'g'), ('g', 'h')
        ])
        self.assertEqual(expected, tree)

    def testGraph2(self):
        tree = prim(graph2)
        expected = set([
            ('a', 'b'), ('a', 'c')
        ])
        self.assertEqual(expected, tree)
