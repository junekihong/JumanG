#!/usr/bin/python
from Graph import *

def tikGraph(graph, l = None):
	output = ""
	output += "% Tik output from JumanG\n"
	output += "\\documentclass{article}\n"
	output += "\\usepackage{tikz}\n"
	output += "\\pagestyle{empty}\n"
	output += "\\usepackage{verbatim}\n"
	output += "\\begin{document}\n"
	output += "\\begin{tikzpicture}[scale=.9, transform shape]\n"
	output += "\t\\tikzstyle{every node} = [circle, fill=gray!30, minimum size = 2cm]\n"

	for n in graph.getNodeList():
                cleanedName = n.Name
                cleanedName = cleanedName.replace("_","")
                
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
	output += "\\end{document}\n"

	if l:
		f=open(l, "w")
		f.write(output)

	else:
		print output
