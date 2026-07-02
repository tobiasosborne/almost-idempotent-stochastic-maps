#!/usr/bin/env python3
r"""
fetch-refs.py — reproducibly reconstruct the gitignored refs/ payload on ANY machine.

THE BRITTLENESS THIS REMOVES: refs/ ground truth used to live only on the original authoring machine,
so a fresh clone could not byte-verify anything (check-refs / sha256sum -c fail). This script rebuilds
refs/ from two reproducible sources, hash-verifying every file against refs/manifest/checksums.sha256:

  1. FETCH (no machine needed) — sources with a `fetch` spec in refs/manifest/sources.lock.json are
     pulled from a PINNED arXiv id. arXiv e-print source tarballs (and the per-version PDF) are
     byte-stable, so these reproduce EXACTLY (verified for kitaev-2405.02434 + vlw-2604.08380).
  2. CACHE (a store YOU control, not a specific machine) — bespoke sources (copyrighted OCR of books,
     text extractions, version-drifting journal PDFs) cannot be re-fetched. They are restored from a
     CONTENT-ADDRESSED cache keyed by sha256: $EXTPROP_REFS_CACHE/<sha256> (a local dir) or
     $EXTPROP_REFS_CACHE_URL/<sha256> (a URL). Seed it ONCE from a populated tree with --populate-cache,
     mirror that dir anywhere durable (private repo / cloud / drive); thereafter any clone restores it.

Every byte written is verified against the recorded sha256 first — a wrong-hash download/cache blob is
never installed. Nothing here is committed to git (refs/ payload stays gitignored); only the lock +
this script are tracked, so the RECONSTRUCTION RECIPE travels with the repo.

Usage:
  python3 scripts/fetch-refs.py                 # reconstruct refs/ (fetch + cache restore); report
  python3 scripts/fetch-refs.py --status        # dry-run: show present / fetchable / cache / missing
  python3 scripts/fetch-refs.py --require-all    # exit non-zero if any file is unresolved (CI mode)
  python3 scripts/fetch-refs.py --populate-cache DIR   # copy every present+valid refs file to DIR/<sha256>
  EXTPROP_REFS_CACHE=/path/to/cache python3 scripts/fetch-refs.py   # restore bespoke files from a CAS dir
"""
import hashlib
import io
import json
import os
import pathlib
import shutil
import sys
import tarfile
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
REFS = ROOT / "refs"
LOCK = REFS / "manifest" / "sources.lock.json"
ARXIV_EPRINT = "https://arxiv.org/e-print/{id}"
ARXIV_PDF = "https://arxiv.org/pdf/{id}"
TIMEOUT = 120


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def load_lock(lock_path=LOCK):
    return json.loads(pathlib.Path(lock_path).read_text())["files"]


# ---------------- fetch backends (network) ----------------

def _get(url):
    with urllib.request.urlopen(url, timeout=TIMEOUT) as r:   # noqa: S310 (trusted arXiv host)
        return r.read()


def fetch_spec(spec, expected_sha, _eprint={}, _pdf={}, _url={}):
    """Return the bytes for a `fetch` spec IFF they hash to expected_sha, else None. Kinds:
      url                 — a direct, stable URL (e.g. an open-access journal galley)
      arxiv-pdf           — arxiv.org/pdf/<id>  (works for new-style and math/NNNN ids)
      arxiv-eprint        — the e-print bundle itself (the recorded *.tar.gz)
      arxiv-eprint-member — a file INSIDE the e-print, selected BY HASH (robust to renames); the bundle
                            may be a tar.gz OR a single gzipped file, so we try raw, gunzip, and members.
    Downloads are memoised per-id/url across calls (default-arg dicts)."""
    kind = spec["kind"]
    try:
        if kind == "url":
            u = spec["url"]
            if u not in _url:
                _url[u] = _get(u)
            return _url[u] if sha256_bytes(_url[u]) == expected_sha else None
        aid = spec["id"]
        if kind == "arxiv-pdf":
            if aid not in _pdf:
                _pdf[aid] = _get(ARXIV_PDF.format(id=aid))
            return _pdf[aid] if sha256_bytes(_pdf[aid]) == expected_sha else None
        if aid not in _eprint:
            _eprint[aid] = _get(ARXIV_EPRINT.format(id=aid))
        raw = _eprint[aid]
        if kind == "arxiv-eprint":
            return raw if sha256_bytes(raw) == expected_sha else None
        if kind == "arxiv-eprint-member":
            cands = [raw]
            try:
                import gzip
                cands.append(gzip.decompress(raw))   # arXiv often serves a single gzipped .tex
            except Exception:   # noqa: BLE001
                pass
            for blob in list(cands):
                try:
                    with tarfile.open(fileobj=io.BytesIO(blob)) as tf:
                        cands += [tf.extractfile(m).read() for m in tf.getmembers() if m.isfile()]
                except Exception:   # noqa: BLE001
                    pass
            for b in cands:
                if sha256_bytes(b) == expected_sha:
                    return b
            return None
    except Exception:   # noqa: BLE001 — any network/parse failure -> fall through to cache
        return None
    return None


