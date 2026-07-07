---
id: conj-tall-zero-face-radial-thickness
kind: lemma
contract: (CONJECTURE) Tall zero-face radial thickness: there exist universal a >= 4, theta in (0,1), delta_0 > 0, and mu = mu(delta, tau, theta) > 0 such that in the tall heavy near-cluster regime (exact signed idempotent, 0 < delta <= delta_0, W(P) nonempty, hidden top v with H > ((5a/4 + 3/2)/theta)*tau carrying near-deep cluster mass >= 1 - theta), v admits an optimal hiddenness datum (h*, lambda, beta) with tangential residual R = 0 or with radial reach r = sup{r' : r'*(R/||R||_1) in conv{p_i - p_v : h*(p_i) = 0}} >= mu.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: 
status: conjecture
af: none
provenance: W41 wave (docs/waves/2026-07-07-W41-tall-blowup-decider.md): the residual named by worker AN (VAN-corrected form); exact-certificate support from worker AM (in every certified construction the alpha blow-up and the hidden-TOP condition are mutually exclusive — forcing v top collapses A_min to 0)
owner: A
workspace: proofs/conj-tall-zero-face-radial-thickness
---

**Role (the named intermediate under the absorption program).** Via
[[lem-radial-alpha-bound]] this gives tall-mode alpha control, which unblocks the
witness-aggregation route toward [[conj-near-cluster-absorption]] (W39-AI's subtraction
becomes coefficient-bounded). HONEST SCOPE: an intermediate, NOT the full residual — even
with bounded alpha the aggregated circuits only upper-bound t* (the dual-direction wall); the
absorption conclusion still needs the primal/feasibility conversion. Certified evidence (W41
bundle): four exact families where topness kills the blow-up; no tall instance with thin
zero face exists in the record.

**Status discipline.** A conjecture — promotes nothing.
