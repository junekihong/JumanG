#!/usr/bin/python

from pprint import pprint
from sys import argv
from copy import deepcopy
from math import pow


def stripAttributes(line):
   #Strip away the edge attributes                                                                                                                    
   attributeLine = ""
   attributes = {}
   if "[" in line and "]" in line:
      attributeLine = line[line.index("[")+1 : line.index("]")]
      line = line[:line.index("[")] + line[line.index("]")+1:]

      # Encode the edge attributes as a dict                                                                                                          
      if "," in attributeLine:
         attributeLine = attributeLine.split(",")
      else:
         attributeLine = [attributeLine]
      for attribute in attributeLine:
         attribute = attribute.split("=")
         attributes[attribute[0]] = attribute[1].strip("\"")

   return (line,attributes)


