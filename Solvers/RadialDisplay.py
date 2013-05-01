#!/usr/bin/python
from Graph import *
from Utils import *
from GraphAnalysis import *
from math import cos, sin, radians


armLength = 3
visited = list()

# @Graph: graph to be sorted
# @Sink: If the sink should be the center, rather than the source
def __recRadial(graph, root, degrees, start, layer, d):

	children = graph.AdjacencyList[root]

	if len(children) ==0:
		return

	subDeg = degrees / len(children)
	currentDegrees = start

	for (c, t) in children:
		if c in visited:
			continue
		if not d:
			visited.append(c)
		x = layer * armLength * cos(radians(currentDegrees+(subDeg/2)))
		y = layer * armLength * sin(radians(currentDegrees+(subDeg/2)))

		if abs(x)< .00001:
			x = 0.0
		if abs(y) < .00001:
			y = 0.0

		c.PosX = x
		c.PosY = y

		__recRadial(graph, c, subDeg, currentDegrees, layer+1, d)
		currentDegrees += subDeg



def radialAssign(g, sink = False):

	graph = g.copy()
	# print graph
	gSorted = list()
	visited = list()

	# Toposort goes HERE:
	GA = GraphAnalysis(graph)

	gSorted = GA.topologicalSort()
	if len(gSorted)<1:
		gSorted.append(graph.getNodeList()[0])
	gSorted[0].PosX=0
	gSorted[0].PosY=0
	# root.PosX=0
	# root.PosY=0
	d = False
	if graph.Type == 1 :
		d = True

	# TODO: Add support for multiple roots

	__recRadial(graph, gSorted[0], 360, 0, 1, d)
	print graph
	return graph

