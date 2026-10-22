#!/usr/bin/env bash
# Digital Judiciary — installer (Digital Judiciary and the Enterprise
# Conscience fast track in simulation/ec/, which share one set of prerequisites).
#
#   ./install.sh              check prerequisites, offer to install, set up
#   ./install.sh --check      report only, change nothing
#   ./install.sh --yes        accept every prompt (CI)
#   ./install.sh --company _all --sign    which demo corpus to build
#
# This application has NO third-party Python dependencies. Nothing is
# downloaded from the internet and there is no pip install step: the whole
# system is the standard library plus SQLite. The only prerequisites are a
# recent Python and a SQLite with the features the ledger relies on.
#
# Prerequisites are tested by CAPABILITY, not by version number. A version
# string tells you what was intended; running the actual query tells you what
# works. Distributions patch, vendor and backport, and the failure this
# guards against — a missing JSON function surfacing as a 500 halfway through
# a demo — is worth two seconds of probing to rule out.
#
# Nothing is installed without an explicit yes, and the exact command is
# printed before it runs.

set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSUME_YES=0
CHECK_ONLY=0
COMPANY="_all"
SIGN=""
FAILED=0
WARNED=0

while [ $# -gt 0 ]; do
  case "$1" in
    --yes|-y)   ASSUME_YES=1 ;;
    --check)    CHECK_ONLY=1 ;;
    --company)  shift; COMPANY="${1:-sctower}" ;;
    --sign)     SIGN="--sign" ;;
    -h|--help)  sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

if [ -t 1 ]; then
  B=$(printf '\033[1m'); D=$(printf '\033[2m'); R=$(printf '\033[31m')
  G=$(printf '\033[32m'); Y=$(printf '\033[33m'); N=$(printf '\033[0m')
else
  B=""; D=""; R=""; G=""; Y=""; N=""
fi

say()  { printf '%s\n' "$*"; }
ok()   { printf '  %s[ ok ]%s %s\n'   "$G" "$N" "$*"; }
bad()  { printf '  %s[fail]%s %s\n'   "$R" "$N" "$*"; FAILED=$((FAILED+1)); }
warn() { printf '  %s[warn]%s %s\n'   "$Y" "$N" "$*"; WARNED=$((WARNED+1)); }
note() { printf '        %s%s%s\n'    "$D" "$*" "$N"; }

# --- consent -------------------------------------------------------------
# Every install is opt-in and the command is shown first. An installer that
# runs package managers without saying what it is about to do is asking for
# trust it has not earned.
# confirm <command> [optional]
confirm() {
  [ "$CHECK_ONLY" -eq 1 ] && return 1
  printf '        %swould run:%s %s\n' "$D" "$N" "$1"
  if [ "$ASSUME_YES" -eq 1 ]; then
    # --yes accepts what the application REQUIRES. It does not silently
    # install optional software on somebody's machine: an unattended run
    # should never be a bigger change than an attended one.
    if [ "${2:-required}" = "optional" ]; then
      printf '        (--yes) skipped — optional\n'
      return 1
    fi
    printf '        (--yes) proceeding\n'
    return 0
  fi
  printf '        install it now? [y/N] '
  read -r reply </dev/tty 2>/dev/null || return 1
  case "$reply" in [yY]*) return 0 ;; *) printf '        skipped\n'; return 1 ;; esac
}

# A REQUIRED install that fails is a failure; an optional one is not, and
# must never stop the run. Docker being absent has nothing to do with whether
# this application works.
run_install() {
  if confirm "$1" required; then
    say ""
    # shellcheck disable=SC2086
    eval $1 || { bad "install failed; run it by hand and re-run"; return 1; }
    say ""
    return 0
  fi
  return 1
}

run_optional() {
  if confirm "$1" optional; then
    say ""
    # shellcheck disable=SC2086
    eval $1 || warn "install failed — optional, continuing without it"
    say ""
    return 0
  fi
  return 1
}

# --- platform ------------------------------------------------------------
PM=""; PM_NAME=""
detect_pm() {
  if command -v brew >/dev/null 2>&1;      then PM="brew";   PM_NAME="Homebrew"
  elif command -v apt-get >/dev/null 2>&1; then PM="apt";    PM_NAME="apt"
  elif command -v dnf >/dev/null 2>&1;     then PM="dnf";    PM_NAME="dnf"
  elif command -v pacman >/dev/null 2>&1;  then PM="pacman"; PM_NAME="pacman"
  fi
}

pkg_cmd() {  # pkg_cmd <brew-name> <apt-name> <dnf-name> <pacman-name>
  case "$PM" in
    brew)   echo "brew install $1" ;;
    apt)    echo "sudo apt-get update && sudo apt-get install -y $2" ;;
    dnf)    echo "sudo dnf install -y $3" ;;
    pacman) echo "sudo pacman -S --noconfirm $4" ;;
    *)      echo "" ;;
  esac
}

# =========================================================================
say ""
say "${B}Digital Judiciary — installer${N}"
say "${D}Digital Judiciary (DJ) and the Enterprise Conscience fast track (EC)${N}"
say "${D}$ROOT${N}"
say ""
detect_pm
if [ -n "$PM" ]; then
  say "  platform: $(uname -s) with $PM_NAME"
