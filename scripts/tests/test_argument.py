#!/usr/bin/env python3
"""
Red-green tests for scripts/argument.py — the argument-DAG linker. Written test-FIRST.
Drives the pure check functions with synthetic registries + injected af "workspace facts";
no real af workspaces needed. Run: python3 scripts/tests/test_argument.py
"""
import importlib.util
import json
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("argument", ROOT / "scripts" / "argument.py")
ag = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ag)

passed = failed = 0
def check(name, cond):
    global passed, failed
    if cond: passed += 1; print(f"PASS  {name}")
    else:    failed += 1; print(f"FAIL  {name}")
def has(msgs, sub): return any(sub in m for m in msgs)

def L(id, deps=(), defs=(), af="none", status="proved", contract="C", workspace=None):
    return {"id": id, "deps": list(deps), "defs": list(defs), "af": af,
            "status": status, "contract": contract,
            "workspace": workspace or f"proofs/{id}"}

def R(id, deps=(), routes=(), defs=(), af="none", status="proved", contract="C", workspace=None):
    """Like L() but with an OR-ROUTE list: routes = ((m1,m2),(m3,)) -> [[m1,m2],[m3]]."""
    d = L(id, deps=deps, defs=defs, af=af, status=status, contract=contract, workspace=workspace)
    d["routes"] = [list(r) for r in routes]
    return d

# --- check_acyclic ---
chain = [L("a", deps=[]), L("b", deps=["a"]), L("c", deps=["b"])]
check("acyclic chain -> no error", ag.check_acyclic(chain) == [])
cyc = [L("a", deps=["b"]), L("b", deps=["a"])]
check("cycle is caught", has(ag.check_acyclic(cyc), "cycle"))

# --- check_imports ---
ids_ok = [L("a"), L("b", deps=["a"], defs=["def-x"])]
check("resolvable imports -> no error", ag.check_imports(ids_ok, {"def-x"}) == [])
bad_dep = [L("b", deps=["nope"])]
check("dangling dep is caught", has(ag.check_imports(bad_dep, set()), "nope"))
bad_def = [L("b", defs=["def-nope"])]
check("dangling def is caught", has(ag.check_imports(bad_def, {"def-x"}), "def-nope"))

# --- check_status: validated cannot rest on unvalidated; frontier/blocked ---
inconsistent = [L("a", af="none"), L("b", deps=["a"], af="validated")]
errs, ready, blocked = ag.check_status(inconsistent)
check("validated-on-unvalidated is caught", has(errs, "validated"))
prop = [L("a", af="validated", status="proved"),
        L("b", deps=["a"], af="none", status="proved"),
        L("c", deps=["b"], af="none", status="proved")]
errs, ready, blocked = ag.check_status(prop)
check("frontier: b ready (deps validated)", "b" in ready)
check("frontier: c blocked (dep b not validated)", "c" in blocked)
check("frontier: c not ready", "c" not in ready)

# --- check_status: a GROUND-TRUTH LEAF (status=cited, af=none) is an AVAILABLE dep ---
# A is a validated internal lemma; L is a cited leaf (e.g. prop-kadison-js / Kadison's
# inequality), never af-proven; B rests on both. B must be READY (not blocked) and must NOT
# trigger the af=validated-but-dep-unvalidated error even when later marked af=validated.
grounded = [L("A", af="validated", status="proved"),
            L("L", deps=[], af="none", status="cited"),
            L("B", deps=["A", "L"], af="none", status="proved")]
errs, ready, blocked = ag.check_status(grounded)
check("grounded leaf: B ready (cited dep is available)", "B" in ready)
check("grounded leaf: B not blocked", "B" not in blocked)
check("grounded leaf: no spurious error about B", not has(errs, "B"))
# and B may later be af=validated resting on a merely-cited leaf without an error
grounded_v = [L("A", af="validated", status="proved"),
              L("L", deps=[], af="none", status="cited"),
              L("B", deps=["A", "L"], af="validated", status="proved")]
errs_v, _, _ = ag.check_status(grounded_v)
check("grounded leaf: af=validated B over cited leaf -> no error", not has(errs_v, "B"))
# CONTROL: an OPEN (not cited) dep is NOT a leaf -> dependent stays blocked, not ready
control = [L("O", deps=[], af="none", status="open"),
           L("D", deps=["O"], af="none", status="proved")]
