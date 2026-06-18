all: report.pdf

report.pdf: report.tex references.bib
	pdflatex report.tex
	bibtex report
	pdflatex report.tex
	pdflatex report.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.pdf *.png
