JumanG - "Graph drawing unleashed"

Declarative Methods Final Project (600.425)
Professor Eisner
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
./Dotparser.py [dot file] [optional output file]

So for example:
./Dotparser.py temp.dot
Will parse the temp.dot file and then solve and display it using Tikz LaTeX.


