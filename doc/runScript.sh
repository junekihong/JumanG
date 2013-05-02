#!/bin/bash


rm *.aux *.log *~
rm *.dvi

latex $1
bibtex ${1%.*}.aux
latex $1
pdflatex $1

./clean.sh
#rm *.dvi
