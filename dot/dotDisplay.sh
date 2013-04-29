#!/bin/sh

dot -Tpng $1.dot -o $1.png ; eog $1.png
