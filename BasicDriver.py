from Graph import *
import RadialDisplay as RD
import TikzWriter as TW
import sys
from DotParser import *
import NBodyRepositioner as NB

argv = sys.argv

infile = ""
outfile = ""
if len(argv) !=3 :
	print "Usage: BasicDriver inputfile outputfile"
	sys.exit()

else:
	infile = argv[1]
	outfile = argv[2]

DP = DotParser()

DP.readFile(infile)
graph = DP.Graph

RD.radialAssign(graph)

graph = NB.reposition(graph)

TW.tikGraph(graph, outfile)

