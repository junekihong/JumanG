from Graph import *
from Utils import *
from sys import float_info

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
				f = (armLength)/(d**2)
				toRet[n1].append((-(m/d)*f, -(n/d)*f))
				for (n3, l) in graph.AdjacencyList[n1]:
					if n2 == n3:
						toRet[n1].append((m,n))

	return toRet





def __jitter(graph, forces):
	for n in forces.keys():
		xTot = 0
		yTot = 0
		for (x, y) in forces[n]:
			xTot += x
			yTot += y 
		n.PosX -= xTot * .01
		n.PosY -= yTot * .01

	


def reposition(graph):
	bestCopy = graph.copy()
	minForce = float_info.max

	for x in xrange(1000):
		forces = __calcForces(graph)
		m = 0
		for n in forces.keys():
			xTot = 0
			yTot = 0
			for (x1, y1) in forces[n]:
				xTot += x1
				yTot += y1
				
			# print n, xTot, yTot

			m += sqrt(xTot**2 + yTot**2)
		# print

		if m < minForce:
			bestCopy = graph.copy()
			minForce = m

		__jitter(graph, forces)

	return bestCopy