errs_c, ready_c, blocked_c = ag.check_status(control)
check("control: dep on OPEN result stays blocked", "D" in blocked_c)
check("control: dep on OPEN result not ready", "D" not in ready_c)

# --- check_contracts: drift between registry and af root ---
lemmas = [L("a", contract="For r in A,  q_r >= 0.")]   # note: double space after comma
ws_match = {"a": "For r in A, q_r >= 0."}              # whitespace differs only (single space)
ws_drift = {"a": "For r in A, q_r >= 1."}
check("contract match (whitespace) -> no error", ag.check_contracts(lemmas, ws_match) == [])
check("contract drift is caught", has(ag.check_contracts(lemmas, ws_drift), "drift"))

# --- check_brittleness: oversized af tree warns REFACTOR ---
lemmas = [L("a"), L("b")]
warns = ag.check_brittleness(lemmas, {"a": 5, "b": 99}, threshold=12)
check("small tree no warn", not has(warns, "proofs/a"))
check("oversized tree warns REFACTOR", has(warns, "REFACTOR") and has(warns, "b"))

# --- brittleness realignment (aism-s64): the default threshold is the ONE shared soft cap
#     (scripts/af_constants.py, also read by af-orchestrate.py's balloon guard) — validated
#     trees in this repo run 14-52 nodes, so the old 12 flagged ~20 healthy trees.
import importlib.util as _ilu
_spec_c = _ilu.spec_from_file_location("af_constants", ROOT / "scripts" / "af_constants.py")
_afc = _ilu.module_from_spec(_spec_c); _spec_c.loader.exec_module(_afc)
check("shared NODE_SOFT_CAP is 26", _afc.NODE_SOFT_CAP == 26)
check("linker default threshold == shared NODE_SOFT_CAP", ag.NODE_THRESHOLD == _afc.NODE_SOFT_CAP)
warns = ag.check_brittleness([L("a"), L("b")], {"a": 26, "b": 27})   # default threshold
check("at-soft-cap tree (26) does not warn", not has(warns, "proofs/a"))
check("just-above-soft-cap tree (27) warns", has(warns, "proofs/b"))
# .get('workspace') fix: a shard record without a workspace key must not crash the linker
warns = ag.check_brittleness([{"id": "c"}], {"c": 99})
check("missing workspace key: no KeyError, warns with fallback path",
      has(warns, "REFACTOR") and has(warns, "proofs/c"))

# --- check_orphans ---
lemmas = [L("a", af="validated", workspace="proofs/a"), L("b", af="none", workspace="proofs/b")]
errs = ag.check_orphans(lemmas, {"proofs/a"})            # b has af=none so missing dir is OK
check("af!=none with missing workspace dir is caught", errs == [])
errs = ag.check_orphans([L("a", af="seeded", workspace="proofs/a")], set())
check("seeded lemma missing workspace dir is caught", has(errs, "proofs/a"))
errs = ag.check_orphans([L("a", af="validated", workspace="proofs/a")], {"proofs/a", "proofs/ghost"})
check("workspace dir with no registry entry is caught", has(errs, "ghost"))

# --- parse_registry round-trip ---
with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d); (d / "lemmas").mkdir()
    (d / "lemmas" / "lem-x.md").write_text(
        "---\nid: lem-x\nkind: lemma\ncontract: Foo.\ndefs: def-a; def-b\ndeps: lem-y\n"
        "status: proved\naf: none\nowner: A\nworkspace: proofs/lem-x\n---\nbody\n", encoding="utf-8")
    lemmas, errs = ag.parse_registry(d)
    check("parse_registry reads one lemma", len(lemmas) == 1)
    check("parse_registry splits defs", lemmas[0]["defs"] == ["def-a", "def-b"])
    check("parse_registry splits deps", lemmas[0]["deps"] == ["lem-y"])

# --- status enum: 'stated' (manuscript-asserted, unverified) is accepted; a bogus status errors ---
with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d); (d / "lemmas").mkdir()
    (d / "lemmas" / "thm-s.md").write_text(
        "---\nid: thm-s\nkind: theorem\ncontract: Bar.\nstatus: stated\naf: none\n---\nbody\n", encoding="utf-8")
    _, errs_ok = ag.parse_registry(d)
    check("status 'stated' is an accepted MATH_STATUS (no error)", not has(errs_ok, "status"))
    (d / "lemmas" / "thm-s.md").write_text(
        "---\nid: thm-s\nkind: theorem\ncontract: Bar.\nstatus: bogus\naf: none\n---\nbody\n", encoding="utf-8")
    _, errs_bad = ag.parse_registry(d)
    check("a bogus status is still caught (enum stays closed)", has(errs_bad, "status"))

