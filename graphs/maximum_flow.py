"""This module contains the following maximum flow algorithms:
    - Ford-Fulkerson - O(E*f), where f is the maximum flow.
    - Edmond-Karp - O(V*E^2)
    - (TODO) Push-relabel - O(E*V^2) -> generally the most performant.

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
http://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
http://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm
http://en.wikipedia.org/wiki/Flow_network
"""

from graphs.shortest_paths import dijkstra
from graphs import util
from graphs.graph import *


def ford_fulkerson (graph, source, sink):
    """Implements the Ford-Fulkerson maximum-flow algorithm.

    @param graph - A graph object.
    @param source - The source node.
    @param sink - The sink node.
    @return The maximum flow through the network.
    """
    # Create the network. We can't use the original graph as we must add reverse edges.
    network = Graph()
    for i in graph.nodes:
        network.add_node(i)
    for (a, b) in graph.weights:
        network.add_edge(a, b, graph.weights[(a, b)])
        network.add_edge(b, a, 0)
    capacities = network.weights

    # Initialize flows to zero.
    flows = {(a, b): 0 for (a, b) in network.weights}

    # Find the first augmenting path to add flow.
    path = _find_augmenting_path(network, capacities, flows, source, sink, [source])

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
        path = _find_augmenting_path(network, capacities, flows, source, sink, [source])

    # Flow to the sink is equal to the flow coming out of the source.
    return sum(flows[(source, b)] for b in network.adjNodes[source])

def edmonds_karp (graph, source, sink):
    """Implements the Edmonds-Karp maximum-flow algorithm. This is an implementation of the 
    Ford-Fulkerson for computing the maximum flow in O(V*E^2) time. This improvement is due
    to the selection of the shortest augmenting path rather than any random one.

    @param graph - A graph object.
    @param source - The source node.
    @param sink - The sink node.
    @return The maximum flow through the network.
    """
    # Create the network. We can't use the original graph as we must add reverse edges.
    network = Graph()
    for i in graph.nodes:
        network.add_node(i)
    for (a, b) in graph.weights:
        network.add_edge(a, b, graph.weights[(a, b)])
        network.add_edge(b, a, 0)
    capacities = network.weights

    # Initialize flows to zero.
    flows = {(a, b): 0 for (a, b) in capacities}

    while True:
        # Find the shortest augmenting path, not just ANY augmenting path, by using a
        # breadth-first search.
        path = _find_path_bfs(network, capacities, flows, source, sink)
        if not path:
            break

        # Maximize the flow through this path by filling up the smallest residual edge.
        flow = min(capacities[(u, v)] - flows[(u, v)] for (u, v) in path)

        # Add flow to the forward edges, subtract flow from the reverse edges.
        for (u, v) in path:
            flows[(u, v)] += flow
            flows[(v, u)] -= flow

    # Flow to the sink is equal to the flow coming out of the source.
    return sum(flows[(source, i)] for i in network.adjNodes[source])

def _find_augmenting_path (graph, capacities, flows, source, sink, path):
    """Helper method to find an augmenting path in the graph. An augmenting path is a path whose
    flow can be increased (none of the edges in the path has a maximized flow). This is used in 
    the Ford-Fulkerson algorithm.

    @param graph - A graph object.
    @param capacities - A dictionary of tuples (source, target) representing edges, to their capacities
    @param flows - A dictionary of tuples (source, target) representing edges, to their current flows
    @param source - The source node.
    @param sink - The sink node.
    @param path - The current path (recursively builds it).
    @return res - The augmenting path.
    """
    if source == sink:
        return path
    for b in graph.adjNodes[source]:
        residual = capacities[(source, b)] - flows[(source, b)]
        if residual > 0 and (source, b) not in util.get_edge_list_from_path(path):
            res = _find_augmenting_path(graph, capacities, flows, b, sink, path + [b])
            if res != None:
                return res

def _find_path_bfs (graph, capacities, flows, source, sink):
    """Helper method to find the shortest augmenting path in the graph. This is used in 
    the Edmonds-Karp algorithm.
    """
    queue = [source]
    paths = {source: []}
    while queue:
        u = queue.pop(0)
        for v in graph.adjNodes[u]:
            if capacities[(u, v)] - flows[(u, v)] > 0 and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == sink:
                    return paths[v]
                queue.append(v)
    return None
