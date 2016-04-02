
def BFSTraversal(G, s):
	start = G.getVertex(s)
	start.setDistance(0)
	start.setPrevious(None)
	vertQueue = Queue()
	vertQueue.enQueue(start)
	while(vertQueue.size>0):
		currentVert = vertQueue.deQueue()
		print currentVert.getVertexID()
		for neighbor in currentVert.getConnections():
			if(neighbor.getColor() == 'white'):
				neighbor.setColor('gray')
				neighbor.setDistance(currentVert.getDistance() + 1)
				neighbor.setPrevious(currentVert)
				vertQueue.enQueue(neighbor)
			currentVert.setColor('black')

def BFS(G):
	for v in G:
		if(v.getColor == 'white'):
			BFSTraversal(G, v.getVertexID())
