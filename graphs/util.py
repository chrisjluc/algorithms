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
