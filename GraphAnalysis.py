#!/usr/bin/python

from sys import *
from collections import deque
from DotParser import *


class GraphAnalysis:
    def __init__(self, graph):
        self.Graph = graph
        self.RootNode = None
        self.DependencyTable = self.buildDependencyTable(self.Graph)


    def buildDependencyTable(self, graph):
        dependencyTable = {}
        
        for node in self.Graph.AdjacencyList:
            edgeList = self.Graph.AdjacencyList[node]
            for (node2,Type) in edgeList:
                dependencyTable[node2] = dependencyTable.get(node2,[])
                dependencyTable[node2].append(node)        
        return dependencyTable

    def printDependencyTable(self):
        print "dependency Table: "
        string = ""
        for node in self.DependencyTable:
            string = string + node.__str__() + ": "
            
            dependencyList = self.DependencyTable[node]
            for dependency in dependencyList:
                string = string + dependency.__str__() + " "
                
            string = string + "\n"
        print string

    def getRootNodes(self):
        rootList = []
        for node in self.Graph.getNodeList():
            if node not in self.DependencyTable:
                rootList.append(node)
        return rootList


    def topologicalSort(self):
        #dependencyTable = self.buildDependencyTable(self.Graph)
        queue = self.getRootNodes()
        topoSort = []

        while queue:
            n = queue.pop()
            topoSort.append(n)

            adjacencies = self.Graph.AdjacencyList.get(n,None)
            if not adjacencies == None: 
                for (adjacency,edgeType) in adjacencies:
                    #print adjacency
                    self.DependencyTable.get(adjacency).remove(n)
                    if not self.DependencyTable.get(adjacency):
                        queue.append(adjacency)
        self.DependencyTable = self.buildDependencyTable(self.Graph)
        return topoSort


    def BFS(self, root):
        DISPLAYSTEPS = False

        queue = deque()
        queue.append(root)
        
        if DISPLAYSTEPS:
            print "ROOT",root,"\n"

        visited = {}
        visited[root] = True
        
        while queue:
            node = queue.popleft()
            children = self.Graph.AdjacencyList[node]
            
            if DISPLAYSTEPS:
                print "CURRENT NODE: ",node

            for child in children:
                childNode = child[0]
                
                if DISPLAYSTEPS:
                    print "CHILD: ", childNode
                if not visited.get(childNode,False):
                    visited[childNode] = True
                    queue.append(childNode)
                    if DISPLAYSTEPS:
                        print "PUSHED: ", childNode

    def numberOfNodes(self):
        return len(self.Graph.AdjacencyList.keys())
    
    def numberOfEdges(self):
        edges = 0
        for node in self.Graph.AdjacencyList:
            edgeList = self.Graph.AdjacencyList[node]
            edges = edges + len(edgeList)
        return edges

    def numberOfLeaves(self):
        count = 0
        for node in self.Graph.AdjacencyList:
            edgeList = self.Graph.AdjacencyList[node]
            if not edgeList:
                count += 1
        return count

    def numberOfNodesEdgesAndLeaves(self):
        nodes = len(self.Graph.AdjacencyList)
        edges = 0
        leafCount = 0
        for node in self.Graph.AdjacencyList: 
            edgeList = self.Graph.AdjacencyList[node]
            if not edgeList:
                leafCount += 1
            else:
                edges += len(edgeList)
        return (nodes, edges, leafCount)

if __name__ == "__main__":
    parser = DotParser()

    filename = argv[1]
    parser.readFile(filename)
    graph = parser.Graph

    analysis = GraphAnalysis(graph)

    print graph

    arbitraryRoot = graph.getNodeList()[0]
    analysis.BFS(arbitraryRoot)
    
    analysis.printDependencyTable
    
    print "ROOTS:"
    rootList = analysis.getRootNodes()
    for root in rootList:
        print root
    print

    print "NUMBER OF ROOTS:", len(rootList)
    print
    

    topoList = analysis.topologicalSort()
    print "TOPOLOGICAL SORT:"
    for node in topoList:
        print node
    print

    print
    print "NUMBER OF EDGES AND TOTAL NUMBER OF NODES:"
    print analysis.numberOfEdges(), analysis.numberOfNodes()
    print 
    print "NUMBER OF LEAVES:"
    print analysis.numberOfLeaves()
    print
    print "ALL 3: "
    print analysis.numberOfNodesEdgesAndLeaves()
    
