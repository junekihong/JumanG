JumanG - "Graph drawing unleashed"

Declarative Methods Final Project (600.425)
Professor Jason Eisner
May 2013

Project members:
-Michael Tango (mtango1@jhu.edu)
-Juneki Hong (juneki@jhu.edu)


Prereqs in order to run our project:
-python
-pdflatex and evince (to compile the Tikz LaTeX and view the pdf)
-GraphViz (we borrowed GraphViz's ring solver for our project)

Without latex, you can still run our project and look at the output file.
Without GraphViz's Circo program, you will not be able to display directed cycle graphs.


In order to run the parser, just call:
./JumanG [dot file] [optional output file]

So for example:
./JumanG dot/ethane.dot
Will parse in the ethane.dot file, then solve, and then display it using Tikz LaTeX.




Files:
JumanG			The run script that runs the program and displays the results
JumanG.py		The program that will call the parsers and solvers
Graph.py		Datastructures that store the representation of the graph
GraphAnalysis.py	Analysis tools that are used by JumanG.py that help determine which solver to use
DotParser.py		The dot parser used to parse in a graph represented in a dot file.
TikzWriter.py		Used to output tikz latex in the end for display.

dot/*			Dot files that represent graphs are stored here as examples
Solvers/*		All of the individuals solvers that can be called are implemented here
doc/*			The documents and our writeup is located here.