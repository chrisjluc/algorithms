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
graph1.add_edge('h', 'a', 9)
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

graph3 = UndirectedGraph()
for v in 'abcde':
    graph3.add_node(v)
graph3.add_edge('a', 'b', 3)
graph3.add_edge('b', 'c', 8)
graph3.add_edge('c', 'd', 4)
graph3.add_edge('d', 'a', 16)
graph3.add_edge('b', 'd', 5)
graph3.add_edge('a', 'c', 1)
graph3.add_edge('b', 'e', 6)
graph3.add_edge('c', 'e', 7)
graph3.add_edge('d', 'e', 8)

# Should produce a forest for kruskal
graph4 = UndirectedGraph()
for v in 'abcdefgh':
    graph4.add_node(v)
graph4.add_edge('a', 'b', 4)
graph4.add_edge('a', 'c', 8)
graph4.add_edge('b', 'c', 1)
graph4.add_edge('d', 'e', 9)
graph4.add_edge('e', 'f', 2)
graph4.add_edge('g', 'h', 6)

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

    def testGraph3(self):
        tree = prim(graph3)
        expected = set([
            ('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'e')
        ])
        self.assertEqual(expected, tree)

class TestKruskal(unittest.TestCase):
    def testGraph1(self):
        forest = kruskal(graph1)
        expected = set([
            ('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'),
            ('c', 'i'), ('c', 'f'), ('f', 'g'), ('g', 'h')
        ])
        self.assertEqual(expected, forest[0].edges)

    def testGraph2(self):
        forest = kruskal(graph2)
        expected = set([
            ('a', 'b'), ('a', 'c')
        ])
        self.assertEqual(expected, forest[0].edges)

    def testGraph3(self):
        forest = kruskal(graph3)
        expected = set([
            ('a', 'b'), ('a', 'c'), ('c', 'd'), ('b', 'e')
        ])
        self.assertEqual(expected, forest[0].edges)

    def testGraph3(self):
        forest = kruskal(graph4)
        expected1 = set([
            ('a', 'b'), ('b', 'c')
        ])
        expected2 = set([
            ('d', 'e'), ('e', 'f')
        ])
        expected3 = set([
            ('g', 'h')
        ])
        self.assertEqual(expected1, forest[0].edges)
        self.assertEqual(expected2, forest[1].edges)
        self.assertEqual(expected3, forest[2].edges)