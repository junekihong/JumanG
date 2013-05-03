from Graph import *
from GraphAnalysis import *

armLength = 3
toAdjust = list()

def layout(nodes, maximum):
	for y in xrange(len(nodes)):
		l = nodes [y]
		for x in xrange(len(l)):
			xMod = maximum/len(l) * armLength
			l[x].PosY = armLength*y
			if len(l) % 2 == 0:
				midpoint = len(l)/2
				l[x].PosX = ((x-midpoint)*xMod) -1.5
			else:
				midpoint = (len(l)+1)/2
				l[x].PosX = (x - midpoint)* xMod



def arrange(g):
	global toAdjust
	
	graph = g.copy()
	GA = GraphAnalysis(graph)
	nodepairs = GA.topologicalSort(True)
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


