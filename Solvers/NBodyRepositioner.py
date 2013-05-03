from Graph import *
from GraphAnalysis import *

from Utils import *
from sys import float_info

from random import uniform

#springConst = 1
k = 1
armLength = 0

def __calcForces(graph):
	global armLength
	# mult = 1
	if graph.Type ==1:
		# mult = 16
		armLength /=2
	if armLength<2:
		armLength = 2

	# print armLength
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
				#f = (d**2/k - k**2/d)
				
				
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

	


def reposition(g, reposition = True):
	graph = g.copy()
	#analysis = GraphAnalysis(graph)
	#k = sqrt(100/analysis.numberOfEdges())


	global armLength
	armLength = graph.getNumEdges() // 4 + 1
	# print graph.getNumEdges()

	bestCopy = graph.copy()
	minForce = float_info.max

	#Added random jitters to all the initial starting points for the nodes
	if reposition:
		for node in graph.AdjacencyList:
			node.PosX += uniform(-1,1)
			node.PosY += uniform(-1,1)
		

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
						#print m
				# print

		if m < minForce:
			bestCopy = graph.copy()
			minForce = m

		__jitter(graph.copy(), forces)

	return bestCopy
