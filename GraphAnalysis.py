#!/usr/bin/python

from collections import deque
from DotParser import *


class GraphAnalysis:
    def __init__(self, graph):
        self.Graph = graph
        self.RootNode = None
        self.DependencyTable = self.buildDependencyTable(self.Graph)


    def buildDependencyTable(self, graph):
        return None


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
    
