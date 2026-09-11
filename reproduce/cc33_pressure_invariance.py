#!/usr/bin/env python3
"""CC-33 — pressure invariance, checked on executed traces.

For every P-pressure case, the disposition, the controlling record and the
stored status must be identical to its named control case.

This is not a tautology. The pressured twin's facts(c) is a strict superset of
its control's, and the distinguishing gate admits a record exactly when
premise(r) is a subset of facts(c) -- so the twin can acquire candidates the
control never had. If retrieval, the gate or the ordering leaked the extra
factor, the controlling record would move and this check would fail.

Usage: cc33_pressure_invariance.py <database> <cases.json>
Exit 0 if every pair holds; 1 otherwise.
"""
import collections, json, sqlite3, sys


def trace_map(db):
    """corpus case id -> runtime case_id, via pr_session.delivery_id ('demo-<pack>-<ID>')."""
    c = sqlite3.connect(db)
    sess = {}
    for sid, did in c.execute("select session_id, delivery_id from pr_session"):
        if did and "-" in did:
            sess[sid] = did.rsplit("-", 1)[-1]
    out = {}
    for sid, cid in c.execute("select session_id, case_id from pr_case"):
        if sid in sess:
            out.setdefault(sess[sid], set()).add(cid)
    return out


def final_state(db):
    """runtime case_id -> final disposition, controlling record, gate state, stored."""
    c = sqlite3.connect(db)
    per = collections.defaultdict(list)
    for seq, disp, detail in c.execute(
            "select seq, disposition, detail from pr_disposition order by seq"):
        try:
            rows = json.loads(detail) or []
        except Exception:
            continue
        for r in rows:
            if isinstance(r, dict) and r.get("case_id"):
                per[r["case_id"]].append((seq, disp, r))
    facts = {cid: set(json.loads(f or "[]"))
             for cid, f in c.execute("select case_id, facts from case_state")}
    stored = {cid for (cid,) in c.execute(
        "select case_id from precedent_record where case_id not like 'SEED-%'")}
    out = {}
    for cid, rows in per.items():
        _, disp, last = rows[-1]
        out[cid] = {"disposition": disp, "outcome": last.get("outcome"),
                    "controlling": last.get("controlling"),
                    "controlling_state": last.get("controlling_state"),
                    "stored": cid in stored, "facts": facts.get(cid, set())}
    return out


def main(db, cases_path):
    doc = json.load(open(cases_path))
    cases = doc["cases"]
    pressure = [c for c in cases if c.get("category") == "P-pressure"]
    if not pressure:
        print("CC-33  SKIP  no P-pressure cases in this pack")
        return 0

    st, tmap = final_state(db), trace_map(db)
    fails, checked = [], 0

    def one(corpus_id):
        ids = [t for t in tmap.get(corpus_id, ()) if t in st]
        return st[ids[0]] if len(ids) == 1 else None

    for p in pressure:
        ctrl_id = p["pressure"]["control_case"]
        a, b = one(p["id"]), one(ctrl_id)
        if a is None or b is None:
            fails.append((p["id"], "UNRESOLVED",
                          f"trace rows: twin={len(tmap.get(p['id'], ()))} "
                          f"control={len(tmap.get(ctrl_id, ()))}"))
            continue
        checked += 1
        for field in ("disposition", "outcome", "controlling_state", "controlling", "stored"):
            if a[field] != b[field]:
                fails.append((p["id"], field, f"{a[field]!r} vs control {b[field]!r}"))
        if not (a["facts"] > b["facts"]):
            fails.append((p["id"], "VACUOUS",
                          "pressured fact set is not a strict superset of the control's"))

    if fails:
        print(f"CC-33  FAIL  {len(fails)} discrepancies over {checked} pairs")
        for cid, field, detail in fails:
            print(f"         {cid}  {field}: {detail}")
        return 1
    print(f"CC-33  PASS  {checked}/{len(pressure)} pressure pairs invariant "
          f"(disposition, outcome, controlling record, gate state, stored status)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
