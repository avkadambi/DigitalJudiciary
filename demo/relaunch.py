#!/usr/bin/env python3
"""Relaunch the demo from scratch: stop, wipe, seed every tenant, restart.

    python3 demo/relaunch.py                    # the whole cycle, all 4 tenants
    python3 demo/relaunch.py --company sctower  # one tenant instead
    python3 demo/relaunch.py --stop             # just stop the server
    python3 demo/relaunch.py --no-start         # stop and rebuild, don't restart

This exists because the cycle has four steps and getting them out of order
looks exactly like the software being broken:

  * Rebuilding while the server runs does nothing visible. The process keeps
    the old database file open, so the browser shows the old data and the
    rebuild appears to have failed.
  * The holdings cache lives in memory. It is not a file to delete — it dies
    with the process, which is another reason the server has to stop first.
  * Seeding before starting keeps startup fast. serve.py replays the corpus
    only into an empty database, so if the data is already there it comes up
    in seconds rather than minutes.

So: stop, wipe, seed, start. In that order, every time.
"""
from __future__ import annotations

import argparse
import os
import shutil
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import reset as reset_mod                                    # noqa: E402

DEFAULT_DB = os.environ.get("DJ_DB", "/tmp/dj.db")
DEFAULT_PORT = int(os.environ.get("DJ_PORT", "8080"))
DEFAULT_HOST = os.environ.get("DJ_HOST", "127.0.0.1")


def step(n: int, text: str) -> None:
    print(f"\n[{n}/4] {text}")


# ---------------------------------------------------------------------------
# 1. stop
# ---------------------------------------------------------------------------
def pidfile_for(port: int) -> str:
    return os.path.join("/tmp", f"dj-serve-{port}.pid")


def find_servers(db: str, port: int) -> list[tuple[int, str]]:
    """The server for this port, from its pid file — and nothing else.

    An earlier version matched `ps` output for "serve.py". That is unsafe: a
    shell whose own command line merely mentions the filename matches too,
    and this script killed the terminal it was running in. Nothing is
    signalled now unless serve.py wrote its own pid down.
    """
    path = pidfile_for(port)
    if not os.path.exists(path):
        return []
    try:
        parts = open(path).read().split("\n")
        pid = int(parts[0].strip())
    except (OSError, ValueError, IndexError):
        return []
    try:
        os.kill(pid, 0)                       # exists and is signallable?
    except ProcessLookupError:
        os.remove(path)                       # stale file, nothing running
        return []
    except PermissionError:
        pass
    recorded_db = parts[1].strip() if len(parts) > 1 else ""
    return [(pid, f"serve.py on :{port}"
                  + (f" db={recorded_db}" if recorded_db else ""))]


def port_free(host: str, port: int) -> bool:
    import socket
    with socket.socket() as sk:
        sk.settimeout(0.6)
        return sk.connect_ex((host, port)) != 0


