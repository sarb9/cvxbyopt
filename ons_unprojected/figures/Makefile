.PHONY: all
.DELETE_ON_ERROR:

all: extension.pdf

extension.pdf: extension.tex
	pdflatex -interaction=nonstopmode -halt-on-error extension.tex
