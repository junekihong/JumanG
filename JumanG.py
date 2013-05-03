#!/usr/bin/python

from Utils import *
from Graph import *
from DotParser import *
from GraphAnalysis import *
import TikzWriter as TW

import Solvers
import Solvers.RadialDisplay as RD
import Solvers.NBodyRepositioner as NB

from sys import argv

class JumanG:
    
    def __init__(self, infile):
        self.Parser = DotParser()
        self.Graph = self.Parser.readFile(infile)
        self.Analysis = GraphAnalysis(self.Graph)

    def outputToTikz(self, graph, outfile):
        TW.tikGraph(graph, outfile)
        
    def runRadial(self):
        return RD.radialAssign(self.Graph)

    def runNBody(self):
        return NB.reposition(self.runRadial(),False)

if __name__ == "__main__":
    try:
        infile = argv[1]
        if len(argv) == 2:
            outfile = "result.out"
        else:
            outfile = argv[2]
        
    except IndexError:
        print
        print "Usage: ./JumanG.py [inputfile] [outputfile]"
        print "if not output file is specified, the default output file will be result.out"
        print
        exit()

    juman = JumanG(infile)

    graph = juman.runRadial()
    print graph
    graph = juman.runNBody()
    print graph

    juman.outputToTikz(graph, outfile)

