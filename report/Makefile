# Build the report. Requires pdflatex + latexmk (both present on this machine).
.PHONY: all clean watch defs check-defs dag check-dag

DEFS_GEN = ../scripts/gen-report-defs.py
DAG_GEN  = ../scripts/gen-report-dag.py

all: defs
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Re-render generated/defs/ from the canonical definitions/ shards (tracked output).
defs:
	python3 $(DEFS_GEN) --dag-anchors

# The gate's view of the same thing; also wired into scripts/check-all.sh.
check-defs:
	python3 $(DEFS_GEN) --check --dag-anchors

# Regenerate the argument-DAG atlas from the registry shards (report/generated/dag/*.tex +
# sections/39_argument_dag.tex). Deliberately NOT a prerequisite of `all`: generation is an
# explicit act (like argument.py --generate); the freshness CHECK lives in scripts/check-all.sh.
dag:
	python3 $(DAG_GEN)

check-dag:
	python3 $(DAG_GEN) --check

watch:
	latexmk -pdf -pvc -interaction=nonstopmode main.tex

clean:
	latexmk -C
	rm -f sections/*.aux
