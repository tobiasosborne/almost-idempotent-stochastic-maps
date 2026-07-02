#!/usr/bin/env python3
"""gen-dag-figure.py — render the argument DAG as a GraphViz figure for the report.

Reuses argument.py's registry parser so the figure is a faithful view of the live
registry (argument/lemmas/*.md). Emits report/figures/dag.dot and, when `dot`
(GraphViz) is on PATH, report/figures/dag.pdf — a vector PDF that latexmk can
\\includegraphics without shell-escape.

This is a one-shot helper, deliberately NOT wired into scripts/check-all.sh (the
figure is a committed artifact like report/main.pdf). Re-run by hand when the
registry changes:

    python3 scripts/gen-dag-figure.py

Node colour encodes status (checked in priority order):
  af-validated -> green | cited -> blue | open -> red | obstruction -> amber |
  otherwise (proved-in-prose, not yet formalised) -> grey.
"""
import sys
import shutil
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import argument  # noqa: E402  — reuse parse_registry / ARG_DIR (importing does not run main())

FIG_DIR = ROOT / "report" / "figures"


def node_fill(l):
    af = l.get("af", "none")
    status = l.get("status", "")
    kind = l.get("kind", "")
    if af == "validated":
        return "#b7e4c7"        # green  — machine-validated
    if status == "cited":
        return "#cfe2ff"        # blue   — from the literature
    if status == "open" or kind == "open-problem":
        return "#ffd6d6"        # red    — open problem / target
    if kind == "obstruction" or status == "obstruction":
        return "#ffe5b4"        # amber  — obstruction / no-go
    return "#e9ecef"            # grey   — proved in prose, not yet af


def build_dot(lemmas):
    ids = {l["id"] for l in lemmas}
    out = [
        "digraph argument {",
        "  rankdir=LR;",
        "  graph [ranksep=0.7, nodesep=0.16];",
        '  node [shape=box, style="rounded,filled", fontname="Helvetica",'
        ' fontsize=9, margin="0.07,0.03"];',
        '  edge [color="#9aa0a6", arrowsize=0.6];',
    ]
    for l in sorted(lemmas, key=lambda d: d.get("id", "")):
        label = l["id"].replace('"', "")
        out.append(f'  "{l["id"]}" [label="{label}", fillcolor="{node_fill(l)}"];')
    for l in lemmas:
        for d in l.get("deps", []):
            if d in ids:
                out.append(f'  "{d}" -> "{l["id"]}";')
    out.append("}")
    return "\n".join(out) + "\n"


def main():
    lemmas, errors = argument.parse_registry(argument.ARG_DIR)
    for e in errors:
        print(f"registry parse warning: {e}")
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    dot = FIG_DIR / "dag.dot"
    dot.write_text(build_dot(lemmas), encoding="utf-8")
    print(f"wrote {dot.relative_to(ROOT)} ({len(lemmas)} nodes)")
    if shutil.which("dot"):
        pdf = FIG_DIR / "dag.pdf"
        subprocess.run(["dot", "-Tpdf", str(dot), "-o", str(pdf)], check=True)
        print(f"wrote {pdf.relative_to(ROOT)}")
    else:
        print("dot (GraphViz) not on PATH — wrote .dot only; "
              "render report/figures/dag.pdf on a machine with graphviz")


if __name__ == "__main__":
    main()