# --- --show: ancestor (transitive deps) / descendant (transitive dependents) closures ---
g = [L("a", deps=[]), L("b", deps=["a"]), L("c", deps=["b"]), L("d", deps=["a"])]
check("deps_closure(c) = {a,b}", ag.deps_closure(g, "c") == {"a", "b"})
check("deps_closure(a) = {} (leaf)", ag.deps_closure(g, "a") == set())
check("dependents_closure(a) = {b,c,d}", ag.dependents_closure(g, "a") == {"b", "c", "d"})
check("dependents_closure(c) = {} (top)", ag.dependents_closure(g, "c") == set())
check("deps_closure(unknown) -> None", ag.deps_closure(g, "zzz") is None)
check("dependents_closure(unknown) -> None", ag.dependents_closure(g, "zzz") is None)
# diamond: e depends on b,d ; b,d depend on a  -> ancestors of e = {a,b,d} (a counted once)
dia = [L("a"), L("b", deps=["a"]), L("d", deps=["a"]), L("e", deps=["b", "d"])]
check("diamond deps_closure(e) = {a,b,d}", ag.deps_closure(dia, "e") == {"a", "b", "d"})
check("diamond dependents_closure(a) = {b,d,e}", ag.dependents_closure(dia, "a") == {"b", "d", "e"})
# closures ignore dangling deps (linker catches those separately)
dangle = [L("a", deps=["ghost"]), L("b", deps=["a"])]
check("deps_closure ignores dangling dep", ag.deps_closure(dangle, "b") == {"a"})
# format_show: names the node + has ancestors/descendants sections; unknown id reports error
txt = ag.format_show(g, "b")
check("format_show names the node", "b" in txt)
check("format_show has ancestors section", "ancestors" in txt.lower())
check("format_show has descendants section", "descendants" in txt.lower())
check("format_show(unknown) reports error", "unknown" in ag.format_show(g, "zzz").lower())

# depth-3+ chain + middle node (both directions nonempty & independent)
ch5 = [L("a"), L("b", deps=["a"]), L("c", deps=["b"]), L("d", deps=["c"]), L("e", deps=["d"])]
check("deep deps_closure(e) = {a,b,c,d}", ag.deps_closure(ch5, "e") == {"a", "b", "c", "d"})
check("deep dependents_closure(a) = {b,c,d,e}", ag.dependents_closure(ch5, "a") == {"b", "c", "d", "e"})
check("middle deps_closure(c) = {a,b}", ag.deps_closure(ch5, "c") == {"a", "b"})
check("middle dependents_closure(c) = {d,e}", ag.dependents_closure(ch5, "c") == {"d", "e"})
# self-consistency invariant: x in deps_closure(y)  <=>  y in dependents_closure(x)
multi = [L("a"), L("b", deps=["a"]), L("c", deps=["a", "b"]), L("d", deps=["b", "c"])]
mids = [l["id"] for l in multi]
check("closure self-consistency (x anc-of y iff y desc-of x)",
      all((x in ag.deps_closure(multi, y)) == (y in ag.dependents_closure(multi, x))
          for x in mids for y in mids))
# format_show CONTENT: direct edges must be distinct from the transitive closures
def _val(txt, label):
    ln = next((l for l in txt.splitlines() if l.startswith(label)), "")
    return ln.split(":", 1)[1] if ":" in ln else ""
fc = ag.format_show(ch5, "c")   # c: direct dep b, direct dependent d; ancestors {a,b}, descendants {d,e}
dep_v, ddep_v = _val(fc, "deps (direct"), _val(fc, "dependents (direct")
anc_v, desc_v = _val(fc, "ancestors"), _val(fc, "descendants")
check("format_show direct deps = b only", "b[" in dep_v and "a[" not in dep_v)
check("format_show direct dependents = d only (NOT closure e)", "d[" in ddep_v and "e[" not in ddep_v)
check("format_show ancestors line = {a,b}", all(x in anc_v for x in "ab") and all(x not in anc_v for x in "de"))
check("format_show descendants line = {d,e}", all(x in desc_v for x in "de") and all(x not in desc_v for x in "ab"))

