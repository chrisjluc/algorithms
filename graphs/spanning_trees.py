"""This module contains the following minimum spanning tree algorithms:
    - Prim's algorithm
    - Kruskal's algorithm
"""
from heapq import heappush, heappop
from graphs.graph import SpanningTree
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

def kruskal(graph):
    """
    Kruskal's algorithm finds a minimum spanning tree for a connected weighted graph
    Sort edges in ascending order and continuously adds and 
    merges trees until a spanning forest is yielded
    @param graph - A graph object
    @return forest - A set of spanning trees
    """
    h = []
    forest = []
    for key, weight in graph.weights.iteritems():
        heappush(h, (weight, key))
    sortedWeights = [heappop(h) for i in range(len(h))]
    
    for elem in sortedWeights:
        weight, (fr, to) = elem;
        cycleExists = False

        for tree in forest:
            # Detects cycles
            if fr in tree.nodes and to in tree.nodes:
                cycleExists = True
                break
            if fr in tree.nodes or to in tree.nodes:
                tree.addEdge((fr, to))
                # If any trees intersect, merge them
                for i in xrange(0, len(forest)):
                    for j in xrange(i+1, len(forest)):
                        if len(forest[i].nodes & forest[j].nodes) > 0:
                            forest[i].merge(forest[j])
                            forest.remove(forest[j])
                            break
                break

        if cycleExists:
            continue
        
        # If no edge was merged and no cycle exists, create new tree
        tree = SpanningTree()
        tree.addEdge((fr, to))
        forest.append(tree)
    return forest