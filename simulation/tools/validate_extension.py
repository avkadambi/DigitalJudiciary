#!/usr/bin/env python3
"""Validate a pack's scenario-extension modules before they are merged.

Usage: python3 tools/validate_extension.py <pack-dir>

Reads <pack>/generator/{vocab,changes,ext_vocab,ext_changes}.py and
simulation/scenarios.json and checks everything the generator, the conformance
suite (VC-47's leak test, VC-49's development-change guard) and the coverage
check (VC-50) will later demand. Exit code 1 on any failure.
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)

HARM = {"legal", "regulatory", "reputational", "safety", "financial"}
ID_RE = {
    "vetpoc": r"^VP-[A-Z]{2}-\d{3}$",
    "semifab": r"^SF-[A-Z]{2}-\d{3}$",
    "frontierllm": r"^FL-[A-Z]{2}-\d{3}$",
    "dcvigil": r"^DV-\d{3}$",
    "meridian": r"^MF-\d{3}$",
}
FACTOR_RE = re.compile(r"^[a-z][a-z0-9_]{8,90}$")


MERGE_MARK = "# --- scenario extension (corpus 2.0.0) ---"


def load(path, name, pre_merge=False):
    """Import a module. With pre_merge, execute only the source above the merge
    marker, so the validator sees vocab.py / changes.py as they were before the
    extension was merged in and can be run after integration as well as before."""
    src = open(path).read()
    if pre_merge and MERGE_MARK in src:
        src = src.split(MERGE_MARK, 1)[0]
        m = type(sys)(name)
        m.__file__ = path
        exec(compile(src, path, "exec"), m.__dict__)
        return m
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(pack):
    pack = os.path.abspath(pack)
    key = next(k for k in ID_RE if k in os.path.basename(pack))
    g = os.path.join(pack, "generator")
    vocab = load(os.path.join(g, "vocab.py"), "vocab", pre_merge=True)
    changes = load(os.path.join(g, "changes.py"), "changes", pre_merge=True)
    ev = load(os.path.join(g, "ext_vocab.py"), "ext_vocab")
    ec = load(os.path.join(g, "ext_changes.py"), "ext_changes")
    scen = json.load(open(os.path.join(SIM, "scenarios.json")))
    scen_ids = {s["id"] for s in scen["scenarios"]}
    scen_by = {s["id"]: s for s in scen["scenarios"]}

    errs, warns = [], []
    E = errs.append
    W = warns.append

    old_ids = {p[0] for p in vocab.PROVISIONS}
    old_fams = set(vocab.FAMILIES)
    old_factors = set()
    for f in vocab.FAMILIES.values():
        old_factors |= set(f["comply"]) | set(f["violate"])
    old_titles = set(changes.VIOLATION_CHANGES.values())
    for lst in changes.COMPLIANT_CHANGES.values():
        old_titles |= set(lst)
    areas = set(getattr(vocab, "AREAS", getattr(changes, "AREAS", [])))
    services = set(getattr(vocab, "SERVICES", getattr(changes, "SERVICES", [])))

    # ---- families -------------------------------------------------------
    new_fams = ev.FAMILIES
    for fam, f in new_fams.items():
        if fam in old_fams:
            E(f"family {fam} already exists")
        if not re.match(r"^[A-Z]{2}$", fam):
            E(f"family code {fam} must be two capitals")
        for k in ("title", "risk", "comply", "violate"):
            if k not in f:
                E(f"{fam}: missing {k}")
        for pool in ("comply", "violate"):
            for x in f.get(pool, []):
                if not FACTOR_RE.match(x):
                    E(f"{fam}.{pool}: bad factor name {x!r}")
                if x in old_factors:
                    E(f"{fam}.{pool}: factor {x} already exists in the pack")
                if "scenario" in x or x.startswith("mk_") or x.startswith("ctx_"):
                    E(f"{fam}.{pool}: forbidden token in {x}")
            if len(set(f.get(pool, []))) != len(f.get(pool, [])):
                E(f"{fam}.{pool}: duplicate factors")
        if fam not in ev.TAU:
            E(f"{fam}: no TAU entry")
        elif not (12 <= ev.TAU[fam] <= 40):
            E(f"{fam}: TAU {ev.TAU[fam]} outside 12..40")
        if fam not in ec.FAMILY_CONTEXT:
            E(f"{fam}: no FAMILY_CONTEXT")
        else:
            ctx = ec.FAMILY_CONTEXT[fam]
            if not set(ctx.get("areas", [])) <= areas or not ctx.get("areas"):
                E(f"{fam}: FAMILY_CONTEXT.areas not a non-empty subset of the pack's areas: {ctx.get('areas')}")
            if not set(ctx.get("services", [])) <= services or not ctx.get("services"):
                E(f"{fam}: FAMILY_CONTEXT.services not a non-empty subset of the pack's services: {ctx.get('services')}")
        if fam not in ec.COMPLIANT_CHANGES or len(ec.COMPLIANT_CHANGES[fam]) < 10:
            E(f"{fam}: need >= 10 COMPLIANT_CHANGES titles")

    all_new_factors = set()
    for f in new_fams.values():
        all_new_factors |= set(f["comply"]) | set(f["violate"])
    cross = set()
    for f in new_fams.values():
        for pool in ("comply", "violate"):
            for x in f[pool]:
                if x in cross:
                    E(f"factor {x} appears in two new families/pools")
                cross.add(x)

    # ---- provisions -----------------------------------------------------
    per_fam = {}
    seen = set()
    n_abs = 0
    for p in ev.PROVISIONS:
        pid = p.get("id", "?")
        if not re.match(ID_RE[key], pid):
            E(f"{pid}: id does not match {ID_RE[key]}")
        if pid in old_ids or pid in seen:
            E(f"{pid}: duplicate or existing id")
        seen.add(pid)
        for k in ("family", "title", "absolute", "citation", "source_status", "status", "origin", "scenarios", "harm_classes"):
            if k not in p:
                E(f"{pid}: missing field {k}")
        fam = p.get("family")
        if fam not in new_fams:
            E(f"{pid}: family {fam} is not a new family (new provisions must sit in new families)")
        per_fam[fam] = per_fam.get(fam, 0) + 1
        if p.get("absolute"):
            n_abs += 1
            if p.get("status") != "in_force":
                E(f"{pid}: absolute but not in_force")
        if p.get("status") not in ("in_force", "deferred", "advisory", "readiness"):
            E(f"{pid}: bad status {p.get('status')}")
        if p.get("origin") != "extension":
            E(f"{pid}: origin must be 'extension'")
        if not set(p.get("scenarios", [])) <= scen_ids or not p.get("scenarios"):
            E(f"{pid}: scenarios must be a non-empty subset of scenarios.json: {p.get('scenarios')}")
        for s in p.get("scenarios", []):
            if key not in scen_by[s]["applies_to"]:
                W(f"{pid}: scenario {s} is not listed as applying to {key} in scenarios.json (add it there if intended)")
        if not set(p.get("harm_classes", [])) <= HARM or not p.get("harm_classes"):
            E(f"{pid}: harm_classes must be a non-empty subset of {sorted(HARM)}")
        t = p.get("title", "")
        if len(t) < 40:
            E(f"{pid}: title too short")
        if "scenario" in t.lower():
            E(f"{pid}: title contains the word 'scenario' (VC-47 leak test)")
        if not p.get("citation", "").strip():
            E(f"{pid}: empty citation")
        if p.get("absolute") and re.search(r"^(practice policy|internal policy|firm policy)$", p.get("citation", "").strip(), re.I):
            W(f"{pid}: absolute provision cited only to internal policy; state why it is a who-may-decide floor in source_status")

    # pool sizing: n-th provision gets comply[3n:3n+8], violate[2n:2n+5]
    for fam, k in per_fam.items():
        f = new_fams[fam]
        if len(f["comply"]) < 3 * k + 5:
            E(f"{fam}: {k} provisions need >= {3*k+5} comply factors (have {len(f['comply'])})")
        if len(f["violate"]) < 2 * k + 3:
            E(f"{fam}: {k} provisions need >= {2*k+3} violate factors (have {len(f['violate'])})")
    for fam in new_fams:
        if fam not in per_fam:
            E(f"{fam}: family has no provisions")

    # ---- change titles --------------------------------------------------
    for fam, f in new_fams.items():
        for v in f["violate"]:
            if v not in ec.VIOLATION_CHANGES:
                E(f"{fam}: violate factor {v} has no VIOLATION_CHANGES title")
    titles = list(ec.VIOLATION_CHANGES.values())
    for lst in ec.COMPLIANT_CHANGES.values():
        titles.extend(lst)
    for t in titles:
        if not changes.is_development_change(t):
            E(f"title fails VC-49 development-change guard: {t!r}")
        low = t.lower()
        for bad in ("scenario", "axiom", "provision", "factor", "judiciary", "adjudicat", "absolute rule"):
            if bad in low:
                E(f"title contains forbidden token {bad!r}: {t!r}")
        if re.search(r"\b(VP|SF|FL|DV|MF)-", t):
            E(f"title names a provision id: {t!r}")
        if t in old_titles:
            E(f"title duplicates an existing catalogue title: {t!r}")
        if len(t) < 25 or len(t) > 110:
            W(f"title length unusual ({len(t)}): {t!r}")
    if len(set(titles)) != len(titles):
        dup = {t for t in titles if titles.count(t) > 1}
        E(f"duplicate titles: {sorted(dup)[:5]}")
    for k in ec.VIOLATION_CHANGES:
        if k not in all_new_factors:
            E(f"VIOLATION_CHANGES key {k} is not a new violate factor")

    # ---- scenario mapping for existing families -------------------------
    fs = getattr(ev, "FAMILY_SCENARIOS", {})
    for fam in old_fams:
        if fam not in fs or not fs[fam]:
            E(f"FAMILY_SCENARIOS missing existing family {fam}")
        elif not set(fs[fam]) <= scen_ids:
            E(f"FAMILY_SCENARIOS[{fam}] has unknown scenario ids")
    for pid, lst in getattr(ev, "PROVISION_SCENARIOS", {}).items():
        if pid not in old_ids:
            E(f"PROVISION_SCENARIOS names unknown provision {pid}")
        if not set(lst) <= scen_ids:
            E(f"PROVISION_SCENARIOS[{pid}] has unknown scenario ids")

    # ---- amendments -----------------------------------------------------
    old_pa = {a["id"] for a in getattr(vocab, "PROPOSED_AMENDMENTS", [])}
    for a in getattr(ev, "PROPOSED_AMENDMENTS", []):
        for k in ("id", "targets", "raised_by", "finding", "proposed", "why_not_applied", "disposition"):
            if k not in a:
                E(f"amendment {a.get('id')}: missing {k}")
        if a.get("id") in old_pa:
            E(f"amendment {a['id']} collides with an existing amendment id")
        for t in a.get("targets", []):
            if t not in old_ids and t not in seen:
                E(f"amendment {a.get('id')}: target {t} unknown")

    # ---- summary --------------------------------------------------------
    n = len(ev.PROVISIONS)
    print(f"{key}: {n} new provisions ({n_abs} absolute) in {len(new_fams)} new families; "
          f"{len(all_new_factors)} new factors; {len(titles)} new titles; "
          f"{len(getattr(ev, 'PROPOSED_AMENDMENTS', []))} new amendments")
    if n < 20:
        W(f"only {n} new provisions; target is 20-26")
    covered = set()
    for p in ev.PROVISIONS:
        covered |= set(p["scenarios"])
    for fam, lst in fs.items():
        covered |= set(lst)
    missing = [s for s in scen_ids if key in scen_by[s]["applies_to"] and s not in covered]
    if missing:
        E(f"scenarios that apply to {key} but map to no provision (old or new): {sorted(missing)}")
    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("ERROR", e)
    print("RESULT:", "OK" if not errs else f"{len(errs)} error(s)")
    return 0 if not errs else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