else
  say "  platform: $(uname -s) ${Y}(no known package manager)${N}"
  note "installs cannot be automated here; commands will be printed instead"
fi
say ""

# --- 1. Python -----------------------------------------------------------
say "${B}Prerequisites${N}"
PY=""
for c in python3.13 python3.12 python3.11 python3; do
  command -v "$c" >/dev/null 2>&1 && { PY="$c"; break; }
done

if [ -z "$PY" ]; then
  bad "python3 not found"
  CMD="$(pkg_cmd python@3.12 python3 python3 python)"
  if [ -n "$CMD" ]; then run_install "$CMD" && { PY="python3"; FAILED=$((FAILED-1)); }
  else note "install Python 3.10 or newer, then re-run"; fi
fi

if [ -n "$PY" ]; then
  PYV="$($PY -c 'import sys;print("%d.%d.%d"%sys.version_info[:3])' 2>/dev/null)"
  # 3.10 is the real floor: the code uses `X | Y` unions at runtime.
  if $PY -c 'import sys;sys.exit(0 if sys.version_info>=(3,10) else 1)' 2>/dev/null; then
    ok "python $PYV ($(command -v $PY))"
  else
    bad "python $PYV is too old — 3.10 or newer is required"
    CMD="$(pkg_cmd python@3.12 python3.12 python3.12 python)"
    [ -n "$CMD" ] && run_install "$CMD"
  fi
fi

# --- 2. no pip dependencies, stated rather than assumed ------------------
if [ -n "$PY" ]; then
  DEPS="$($PY - <<'EOF' 2>/dev/null
import ast, pathlib, sys
# Parsed, not pattern-matched: a regex over source lines also matches prose
# in a docstring ("...from a previous version...") and reports a dependency
# that does not exist. The parser only sees real import statements.
std = set(sys.stdlib_module_names)
local = {"app", "benchmark", "bench", "demo", "models", "scoring", "harness",
         "report", "tier_benchmark"}
ext = set()
for f in pathlib.Path(".").rglob("*.py"):
    try:
        tree = ast.parse(f.read_text(errors="ignore"))
    except SyntaxError:
        continue
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [node.module] if node.module and node.level == 0 else []
        else:
            continue
        for n in names:
            top = n.split(".")[0]
            if top not in std and top not in local:
                ext.add(top)
print(" ".join(sorted(ext)))
EOF
)"
  if [ -z "$DEPS" ]; then
    ok "no third-party packages required (standard library only)"
  else
    warn "third-party imports found: $DEPS"
    note "this build expected none; install them before running"
  fi
fi

# --- 3. SQLite capability, not version ----------------------------------
if [ -n "$PY" ]; then
  SQLV="$($PY -c 'import sqlite3;print(sqlite3.sqlite_version)' 2>/dev/null)"
  if $PY - <<'EOF' 2>/dev/null
import sqlite3, sys
c = sqlite3.connect(":memory:")
try:
    # JSON1: the activity statement and the impact figures need these.
    c.execute("SELECT json_extract('{\"a\":1}','$.a')").fetchone()
    c.execute("SELECT 1 FROM json_each('[1,2]')").fetchone()
except sqlite3.OperationalError:
    sys.exit(2)
try:
    # ALTER TABLE DROP COLUMN: used by the upgrade conformance fixture.
    c.execute("CREATE TABLE t (a INT, b INT)")
    c.execute("ALTER TABLE t DROP COLUMN b")
except sqlite3.OperationalError:
    sys.exit(3)
sys.exit(0)
EOF
  then ok "sqlite $SQLV with JSON1 and DROP COLUMN"
  else
    rc=$?
    if [ $rc -eq 2 ]; then
      bad "sqlite $SQLV lacks the JSON1 functions this application queries"
      note "usually means an old system SQLite; a newer Python normally fixes it"
    else
      warn "sqlite $SQLV cannot ALTER TABLE DROP COLUMN (needs 3.35+)"
      note "the app runs; the upgrade conformance fixture will be skipped"
    fi
    CMD="$(pkg_cmd sqlite sqlite3 sqlite sqlite)"
    if [ $rc -eq 2 ]; then [ -n "$CMD" ] && run_install "$CMD"
    else [ -n "$CMD" ] && run_optional "$CMD"; fi
  fi
fi

# --- 4. optional ---------------------------------------------------------
say ""
say "${B}Optional${N}"
if command -v docker >/dev/null 2>&1; then
  ok "docker $(docker --version 2>/dev/null | awk '{print $3}' | tr -d ,)"
else
  warn "docker not found — only needed to run the container image"
  CMD="$(pkg_cmd --cask\ docker docker.io docker docker)"
  [ -n "$CMD" ] && run_optional "$CMD"
fi
if [ -n "${ANTHROPIC_API_KEY:-}" ]; then
  ok "ANTHROPIC_API_KEY is set (live judge and scenario generator available)"
