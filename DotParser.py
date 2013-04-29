#!/usr/bin/python

from Utils import *
from Graph import *


class DotParser:

   def __init__(self):
      self.Graph = Graph()

   def readFile(self, filename):
      FILE = open(filename,'r')
      FILE = FILE.read()

      # find outer { }
      outer = 0
      for x in FILE:
         outer = outer + 1
         if x == "{":
            break
      if outer == 0:
         print "ERROR"
         exit()
      outerClose = outer
      braceStack = 1
      for x in range(outer,len(FILE)):
         if FILE[x] == "{":
            braceStack = braceStack + 1
         if FILE[x] == "}":
            braceStack = braceStack - 1
         
         if braceStack == 0:
            break
         outerClose = outerClose + 1
            

      # From within the outer { } braces, we parse the graph
      graphText = FILE[outer:outerClose].strip().split("\n")
      commentBlock = False
      
      for line in graphText:                  
         # Strip away surrounding whitespace
         line = line.strip()

         #Handling comments
         if commentBlock and ("*/" not in line):
            continue
         elif "*/" in line:
            commentBlock = False
            line = line[line.index("*/")+2:]
         if "/*" in line:
            commentBlock = True
            line = line[:line.index("/*")]
         if "//" in line:
            line = line[:line.index("//")]                  
         if len(line) == 0:
            continue

         # Gets rid of the semicolon at the end.
         if line[-1] == ";":
            line = line[:-1]

         # Directed Edges
         if "->" in line:
            #Strip away the edge attributes
            (line,attributes) = stripAttributes(line)

            edgeLine = line.strip().split("->")
            n1 = Node(edgeLine[0].strip())
            n2 = Node(edgeLine[1].strip())
            e = Edge(n1,n2,"->")
            self.Graph.addEdge(e)
         # Undirected Edges
         elif "--" in line:
            #Strip away the edge attributes
            (line,attributes) = stripAttributes(line)

            edgeLine = line.strip().split("--")
            n1 = Node(edgeLine[0].strip())
            n2 = Node(edgeLine[1].strip())
            e1 = Edge(n1,n2,"--")
            e2 = Edge(n2,n1,"--")
            
            e1.Attributes = attributes
            e2.Attributes = attributes            

            self.Graph.addEdge(e1)
            self.Graph.addEdge(e2)
         elif "[" in line and "]" in line:
            #Information about the node
            (line,attributes) = stripAttributes(line)            
            name = line.strip()
            n = Node(name)
            n.Attributes = attributes

            self.Graph.addNode(n)

      for n in self.Graph.AdjacencyList:
         self.Graph.addNode(n)
      return self.Graph


if __name__ ==  "__main__":
   parser = DotParser()

   n1 = Node("A")
   print n1

   n2 = Node("B")
   print n2

   e1 = Edge(n1,n2, "--")
   print e1

   g = Graph("Z")
   g.addEdge(e1)
   print g
   
   print "----"
   print 

   #try:
   filename = argv[1]
   graph = parser.readFile(filename)

   print graph

#   except(IndexError):
#      print "ERROR: No file given"

   
