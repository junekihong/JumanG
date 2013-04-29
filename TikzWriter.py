from Graph import *

def tikGraph(graph, l = None):
	output = ""
	oputput += "% Tik output from JumanG\n"
	output += "\\documentclass{article}\n"
	output += "\\usepackage{tikz}\n"
	output += "\\pagestyle{empty}\n"
	output += "\\usepackage{verbatim}\n"
	output += "\\begin{document}\n"
	output += "\\begin{tikzpicture}[scale=.9, transform shape]\n"
	output += "\t\\tikzstyle{every node} = [circle, fill=gray!30, minimum size = 2cm]\n"

	for n in graph.NodeList:
		output+="\t\\node ("+n.Name+") at ("+n.Posx+", "+n.PosY+") {"+n.Name+"};\n"

	for n1 in graph.NodeList:
		for n2 in graph.AdjacencyList[n1]:
			output+="\t\\draw [->] ("+n1.Name+")--("+n2.Name+");\n"

	output += "\\end{tikzpicture}\n"
	output += "\\end{document}\n"

	if l:
		f=open(l, "r")
		f.write(output)

	else:
		print output