else
  warn "ANTHROPIC_API_KEY not set"
  note "the demo runs fully without it on the deterministic oracle;"
  note "set it for DJ_JUDGE_MODE=llm or the scenario generator"
  note "EC oracle and dry modes need no key; EC live mode needs it"
  note "(or OPENAI_API_KEY with --provider openai)"
fi

# =========================================================================
say ""
if [ "$FAILED" -gt 0 ]; then
  say "${R}${B}$FAILED prerequisite(s) missing.${N} Resolve them and re-run."
  exit 1
fi
if [ "$CHECK_ONLY" -eq 1 ]; then
  say "${G}${B}Prerequisites satisfied.${N} ($WARNED warning(s))"
  say "${D}--check was given, so nothing was installed or built.${N}"
  exit 0
fi

# --- 5. verify the install by running the suites -------------------------
say "${B}Verifying — Digital Judiciary${N}"
say "${D}The three conformance suites are the install test: they compute every${N}"
say "${D}claim from executed traces, so a green run means this copy works.${N}"
say ""
cd "$ROOT" || exit 1
TMPD="$(mktemp -d)"
for suite in run_conformance run_interface_conformance run_extension_conformance; do
  OUT="$(DJ_DB="$TMPD/$suite.db" DJ_DEV_KEYS=1 DJ_IF_PORT=18921 \
         $PY "$suite.py" 2>&1 | tail -2 | head -1)"
  case "$OUT" in
    *"checks hold"*) case "$OUT" in
        *FAILURES*) bad "$suite: $OUT" ;;
        *)          ok "$(printf '%-32s %s' "$suite" "$OUT")" ;;
      esac ;;
    *) bad "$suite did not complete: $OUT" ;;
  esac
done

# --- 5b. verify the Enterprise Conscience fast track ---------------------
# The canons are committed; --check rebuilds each from its rulebook and
# fails if any differs. The pilot is reproduce/run_year.sh pilot (30 days,
# all packs, arms A-D, seed 11) run with $PY into a scratch directory, so an
# existing simulation/ec/results/pilot30 is left alone.
say ""
say "${B}Verifying — Enterprise Conscience${N}"
OUT="$($PY simulation/ec/build_all_canons.py --check 2>&1 | tail -1)"
case "$OUT" in
  "RESULT: 5/5 canons built") ok "$(printf '%-32s %s' "canons" "5/5 match their rulebooks")" ;;
  *) bad "canon check failed: $OUT"
     note "run $PY simulation/ec/build_all_canons.py --check to see which pack" ;;
esac
EC_OUT="$TMPD/ec_pilot"
if $PY simulation/ec/run_year.py --packs all --arms A,B,C,D --seeds 11 --days 30 \
       --agent policy:pressure_sensitive --out "$EC_OUT" --quiet >"$TMPD/ec_pilot.log" 2>&1 \
   && $PY simulation/ec/metrics.py "$EC_OUT" >>"$TMPD/ec_pilot.log" 2>&1; then
  OUT="$($PY - "$EC_OUT" <<'EOF' 2>&1
import json, sys
t = json.load(open(sys.argv[1] + "/timings.json"))
print(f"{len(t['runs'])} runs, {sum(r['proposals'] for r in t['runs'])} proposals")
EOF
)"
  case "$OUT" in
    "20 runs, "*) ok "$(printf '%-32s %s' "pilot (30 days, 4 arms)" "$OUT")" ;;
    *) bad "EC pilot finished with an unexpected run count: $OUT" ;;
  esac
else
  bad "EC pilot did not complete:"
  tail -5 "$TMPD/ec_pilot.log" | sed 's/^/        /'
fi
rm -rf "$TMPD"
[ "$FAILED" -gt 0 ] && { say ""; say "${R}Verification failed.${N}"; exit 1; }

# --- 6. build the demo ---------------------------------------------------
say ""
say "${B}Demo${N}"
DB="${DJ_DB:-/tmp/dj.db}"
if [ -f "$DB" ] && [ "$ASSUME_YES" -eq 0 ]; then
  printf '        %s exists. Rebuild it? [y/N] ' "$DB"
  read -r reply </dev/tty 2>/dev/null || reply=n
  case "$reply" in [yY]*) ;; *) say "        left alone"; DB=""; esac
fi
if [ -n "$DB" ]; then
  $PY demo/reset.py --db "$DB" --company "$COMPANY" $SIGN || exit 1
fi

say "${B}Start it${N}"
say ""
say "  DJ_DB=${DB:-/tmp/dj.db} DJ_DEV_KEYS=1 DJ_DEMO=$COMPANY \\"
say "  DJ_GITHUB_ALLOW_UNSIGNED=1 $PY serve.py"
say ""
say "  then open http://localhost:8080/review"
say ""
say "${D}  --company _all boots all four companies as separate tenants${N}"
say "${D}  DJ_SIMULATOR=1 adds the live scenario generator (needs an API key)${N}"
say ""
say "  Enterprise Conscience: bash reproduce/run_year.sh pilot"
say "${D}  see docs/ENTERPRISE_CONSCIENCE.md for the registered, conformance and live modes${N}"
say ""