# --- render_dag / proof_class / check_generated (CI staleness gate) ---
# proof_class picks the most-solid status colour
check("proof_class: af=validated -> validated", ag.proof_class(L("x", af="validated")) == "validated")
check("proof_class: af=seeded/status=stated -> seeded", ag.proof_class(L("x", af="seeded", status="stated")) == "seeded")
check("proof_class: status=open -> open", ag.proof_class(L("x", status="open")) == "open")
check("proof_class: open-problem kind + status open -> open",
      ag.proof_class({**L("x", status="open"), "kind": "open-problem"}) == "open")
check("proof_class: status=cited -> cited", ag.proof_class(L("x", status="cited")) == "cited")
# The rigour ladder honestly: a non-rigorous STATUS (conjecture/heuristic/numerical) wins over an
# open-problem KIND, so a conjecture/heuristic reads ORANGE (non-rigorous), not RED (genuinely open).
check("proof_class: status=heuristic -> nonrigorous", ag.proof_class(L("x", status="heuristic")) == "nonrigorous")
check("proof_class: nonrigorous status beats open-problem kind",
      ag.proof_class({**L("x", status="conjecture"), "kind": "open-problem"}) == "nonrigorous")
# render_dag is deterministic and carries status colouring (the Mermaid the CI enforces)
reg = [L("lem-a", af="validated", status="proved"), L("lem-b", deps=["lem-a"], af="seeded", status="stated"),
       L("op-x", status="open", contract="C2")]
check("render_dag deterministic", ag.render_dag(reg) == ag.render_dag(reg))
dag = ag.render_dag(reg)
check("render_dag has classDef styling", "classDef validated" in dag and "classDef open" in dag)
check("render_dag colour-codes nodes by status", "validated;" in dag and "seeded;" in dag and "open;" in dag)
check("render_dag draws the dep edge", "lem-a --> lem-b" in dag)
check("render_dag carries a proof-status legend", "Proof-status legend" in dag)
# staleness gate red->green through a temp dir
with tempfile.TemporaryDirectory() as _td:
    _d = pathlib.Path(_td)
    ag.generate(reg, arg_dir=_d)
    check("fresh generated -> not stale (green)", ag.check_generated(reg, arg_dir=_d) == [])
    (_d / "DAG.md").write_text("hand-edited junk\n", encoding="utf-8")
    check("tampered DAG -> STALE (red)", has(ag.check_generated(reg, arg_dir=_d), "STALE"))
    ag.generate(reg, arg_dir=_d)
    check("regenerated -> green again", ag.check_generated(reg, arg_dir=_d) == [])
    reg2 = [L("lem-a", af="validated", status="proved"), L("lem-b", deps=["lem-a"], af="validated", status="proved"),
            L("op-x", status="open", contract="C2")]  # a status changed without regenerating
    check("shard status change without regen -> STALE", has(ag.check_generated(reg2, arg_dir=_d), "STALE"))

# --- plan_beads_sync (pure planner for --sync-beads; the executor shells out to bd, not tested here) ---
# Empty beads DB -> create every result, mirror every DAG edge, close the already-available ones
# (af=validated / status=cited — the SAME availability rule as check_status, so bd ready == frontier).
sreg = [L("lem-avail", af="validated", status="proved", contract="A validated lemma"),
        L("lem-leaf", status="cited", contract="A cited ground-truth leaf"),
        L("op-goal", deps=["lem-avail", "lem-leaf"], status="conjecture", contract="The open target")]
sreg[2]["kind"] = "open-problem"
acts, warns = ag.plan_beads_sync(sreg, {})
check("sync plan: one create per missing result", [a[0] for a in acts].count("create") == 3)
check("sync plan: creates precede deps precede closes",
      [a[0] for a in acts] == sorted([a[0] for a in acts], key=["create", "dep", "close"].index))
check("sync plan: DAG edges mirrored as bd deps",
      ("dep", "op-goal", "lem-avail") in acts and ("dep", "op-goal", "lem-leaf") in acts)
check("sync plan: available results get closed",
      any(a[0] == "close" and a[1] == "lem-avail" for a in acts)
      and any(a[0] == "close" and a[1] == "lem-leaf" for a in acts))
check("sync plan: non-available target stays open", not any(a[0] == "close" and a[1] == "op-goal" for a in acts))
check("sync plan: open-problem kind -> P1, others P2",
      next(a[4] for a in acts if a[0] == "create" and a[1] == "op-goal") == 1
      and next(a[4] for a in acts if a[0] == "create" and a[1] == "lem-avail") == 2)
