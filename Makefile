SHELL := /bin/bash
ex=11
all: exercises.tex
	echo "\\newcommand{\currentexercise}{$(ex).tex}" > tmp.tex
	pdflatex exercises.tex
	open exercises.pdf


all_sources=$(shell basename solutions/*.tex)
save: $(all_sources)

%.tex:
	@echo "-> running pdflatexfor $@"
	echo "\\newcommand{\currentexercise}{$@}" > tmp.tex
	pdflatex exercises.tex
	mv "exercises.pdf" "pdfs/$(addsuffix .pdf, $(basename $@))"; \
