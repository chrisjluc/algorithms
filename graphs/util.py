from graph import *

MAX_WEIGHT = 1000000000

# Converts an adjacency matrix representation to a Graph representation.
#
# @param adj - An adjacency matrix represented using a 2D array.
# @return gr - The converted Graph object.
def convertAdjToGraph (adj):
    gr = Graph()
    L = len(adj)

    for i in range(L):
        gr.addNode(i)

    for i in range(L):
        for j in range(L):
            if adj[i][j] != 0:
                gr.addEdge(i, j, adj[i][j])

    return gr

# Reconstructs the path to the target from a prev dictionary created by one of the
# shortest path algorithms. 
#
# @param prev - The map of nodes to previous nodes.
# @param target - The target node.
# @return path - The path to the node from the source.
def getPathFromPrev (prev, target):
    u = target
    path = []

    while u in prev:
        u = prev[u]
        path.append(u)

    path.reverse()
    return path

# Converts a list of nodes representing a path to a list of edges.
# For example, ['a', 'b', 'c', 'd'] becomes [('a', 'b'), ('b', 'c'), ('c', 'd')]
#
# @param path - The path represented as a list of nodes.
# @return edgeList - The path represented as a list of edges.
def getEdgeListFromPath (path):
    edgeList = []
    L = len(path)
    if L <= 1: 
        return edgeList

    for i in range(L-1):
        edgeList.append((path[i], path[i+1]))

    return edgeList
