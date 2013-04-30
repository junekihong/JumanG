from Graph import *
from Utils import *
from sys import floatinfo

bestCopy = None
minForce = floatinfo.max
armLength = 3
springConst = 1

def __calcForces(graph):
	toRet = dict()
	for n1 in graph.getNodeList():
		toRet[n1] = list()
		for n2 in graph.getNodeList():
			if n1 != n2:
				(m,n) = Graph.nodeDistVect(n1,n2)
				d = Graph.nodeDist(n1, n2)
				f = (armLength**3)/(d**2)
				toRet[n1].append(((m/d)*f, (n/d)*f))
				if n2 in graph.AdjacencyList[n1]:
					toRet[n1].append((m,n))





def __jitter(graph, forces):
	pass

	


def reposition(graph):
	bestCopy = graph.copy()

	for x in xrange(1000):
		forces = __calcForces(graph)
		m = sum(forces)
		if m < minForce:
			bestCopy = graph.copy()
			minForce = m

		__jitter(graph, forces)

	return bestCopy
