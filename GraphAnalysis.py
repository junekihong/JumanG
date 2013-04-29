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
        for node in self.Graph.NodeList:
            if node not in self.DependencyTable:
                rootList.append(node)
        return rootList


    def topologicalSort(self):
        dependencyTable = self.buildDependencyTable(self.Graph)

        queue = self.getRootNodes()
        topoSort = []

        while queue:
            n = queue.pop()
            topoSort.append(n)

            adjacencies = self.Graph.AdjacencyList.get(n,None)
            if not adjacencies == None: 
                for (adjacency,edgeType) in adjacencies:
                    #print adjacency
                    dependencyTable.get(adjacency).remove(n)
                    if not dependencyTable.get(adjacency):
                        queue.append(adjacency)

        return topoSort


    def BFS(self, root):
        DISPLAYSTEPS = False

        queue = deque()
        queue.append(root)
        
        if DISPLAYSTEPS:
            print "ROOT",root
            print
        
        visited = {}
        visited[root] = True
        
        while queue:
            node = queue.popleft()
            children = self.Graph.AdjacencyList.get(node,None)
            
            if children == None:
                continue
            
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
            if DISPLAYSTEPS:
                print



if __name__ == "__main__":
    parser = DotParser()

    filename = argv[1]
    parser.readFile(filename)
    graph = parser.Graph

    analysis = GraphAnalysis(graph)

    print graph

    arbitraryRoot = graph.NodeList.keys()[0]
    analysis.BFS(arbitraryRoot)
    
    analysis.printDependencyTable
    
    print "ROOTS:"
    rootList = analysis.getRootNodes()
    for root in rootList:
        print root
    print
    

    topoList = analysis.topologicalSort()
    print "TOPOLOGICAL SORT:"
    for node in topoList:
        print node
    print
