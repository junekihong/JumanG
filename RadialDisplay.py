from Graph import *
from Utils import *
from GraphAnalysis import *
from math import cos, sin, radians


armLength = 5

# @Graph: graph to be sorted
# @Sink: If the sink should be the center, rather than the source
def __recRadial(graph, root, degrees, start, layer):

	if root in graph.AdjacencyList.keys():
		children = graph.AdjacencyList[root]

	else:
		return

	subDeg = degrees / len(children)
	currentDegrees = start

	for (c, t) in children:
		x = layer * armLength * cos(radians(currentDegrees+(subDeg/2)))
		y = layer * armLength * sin(radians(currentDegrees+(subDeg/2)))

		if x < .00001:
			x = 0.0
		if y < .00001:
			y = 0.0

		c.PosX = x
		c.PosY = y

		__recRadial(graph, c, subDeg, currentDegrees, layer+1)
		currentDegrees += subDeg



def radialAssign(graph, sink = False):

	gSorted = list()

	# Toposort goes HERE:
	GA = GraphAnalysis(graph)

	gSorted = GA.topologicalSort()

	gSorted[0].PosX=0
	gSorted[0].PosY=0
	# root.PosX=0
	# root.PosY=0

	# TODO: Add support for multiple roots

	__recRadial(graph, gSorted[0], 360, 0, 1)
	# __recRadial(graph, root, 360,0,1)


