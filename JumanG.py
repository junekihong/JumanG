#!/usr/bin/python

from Utils import *
from DotParser import *
import TikzWriter as TW

import RadialDisplay as RD

from sys import argv

class JumanG:
    
    def __init__(self, infile):
        self.Parser = DotParser()
        self.Graph = Parser.readFile(infile)
    

    def outputToTikz(outfile):
        TW.tikGraph(self.Graph, outfile)
        
    def runRadial(self):
        RD.radialAssign(self.Graph)

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
    juman.runRadial()
    juman.outputToTikz()

