"""This module contains the following shortest path algorithms:
    - Dijjkstra's (with PriorityQueue) - O(E + V*logV)
    - Bellman-Ford - O(V*E)
    - Floyd-Warshall - O(V^3)

The shortest path of a graph is the path between two nodes such that the
sum of the weights of the edges in the path is minimized. 

References:
http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
"""

from graphs.util import MAX_WEIGHT
from Queue import PriorityQueue

# Implements dijkstra's algorithm for a weighted graph. If the graph is in
# adjacency matrix representation, convert it to a Graph object with
# util.convertAdjToGraph. Note that this algorithm does not work for
# graphs whose weights may contain negative numbers.
# 
# @param graph - A graph object
# @param source - The source node
# @return dist - An dictionary of shortest path lengths from the source node to 
#   all other nodes.
def dijkstra(graph, source):
    dist = {n: MAX_WEIGHT for n in graph.nodes}
    prev = dict()

    dist[source] = 0

    pq = PriorityQueue()
    for k, v in dist.iteritems():
        pq.put((v, k))

    while not pq.empty():
        n = pq.get()[1]

        for i in graph.adjNodes[n]:
            prop = dist[n] + graph.weights[(n, i)]
            if prop < dist[i]:
                dist[i] = prop
                prev[i] = n
                pq.put((prop, i))

    return dist, prev   

# Implements the Bellman-Ford algorithm. This is slower than Dijkstra's algorithm but is
# more versatile as it can handle negative edge weights. If the graph has a cycle whose numbers
# sum to a negative number, the shortest path can continuously be reduced by one more trip around
# this cycle. This algorithm can detect if a cycle like that exists and throws an exception if it does.
#
# @throws Exception - Throws an exception if the graph contains a negative edge weight cycle.
# @param graph - A graph object
# @param source - The source node
# @return dist - An dictionary of shortest path lengths from the source node to 
#   all other nodes.
def bellmanFord(graph, source):
    L = len(graph.nodes)
    dist = {n: MAX_WEIGHT for n in graph.nodes}
    prev = dict()

    dist[source] = 0

    for i in range(L):
        for a, adjs in graph.adjNodes.iteritems():
            for b in adjs:
                if dist[a] + graph.weights[(a, b)] < dist[b]:
                    dist[b] = dist[a] + graph.weights[(a, b)]
                    prev[b] = a

    # Check for negative-weight cycles.
    for a, adjs in graph.adjNodes.iteritems():
        for b in adjs:
            if dist[a] + graph.weights[(a, b)] < dist[b]:
                raise Exception('Error: This graph has a negative edge weight cycle.')

    return dist, prev

# Implements the Floyd-Warshall all-pairs shortest path algorithm. This runs slower than
# Dijkstra's algorithm and should be used for a quick test or for small datasets (n < 100).
# This runs in O(n^3).
#
# @param graph - A graph object.
# @return sp - A 2D array where sp[i][j] contains the shortest path from i to j.
def floydWarshall(graph):
    L = len(graph.nodes)
    sp = [[MAX_WEIGHT for x in range(L)] for x in range(L)] 

    for i in range(L):
        sp[i][i] = 0
    for a, adjs in graph.adjNodes.iteritems():
        for b in adjs:
            sp[a][b] = graph.weights[(a, b)]

    for k in range(L):
        for i in range(L):
            for j in range(L):
                sp[i][j] = min(sp[i][j], sp[i][k] + sp[k][j])

    return sp