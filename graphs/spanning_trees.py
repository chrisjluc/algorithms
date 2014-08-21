"""This module contains the following minimum spanning tree algorithms:
    - Prim's algorithm
"""
from graphs.util import MAX_WEIGHT

def prim(graph):
    """Implements prim's algorithm to solve the minimum spanning tree problem. This
    is non-deterministic for graphs that are not connected as it picks a random node
    as the root. For graphs that are not connected, use kruskal's algorithm, which will
    yield a minimum spanning forest.

    @param graph - A graph object
    @return tree - A set of tuples (a, b) where each tuple is an edge from node a to node b.
    """
    unvisited = set(graph.nodes)
    visited = set()

    visited.add(unvisited.pop())
    tree = set()

    while len(unvisited) != 0:
        min_weight = MAX_WEIGHT
        min_edge = None

        for v in visited:
            adj = graph.adjNodes[v]
            for a in adj:
                if a not in visited and graph.weights[(v, a)] < min_weight:
                    min_weight = graph.weights[(v, a)]
                    min_edge = (v, a)

        tree.add(min_edge)
        visited.add(min_edge[1])
        unvisited.remove(min_edge[1])

    return tree
