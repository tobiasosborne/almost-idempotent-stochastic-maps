#!/usr/bin/env bash
# Sharded lab-book gate (ported from ../arithmetic-quantum-mechanics, adapted to the
# report/main.tex master + report/sections/NN_slug.tex shard layout and the AISM- prefix).
# Enforces: master purity (no body sectioning in main.tex), includes resolve/unique/under
# sections/, per-shard SHARD-ID/TITLE/SUMMARY(x2-3)/KEYWORDS headers with prefix-matched IDs,
# README + SHARD_CATALOG cross-index consistency, shard size guard, and no orphan shards.
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

MASTER="report/main.tex"
SECTIONS_DIR="report/sections"
README="report/README.md"
CATALOG="report/SHARD_CATALOG.md"
MAX_LINES="${REPORT_SHARD_MAX_LINES:-280}"
PREFIX="AISM"

failures=0
fail() { printf 'report shard check: %s\n' "$*" >&2; failures=1; }

[[ -f "$MASTER" ]]       || fail "missing master $MASTER"
[[ -d "$SECTIONS_DIR" ]] || fail "missing sections directory $SECTIONS_DIR"
[[ -f "$README" ]]       || fail "missing report map $README"
[[ -f "$CATALOG" ]]      || fail "missing shard catalog $CATALOG"

# \include{sections/NN_slug} lines (relative to report/, since latexmk runs from report/).
mapfile -t includes < <(
  sed -nE '/^[[:space:]]*%/!s/.*\\include\{([^}]+)\}.*/\1/p' "$MASTER"
)
# An empty scaffold (no shards yet) is legal: pass cleanly if zero includes AND zero shard files.
shard_count="$(find "$SECTIONS_DIR" -type f -name '*.tex' | wc -l)"
if (( ${#includes[@]} == 0 && shard_count == 0 )); then
  printf 'report shard check: no shards yet (empty scaffold) — OK\n'
  exit 0
fi
if (( ${#includes[@]} == 0 )); then
  fail "$MASTER has no \\include statements but $SECTIONS_DIR has $shard_count shard(s)"
fi

declare -A seen=()
declare -A seen_ids=()

for include in "${includes[@]}"; do
  if [[ "$include" != sections/* ]]; then
    fail "\\include{$include} should point under sections/ (relative to report/)"
    continue
  fi
  file="report/${include}.tex"
  if [[ -n "${seen[$file]+x}" ]]; then fail "$file is included more than once"; fi
  seen["$file"]=1
  if [[ ! -f "$file" ]]; then fail "\\include{$include} points to missing $file"; continue; fi

  lines="$(wc -l < "$file")"
  if (( lines > MAX_LINES )); then
    fail "$file has $lines lines; target is about 200 and hard guard is $MAX_LINES"
  fi
  if [[ -f "$README" ]] && ! grep -Fq "\`$file\`" "$README"; then
    fail "$README does not list $file"
  fi

  id="$(sed -nE 's/^% SHARD-ID:[[:space:]]*(.+)$/\1/p' "$file" | head -n 1)"
  title="$(sed -nE 's/^% SHARD-TITLE:[[:space:]]*(.+)$/\1/p' "$file" | head -n 1)"
  keywords="$(sed -nE 's/^% SHARD-KEYWORDS:[[:space:]]*(.+)$/\1/p' "$file" | head -n 1)"
  mapfile -t summaries < <(sed -nE 's/^% SHARD-SUMMARY:[[:space:]]*(.+)$/\1/p' "$file")

  if [[ -z "$id" ]]; then
    fail "$file is missing SHARD-ID header"
  elif [[ ! "$id" =~ ^${PREFIX}-[0-9]{2}[A-Z]?-[A-Z0-9-]+$ ]]; then
    fail "$file has invalid SHARD-ID '$id'"
  elif [[ -n "${seen_ids[$id]+x}" ]]; then
    fail "duplicate SHARD-ID $id"
  else
    seen_ids["$id"]=1
    file_prefix="$(basename "$file" | cut -c1-2)"
    if [[ "$id" != ${PREFIX}-"$file_prefix"-* ]]; then
      fail "$file has SHARD-ID $id, expected prefix ${PREFIX}-$file_prefix-"
    fi
  fi

  [[ -z "$title" ]]    && fail "$file is missing SHARD-TITLE header"
  [[ -z "$keywords" ]] && fail "$file is missing SHARD-KEYWORDS header"
  if (( ${#summaries[@]} < 2 || ${#summaries[@]} > 3 )); then
    fail "$file must have 2-3 SHARD-SUMMARY lines; found ${#summaries[@]}"
  fi

  if [[ -f "$README" && -n "$id" ]] && ! grep -Fq "\`$id\`" "$README"; then
    fail "$README does not list shard label $id"
  fi
  if [[ -f "$CATALOG" ]]; then
    for value in "$id" "$file" "$title" "$keywords"; do
      if [[ -n "$value" ]] && ! grep -Fq "$value" "$CATALOG"; then
        fail "$CATALOG does not list '$value' from $file"
      fi
    done
    for summary in "${summaries[@]}"; do
      if ! grep -Fq "$summary" "$CATALOG"; then
        fail "$CATALOG does not mirror summary from $file: $summary"
      fi
    done
  fi
done

while IFS= read -r -d '' path; do
  file="${path#./}"
  if [[ -z "${seen[$file]+x}" ]]; then
    fail "$file exists but is not included by $MASTER"
  fi
done < <(find "$SECTIONS_DIR" -type f -name '*.tex' -print0 | sort -z)

tmp="$(mktemp)"
if grep -nE '^[[:space:]]*\\(section|subsection|subsubsection|paragraph)\{' "$MASTER" >"$tmp"; then
  cat "$tmp" >&2
  fail "$MASTER contains body sectioning commands; move prose to report/sections/"
fi
rm -f "$tmp"

(( failures != 0 )) && exit 1
printf 'report shard check: %d shards included, labeled, cataloged, all <= %s lines\n' "${#includes[@]}" "$MAX_LINES"
