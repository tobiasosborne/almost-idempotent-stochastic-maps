"""Shared af proof-tree size constants (aism-s64) — the ONE source of truth read by BOTH
scripts/argument.py (the linker's brittleness REFACTOR warning) and scripts/af-orchestrate.py
(the balloon-tripwire --node-cap default), so the two gates cannot drift apart again.

History of the drift this file fixes: the linker warned above 12 nodes while the orchestrator's
balloon guard defaulted to 40 and actual af-VALIDATED trees in this repo run 14-52 total nodes —
so the linker cried REFACTOR on ~20 perfectly healthy validated trees (noise that buries the
signal). NODE_SOFT_CAP realigns the warning to flag only the genuine extremes (the >26-node
trees: lem-residual-upper 52, lem-residual-lower 36, lem-collateral-import 32,
lem-hiddenness-depth-markov 32, lem-classical-equiv 29, lem-fan-payment-restricted 27).

Usage:
  * argument.py:      warn REFACTOR only when an af tree exceeds NODE_SOFT_CAP nodes.
  * af-orchestrate.py: --node-cap (abort on live, non-archived nodes) defaults to
    2*NODE_SOFT_CAP = 52 — headroom for legitimate large trees, while genuine balloons
    (observed 75-102 nodes) still trip it well before burning the round budget.
"""

NODE_SOFT_CAP = 26