def stop(db: str, host: str, port: int) -> bool:
    """Stop the server. Returns True only if the port is genuinely free.

    The return value is load-bearing. An earlier version returned nothing and
    the caller carried on regardless, which meant that when this refused to
    kill an unattributable process it went on to wipe and reseed the database
    anyway — while the old server kept serving the old code, from the old
    file, on the same port. The visible symptom was "I ran relaunch and
    nothing changed", which is exactly the wrong thing to conclude.
    """
    found = find_servers(db, port)
    if not found:
        if port_free(host, port):
            print("      nothing running")
            return True
        print(f"      something is answering on {host}:{port} but wrote no"
              f" pid file.")
        print("      That usually means it was started by a build older than"
              " this one.")
        print("      Refusing to guess which process to kill. Stop it by"
              " hand:")
        print("        · Ctrl-C in the terminal running serve.py, or")
        print(f"        · lsof -ti tcp:{port} | xargs kill      (macOS/Linux)")
        return False
    for pid, args in found:
        print(f"      stopping pid {pid}  {args}")
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        except PermissionError:
            print(f"      cannot signal pid {pid} — stop it by hand")
    for _ in range(40):                      # up to ~8s for a clean exit
        if port_free(host, port) and not find_servers(db, port):
            print("      stopped")
            return True
        time.sleep(0.2)
    # A clean shutdown had its chance; the ledger is on disk and consistent
    # either way, so escalating here costs nothing but an unclean journal.
    for pid, _ in find_servers(db, port):
        print(f"      pid {pid} did not exit; sending SIGKILL")
        try:
            os.kill(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    time.sleep(1.0)
    if port_free(host, port):
        print("      stopped")
        return True
    print(f"      WARNING: {host}:{port} is still answering")
    return False


# ---------------------------------------------------------------------------
# 2. wipe
# ---------------------------------------------------------------------------
def wipe(db: str, keep_backup: bool) -> None:
    stamp = time.strftime("%Y%m%d-%H%M%S")
    moved = 0
    for suffix in ("", "-wal", "-shm"):
        path = db + suffix
        if not os.path.exists(path):
            continue
        if keep_backup:
            shutil.move(path, f"{db}.{stamp}.bak{suffix}")
        else:
            os.remove(path)
        moved += 1
    if moved:
        print(f"      {'moved aside' if keep_backup else 'deleted'}"
              f" {moved} file(s)"
              + (f" -> {db}.{stamp}.bak*" if keep_backup else ""))
    else:
        print("      no existing database")

    # Python bytecode caches. Not data, but they are the other thing people
    # mean by "the cache", and a stale one after an edit is confusing.
    cleared = 0
    for base, dirs, _ in os.walk(ROOT):
        for d in list(dirs):
            if d == "__pycache__":
                shutil.rmtree(os.path.join(base, d), ignore_errors=True)
                dirs.remove(d)
                cleared += 1
    print(f"      cleared {cleared} bytecode cache dir(s)")
    print("      the holdings cache is in memory and went with the process")


# ---------------------------------------------------------------------------
# 4. start
# ---------------------------------------------------------------------------
def start(db: str, host: str, port: int, company: str,
          wait: int) -> subprocess.Popen | None:
    env = dict(os.environ)
    env.update({"DJ_DB": db, "DJ_HOST": host, "DJ_PORT": str(port),
                "DJ_DEMO": company, "DJ_DEV_KEYS": "1",
                "DJ_GITHUB_ALLOW_UNSIGNED": "1"})
    log = os.path.join("/tmp", f"dj-serve-{port}.log")
    fh = open(log, "w")
    proc = subprocess.Popen([sys.executable, "serve.py"], cwd=ROOT, env=env,
                            stdout=fh, stderr=subprocess.STDOUT,
                            start_new_session=True)
    print(f"      pid {proc.pid}, log {log}")
    url = f"http://{host}:{port}/v1/admin/status"
    for i in range(wait * 2):
        if proc.poll() is not None:
            print(f"      the server exited immediately — see {log}")
            fh.close()
            return None
        try:
            with urllib.request.urlopen(url, timeout=2):
                print(f"      answering after {i / 2:.0f}s")
                return proc
        except (urllib.error.URLError, OSError):
            time.sleep(0.5)
    print(f"      not answering after {wait}s — see {log}")
    return proc


# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(
        description="Stop the server, wipe the database, seed every tenant,"
                    " and start it again.")
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--host", default=DEFAULT_HOST)
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument("--company", default="_all",
                    help=f"corpus to seed (default _all): "
                         f"{', '.join(reset_mod.companies()) or 'none built'}")
    ap.add_argument("--no-sign", action="store_true",
                    help="leave the escalated reviews OPEN, so the risk"
                         " owner's queue has real work waiting")
    ap.add_argument("--limit", type=int, default=0,
                    help="seed only the first N scenarios (faster)")
    ap.add_argument("--no-backup", action="store_true",
                    help="delete the old database instead of keeping a copy")
    ap.add_argument("--stop", action="store_true", help="stop and do no more")
    ap.add_argument("--no-start", action="store_true",
                    help="stop and rebuild, but do not start the server")
    ap.add_argument("--wait", type=int, default=600,
                    help="seconds to wait for the server to answer")
    a = ap.parse_args()

    print("\nDigital Judiciary — relaunch")
    print(f"  database {a.db}")
    print(f"  address  http://{a.host}:{a.port}")
    print(f"  corpus   {a.company}")

    step(1, "Stopping the server")
    stopped = stop(a.db, a.host, a.port)
    if a.stop:
        print("\n  --stop given; nothing else done.\n")
        return 0 if stopped else 3

    # Abort BEFORE touching the database. Rebuilding under a server that is
    # still running destroys the old data and changes nothing the browser can
    # see — the worst of both outcomes.
    if not stopped:
        print(f"\n  Nothing was changed. The old server still holds"
              f" {a.host}:{a.port},\n  so rebuilding now would wipe the data"
              f" and leave the browser showing\n  exactly what it shows"
              f" today.\n", file=sys.stderr)
        return 3

    step(2, "Removing the old data")
    wipe(a.db, keep_backup=not a.no_backup)

    step(3, f"Seeding {a.company} — constitutions, jurisprudence, users")
    # Delegated to reset.py rather than reimplemented: it already replays the
    # corpus through the real gateway and verifies the result afterwards.
    rc = reset_mod.rebuild(a.db, a.company, sign=not a.no_sign,
                           limit=a.limit, backup=False,
                           show_next_steps=False)
    if rc != 0:
        print("\n  seeding failed; the server was not started.\n",
              file=sys.stderr)
        return rc

    if a.no_start:
        print("\n  --no-start given; the database is ready.\n")
        return 0

    step(4, "Starting the server")
    proc = start(a.db, a.host, a.port, a.company, a.wait)
    if proc is None:
        return 1

    print(f"\n  Ready — http://{a.host}:{a.port}/review")
    print("  Sign in from the dropdown; every tenant's officers are listed.")
    print(f"  Stop it with: python3 demo/relaunch.py --stop"
          f" --port {a.port}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
