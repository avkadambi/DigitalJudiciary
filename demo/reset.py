#!/usr/bin/env python3
"""Rebuild the demo database.

    python3 demo/reset.py --check                 # what is in there now
    python3 demo/reset.py                         # rebuild it
    python3 demo/reset.py --company _all --sign   # all four tenants, signed

=== Why this rebuilds rather than deletes ===

There is no "delete the old demo" path, and there cannot be one. Every table
that records what the system did carries a BEFORE DELETE trigger that aborts:
precedent_record, pr_session, pr_disposition, review_task, contest_event,
judgment_invocation, and the rest. That is not an oversight to work around —
it is the property that makes the ledger worth reading. A system that will
quietly erase its own history to tidy up a demo would erase it for other
reasons too.

So this moves the old database aside, builds a new one, and replays the
corpus into it. The old file is kept, with a timestamp, unless you say
otherwise. Nothing is destroyed; something is superseded, which is the same
distinction the architecture draws everywhere else.

=== Why an old demo needs rebuilding at all ===

Schema changes migrate in place on boot — columns are added, views are
rebuilt. What CANNOT migrate is data written before a column existed. A
pr_session filed before tenancy has organization = NULL, and no UPDATE can
fix it, because pr_session refuses UPDATE too. Those rows will show as
"platform" in the activity statement forever. The only honest remedy is a
fresh ledger.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sqlite3
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PACKS = os.path.join(HERE, "companies")

LEDGER_TABLES = ("pr_session", "pr_disposition", "review_task",
                 "precedent_record", "draft_amendment",
                 "precedent_lifecycle_event", "judgment_invocation")


def companies() -> list[str]:
    if not os.path.isdir(PACKS):
        return []
    return sorted(d for d in os.listdir(PACKS)
                  if os.path.isdir(os.path.join(PACKS, d)))


# ---------------------------------------------------------------------------
def in_use(path: str) -> bool:
    """Is another process holding this database?

    Probed with a short busy timeout and an immediate transaction. Deleting
    the write-ahead log out from under a live SQLite connection does not fail
    cleanly — it BLOCKS, which from the outside is indistinguishable from
    this script being broken. Two seconds of probing beats an indefinite
    hang with no explanation.
    """
    try:
        c = sqlite3.connect(path, timeout=2.0)
        c.execute("PRAGMA busy_timeout = 2000")
        c.execute("BEGIN IMMEDIATE")
        c.execute("ROLLBACK")
        c.close()
        return False
    except sqlite3.OperationalError:
        return True
    except sqlite3.DatabaseError:
        return False


def inspect(path: str) -> dict:
    """What is in this database, and is any of it stale?"""
    if not os.path.exists(path):
        return {"exists": False}
    c = sqlite3.connect(path)
    c.row_factory = sqlite3.Row
    out = {"exists": True, "counts": {}, "untenanted": {}, "missing": []}
    try:
        names = {r["name"] for r in c.execute(
            "SELECT name FROM sqlite_master WHERE type IN ('table','view')")}
        for t in LEDGER_TABLES:
            if t not in names:
                out["missing"].append(t)
                continue
            out["counts"][t] = c.execute(
                f"SELECT COUNT(*) AS n FROM {t}").fetchone()["n"]

        # A column added after these rows were written cannot be backfilled.
        has_orgs = "organization" in names and c.execute(
            "SELECT COUNT(*) AS n FROM organization").fetchone()["n"] > 0
        out["tenants"] = has_orgs
        for t in ("pr_session", "review_task", "draft_amendment",
                  "precedent_record"):
            if t in names and "organization" in {
                    r[1] for r in c.execute(f"PRAGMA table_info({t})")}:
                n = c.execute(f"SELECT COUNT(*) AS n FROM {t}"
                              f" WHERE organization IS NULL").fetchone()["n"]
                if n:
                    out["untenanted"][t] = n

        cols = {r[1] for r in c.execute("PRAGMA table_info(record_effective)")}
        out["view_current"] = "superseded" in cols
    finally:
        c.close()

    out["stale"] = bool(out["missing"]) or not out.get("view_current") or (
        out["tenants"] and out["untenanted"])
    return out


def report(path: str, s: dict) -> None:
    print(f"\n  {path}")
    if not s["exists"]:
        print("    does not exist — nothing to rebuild\n")
        return
    for t, n in s["counts"].items():
        print(f"    {t:28s} {n}")
    print(f"    {'record_effective current':28s} "
          f"{'yes' if s.get('view_current') else 'NO — pre-supersession'}")
    if s["missing"]:
        print(f"    {'missing tables':28s} {', '.join(s['missing'])}")
    if s["untenanted"]:
        print(f"    {'rows with no company':28s} {s['untenanted']}")
        print("      (these predate tenancy and cannot be backfilled: the"
              " tables refuse UPDATE)")
    print(f"\n    => {'STALE, rebuild recommended' if s['stale'] else 'current'}\n")


# ---------------------------------------------------------------------------
def rebuild(path: str, company: str, sign: bool, limit: int,
            backup: bool, show_next_steps: bool = True) -> int:
    if company not in companies():
        print(f"  no such corpus: {company!r}. Available: "
              f"{', '.join(companies())}", file=sys.stderr)
        return 2

    if os.path.exists(path) and in_use(path):
        print("\n  This database is in use — most likely serve.py is still\n"
              "  running against it. Stop the server and run this again.\n"
              f"  (checked {path})\n", file=sys.stderr)
        return 3

    if os.path.exists(path):
        if backup:
            kept = f"{path}.{time.strftime('%Y%m%d-%H%M%S')}.bak"
            shutil.move(path, kept)
            print(f"  old database moved aside -> {kept}")
        else:
            os.remove(path)
            print("  old database removed (--no-backup)")
    # The journal files belong to the database being retired. Removing them
    # under a live connection is exactly the hang this guards against.
    for suffix in ("-wal", "-shm"):
        stray = path + suffix
        if os.path.exists(stray):
            os.remove(stray)

    # Set before importing app: bootstrap resolves the seed directory at
    # import time, exactly as serve.py does.
    os.environ["DJ_DB"] = path
    os.environ["DJ_SEED_DIR"] = os.path.join(PACKS, company)
    os.environ.setdefault("DJ_DEV_KEYS", "1")
    os.environ.setdefault("DJ_GITHUB_ALLOW_UNSIGNED", "1")
    sys.path.insert(0, ROOT)

    from app import bootstrap, demo                       # noqa: E402

    svc = bootstrap.build_services()
    keys = bootstrap.bootstrap(svc)
    print(f"  bootstrapped {len(keys)} principal(s)")

    t0 = time.monotonic()
    if os.environ.get("DJ_JUDGE_MODE") == "llm":
        print("      a model is judging, so each scenario makes real API"
              " calls —")
        print("      expect minutes, not seconds. Progress follows.")
    result = demo.run(svc, company, limit=limit, sign=sign)
    if not result.get("ran"):
        print(f"  demo did not replay: {result.get('reason')}",
              file=sys.stderr)
        return 1
    print(f"  replayed {result['cases']} scenario(s) in "
          f"{time.monotonic() - t0:.0f}s")
    for d, n in sorted(result["dispositions"].items(), key=lambda kv: -kv[1]):
        print(f"    {d:26s} {n}")
    if result["expectation_mismatches"]:
        print(f"    note: {len(result['expectation_mismatches'])} case(s)"
              f" differ from the original engine (see demo/README.md)")

    after = inspect(path)
    ok = not after["stale"]
    print(f"\n  verification: {'clean' if ok else 'STILL STALE'}")
    if after["untenanted"]:
        print(f"    rows with no company: {after['untenanted']}")
    orgs = svc.registry.organizations()
    if orgs:
        print(f"    tenants: {', '.join(o['name'] for o in orgs)}")
    # Suppressed when the caller is about to start the server itself
    # (relaunch.py): telling somebody to restart a server that is being
    # restarted for them is noise that reads like a warning.
    if show_next_steps:
        print("\n  now restart the server against this database:\n")
        print(f"    DJ_DB={path} DJ_DEV_KEYS=1 DJ_DEMO={company} \\")
        print("    DJ_GITHUB_ALLOW_UNSIGNED=1 python3 serve.py\n")
        # Detection cannot be perfect: an idle SQLite connection in WAL mode
        # holds no write lock, so a quietly-running server is
        # indistinguishable from a stale journal file. Rather than guess, say
        # what to do either way.
        print("    A server started earlier is still holding the OLD file"
              " and will\n    not show any of this until you stop and start"
              " it again.")
    print("\n  sign in with:")
    for pid, key in sorted(keys.items()):
        org = svc.registry.organization_of(pid) or "ALL TENANTS"
        if not pid.startswith("svc:"):
            print(f"    {pid:22s} {key:26s} {org}")
    print()
    return 0 if ok else 1


def _looks_in_use(path: str) -> bool:
    """Is something holding this database open right now?

    SQLite leaves -wal and -shm files beside an open database and tidies them
    away on a clean close, so their presence is a good-enough signal without
    needing lsof or /proc. False positives are possible after a hard kill,
    which is why this warns rather than refuses.
    """
    return any(os.path.exists(path + suffix) for suffix in ("-wal", "-shm"))


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Rebuild the demo database. The old file is moved aside,"
                    " never deleted in place: the ledger's own tables refuse"
                    " DELETE, and this script holds itself to the same rule.")
    ap.add_argument("--db", default=os.environ.get("DJ_DB", "/tmp/dj.db"),
                    help="database path (default: $DJ_DB or /tmp/dj.db)")
    ap.add_argument("--company", default="_all",
                    help=f"corpus to replay: {', '.join(companies()) or 'none built'}")
    ap.add_argument("--sign", action="store_true",
                    help="close the tier-k reviews with a stand-in risk owner"
                         " (leaves a fuller ledger; omit to leave real work"
                         " waiting in the queue)")
    ap.add_argument("--limit", type=int, default=0,
                    help="replay only the first N scenarios")
    ap.add_argument("--no-backup", action="store_true",
                    help="delete the old file instead of keeping a copy")
    ap.add_argument("--check", action="store_true",
                    help="report what is in the database and exit")
    ap.add_argument("--yes", "-y", action="store_true",
                    help="do not prompt (for scripts)")
    a = ap.parse_args()

    if a.check:
        report(a.db, inspect(a.db))
        return 0

    # The two ways a rebuild silently appears not to work, both checked
    # before anything is moved.
    env_db = os.environ.get("DJ_DB")
    if env_db and os.path.abspath(env_db) != os.path.abspath(a.db):
        print(f"\n  NOTE: DJ_DB in your environment is {env_db!r} but this"
              f" will rebuild {a.db!r}.")
        print("        Point them at the same file, or the server will keep"
              " reading the other one.")
    # No "continue anyway". Rebuilding under a live server keeps the old file
    # open in that process: the rebuild appears to succeed, the browser shows
    # no change, and the honest conclusion is that this script is broken.
    # Offering a choice between "fail" and "silently do nothing useful" is
    # not a choice worth offering.
    # Only the LOCK PROBE may refuse. The -wal/-shm heuristic below survives a
    # hard kill, so treating it as authoritative blocks a database that is
    # genuinely free — permanently, until someone deletes those files by
    # hand. That is the difference between a guard and a trap.
    if _looks_in_use(a.db) and not in_use(a.db):
        print(f"\n  NOTE: {a.db} has leftover -wal/-shm files, usually from a"
              f" server that was\n  killed rather than stopped. Nothing is"
              f" holding the database now, so this\n  will proceed.\n")
    if in_use(a.db):
        print(f"\n  {a.db} is open in a running server.", file=sys.stderr)
        print("  Rebuilding underneath it would not change what that server"
              " serves:\n  it keeps the old file open, and the browser would"
              " look unchanged.\n", file=sys.stderr)
        print("  Stop the server (Ctrl-C in its terminal), then run this"
              " again.\n", file=sys.stderr)
        return 3

    print(f"\nRebuilding {a.company} into {a.db}")
    before = inspect(a.db)
    if before["exists"]:
        print(f"  existing database: "
              f"{'stale' if before['stale'] else 'current'}, "
              f"{sum(before['counts'].values())} ledger row(s)")
    return rebuild(a.db, a.company, a.sign, a.limit, not a.no_backup)


if __name__ == "__main__":
    sys.exit(main())
