#!/usr/bin/env python3
"""PostgreSQL advisory locks — runnable example for Digital Judiciary.

Prerequisites
-------------
  pip install 'psycopg[binary]>=3.1'
  export DJ_DATABASE_URL=postgres://dj:dj@localhost:5432/judiciary

What this demonstrates
----------------------
1. lock_key() — stable bigint from a string namespace
2. Transaction-scoped exclusive lock (preferred around Gate.admit)
3. Non-blocking try-lock (lifecycle leader election)
4. Two workers contending for the same tenant lock

Run::

  python3 examples/pg_advisory_locks_example.py
"""
from __future__ import annotations

import os
import sys
import threading
import time

# Allow running from repo root without installing a package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.platform.pg_locks import (
    advisory_xact,
    gate_lock_key,
    lock_key,
    try_advisory_xact,
    with_gate_lock,
)


def example_transaction_lock() -> None:
    key = gate_lock_key("acme")
    print(f"1) transaction lock key={key} (gate:acme)")
    with advisory_xact(key) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1 AS ok")
            print("   held; query=", cur.fetchone())
    print("   released on commit/close")


def example_try_lock() -> None:
    key = lock_key("dj", "lifecycle", "sweep")
    print(f"2) try-lock key={key}")
    with try_advisory_xact(key) as got:
        print(f"   acquired={got}")
        if got:
            time.sleep(0.1)  # pretend to sweep
    print("   done")


def example_contention() -> None:
    key = gate_lock_key("acme")
    order: list[str] = []

    def worker(name: str, delay: float) -> None:
        time.sleep(delay)
        with advisory_xact(key):
            order.append(f"{name}:enter")
            time.sleep(0.15)
            order.append(f"{name}:exit")

    print("3) two threads, one tenant lock — must not interleave")
    t1 = threading.Thread(target=worker, args=("A", 0.0))
    t2 = threading.Thread(target=worker, args=("B", 0.05))
    t1.start(); t2.start()
    t1.join(); t2.join()
    print("   order:", order)
    # One worker fully enters+exits before the other enters
    assert order in (
        ["A:enter", "A:exit", "B:enter", "B:exit"],
        ["B:enter", "B:exit", "A:enter", "A:exit"],
    ), order
    print("   serialisation OK")


def example_with_gate_lock_helper() -> None:
    print("4) with_gate_lock helper (no-op if not on Postgres)")

    def admit_stub():
        return "PREC-example"

    rid = with_gate_lock("acme", admit_stub)
    print(f"   admit -> {rid}")


def main() -> int:
    url = os.environ.get("DJ_DATABASE_URL", "")
    if not url.startswith("postgres"):
        print("Set DJ_DATABASE_URL=postgres://... to run this example.")
        print("Showing lock_key values only:\n")
        for label in ("global", "acme", "contoso"):
            print(f"  gate:{label:8s} -> {gate_lock_key(label if label != 'global' else None)}")
        return 0
    try:
        example_transaction_lock()
        example_try_lock()
        example_contention()
        example_with_gate_lock_helper()
    except Exception as e:
        print("ERROR:", e)
        return 1
    print("\nAll advisory-lock examples passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
