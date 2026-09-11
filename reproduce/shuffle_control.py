#!/usr/bin/env python3
"""Negative control: re-pair every intact seed record to a different provision.

The claim under test is that the ordering and the gate are doing the work, not the
mere presence of records. If every seed record is re-pointed at a provision other
than the one its holding was about, retrieval should surface almost nothing that
survives the gate, so controlled cases and bound decision events should collapse —
while admissions, which depend on contest and not on retrieval quality, should not
move at all.

The re-pairing is deterministic: the seed records are taken in file order and each
is moved to the next distinct provision in the rulebook's own order that is not the
one it already has. Lapsed (expired) records are left where they are, since they are
excluded from retrieval anyway and moving them would confound the control.

Usage:  python3 reproduce/shuffle_control.py [company]      (default: sctower)
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPANY = sys.argv[1] if len(sys.argv) > 1 else "sctower"


def repair(seed_path, rulebook_path, out_path):
    seeds = json.load(open(seed_path))
    provs = [p["provision_id"] for p in json.load(open(rulebook_path))["provisions"]]
    moved = 0
    for rec in seeds["records"]:
        if rec.get("expiry"):                      # lapsed/acceptance: leave in place
            continue
        cur = rec["provision_id"]
        i = provs.index(cur) if cur in provs else 0
        rec["provision_id"] = provs[(i + 1) % len(provs)]
        moved += 1
    json.dump(seeds, open(out_path, "w"), indent=1)
    return moved, len(seeds["records"])


def run(company, seed_file, db):
    env = dict(os.environ,
               DJ_JUDGE_MODE="oracle", DJ_DEV_KEYS="1",
               DJ_GITHUB_ALLOW_UNSIGNED="1", DJ_SEED_STORE=seed_file)
    subprocess.run([sys.executable, "demo/reset.py", "--db", db,
                    "--company", company, "--sign", "--yes"],
                   cwd=ROOT, env=env, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    out = subprocess.run([sys.executable, "reproduce/report.py", db, company],
                         cwd=ROOT, env=env, check=True, capture_output=True, text=True)
    return out.stdout.strip()


def main():
    cdir = os.path.join(ROOT, "demo", "companies", COMPANY)
    seed = os.path.join(cdir, "store_seed_initial.json")
    rules = os.path.join(cdir, "rulebook.json")
    shuffled_name = "store_seed_shuffled.json"
    shuffled = os.path.join(cdir, shuffled_name)

    moved, total = repair(seed, rules, shuffled)
    print(f"re-paired {moved} of {total} seed records to a different provision"
          f" (lapsed records left in place)\n")
    try:
        base = run(COMPANY, "store_seed_initial.json", "/tmp/dj_ctrl_base.db")
        ctrl = run(COMPANY, shuffled_name, "/tmp/dj_ctrl_shuf.db")
        print("baseline  " + base.strip())
        print("shuffled  " + ctrl.strip())
    finally:
        if os.path.exists(shuffled):
            os.remove(shuffled)
        for f in ("/tmp/dj_ctrl_base.db", "/tmp/dj_ctrl_shuf.db"):
            if os.path.exists(f):
                os.remove(f)


if __name__ == "__main__":
    main()
