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

    def add_node(self, data):
        self.nodes.add(data)

    def add_edge(self, fr, to, weight=0):
        self.adjNodes[fr].append(to)
        self.weights[(fr, to)] = weight

# Represents an undirected graph.
class UndirectedGraph(Graph):
    def add_edge(self, fr, to, weight=0):
        Graph.add_edge(self, fr, to, weight)
        self.weights[(to, fr)] = weight

# Represents a minimal spanning tree with set of nodes and set of edge tuples
# Used in kruskal's algorithm
class SpanningTree:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def addEdge(self, edge):
        fr, to = edge;
        self.nodes.add(fr)
        self.nodes.add(to)
        self.edges.add(edge)

    def merge(self, tree):
        self.nodes = self.nodes | tree.nodes
        self.edges = self.edges | tree.edges