#!/usr/bin/python

from Utils import *
from Graph import *
from DotParser import *
from GraphAnalysis import *
import TikzWriter as TW

import Solvers
import Solvers.RadialDisplay as RD
import Solvers.NBodyRepositioner as NB
import Solvers.TopDownSolver as TD

from sys import argv


NBODY = 0
NBODY_RADIAL = 10
NBODY_JITTER = 3
TOPDOWN = 1
RADIAL = 2
#NBODYJ = 3

class JumanG:
    def __init__(self, infile):
        self.Parser = DotParser()
        self.Graph = self.Parser.readFile(infile)
        self.Analysis = GraphAnalysis(self.Graph)
        self.State = NBODY
        
    def outputToTikz(self, graph, outfile):
        TW.tikGraph(graph, outfile)
        
    def runRadial(self):
        return RD.radialAssign(self.Graph)

    def runNBody(self, useRadialSeed = True):
        if useRadialSeed:
            return NB.reposition(self.runRadial(),False)
        else:
            return NB.reposition(self.Graph,True)

    def runTopDown(self):
        return TD.arrange(self.Graph)

    def chooseSolver(self):
        (numberOfNodes,numberOfEdges,numberOfLeaves) = self.Analysis.numberOfNodesEdgesAndLeaves()

        rootNodes = self.Analysis.getRootNodes()
        numberOfRootNodes = len(rootNodes)
        hasCycles = True
        #If it is an acyclic graph, we can run topdown
        if self.Graph.Type==1:


            hasCycles = self.Analysis.BFS(rootNodes[0],True)
            if not hasCycles:
                topoList = self.Analysis.topologicalSort(True)
                treeDepth = topoList[-1][1]
                
                print "numberOfNodes",numberOfNodes,"treeDepth",treeDepth

                if numberOfNodes > pow(3,treeDepth) and numberOfRootNodes==1: 
                #nodeToDepthRatio = float(numberOfNodes)/treeDepth
                #if nodeToDepthRatio > 4:

                    self.State = RADIAL
                    return self.State
                else:
                    self.State = TOPDOWN
                    return self.State
        else: # undirected graph
            # Metric for graph: connectedness: #nodes/#edges, < 3
            connectedness = self.Graph.getNumEdges()/float(numberOfNodes)
            print connectedness
            if connectedness < 3:
                #radial -> nbody
                self.State = NBODY
            else:
                #nbody random
                self.State = NBODY_JITTER

        return self.State

    def runChosenSolver(self, choice = None):
        if choice == None:
            choice = self.State
            print choice
        return {
            NBODY:self.runNBody(),
            NBODY_RADIAL:self.runNBody(True),
            NBODY_JITTER:self.runNBody(False),
            TOPDOWN:self.runTopDown(),
            RADIAL:self.runRadial(),
            #NBODYJ:self.runNBody(False),
        }.get(choice,self.runNBody())
    
    def printChoice(self):
        return {
            NBODY:"NBODY",
            NBODY_RADIAL:"NBODY_RADIAL",
            NBODY_JITTER:"NBODY_JITTER", 
            TOPDOWN:"TOPDOWN",
            RADIAL:"RADIAL",
        }.get(self.State,"???")
    

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

    #graph = juman.runRadial()
    # print graph
    #graph = juman.runRadial()
    # print graph
    #graph = juman.runNBody(False)
    
    choice = juman.chooseSolver()
    print choice, juman.printChoice()

    graph = juman.runChosenSolver()
    #print graph

    
    juman.outputToTikz(graph, outfile)

