from Graph import *
from Utils import *
from sys import floatinfo

bestCopy = None
minForce = floatinfo.max

def __calcForce(graph):
	for 

def __jitter(graph):
	tHold = graph.copy()


def reposition(graph):
	bestCopy = graph.copy()

	for x in xrange(1000):
		(graph, m) = __jitter(graph).copy()
		if m < minForce:
			bestCopy = graph.copy()
			minForce = m

	return bestCopy