check("sync plan: title starts with the registry id (the stable match key)",
      next(a[2] for a in acts if a[0] == "create" and a[1] == "op-goal").startswith("op-goal: "))
# Fully-synced beads state -> NO actions (idempotency is the contract; re-run must not duplicate).
synced = {"lem-avail": {"issue": "x-a", "status": "closed", "deps": set()},
          "lem-leaf":  {"issue": "x-l", "status": "closed", "deps": set()},
          "op-goal":   {"issue": "x-g", "status": "open", "deps": {"lem-avail", "lem-leaf"}}}
acts2, warns2 = ag.plan_beads_sync(sreg, synced)
check("sync plan: idempotent on a fully-synced state", acts2 == [] and warns2 == [])
# A result whose bd issue is closed but which is NOT rigorous -> WARN, never auto-reopen
# (a human may have deliberately de-scoped it; the mirror must not fight that silently).
descoped = dict(synced); descoped["op-goal"] = {"issue": "x-g", "status": "closed", "deps": {"lem-avail", "lem-leaf"}}
acts3, warns3 = ag.plan_beads_sync(sreg, descoped)
check("sync plan: closed-but-non-rigorous warns instead of reopening",
      acts3 == [] and has(warns3, "op-goal"))
# Partial state: issue exists but one edge is missing -> only the missing edge is planned
partial = dict(synced); partial["op-goal"] = {"issue": "x-g", "status": "open", "deps": {"lem-avail"}}
acts4, _ = ag.plan_beads_sync(sreg, partial)
check("sync plan: only the missing dep edge is added", acts4 == [("dep", "op-goal", "lem-leaf")])

# --- beads_snapshot (executor layer, injectable bd runner): the reviewer-found CLI bugs, pinned ---
# (1) `bd list` defaults to --limit 50: an unbounded mirror MUST pass --limit 0, else the snapshot
#     silently truncates once the tracker grows and re-runs create DUPLICATES (idempotency broken).
# (2) `bd dep list` returns edges of ALL types: the mirror manages only `blocks` edges, so a
#     relates-to edge between two mirror issues must never suppress a needed blocks edge.
_calls = []
def _fake_bd(cli, timeout=60):
    _calls.append(cli)
    class P: returncode = 0; stderr = ""; stdout = "[]"
    p = P()
    if cli[0] == "list":
        p.stdout = json.dumps([
            {"id": "x-1", "title": "lem-x: some contract", "status": "open"},
            {"id": "x-2", "title": "lem-y: other contract", "status": "closed"},
            {"id": "x-3", "title": "lem-z: third contract", "status": "open"},
            {"id": "x-9", "title": "unrelated infra issue", "status": "open"}])
    elif cli[:2] == ["dep", "list"] and cli[2] == "x-1":
        p.stdout = json.dumps([{"id": "x-2", "dependency_type": "blocks"},
                               {"id": "x-3", "dependency_type": "relates-to"}])
    return p
snap = ag.beads_snapshot({"lem-x", "lem-y", "lem-z"}, bd=_fake_bd)
_lists = [c for c in _calls if c[0] == "list"]
_deps = [c for c in _calls if c[:2] == ["dep", "list"]]
check("snapshot: bd list passes --limit 0 (default 50 truncates -> duplicate creates)",
      _lists and all("--limit" in c and c[c.index("--limit") + 1] == "0" for c in _lists))
check("snapshot: bd dep list passes --type blocks",
      _deps and all("--type" in c and c[c.index("--type") + 1] == "blocks" for c in _deps))
check("snapshot: only registry-titled issues are mapped",
      set(snap) == {"lem-x", "lem-y", "lem-z"})
check("snapshot: closed status survives the round-trip", snap["lem-y"]["status"] == "closed")
check("snapshot: non-blocks edges are filtered even if bd's --type filter fails",
      snap["lem-x"]["deps"] == {"lem-y"})

# =====================================================================================
# OR-ROUTE (disjunctive deps) — P0 feature aism-3ne. Grammar: routes: [a; b] | [c]
#   each bracketed group = one route (conjunction of members); groups OR-combined.
# =====================================================================================

