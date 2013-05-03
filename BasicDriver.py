#!/usr/bin/python

from Graph import *

import Solvers.RadialDisplay as RD
import TikzWriter as TW
import sys
from DotParser import *
import Solvers.NBodyRepositioner as NB
import Solvers.TopDownSolver as TD

argv = sys.argv

infile = ""
outfile = ""
if len(argv) !=3 :
	print "Usage: BasicDriver inputfile outputfile"
	sys.exit()

else:
	infile = argv[1]
	outfile = argv[2]

directed = False
DP = DotParser()

DP.readFile(infile)
graph = DP.Graph
# print graph
graph3 = RD.radialAssign(graph)
# print graph
# print graph
# graph = TD.arrange(graph)
graph2 = NB.reposition(graph3, False)

TW.tikGraph(graph2, outfile)


