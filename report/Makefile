# Build the report. Requires pdflatex + latexmk (both present on this machine).
.PHONY: all clean watch
all:
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

watch:
	latexmk -pdf -pvc -interaction=nonstopmode main.tex

clean:
	latexmk -C
	rm -f sections/*.aux
