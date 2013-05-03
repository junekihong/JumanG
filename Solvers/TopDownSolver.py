from Graph import *
from GraphAnalysis import *

from math import log

armLength = 3
toAdjust = list()

def layout(nodes, maximum):
	for y in xrange(len(nodes)):
		l = nodes [y]
                count = 0
		for x in xrange(len(l)):
			xMod = maximum/len(l) * armLength
			l[x].PosY = -armLength*y
                        if len(l) % 2 == 0:
				midpoint = len(l)/2
				l[x].PosX = ((x-midpoint)*xMod) -1.5 +armLength*x
			else:
				midpoint = (len(l)+1)/2
				l[x].PosX = (x - midpoint)* xMod +armLength*x


def arrange(g):
	global toAdjust
	
	graph = g.copy()
	GA = GraphAnalysis(graph)
	nodepairs = GA.topologicalSort(True)
        (_,lengthOfGraph) = nodepairs[-1]
        armLength = 3 / log(lengthOfGraph)

	most = 0
	nodes = list()
	nodes.append(list())

	current = 0
	count = 0

	for (n, l) in nodepairs:
		if l>current:
			current+=1
			if count > most:
				most = count
			count = 0
			nodes.append(list())
		nodes[l].append(n)

	layout(nodes, most)
	return graph


