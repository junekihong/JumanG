from Graph import *
from Utils import *
from math import cos, sin, radians

# @Graph: graph to be sorted
# @Sink: If the sink should be the center, rather than the source
def __recRadial(graph, root, degrees, start, layer):

	children = graph.AdjacencyList[root]

	subDeg = degrees / len(children)
	currentDegrees = start

	for c in children:
		c.PosX = layer*5 * cos(radians(currentDegrees+(subDeg/2)))
		c.PosY = layer*5 * sin(radians(currentDegrees+(subDeg/2)))
		__recRadial(graph, c, subDeg, currentDegrees, layer+1)
		currentDegrees += subDeg



def radialAssign(graph, sink = False):

	gSorted = list()

	# Toposort goes HERE:
	# gSorted = topolayer(graph)


	gSorted[0].PosX=0
	gSorted[0].PosY=0

	# TODO: Add support for multiple roots

	__recRadial(graph, gSorted[0], 360, 0, 1)


