# BRIEF v2 — the bijectivity bridge + typed M17 package (aism-73ur; user scope decision 2026-08-01)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation. Write to
`docs/plans/2026-08-01-M17-TYPING-design/DESIGN-M17-TYPING-v2.md`.
A fresh hostile audit and user ratification follow.

## Context

Read `BRIEF-M17-TYPING.md` and `DESIGN-M17-TYPING.md` (v1) in this
directory first. v1 established: the typed M17 contract (its §1 candidate is
a good draft) is consumer-dischargeable EXCEPT for bijectivity of the four
corner maps — M12 proves it internally (its tree's nodes 1.4/1.6) but
exports no such clause. The USER has decided the scope (2026-08-01,
in-session): **a NEW bijectivity bridge row** — no amendment to any T0 row
(M12, M19-S3 stay frozen exactly as banked).

## Your task — the complete two-row package

1. **The bridge row** — propose id (suggestion:
   `lem-maincb-cross-datum-bijectivity`; final naming yours), with:
   - a one-physical-line ASCII contract exporting BIJECTIVITY of the four
     fixed level-one corner maps of the Stage-3 four-corner datum that
     lem-maincb-cross-class-merging-datum furnishes, under M12's exact
     hypotheses (quote them; the bridge quantifies over the same supplied
     data so its conclusion attaches to the SAME explicit datum — make the
     same-datum identification typed-witness-lawful, not anaphoric);
   - proof route: re-derive bijectivity from the construction — the two
     diagonal maps are outer-compressions of the supplied extended reset
     ISOMORPHISMS (bijective by def-extended-delta-inclusion; check what
     lem-maincb-outer-compression-transfer exports about preserving
     bijectivity at level one) and the two zero-corner maps are the unique
     maps between zero corners (`lem-maincb-cross-union-zero-corners`, T0);
     cite exact T0 export loci for each step;
   - defs/deps (all T0 or cited), provenance loci
     (`approximate_algebras.tex:1325-1359,1363-1369` as applicable), budget
     (nodes/rounds/cap).
2. **The typed M17 contract** — start from v1 §1's candidate; add the
   bridge row to deps; restate the bijectivity hypothesis so that M26
   discharges it VIA THE BRIDGE (trace the discharge chain
   M26 -> M19-S3 -> M12 + bridge, quoting each exporting clause). Keep the
   sign-safe C_iso_unit handling v1 prescribed (ch-40fe16a76915988d).
3. **Full dischargeability re-check** for M26 (every M17 hypothesis, one
   line each: which T0 clause supplies it).
4. **Budgets + re-seed guidance**: bridge row fresh; M17 re-seed per v1 §4
   (6-node positive tree; countermodel retained as red test).
5. **Risk register**: what a hostile verifier attacks first on each row;
   top two ways this could be wrong.

## Hard constraints

- Exactly ONE new row + ONE amended contract (M17). NO def changes, NO T0
  amendments. If that cannot work, STOP and report why.
- Typed-witness laws i/ii; dimension-free; no numerical constants in
  contracts; exact refs/ loci (L1).
- The bridge must be provable from EXPORTED T0 clauses + the pinned source
  only — if any needed fact is neither exported nor at a citable locus,
  STOP and say exactly what is missing.
