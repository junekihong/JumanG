#!/usr/bin/python
from Graph import *
from GraphAnalysis import *
from math import *

def tikGraph(graph, l = None):
        analysis = GraphAnalysis(graph)
        n = analysis.numberOfNodes()
        #scaleFactor = 1 / log(n)
        scaleFactor = 0.9
        #print n, scaleFactor
        #exit()
        
	output = ""
	output += "% Tik output from JumanG\n"
	output += "\\documentclass[class=minimal,border=0pt]{article}\n"
	output += "\\usepackage{tikz}\n"
	output += "\\pagestyle{empty}\n"
	output += "\\usepackage{verbatim}\n"
	output += "\\begin{document}\n"

        #output += "\\resizebox{100}{100}{\n"
	output += "\\begin{tikzpicture}[scale="+"{0:.2f}".format(scaleFactor)+", transform shape]\n"
	output += "\t\\tikzstyle{every node} = [circle, fill=gray!30, minimum size = 2cm]\n"

	for n in graph.getNodeList():
                cleanedName = n.Name
                cleanedName = cleanedName.replace("_","")
                x = n.PosX
                y = n.PosY

		output+="\t\\node ("+cleanedName+") at ("+"{0:.2f}".format(n.PosX)+", "+"{0:.2f}".format(n.PosY)+") {"+cleanedName+"};\n"

	for n1 in graph.getNodeList():
		for (n2, t) in graph.AdjacencyList[n1]:
                        cleanedN = n1.Name
                        cleanedN = cleanedN.replace("_", "")
                        cleanedN2 = n2.Name
                        cleanedN2 = cleanedN2.replace("_","")

			if t.Type==1:
				output+="\t\\draw [->] ("+cleanedN+")--("+cleanedN2+");\n"
			else:
				output+="\t\\draw [-] ("+cleanedN+")--("+cleanedN2+");\n"


	output += "\\end{tikzpicture}\n"
        #output += "}\n"
        
	output += "\\end{document}\n"

	if l:
		f=open(l, "w")
		f.write(output)

	else:
		print output
