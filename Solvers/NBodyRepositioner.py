from Graph import *
from Utils import *
from sys import float_info

springConst = 1
armLength = 0

def __calcForces(graph):

	print armLength

	toRet = dict()
	for n1 in graph.getNodeList():
		toRet[n1] = list()
		for n2 in graph.getNodeList():
			if n1 != n2:
				(m,n) = Graph.nodeDistVect(n1,n2)
				d = Graph.nodeDist(n1, n2)
				if d ==0:
					d = 1
				f = (armLength**3)/(d**2)
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
	global armLength
	armLength = graph.getNumEdges() // 4 + 1
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

		__jitter(graph.copy(), forces)

	return bestCopy
