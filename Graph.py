#!/usr/bin/python

from pprint import pprint
from math import sqrt
from Utils import *

class Node:
    def __init__(self, name, label=None):
        self.Name = name
        self.Label = label
        self.PosX = 0
        self.PosY = 0
        self.Attributes = {}
        
    def copy(self):
        name = self.Name
        label = self.Label

        node = Node(name, label)
        node.PosX = deepcopy(self.PosX)
        node.PosY = deepcopy(self.PosY)
        node.Attributes = deepcopy(self.Attributes)
        return node
        
    def setPosition(self,x,y):
        self.PosX = x
        self.PosY = y
        
    def __str__(self):
        result = "[" + self.Name + "] @(" + str(self.PosX)+","+str(self.PosY)+")"
        
        if self.Attributes:
            result = result + "\t"
            for attribute in self.Attributes:
                result = result + attribute + ": " + self.Attributes[attribute]+ ", "
            result = result
        return result 

    def __eq__(self, other):
        return self.Name == other.Name

    def __neq__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.Name)

    def __repr__(self):
        return self.__str__()

class Edge:
    def __init__(self, n1, n2, dirType):
        self.Node1 = n1
        self.Node2 = n2
        self.Type = EdgeType(dirType)
        self.Attributes = {}

    def copy(self):
        node1 = self.Node1.copy()
        node2 = self.Node2.copy()
        dirType = self.Type.copy()

        edge = Edge(node1, node2, dirType)
        edge.Attributes = copy.deepcopy(self.Attributes)
        return edge

    def __str__(self):
        result =  "[" + self.Node1.Name + self.Type.__str__() + self.Node2.Name + "]"
        if self.Attributes:
            result = result + "\t"
            for attribute in self.Attributes:
                result = result + attribute + ": " + self.Attributes[attribute] + ", "
        return result

    def __repr__(self):
        return self.__str__()

typeDict = {
   0:0,
   1:1,
   "--":0,
   "->":1,
}

displayDict = {
   0:"--",
   1:"->",
}


class EdgeType:
    def __init__(self, edgeType):
        if(edgeType != 0 and edgeType != 1):
            edgeType = str(edgeType)
        self.Type = typeDict.get(edgeType, None)
        #print "AAAAAA", edgeType, self.Type, edgeType == "->"
        #print edgeType, edgeType.strip()
        
    def copy(self):
        theType = deepcopy(self.Type)
        edgeType = EdgeType(theType)
        return edgeType
    
    def __str__(self):
        return displayDict[self.Type]
    def __repr__(self):
        return self.__str__()




class Graph:
    def __init__(self, name = None):
        #self.NodeList = {}
        self.AdjacencyList = {}
        self.Name = name

        # 0 is an undirected graph.
        # 1 is a directed graph.
        self.Type = None

    def copy(self):
        name = deepcopy(self.Name)
        graph = Graph(name)
        graph.Type = self.Type

        for node in self.AdjacencyList:
            copiedNode = node.copy()
            graph.AdjacencyList[copiedNode] = []
            edgeList = self.AdjacencyList[node]
            
            for (node2,Type) in edgeList:
                copiedNode2 = node2.copy()
                copiedType = Type.copy()
                copiedEdge = Edge(copiedNode, copiedNode2, copiedType)
                
                graph.addEdge(copiedEdge)
                #graph.AdjacencyList[copiedNode].append((copiedNode2,copiedType))
        return graph


    def getNodeList(self):
        return self.AdjacencyList.keys()

    def addNode(self, n):
        #if self.NodeList.get(n,None) == None:
        #    self.NodeList[n] = True
        if self.AdjacencyList.get(n,None) == None:
            self.AdjacencyList[n] = []
        else:
            index = self.AdjacencyList.keys().index(n)
            node = self.AdjacencyList.keys()[index]
            node.Name = n.Name
            node.Attributes = n.Attributes
            node.Label = n.Label
            node.PosX = n.PosX
            node.PosY = n.PosY

    def addEdge(self, e):
        #If both node1 and node2 of the edge does not exist:
        if self.AdjacencyList.get(e.Node1,None) == None and self.AdjacencyList.get(e.Node2,None) == None:
            self.AdjacencyList[e.Node2] = []
            self.AdjacencyList[e.Node1] = [(e.Node2, e.Type)]
        # If node1 does not exist and node2 does:
        elif self.AdjacencyList.get(e.Node1,None) == None:
            node2 = self.AdjacencyList.keys().get(e.Node2)
            self.AdjacencyList[e.Node1] = [(node2, e.Type)]
        # If node2 does not exist and node1 does: 
        elif self.AdjacencyList.get(e.Node2,None) == None:
            self.AdjacencyList[e.Node2] = []
            self.AdjacencyList[e.Node1].append((e.Node2, e.Type))
        # Else, both exist:
        else:
            index = self.AdjacencyList.keys().index(e.Node2)
            node2 = self.AdjacencyList.keys()[index]
            self.AdjacencyList[e.Node1].append((node2, e.Type))


    def __str__(self):
        result = "Graph "
        
        if self.Name != None:
            result = result + self.Name + " "

        if self.Type != None:
            result = result + "(" + {0:"Undirected Graph", 1:"Directed Graph"}[self.Type] + ")"

        result = result + "\n"
        result = result + "Nodes: \n"
        
        for n1 in self.getNodeList():
            result = result + n1.__str__() + ", "

        result = result + "\n\n"
        result = result + "Adjacencies: "
        result = result + " {\n"
        for n1 in self.AdjacencyList:
            edgeList = self.AdjacencyList[n1]
            result = result + n1.__str__() + "\t"
            for (n2,Type) in edgeList:
                result = result + "(" + Type.__str__() + " " + n2.__str__() + ") , "

            result = result + "\n"
        result = result + "}\n"
       
        return result
    def __repr__(self):
        return self.__str__()

    @staticmethod
    def nodeDist(n1, n2):
        x = n1.PosX - n2.PosX
        y = n1.PosY - n2.PosY
        return sqrt(x**2 + y**2)

    @staticmethod
    def nodeDistVect(n1, n2):
        return (n1.PosX-n2.PosX, n1.PosY-n2.PosY)



if __name__ == "__main__":
    graph = Graph()
    n1 = Node("1")
    n1.setPosition(1,1)
    n2 = Node("2")
    n2.setPosition(2,2)
    graph.addNode(n1)
    graph.addNode(n2)
    e1 = Edge(n1,n2,"->")
    graph.addEdge(e1)
    
    graph2 = graph.copy()
    nodes2 = graph2.AdjacencyList.keys()
    for n in nodes2:
        n.setPosition(n.PosX*10,n.PosY*10)

    print graph
    print graph2
