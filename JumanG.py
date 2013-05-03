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
TOPDOWN = 1
RADIAL = 2

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
        if rootNodes:
            hasCycles = self.Analysis.BFS(rootNodes[0],True)
            if not hasCycles:
                topoList = self.Analysis.topologicalSort(True)
                treeDepth = topoList[-1][1]
                
                print "numberOfNodes",numberOfNodes,"treeDepth",treeDepth

                if numberOfNodes > pow(2,treeDepth+1)-1: 
                #nodeToDepthRatio = float(numberOfNodes)/treeDepth
                #if nodeToDepthRatio > 4:
                    self.State = RADIAL
                    return self.State
                else:
                    self.State = TOPDOWN
                    return self.State



        self.State = NBODY
        return self.State

    def runChosenSolver(self, choice = None):
        if choice == None:
            choice = self.State
        return {
            NBODY:self.runNBody(),
            TOPDOWN:self.runTopDown(),
            RADIAL:self.runRadial(),
        }.get(choice,self.runNBody())
    
    #def printChoice(self):
    #     return {
   
    #    }.get(choice)
    

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
    graph = juman.runNBody(False)
 #print graph

    #graph = juman.runTopDown()
    
    #choice = juman.chooseSolver()
   # print choice

    #graph = juman.runChosenSolver(0)
    print graph
    
    juman.outputToTikz(graph, outfile)

