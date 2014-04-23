from collections import defaultdict

# Representation of a weighted, directed graph.
class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.weights = {}

	def addNode(self, data):
		self.nodes.add(data)

	def addEdge(self, fr, to, weight=0):
		self.edges[fr].append(to)
		self.weights[(fr, to)] = weight

# Represents an undirected graph.
class UndirectedGraph(Graph):
	def addEdge(self, fr, to, weight=0):
		Graph.addEdge(self, fr, to, weight)
		self.weights[(to, fr)] = weight