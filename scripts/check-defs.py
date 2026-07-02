#!/usr/bin/env python3
"""
check-defs.py — Definitions DB gate (Layer 0).

Validates definitions/<id>.md shards:
  * required fields present; id == filename stem; kind/status from the allowed sets
  * DEDUP/DRIFT: no two shards claim the same term or alias  (the core guard)
  * CITED: source is a known refs/ source-id and the 16-hex sha256 prefix is in the
    refs/manifest/checksums.sha256 manifest (WARN if the gitignored payload is absent locally)
  * CONSENSUS-GATE: consensus|original shards must record `consensus:`; `status: draft` -> WARN

Usage:
  python3 scripts/check-defs.py --check            # validate (exit 1 on any ERROR)
  python3 scripts/check-defs.py --generate-index   # (re)write definitions/INDEX.md
  python3 scripts/check-defs.py                     # both

Core logic is the pure function check_defs(defs_dir, manifest_path, generate_index) ->
(errors, warnings, parsed), so it is unit-testable on temp directories (see scripts/tests/).
"""
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
KINDS = {"cited", "consensus", "original"}
STATUSES = {"draft", "locked"}
REQUIRED = ["id", "term", "kind", "status"]
SKIP = {"README.md", "INDEX.md"}


def parse_frontmatter(path, errors):
    """Parse flat `key: value` YAML frontmatter. Returns (fm_dict | None, body)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    block = text[3:end].strip("\n")
    body = text[end + 4:]
    fm = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{path.name}: frontmatter line without ':' -> {line!r}")
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, body


def load_manifest(manifest_path, warnings):
    """Return (prefix2path, source_ids, present_paths) from a checksums.sha256 file."""
    prefix2path, source_ids, present = {}, set(), set()
    manifest_path = pathlib.Path(manifest_path)
    if not manifest_path.exists():
        warnings.append(f"manifest absent: {manifest_path} (cannot verify cited hashes)")
        return prefix2path, source_ids, present
    refs_root = manifest_path.parent.parent  # .../refs/manifest/x -> .../refs
    for line in manifest_path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        h, _, p = line.partition("  ")
        p = p.lstrip("./")
        prefix2path[h[:16]] = p
        if "/" in p:
            source_ids.add(p.split("/", 1)[0])
        if (refs_root / p).exists():
            present.add(p)
    return prefix2path, source_ids, present


def check_defs(defs_dir, manifest_path, generate_index=False):
    """Pure checker. Returns (errors, warnings, parsed_frontmatters)."""
    defs_dir = pathlib.Path(defs_dir)
    errors, warnings, parsed = [], [], []
    prefix2path, source_ids, present = load_manifest(manifest_path, warnings)
    shards = sorted(p for p in defs_dir.glob("*.md") if p.name not in SKIP)
    term_owner, alias_owner = {}, {}

    for path in shards:
        fm, _ = parse_frontmatter(path, errors)
        if fm is None:
            errors.append(f"{path.name}: missing/unterminated frontmatter")
            continue
        for field in REQUIRED:
            if not fm.get(field):
                errors.append(f"{path.name}: missing required field '{field}'")
        if fm.get("id") and fm["id"] != path.stem:
            errors.append(f"{path.name}: id '{fm.get('id')}' != filename stem '{path.stem}'")
        if fm.get("kind") and fm["kind"] not in KINDS:
            errors.append(f"{path.name}: kind '{fm['kind']}' not in {sorted(KINDS)}")
        if fm.get("status") and fm["status"] not in STATUSES:
            errors.append(f"{path.name}: status '{fm['status']}' not in {sorted(STATUSES)}")

        # dedup / drift: one name namespace (term + aliases) across the whole DB
        term = (fm.get("term") or "").strip()
        names = [term] + [a.strip() for a in (fm.get("aliases", "") or "").split(";") if a.strip()]
        for nm in names:
            key = nm.lower()
            if not key:
                continue
            if key in alias_owner and alias_owner[key] != path.name:
                errors.append(f"DRIFT: name '{nm}' claimed by both {alias_owner[key]} and {path.name}")
            alias_owner[key] = path.name
        if term:
            term_owner.setdefault(term.lower(), path.name)

        kind, status = fm.get("kind"), fm.get("status")
        if kind == "cited":
            src, sha = fm.get("source"), (fm.get("sha256") or "").strip()
            if src and source_ids and src not in source_ids:
                errors.append(f"{path.name}: cited source '{src}' not a refs/ source-id {sorted(source_ids)}")
            if sha and sha != "-":
                if prefix2path and sha not in prefix2path:
                    errors.append(f"{path.name}: sha256 prefix '{sha}' not in refs manifest")
                elif sha in prefix2path:
                    p = prefix2path[sha]
                    if src and not p.startswith(src + "/"):
                        warnings.append(f"{path.name}: sha256 {sha} -> {p}, not under source '{src}'")
                    if p not in present:
                        warnings.append(f"{path.name}: source payload absent locally ({p}); hash unverifiable")
        elif kind in ("consensus", "original"):
            if not fm.get("consensus"):
                errors.append(f"{path.name}: {kind} shard must record 'consensus:'")
        if status == "draft":
            warnings.append(f"{path.name}: status=draft (not yet consensus-gated)")
        parsed.append(fm)

    if generate_index and not errors:
        rows = ["| id | term | kind | status | source |", "|---|---|---|---|---|"]
        for fm in sorted(parsed, key=lambda d: d.get("id", "")):
            rows.append("| `{id}` | {term} | {kind} | {status} | {source} |".format(
                id=fm.get("id", "?"), term=fm.get("term", "?"),
                kind=fm.get("kind", "?"), status=fm.get("status", "?"),
                source=fm.get("source", "-")))
        idx = ("<!-- GENERATED by scripts/check-defs.py --generate-index. Do not hand-edit. -->\n"
               f"# Definitions index ({len(parsed)} terms)\n\n" + "\n".join(rows) + "\n")
        (defs_dir / "INDEX.md").write_text(idx, encoding="utf-8")

    return errors, warnings, parsed


def main(argv):
    args = set(argv) or {"--check", "--generate-index"}
    defs_dir = ROOT / "definitions"
    manifest = ROOT / "refs" / "manifest" / "checksums.sha256"
    errors, warnings, parsed = check_defs(defs_dir, manifest, generate_index="--generate-index" in args)
    if "--generate-index" in args and not errors:
        print(f"wrote definitions/INDEX.md ({len(parsed)} terms)")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\ncheck-defs: {len(parsed)} shards, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
