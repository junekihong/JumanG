#!/usr/bin/python

from pprint import pprint

class Node:
    def __init__(self, name, label=None):
        self.Name = name
        self.Label = label
        self.PosX = 0
        self.PosY = 0
        self.Attributes = {}

    def __str__(self):
        result = "[" + self.Name + "]"

        if self.Attributes:
            result = result + "\t"
            for attribute in self.Attributes:
                result = result + attribute + ": " + self.Attributes[attribute]+ ", "
            result = result + "\n"

        return result 

    def __eq__(self, other):
        return self.Name == other.Name


    def __neq__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.Name)

class Edge:
   def __init__(self, n1, n2, dirType):
      self.Node1 = n1
      self.Node2 = n2
      self.Type = EdgeType(dirType)
      self.Attributes = {}

   def __str__(self):
      result =  "[" + self.Node1.Name + self.Type.__str__() + self.Node2.Name + "]"
      if self.Attributes:
          result = result + "\t"
          for attribute in self.Attributes:
              result = result + attribute + ": " + self.Attributes[attribute] + ", "

      return result

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
      self.Type = typeDict.get(edgeType, None)

   def __str__(self):
      return displayDict[self.Type]




class Graph:
    def __init__(self, name = None):
        self.NodeList = {}
        self.AdjacencyList = {}
        self.Name = name
        

    def addNode(self, n):
        if self.NodeList.get(n,None) == None:
            self.NodeList[n] = True

    def addEdge(self, e):
        if self.AdjacencyList.get(e.Node1,None) == None:
            self.AdjacencyList[e.Node1] = [(e.Node2, e.Type)]
        else:
            self.AdjacencyList[e.Node1].append((e.Node2, e.Type))


    def __str__(self):
        result = "Graph "
        
        if self.Name != None:
            result = result + self.Name

        result = result + "\n"
        result = result + "Nodes: \n"
        
        for n1 in self.NodeList:
            result = result + n1.__str__()

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
