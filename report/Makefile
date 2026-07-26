# Build the report. Requires pdflatex + latexmk (both present on this machine).
.PHONY: all clean watch defs check-defs dag check-dag stats stats-check stats-refresh

DEFS_GEN  = ../scripts/gen-report-defs.py
DAG_GEN   = ../scripts/gen-report-dag.py
STATS_GEN = ../scripts/gen-report-stats.py

# `make` re-renders the generated layers that own a committed snapshot (defs, stats) first, so a
# stale generated/ can never silently reach the PDF. It does NOT re-mine the live repositories —
# that is the deliberate `make stats-refresh` step (see report/README.md and the colophon of
# report/sections/40_campaign_statistics.tex).
all: defs stats
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

# Campaign-statistics layer (report/generated/stats/*.tex) ---------------------
stats:                     ## render report/generated/stats/*.tex from the committed snapshot
	python3 $(STATS_GEN)

stats-check:               ## the freshness gate (also run by scripts/check-all.sh)
	python3 $(STATS_GEN) --check

stats-refresh:             ## RE-MINE the live repositories into the committed snapshot, then render
	python3 $(STATS_GEN) --extract

watch:
	latexmk -pdf -pvc -interaction=nonstopmode main.tex

clean:
	latexmk -C
	rm -f sections/*.aux
