#!/usr/bin/python

from Utils import *
from DotParser import *
import TikzWriter as TW

import RadialDisplay as RD

from sys import argv


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

    Parser = DotParser()
    graph = Parser.readFile(infile)

    RD.radialAssign(graph)

    TW.tikGraph(graph, outfile)

