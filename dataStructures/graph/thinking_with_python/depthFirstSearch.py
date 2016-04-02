
def dfs(G, currentVert, visited):
	visited[currentVert] = True
	print "traversal: " + currentVert.getVertexID()
	for neighbor in currentVert.getConnections()
		if neighbor not in visited:
			dfs(G, neighbor, visited)

def DFSTraversal:
	visited = []
	for currentVert in G:
		if currentVert not in visited:
			dfs(G, currentVert, visited)
			