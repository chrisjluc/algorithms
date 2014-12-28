"""This module contains the following topological sort algorithms:
    - DFS method - O(V + E)

A topological sort is a linear ordering of vertices such that for every directed edge (a, b),
vertex a comes before vertex b in the ordering. This is only possible in a DAG (there is no
ordering if a cycle exists).

References:
http://en.wikipedia.org/wiki/Topological_sorting
"""


from graph import Graph

def topsort_dfs(graph):
    """Computes the topological ordering by DFSing each node, pushing nodes to a global stack.
    Adjacent nodes of a node are pushed to the stack before the node itself. This way, a
    topological ordering is created when reading the stack from top to bottom.

    @param graph - A graph object.
    @return stk - The ordering, represented as a list of nodes.
    """
    visited = { n: False for n in graph.nodes }
    stk = []

    for node in graph.nodes:
        if not visited[node]:
            _topsort_dfs_recursive(graph, node, stk, visited)
    return stk

def _topsort_dfs_recursive (graph, node, stk, visited):
    """Utility method for topsort_dfs. Recurses on each adjacent node, then pushes the node to
    the global stack.
    """
    visited[node] = True

    for n in graph.adjNodes[node]:
        if not visited[n]:
            _topsort_dfs_recursive(graph, n, stk, visited)
    stk.insert(0, node)