# --- (0) parse_routes grammar ---
check("parse_routes: two routes", ag.parse_routes("[a; b] | [c]") == [["a", "b"], ["c"]])
check("parse_routes: blank/None -> []", ag.parse_routes("") == [] and ag.parse_routes(None) == [])
check("parse_routes: single group", ag.parse_routes("[a; b]") == [["a", "b"]])
check("parse_routes: whitespace + empty group tolerated", ag.parse_routes(" [ a ;b ] |  ") == [["a", "b"]])
# frontmatter round-trip: a shard with a routes: line parses into list-of-lists
with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d); (d / "lemmas").mkdir()
    (d / "lemmas" / "op-g.md").write_text(
        "---\nid: op-g\nkind: open-problem\ncontract: G.\ndeps: \n"
        "routes: [lem-a; lem-b] | [lem-c]\nstatus: open\naf: none\n---\nbody\n", encoding="utf-8")
    (d / "lemmas" / "lem-plain.md").write_text(   # no routes line at all
        "---\nid: lem-plain\nkind: lemma\ncontract: P.\ndeps: op-g\nstatus: proved\naf: none\n---\nx\n", encoding="utf-8")
    _lem, _e = ag.parse_registry(d)
    _byid = {x["id"]: x for x in _lem}
    check("parse_registry: routes parse to list-of-lists", _byid["op-g"]["routes"] == [["lem-a", "lem-b"], ["lem-c"]])
    check("parse_registry: no-routes shard -> [] (backward-compat)", _byid["lem-plain"]["routes"] == [])

# --- (1) disjunctive ready/blocked: ready iff SOME route fully available; blocked iff none ---
reg = [L("X", af="validated", status="proved"), L("Y", af="none", status="proved"),
       R("G", routes=[["X"], ["Y"]], af="none", status="proved")]
_, ready, blocked = ag.check_status(reg)
check("OR-route: G ready when route1 (X validated) fires", "G" in ready and "G" not in blocked)
reg2 = [L("X", af="none", status="proved"), L("Y", af="none", status="proved"),
        R("G", routes=[["X"], ["Y"]], af="none", status="proved")]
_, ready2, blocked2 = ag.check_status(reg2)
check("OR-route: G blocked when NO route fully available", "G" in blocked2 and "G" not in ready2)
reg3 = [L("X", af="none", status="proved"), L("Y", af="none", status="cited"),
        R("G", routes=[["X"], ["Y"]], af="none", status="proved")]
_, ready3, _ = ag.check_status(reg3)
check("OR-route: G ready when route2 (cited leaf) fires", "G" in ready3)
reg4 = [L("X", af="validated"), L("Y", af="none", status="proved"),
        R("G", routes=[["X", "Y"]], af="none", status="proved")]
_, ready4, blocked4 = ag.check_status(reg4)
check("OR-route: a route is conjunctive (BOTH members required)", "G" in blocked4 and "G" not in ready4)
reg5 = [L("D", af="none", status="proved"), L("X", af="validated"),
        R("G", deps=["D"], routes=[["X"]], af="none", status="proved")]
_, _, blocked5 = ag.check_status(reg5)
check("OR-route: unmet unconditional dep blocks even with a firing route", "G" in blocked5)

# --- (2) acyclicity over the UNION: a cycle hidden in a NON-FIRST route is still caught ---
acyc = [L("safe", deps=[]), R("G", routes=[["safe"], ["H"]]), L("H", deps=["G"])]
check("OR-route: cycle hidden in a non-first route is caught", ag.check_acyclic(acyc) != [])
noc = [L("safe"), L("H2"), R("G", routes=[["safe"], ["H2"]])]
check("OR-route: acyclic when no route cycles", ag.check_acyclic(noc) == [])
# route members must resolve (check_imports)
bad_rm = [R("G", routes=[["ghost"]])]
check("OR-route: dangling route member is caught", has(ag.check_imports(bad_rm, set()), "ghost"))

# --- (3) status propagation: af=validated needs ONE fully-validated/cited route (red->green) ---
ok = [L("X", af="validated", status="proved"), L("Y", af="none", status="proved"),
      R("G", routes=[["X"], ["Y"]], af="validated", status="proved")]
errs_ok, _, _ = ag.check_status(ok)
check("OR-route status-prop: validated G with one fully-validated route -> no error (green)", not has(errs_ok, "G"))
bad = [L("X", af="none", status="proved"), L("Y", af="none", status="proved"),   # perturb: demote X
       R("G", routes=[["X"], ["Y"]], af="validated", status="proved")]