# ---------------- cache backend (content-addressed, no network) ----------------

def cache_lookup(expected_sha, cache_dir=None, cache_url=None):
    """Return bytes for a content-addressed cache hit (verified), else None.

    Looks up $EXTPROP_REFS_CACHE/<sha256> (a local dir) then $EXTPROP_REFS_CACHE_URL/<sha256> (a URL)."""
    if cache_dir:
        p = pathlib.Path(cache_dir) / expected_sha
        if p.is_file():
            b = p.read_bytes()
            if sha256_bytes(b) == expected_sha:
                return b
    if cache_url:
        try:
            b = _get(cache_url.rstrip("/") + "/" + expected_sha)
            if sha256_bytes(b) == expected_sha:
                return b
        except Exception:   # noqa: BLE001
            return None
    return None


# ---------------- reconstruct / populate ----------------

def install(refs_dir, relpath, data):
    dst = pathlib.Path(refs_dir) / relpath
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)


def reconstruct(files, refs_dir=REFS, cache_dir=None, cache_url=None, write=True, allow_fetch=True):
    """Resolve every lock file. Returns [(path, status)] with status in
    present|fetched|restored|MISSING (or would-* when write=False)."""
    rows = []
    for f in files:
        rel, sha, spec = f["path"], f["sha256"], f.get("fetch")
        dst = pathlib.Path(refs_dir) / rel
        if dst.is_file() and sha256_file(dst) == sha:
            rows.append((rel, "present"))
            continue
        data = None
        via = None
        if allow_fetch and spec:
            data = fetch_spec(spec, sha)
            via = "fetched" if data is not None else None
        if data is None:
            data = cache_lookup(sha, cache_dir, cache_url)
            via = "restored" if data is not None else None
        if data is None:
            if spec and not allow_fetch:        # --status: name it fetchable rather than downloading
                rows.append((rel, "fetchable"))
            else:
                rows.append((rel, "MISSING"))
            continue
        if write:
            install(refs_dir, rel, data)
            rows.append((rel, via))
        else:
            rows.append((rel, "would-" + via))
    return rows


def populate_cache(files, cache_dir, refs_dir=REFS):
    """Copy every present+valid refs file into cache_dir/<sha256> (a CAS to mirror durably)."""
    cache_dir = pathlib.Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    n = skipped = 0
    for f in files:
        rel, sha = f["path"], f["sha256"]
        src = pathlib.Path(refs_dir) / rel
        if src.is_file() and sha256_file(src) == sha:
            shutil.copy2(src, cache_dir / sha)
            n += 1
        else:
            skipped += 1
    return n, skipped


def main(argv):
    argv = list(argv)
    cache_dir = os.environ.get("EXTPROP_REFS_CACHE")
    cache_url = os.environ.get("EXTPROP_REFS_CACHE_URL")
    files = load_lock()

    if "--populate-cache" in argv:
        i = argv.index("--populate-cache")
        if i + 1 >= len(argv):
            print("usage: --populate-cache <dir>")
            return 2
        n, skipped = populate_cache(files, argv[i + 1])
        print(f"populate-cache: wrote {n} blobs to {argv[i + 1]} ({skipped} not present/valid, skipped)")
        return 0

    status_only = "--status" in argv
    rows = reconstruct(files, cache_dir=cache_dir, cache_url=cache_url,
                       write=not status_only, allow_fetch=not status_only)
    from collections import Counter
    counts = Counter(s.replace("would-", "") for _, s in rows)
    for rel, st in rows:
        if "MISSING" in st or status_only:
            mark = {"present": "ok   ", "fetched": "FETCH", "restored": "CACHE",
                    "fetchable": "fetch", "would-restored": "cache", "MISSING": "MISS "}.get(st, st)
            print(f"  [{mark}] {rel}")
    miss = [r for r, s in rows if s == "MISSING"]
    print(f"\nfetch-refs: {len(rows)} files — "
          + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    if miss:
        print(f"  {len(miss)} MISSING (no fetch spec and no cache hit). Seed a content-addressed cache on a")
        print(f"  populated machine:  python3 scripts/fetch-refs.py --populate-cache <dir>")
        print(f"  then on this machine:  EXTPROP_REFS_CACHE=<dir> python3 scripts/fetch-refs.py")
    if "--require-all" in argv and miss:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
