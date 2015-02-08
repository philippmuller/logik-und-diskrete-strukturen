SHELL := /bin/bash
new_path="pdfs/$(ex).pdf"

all: $(ex).tex
	open "$(new_path)"

all_sources=$(shell basename solutions/*.tex)
save: $(all_sources)

%.tex:
	@echo "-> running pdflatexfor $@"
	echo "\\newcommand{\currentexercise}{$@}" > tmp.tex
	pdflatex exercises.tex
	mkdir -p pdfs
	mv "exercises.pdf" "pdfs/$(addsuffix .pdf, $(basename $@))"; \