errs_bad, _, _ = ag.check_status(bad)
check("OR-route status-prop: validated G with NO fully-validated route -> ERROR (red)", has(errs_bad, "G"))
errs_restore, _, _ = ag.check_status(ok)                                          # restore
check("OR-route status-prop: restore -> green again", not has(errs_restore, "G"))

# --- (4) backward-compat: live registry non-route shards classify IDENTICALLY to the deps-only rule ---
real, real_errs = ag.parse_registry(ROOT / "argument")
check("backward-compat: live registry parses clean", real_errs == [])
def _ref_deps_only(lemmas):
    af_of = {l["id"]: l.get("af", "none") for l in lemmas}
    st_of = {l["id"]: l.get("status") for l in lemmas}
    avail = lambda d: af_of.get(d, "none") == "validated" or st_of.get(d) == "cited"
    ready, blocked = set(), set()
    for l in lemmas:
        ok = all(avail(d) for d in l.get("deps", []))
        if l.get("af", "none") != "validated" and not ok: blocked.add(l["id"])
        if l.get("af", "none") in ("none", "seeded") and l.get("status") in ("proved", "consensus") and ok:
            ready.add(l["id"])
    return ready, blocked
_, nready, nblocked = ag.check_status(real)
rready, rblocked = _ref_deps_only(real)
routed = {l["id"] for l in real if l.get("routes")}
check("backward-compat: non-route shards' READY set unchanged",
      {x for x in nready if x not in routed} == {x for x in rready if x not in routed})
check("backward-compat: non-route shards' BLOCKED set unchanged",
      {x for x in nblocked if x not in routed} == {x for x in rblocked if x not in routed})
# once op-hlc is wired (routes present), it must be BLOCKED (no route fully validated) — meaningful post-wiring
if "op-hlc" in routed:
    check("backward-compat: wired op-hlc (routes) is blocked", "op-hlc" in nblocked)

# --- (5) DAG rendering with routes: OR-junctions, solid member edges, dashed OR edge; valid Mermaid ---
rreg = [L("m1", af="validated", status="proved"), L("m2", status="cited"), L("m3", status="proved"),
        R("goal", routes=[["m1", "m2"], ["m3"]], af="none", status="open")]
rreg[3]["kind"] = "open-problem"
dag = ag.render_dag(rreg)
check("DAG routes: junction node goal__route1 rendered", 'goal__route1{"route 1"}' in dag)
check("DAG routes: junction node goal__route2 rendered", 'goal__route2{"route 2"}' in dag)
check("DAG routes: conjunctive member solid edge m1 --> goal__route1", "m1 --> goal__route1" in dag)
check("DAG routes: dashed OR edge junction -> goal", "goal__route1 -. OR .-> goal" in dag)
check("DAG routes: route-junction classDef + class assignment",
      "classDef routejct" in dag and "class goal__route1,goal__route2 routejct" in dag)
check("DAG routes: deterministic", ag.render_dag(rreg) == ag.render_dag(rreg))
check("DAG routes: valid Mermaid skeleton (graph header + balanced fences)",
      "```mermaid\ngraph LR\n" in dag and dag.count("```") == 2)
check("DAG routes: every dashed OR link is well-formed ('-. OR .->')",
      dag.count("-.") == dag.count(".->") == 2)   # exactly the two OR edges
with tempfile.TemporaryDirectory() as _td:
    _d = pathlib.Path(_td)
    ag.generate(rreg, arg_dir=_d)
    check("DAG routes: fresh routed generate -> not stale (staleness gate green)",
          ag.check_generated(rreg, arg_dir=_d) == [])

# --- route_closures / --closure-min helper: per-route ancestor sets ---
prc = [L("a1"), L("a2", deps=["a1"]), L("b1"),
       R("goal", routes=[["a2"], ["b1"]], status="open")]
prc[3]["kind"] = "open-problem"
rc = ag.route_closures(prc, "goal")
check("route_closures: one entry per route", len(rc) == 2)
check("route_closures: route1 ancestors = {a1,a2}", rc[0][2] == {"a1", "a2"})
check("route_closures: route2 ancestors = {b1}", rc[1][2] == {"b1"})
check("route_closures: deps-only shard -> [] (no routes)", ag.route_closures([L("x")], "x") == [])
# union closure (deps_closure) spans ALL routes ('potentially relevant ancestors')
check("deps_closure over routes = union of all route ancestors", ag.deps_closure(prc, "goal") == {"a1", "a2", "b1"})

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
