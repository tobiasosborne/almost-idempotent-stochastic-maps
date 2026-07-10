#!/bin/bash
# scripts/beads-sync.sh — committed-JSONL-over-git beads sync (user-approved
# option (b): no new external dependency, rides the existing git backbone).
#
# This addresses the cycle-319 cross-device reconciliation incident: the
# Dolt DB under .beads/ is per-machine/local (embeddeddolt, gitignored), so
# without an explicit export/import step, beads state silently diverges
# across clones. This script does NOT wire itself into any hook — it is
# invoked EXPLICITLY, per this protocol:
#
#   * At SESSION CLOSE, before `git push`:
#       scripts/beads-sync.sh export
#     This regenerates .beads/issues.jsonl from the local bd DB (sorted
#     deterministically for clean git diffs) and stages it for commit like
#     any other tracked file.
#
#   * On a device whose local bd DB is behind (e.g. right after `git pull`
#     brought a newer .beads/issues.jsonl from another machine):
#       scripts/beads-sync.sh import
#     This upserts .beads/issues.jsonl into the local bd DB.
#
# USAGE
#   scripts/beads-sync.sh export   # bd export -> .beads/issues.jsonl, prints row count
#   scripts/beads-sync.sh import   # bd import <- .beads/issues.jsonl, prints result
#
# NOTES
#   - `bd export` has no --sort flag (checked: `bd export --help`), but was
#     observed to emit a stable row order across repeated runs against the
#     same DB state. To keep the committed JSONL git-diff-friendly and
#     independent of any DB-iteration-order assumption, this script
#     re-sorts the exported rows by `.id` (issues) / `.key` (memory
#     records) via `jq`, and canonicalizes each row's key order (`jq -S`).
#   - `bd export` includes memories by default (round-trips with `bd
#     import`, which auto-detects `"_type":"memory"` lines) — this script
#     keeps that default; pass-through flags are not exposed (add here if
#     ever needed).
#   - This script is NOT run by any git hook. Nothing under
#     `.beads/hooks/*` was touched.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
JSONL_PATH="$REPO_ROOT/.beads/issues.jsonl"

usage() {
  echo "usage: $0 <export|import>" >&2
  exit 2
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { echo "$0: required command not found: $1" >&2; exit 2; }
}

cmd_export() {
  require_cmd bd
  require_cmd jq
  local raw
  raw="$(mktemp)"
  trap 'rm -f "$raw"' RETURN
  bd export -o "$raw" -q
  jq -c -S -s 'sort_by(.id // .key // ._type) | .[]' "$raw" > "$JSONL_PATH"
  local n
  n=$(wc -l < "$JSONL_PATH" | tr -d ' ')
  echo "[beads-sync] export: wrote $n rows to $JSONL_PATH"
}

cmd_import() {
  require_cmd bd
  if [ ! -f "$JSONL_PATH" ]; then
    echo "[beads-sync] import: $JSONL_PATH does not exist — nothing to import" >&2
    exit 1
  fi
  bd import "$JSONL_PATH"
  echo "[beads-sync] import: done from $JSONL_PATH"
}

[ "$#" -eq 1 ] || usage

case "$1" in
  export) cmd_export ;;
  import) cmd_import ;;
  -h|--help) usage ;;
  *)
    echo "$0: unrecognized subcommand: $1" >&2
    usage
    ;;
esac
