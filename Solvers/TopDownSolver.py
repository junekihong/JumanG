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
                        #print "xMod:",xMod, "max",maximum,"len", len(l)

			l[x].PosY = -armLength*y
                                
                        if len(l) % 2 == 0:
				midpoint = len(l)/2
				l[x].PosX = ((x-midpoint+1)*xMod) - 0.5*xMod
			else:
				midpoint = len(l)/2
				l[x].PosX = ((x-midpoint)*xMod)# +armLength*(x-1)
                        #print l[x].PosX, "AAA"


def arrange(g):
	global toAdjust
	
	graph = g.copy()
	GA = GraphAnalysis(graph)
	nodepairs = GA.topologicalSort(True)
        (_,lengthOfGraph) = nodepairs[-1]
        armLength = 3 / log(lengthOfGraph)


	nodes = list()
	nodes.append(list())

	most = 0
	current = 0
        layerCount = {}
	for (n, l) in nodepairs:
		layerCount[l] = layerCount.get(l,0)+1
                if l>current:
                        nodes.append(list())
		nodes[l].append(n)

        for layer in layerCount:
                count = layerCount[layer]
                if count > most:
                        most = count

        # Here, we try to minimize edge crossings between the nodes
        if len(nodes) > 2:
                # We keep track of two layers. Our current layer and the layer above it.
                layer1 = nodes[0]
                layer2 = nodes[1]
                for i in xrange(2,len(nodes)):
                        layer3 = nodes[i]
                        layer1Size = len(layer1)
                        layer2Size = len(layer2)
                        layer3Size = len(layer3)
                        #print "layer 1 size: ", layer1Size
                        #print "layer 2 size: ", layer2Size
                        
                        weightedLayer2Values = []
                        for nodej in xrange(len(layer2)):
                                nodejWeight = 0
                                nodejCount = 0
                                node2 = layer2[nodej]
                                for nodei in xrange(len(layer1)):
                                        node1 = layer1[nodei]
                                        isAdjacent = graph.isAdjacent(node1, node2)
                                        if isAdjacent:
                                                nodejCount += 1
                                                nodejWeight += nodei*layer1Size
                                for nodek in xrange(len(layer3)):
                                        node3 = layer3[nodek]
                                        isAdjacent = graph.isAdjacent(node2,node3)
                                        if isAdjacent:
                                                nodejCount +=1
                                                nodejWeight += nodek*layer3Size
                                normalizedWeight = nodejWeight / nodejCount
                                #print node2.Name, "normalizedWeight:",normalizedWeight, nodejWeight, nodejCount
                                weightedLayer2Values.append((node2, normalizedWeight))

                        sorted_by_second = sorted(weightedLayer2Values, key=lambda tup: tup[1])
                        
                        for nodej in xrange(len(layer2)):
                                layer2[nodej] = sorted_by_second[nodej][0]

                        layer1 = layer2
                        layer2 = layer3


	layout(nodes, most)
	return graph


