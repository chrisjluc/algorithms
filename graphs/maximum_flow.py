"""This module contains the following maximum flow algorithms:
	- Ford-Fulkerson - O(E*f), where f is the maximum flow.
	- (TODO) Edmond-Karp - O(V*E^2)
	- (TODO) Push-relabel - O(E*V^2)

Given a set of nodes and edges that connect them, and "capacities" assigned to each edge,
the maximum flow problem asks what is the maximum amount of X that you can route from one
node to another.

For example, the edges of the graph could be pipes, and the capacities could be the amount
of water that can flow through each pipe. By using max-flow, you can find the maximum water
that you can route from a starting point to an end point. Basically, how do you distribute water
among all the intermediary pipes such that the maximum amount of water reaches the end.

An optimal solution to this problem can be found in this image (from TopCoder's algorithm tutorials):
https://community.topcoder.com/i/education/maxFlow01.gif. The flow here is going from X -> Y.

References:
https://community.topcoder.com/tc?module=Static&d1=tutorials&d2=maxFlow
http://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
http://en.wikipedia.org/wiki/Flow_network
"""

from graphs.shortest_paths import dijkstra
from graphs import util
from graphs.graph import *

# Helper method to find an augmenting path in the graph. An augmenting path is a path whose
# flow can be increased (none of the edges in the path has a maximized flow).
#
# @param graph - A graph object.
# @param capacities - A dictionary of tuples (source, target) representing edges, to their capacities
# @param flows - A dictionary of tuples (source, target) representing edges, to their current flows
# @param source - The source node.
# @param sink - The sink node.
# @param path - The current path (recursively builds it).
# @reutrn res - The augmenting path.
def _findAugmentingPath (graph, capacities, flows, source, sink, path):
	if source == sink:
		return path
	for b in graph.adjNodes[source]:
		residual = capacities[(source, b)] - flows[(source, b)]
		if residual > 0 and (source, b) not in util.getEdgeListFromPath(path):
			res = _findAugmentingPath(graph, capacities, flows, b, sink, path + [b])
			if res != None:
				return res

# Implements the Ford-Fulkerson maximum-flow algorithm.
#
# @param graph - A graph object.
# @param source - The source node.
# @param sink - The sink node.
# @return The maximum flow through the network.
def fordFulkerson (graph, source, sink):
	# Create the network. We can't use the original graph as we must add reverse edges.
	network = Graph()
	for i in graph.nodes:
		network.addNode(i)
	for (a, b) in graph.weights:
		network.addEdge(a, b, graph.weights[(a, b)])
		network.addEdge(b, a, 0)
	capacities = network.weights

	# Initialize flows to zero.
	flows = {(a, b): 0 for (a, b) in network.weights}

	# Find the first augmenting path to add flow.
	path = _findAugmentingPath(network, capacities, flows, source, sink, [source])

	# Continue until no more augmenting paths can be found.
	while path != None:
		residuals = []
		for i in range(len(path) - 1):
			edge = (path[i], path[i+1])
			residuals.append(capacities[edge] - flows[edge])

		# Maximize the flow through this path by filling up the smallest residual edge.
		additionalFlow = min(residuals)

		# Add flow to the forward edges, subtract flow from the reverse edges.
		for i in range(len(path) - 1):
			edge = (path[i], path[i+1])
			flows[edge] += additionalFlow
			flows[(edge[1], edge[0])] -= additionalFlow

		# Find another augmenting path with the updated flows.
		path = _findAugmentingPath(network, capacities, flows, source, sink, [source])

	return sum(flows[(source, b)] for b in network.adjNodes[source])