from collections import defaultdict

# Representation of a weighted, directed graph.
class Graph:
    def __init__(self):
        # Set of nodes.
        self.nodes = set()

        # A mapping of node to list(node), to query adjacent nodes of a node.
        self.adjNodes = defaultdict(list)

        # Dictionary of weights. Keys are tuples (a, b) where a is the source
        # node and b is the destination node.
        self.weights = dict()

    def addNode(self, data):
        self.nodes.add(data)

    def addEdge(self, fr, to, weight=0):
        self.adjNodes[fr].append(to)
        self.weights[(fr, to)] = weight

# Represents an undirected graph.
class UndirectedGraph(Graph):
    def addEdge(self, fr, to, weight=0):
        Graph.addEdge(self, fr, to, weight)
        self.weights[(to, fr)] = weight