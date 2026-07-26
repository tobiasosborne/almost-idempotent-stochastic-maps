# BRIEF — S1-POLAR repair round (fresh designer; input = design + hostile audit)

You are a fresh, independent design mathematician. A prior designer produced
`DESIGN-S1-POLAR.md` (8-row polar sub-DAG) and a hostile auditor returned
**REDESIGN** in `AUDIT-S1-POLAR.md` with three blockers (its §0) and per-row
corrections (its §3). Your job: produce the repaired design that clears every
audit finding — or show a finding cannot be cleared from local sources.

Read, in order: `BRIEF-S1-POLAR.md` (original constraints — all still bind),
`DESIGN-S1-POLAR.md`, `AUDIT-S1-POLAR.md` (BINDING: treat every finding as
mandatory unless you can refute it with exact loci), plus the sources both
cite.

## The three blockers to clear

1. **Smoothness mismatch (audit §0.1).** The polar rows deliver C¹; the
   landed topology consumers (`lem-topology-quotient-manifold`,
   `lem-topology-finite-triangulation`, `lem-topology-local-index-sign` —
   read their landed contracts) demand smooth. Kitaev's TeX makes the same
   unsupported C¹→smooth jump (795–807 vs 947–954). Resolve it:
   - FIRST check the local refs for a C¹→C^∞ (or C^r→C^s) compatible-structure
     upgrade theorem: `refs/munkres-elementary-differential-topology/` is in
     the manifest (Munkres, *Elementary Differential Topology*) and is the
     most likely local home for smoothing/approximation theorems — cite exact
     theorem numbers and page loci if found; also check
     `refs/lee-smooth-manifolds/` and `refs/hatcher-algebraic-topology/`.
   - Design the minimal producer row(s): e.g. a compatible smooth structure on
     the C¹ quotient + smooth approximation of the C¹ inversion self-map
     preserving its fixed-point/index data, with every hypothesis matched to
     the landed consumers' contracts.
   - If a required upgrade theorem is NOT in local refs, say NOT IN LOCAL
     REFS, name the precise classical statement needed, and STOP on that
     point (it becomes a source-acquisition escalation, not a guess).
   - Re-scoping the LANDED topology rows to C¹ is NOT yours to decide: if you
     conclude that is the better route, mark it USER-DECISION with the exact
     trade-off, and still provide the smoothing alternative.
2. **Self-containment (audit §0.2).** Every proposed contract must be
   readable stand-alone: inline `r_±`, `η_path` with where-clauses; replace
   free cross-row witnesses by per-row existential quantification or an
   explicit witness-package produced by a dependency row (theorem-free datum
   discipline, R35). Follow the audit's per-row corrections in its §3.
3. **Dependency completeness (audit §0.3).** Add the missing
   group-laws → derivative-control edge; produce an explicit obligation
   ledger for `lem-stage1-extra-fixed-class` (each landed consumer
   obligation → which row discharges it, including the maximal-simplex
   obligation on `lem-topology-lefschetz-hopf` and the new smoothness rows).

## Deliverable — write `docs/plans/2026-07-26-S1-POLAR-design/DESIGN-S1-POLAR-v2.md`

Same table format and discipline as the original brief (closed formula-level
contracts, per-row feasibility verdicts, dimension-freeness audit, unblocking
map, definition provisioning, ≤12 nodes / depth ≤3 per row). Include a
"disposition of audit findings" table: every AUDIT-S1-POLAR finding →
CLEARED-BY (what changed) / REFUTED (exact loci) / ESCALATED (user decision or
source acquisition, precisely stated).

## Hard constraints

Unchanged from the original brief: design only; write ONLY inside
`docs/plans/2026-07-26-S1-POLAR-design/`; no registry mutation; no status
promotion; no guessed radii; NOT IN LOCAL REFS discipline; hostile stance —
an uncloseable finding honestly escalated beats a papered-over one.
