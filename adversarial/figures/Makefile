.PHONY: all
.DELETE_ON_ERROR:

all: extension.pdf algorithm.pdf

%.pdf: %.tex
	pdflatex -interaction=nonstopmode -halt-on-error $<
