#!/usr/bin/env python3
"""Build the Numerals enterprise constitution, the inheritance map against the
five division packs, and the 3,000-case federated stream with computed ground
truth.

    python3 generator/build_enterprise.py

Deterministic (seed 20260907). Reads the five division rulebooks and
organizations files; writes nothing into any division pack.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SIM = os.path.dirname(ROOT)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import enterprise_vocab as V  # noqa: E402
import enterprise_changes as CH  # noqa: E402
import engine  # noqa: E402
import federation as F  # noqa: E402

SEED = 20260907
rng = random.Random(SEED)
RULEBOOK_VERSION = "numerals-rb-000001"
CORPUS_VERSION = "1.3.0"
THETA = 0.25
TS_CASE_START = 1000

# The division packs' lexical development-change guard, applied to every title.
NON_DEV = ("complete the", "complete vendor", "rehearse the", "rehearse regional", "exercise the",
           "exercise failover", "retro-approve", "notify the", "escalate overdue", "issue the",
           "cite the", "get sre", "have the safety", "have the external", "sample production",
           "audit the orphaned", "close complaints", "close last", "close the tool", "correct the mis",
           "correct the mistyped", "export the whole", "export the quarterly", "export the mature",
           "provision external", "review the benchmark", "review alert", "mark the shipment",
           "send the capacity", "run the retention sweep", "file the ", "file blocked")


def is_development_change(t):
    t = " ".join(t.lower().split())
    if t.startswith(("file a draft amendment", "file an amendment")):
        return True
    return not any(t.startswith(x) for x in NON_DEV)


def slice_pool(pool, offset, count):
    return [pool[(offset + i) % len(pool)] for i in range(min(count, len(pool)))]


# ---------------------------------------------------------------------------
# 1. Constitution and inheritance
# ---------------------------------------------------------------------------

def load_divisions():
    out = {}
    for key, label, d in V.DIVISIONS:
        root = os.path.join(SIM, d)
        rb = json.load(open(os.path.join(root, "constitution", "rulebook.json")))
        orgs = json.load(open(os.path.join(root, "constitution", "organizations.json")))
        out[key] = {"label": label, "dir": d, "provisions": rb["provisions"], "orgs": orgs,
                    "rulebook_version": rb["rulebook_version"], "corpus_version": rb.get("corpus_version")}
    return out


def build_constitution(divisions):
    """Enterprise provisions with their factor slices and the curated inheritance
    map resolved against the division rulebooks. The floor rule is applied here:
    an enterprise provision is stated ABSOLUTE only where every applicable
    division already states a floor for it. Where the author asked for a floor
    and a division states the duty ordinarily, the enterprise cannot impose it
    over a frozen division constitution — that is exactly the act A3 forbids —
    so the provision is stated ordinarily with `proposed_absolute: true` and a
    draft amendment is filed against the loosening division provisions."""
    by_div = {d: {p["id"]: p for p in v["provisions"]} for d, v in divisions.items()}
    provisions, fam_ix, amendments = [], {}, []
    for pid, fam, title, absolute_requested, citation, source in V.PROVISIONS:
        f = V.FAMILIES[fam]
        n = fam_ix.get(fam, 0); fam_ix[fam] = n + 1
        slug = pid.lower().replace("-", "_")
        comply = slice_pool(f["comply"], n * 3, 8) + [f"{slug}_control_evidenced"]
        violate = slice_pool(f["violate"], n * 2, 5) + [f"{slug}_control_absent"]
        implemented_by, loosening, gaps = {}, [], []
        for dkey in divisions:
            ids = V.IMPLEMENTED_BY[pid][dkey]
            if ids is None:
                implemented_by[dkey] = {"applies": False, "provisions": []}
                continue
            rows = []
            for i in ids:
                if i not in by_div[dkey]:
                    raise SystemExit(f"{pid}: {dkey} has no provision {i}")
                q = by_div[dkey][i]
                rows.append({"id": i, "absolute": q["absolute"], "status": q.get("status", "in_force"), "title": q["title"]})
            implemented_by[dkey] = {"applies": True, "provisions": rows}
            if not rows:
                gaps.append(dkey)
            elif absolute_requested and not any(r["absolute"] for r in rows):
                loosening.append((dkey, [r["id"] for r in rows]))
        absolute = absolute_requested and not loosening
        if absolute_requested and loosening:
            amendments.append({
                "id": f"NPA-{len(amendments) + 1:02d}", "level": "division",
                "targets": {d: ids for d, ids in loosening}, "enterprise_provision": pid,
                "raised_by": "Numerals group compliance office, inheritance survey 1.0.0",
                "finding": (f"The enterprise states {pid} as a floor and the division provision(s) named state the same duty "
                            f"as an ordinary provision that a division risk owner may accept. Under minimum harmonisation a "
                            f"division may not be looser than the enterprise."),
                "proposed": "Restate the named division provisions as absolute, or narrow them and add an absolute limb.",
                "why_not_applied": ("The division constitutions are frozen revisions with executed corpora. Re-classifying a "
                                    "division provision changes which cases short-circuit under A6; only that division's "
                                    "lawmakers may do it (A3). Until they do, the enterprise states the duty ordinarily and "
                                    "records that a floor was proposed."),
                "disposition": "pending"})
        for dkey in gaps:
            amendments.append({
                "id": f"NPA-{len(amendments) + 1:02d}", "level": "division", "targets": {dkey: []},
                "enterprise_provision": pid, "raised_by": "Numerals group compliance office, inheritance survey 1.0.0",
                "finding": f"{dkey} has no provision implementing enterprise provision {pid} ({title[:80]}...).",
                "proposed": f"Add an implementing provision to the {dkey} constitution, by addition.",
                "why_not_applied": "A3: the enterprise proposes; the division's lawmakers dispose.",
                "disposition": "pending"})
        provisions.append({
            "id": pid, "level": "enterprise", "family": fam, "family_title": f["title"], "title": title,
            "absolute": absolute, "proposed_absolute": bool(absolute_requested and not absolute),
            "citation": citation, "source_status": source, "risk_framework": f["risk"],
            "status": "in_force", "origin": "enterprise", "tau": V.TAU[fam], "scope_domain": "NM:" + fam,
            "factors": {"comply": sorted(set(comply)), "violate": sorted(set(violate))},
            "implemented_by": implemented_by,
        })
    return provisions, amendments


def inheritance(provisions):
    """Per enterprise provision and division: implemented / tightened / loosened / gap."""
    rows, loosened, gaps = [], [], []
    for p in provisions:
        for dkey, m in p["implemented_by"].items():
            if not m["applies"]:
                rows.append({"enterprise": p["id"], "division": dkey, "status": "not_applicable", "division_provisions": []})
                continue
            ids = [x["id"] for x in m["provisions"]]
            if not ids:
                rows.append({"enterprise": p["id"], "division": dkey, "status": "gap", "division_provisions": []})
                gaps.append((p["id"], dkey))
                continue
            any_abs = any(x["absolute"] for x in m["provisions"])
            if p["absolute"] and not any_abs:
                st = "loosened"; loosened.append((p["id"], dkey, ids))
            elif (not p["absolute"]) and any_abs:
                st = "tightened"
            else:
                st = "implemented"
            rows.append({"enterprise": p["id"], "division": dkey, "status": st, "division_provisions": ids})
    return rows, loosened, gaps


# ---------------------------------------------------------------------------
# 2. The federated stream
# ---------------------------------------------------------------------------

DIV_KEYS = [d[0] for d in V.DIVISIONS]


def main():
    divisions = load_divisions()
    provisions, amendments = build_constitution(divisions)
    rows, loosened, gaps = inheritance(provisions)
    for t in list(CH.VIOLATION_CHANGES.values()) + [t for l in CH.COMPLIANT_CHANGES.values() for t in l] + CH.CONTROL_PLANE_CHANGES:
        if not is_development_change(t):
            raise SystemExit(f"title fails the development-change guard: {t!r}")
    for fam, f in V.FAMILIES.items():
        for v in f["violate"]:
            if v not in CH.VIOLATION_CHANGES:
                raise SystemExit(f"{fam}: violate factor {v} has no title")

    os.makedirs(os.path.join(ROOT, "constitution"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "corpus"), exist_ok=True)

    principals = []
    for a in V.LAWMAKERS:
        principals.append({"principal_id": a, "branch": "lawmakers", "kind": "human", "role": a.split(":", 1)[1].replace("-", " ")})
    for a in V.JUDGES:
        principals.append({"principal_id": a, "branch": "judges", "kind": "automated instance", "role": a.split(":", 1)[1].replace("-", " ")})
    for a in V.RISK_OWNERS:
        principals.append({"principal_id": a, "branch": "riskowner", "kind": "human", "role": a.split(":", 1)[1].replace("-", " ")})
    orgs = {"organizations": [{"org_id": "numerals", "name": "Numerals (enterprise)", "principals": principals,
                               "divisions": [{"org_id": k, "name": v["label"], "pack": v["dir"]} for k, v in divisions.items()]}],
            "disjointness": ("A1 per level: no enterprise principal appears in any division roster, and the "
                             "three enterprise branches are pairwise disjoint. FC-04 checks both against the six files."),
            "founding_scope": "numerals"}
    _write(os.path.join(ROOT, "constitution", "organizations.json"), orgs)
    engine.load_roster(os.path.join(ROOT, "constitution", "organizations.json"))

    rulebook = {
        "rulebook_version": RULEBOOK_VERSION, "corpus_version": CORPUS_VERSION, "level": "enterprise",
        "name": "Numerals Enterprise Constitution",
        "description": ("The constitution every Numerals division inherits. Inheritance is minimum harmonisation: a "
                        "division may tighten an enterprise provision and may never loosen one; an enterprise absolute "
                        "is a floor in every division. Records on enterprise provisions bind enterprise-wide; a "
                        "division's own record is narrower in scope and wins on the ordering rule's scope key."),
        "inheritance_rule": {"may_tighten": True, "may_loosen": False, "enterprise_absolute_is_division_floor": True,
                             "foreign_record_scope_offset": F.FOREIGN_SCOPE_OFFSET},
        "counts": {"provisions": len(provisions), "absolute": sum(1 for p in provisions if p["absolute"]),
                   "proposed_absolute": sum(1 for p in provisions if p["proposed_absolute"]),
                   "families": len(V.FAMILIES), "divisions": len(divisions)},
        "authorities": {"lawmakers": V.LAWMAKERS, "judges": V.JUDGES, "riskowner": V.RISK_OWNERS},
        "standing_declaration": {"id": "NM-STAND-0001", "scope": "global", "adverse_contest_standing_exists": True,
                                 "declared_by": "lawmaker:numerals-group-compliance-office", "declared_at": 0,
                                 "note": "A9 first limb at the enterprise level: the group compliance office holds contest standing adverse to grants in every division."},
        "divisions": {k: {"label": v["label"], "pack": v["dir"], "rulebook_version": v["rulebook_version"], "corpus_version": v["corpus_version"]} for k, v in divisions.items()},
        "provisions": provisions,
    }
    _write(os.path.join(ROOT, "constitution", "rulebook.json"), rulebook)
    _write(os.path.join(ROOT, "constitution", "factors.json"), {p["id"]: p["factors"] for p in provisions})
    _write(os.path.join(ROOT, "constitution", "parameters.json"),
           {"theta": THETA, "N0": 2, "delta_days": 14, "escalation_ladder": ["NJ1", "NJ2", "NJ3", "riskowner"],
            "acceptance_expiry_days": 180, "foreign_record_scope_offset": F.FOREIGN_SCOPE_OFFSET,
            "amendable_only_by": "Legislate", "federation_check_ids": [f"FC-{i:02d}" for i in range(1, 11)]})
    _write(os.path.join(ROOT, "constitution", "proposed_amendments.json"),
           {"note": ("Findings from the inheritance survey, filed by the enterprise against division constitutions and "
                     "never applied. Under A3 the enterprise proposes and each division's lawmakers dispose."),
            "amendments": amendments})
    _write(os.path.join(ROOT, "constitution", "inheritance.json"),
           {"rule": "minimum harmonisation — a division may tighten, never loosen; an enterprise absolute is a floor everywhere",
            "rows": rows,
            "loosened": [{"enterprise": e, "division": d, "division_provisions": ids} for e, d, ids in loosened],
            "gaps": [{"enterprise": e, "division": d} for e, d in gaps]})
    print(f"constitution: {len(provisions)} enterprise provisions, {rulebook['counts']['absolute']} absolute "
          f"({sum(1 for p in provisions if p['proposed_absolute'])} proposed floors held ordinary pending division amendment); "
          f"inheritance rows {len(rows)}, loosened {len(loosened)}, gaps {len(gaps)}, draft amendments {len(amendments)}")
    if gaps:
        for e, d in gaps:
            print("   GAP", e, d)

    # ---- provisions as engine objects --------------------------------------
    P = {p["id"]: engine.Provision.from_dict(p) for p in provisions}
    ORD = [p for p in P.values() if not p.absolute]
    ABS = [p for p in P.values() if p.absolute]
    ALL = list(P.values())

    # ---- seed store: for every ordinary provision, one seed record per division
    # with a distinct premise, so cross-division binding and vertical precedent are
    # both available from the first arrival.
    seed, seed_div = [], {}
    ts_seed = 0
    for p in ORD:
        comply = list(p.comply_factors)
        viol = [v for v in p.violate_factors if v in CH.VIOLATION_CHANGES] or list(p.violate_factors)
        for i, dkey in enumerate(DIV_KEYS):
            ts_seed += 1
            base = comply[(2 * i) % len(comply):(2 * i) % len(comply) + 2]
            if len(base) < 2:
                base = comply[:2]
            # Divisions alternate: an even-indexed division's seed is a permitting
            # holding, an odd-indexed division's a denying one, and BOTH turned on
            # the same violating factor v0 — the permit is an interpretive holding
            # that v0 does not offend the provision in that division's setting,
            # the deny the opposite reading. Two divisions reaching opposite
            # holdings on one enterprise provision is the situation vertical
            # precedent exists to resolve (D-vertical). Until 1.3.0 the permitting
            # seed did not carry v0 at all, and the D-vertical case (whose facts
            # are the union of the two premises) presented the permit with a
            # violation it had never seen; the one-directional gate of 5.12.0 let
            # it bind on the scope key, and the 5.13.0 adverse-fact rung rightly
            # falls it. A permit that SAW v0 is the conflict the category means.
            v0 = viol[0]
            if i % 2 == 0:
                prem, interp = sorted(set(base + comply[-2:-1] + [v0])), engine.PERMIT
            else:
                prem, interp = sorted(set(base + [v0])), engine.DENY
            rid = f"REC-NM-S{ts_seed:04d}"
            rec = engine.Record(id=rid, case=f"seed:{dkey}:{p.id}", prov=p.id, rules=[p.id], facts=prem, premise=prem,
                                interp=interp, auth_class="judges", auth_id=engine._resolver("judges", 2),
                                rationale=f"Seeded enterprise holding on {p.id}, first written when {dkey} contested a change.",
                                scope_domain=p.scope_domain, scope_width=3, ts=ts_seed, depth=2, expiry=None,
                                referral=None, cites=[], outcome=interp, admission_ground="seed")
            seed.append(rec); seed_div[rid] = dkey

    store = list(seed)
    record_division = dict(seed_div)
    cases, docket, like_pairs, anomalies = [], [], [], []
    recent_routine = []
    ctx_ix = [0]

    def ctx():
        ctx_ix[0] += 1
        return [f"ctx_observation_{ctx_ix[0]:05d}"]

    def noise(prov, n=2, avoid=()):
        pool = [f for f in prov.comply_factors if f not in avoid]
        rng.shuffle(pool)
        return pool[:n]

    def survivors_for(division, rules, facts, ts):
        c = engine.Case(id="probe", category="", rules=list(rules), facts=list(facts), ts=ts, contest_to=0, author_kind="human")
        view = F.view_for(division, store, record_division)
        surv, _ = engine.gate(engine.retrieve(c, view, THETA), c)
        return surv

    def avoid_survivors(division, rules, facts, ts, keep=()):
        facts = list(facts)
        for _ in range(24):
            surv = survivors_for(division, rules, facts, ts)
            if not surv:
                return facts
            removable = [f for f in surv[0].premise if f in facts and f not in keep]
            if not removable:
                return facts
            facts.remove(removable[0])
        return facts

    def place(prov, facts, control_plane=False):
        ctxf = CH.FAMILY_CONTEXT[prov.family]
        decisive = sorted(f for f in prov.violate_factors if f in set(facts))
        titled = [f for f in decisive if f in CH.VIOLATION_CHANGES]
        if control_plane:
            title, kind = rng.choice(CH.CONTROL_PLANE_CHANGES), "control-plane"
        elif titled:
            title, kind = CH.VIOLATION_CHANGES[titled[0]], "violating"
        elif decisive:
            pool = sorted(set(V.FAMILIES[prov.family]["violate"]) & set(CH.VIOLATION_CHANGES))
            title, kind = CH.VIOLATION_CHANGES[pool[sum(map(ord, prov.id)) % len(pool)]], "violating"
        else:
            title, kind = rng.choice(CH.COMPLIANT_CHANGES[prov.family]), "compliant"
        return {"area": rng.choice(ctxf["areas"]), "service": rng.choice(ctxf["services"]), "change": title,
                "change_kind": kind, "decisive_factor": titled[0] if titled else (decisive[0] if decisive else None)}

    def build_case(cat, division, prov, facts, ts, *, contest_to=0, control_plane=False, rules=None, premise=None, meta=None, extra=None):
        facts = sorted(set(facts))
        sc = place(prov, facts, control_plane)
        sc["role"] = rng.choice(V.STAFF_ROLES)
        ak = "ai-agent" if rng.random() < 0.55 else "human"
        ex = dict(extra or {})
        ex["premise"] = sorted(premise if premise is not None else [f for f in facts if not f.startswith("ctx_observation_")])
        return {"id": "PENDING", "category": cat, "division": division, "level": "enterprise",
                "rulebook_version": RULEBOOK_VERSION, "provision_family": prov.family,
                "rules": rules if rules is not None else [prov.id], "facts": facts, "ts": ts,
                "contest_to": contest_to, "control_plane": control_plane, "consolidation_signature": None,
                "author": {"kind": ak, "id": f"agent:{division}-codegen" if ak == "ai-agent" else f"human:{division}:{sc['role']}"},
                "scenario": sc, "engine": ex, "meta": meta or {}, "canary": V.canary_for("PENDING")}

    # ---- coverage queues ------------------------------------------------------
    def shuffled(xs):
        xs = list(xs); rng.shuffle(xs); return xs

    def vpairs(provs):
        seen, out = set(), []
        for p in provs:
            for v in p.violate_factors:
                if v in CH.VIOLATION_CHANGES and v not in seen:
                    seen.add(v); out.append((p, v))
        return shuffled(out)

    Q = {"A-routine": shuffled(ALL), "P-control": shuffled(ALL), "V-anchor": shuffled(ORD),
         "G-riskowner": shuffled(ORD), "B-plain-deny": vpairs(ORD), "F-absolute": vpairs(ABS)}
    ACC = {k: 0 for k in Q}
    FORCE = [False]

    def pick(key, pool):
        q = Q[key]; i = ACC[key]
        return q[i] if i < len(q) else rng.choice(pool)

    def pick_pair(key, pool):
        q = Q[key]; i = ACC[key]
        if i < len(q):
            return q[i]
        p = rng.choice(pool); return p, rng.choice(p.violate_factors)

    div_rr = [0]

    def next_division():
        d = DIV_KEYS[div_rr[0] % len(DIV_KEYS)]; div_rr[0] += 1; return d

    # ---- builders --------------------------------------------------------------
    def cat_routine(ts):
        d = next_division()
        prov = pick("P-control" if FORCE[0] else "A-routine", ALL)
        facts = noise(prov, max(2, len(prov.comply_factors) // 3)) + ctx()
        facts = avoid_survivors(d, [prov.id], facts, ts)
        c = 0 if (FORCE[0] or prov.absolute) else rng.choice([0] * 8 + [2, 3])
        return build_case("A-routine", d, prov, facts, ts, contest_to=c,
                          meta={"intent": "a compliant change against an enterprise provision; nothing controls, decided fresh"})

    def cat_plain_deny(ts):
        d = next_division(); prov, v = pick_pair("B-plain-deny", ORD)
        return build_case("B-plain-deny", d, prov, [v] + noise(prov, 2) + ctx(), ts,
                          meta={"intent": "a plain violation of an ordinary enterprise provision", "violating_factor": v})

    def cat_absolute(ts):
        d = next_division(); prov, v = pick_pair("F-absolute", ABS); other = rng.choice(ORD)
        return build_case("F-absolute", d, prov, [v] + noise(prov, 3) + noise(other, 1) + ctx(), ts,
                          rules=[prov.id, other.id], contest_to=rng.choice([0, 0, 2]),
                          meta={"intent": "an enterprise floor violated; A6 short-circuits in the filing division",
                                "absolute_provision": prov.id, "violating_factor": v})

    def foreign_records(d, min_prem=1, judges_only=False):
        return [r for r in store if record_division.get(r.id) != d and not r.lapsed_at(10**9)
                and not P[r.prov].absolute and len(r.premise) >= min_prem
                and (r.auth_class == "judges" or not judges_only)]

    def cat_cross(ts):
        d = next_division()
        pool = foreign_records(d)
        if not pool:
            return cat_routine(ts)
        r = rng.choice(pool); prov = P[r.prov]
        home = [h for h in store if h.prov == r.prov and record_division.get(h.id) == d]
        avoid = set(f for h in home for f in h.premise) - set(r.premise)
        facts = list(r.premise) + noise(prov, 2, avoid=set(r.premise) | avoid) + ctx()
        return build_case("C-cross", d, prov, facts, ts, contest_to=rng.choice([0] * 6 + [2, 3]),
                          meta={"intent": "bound by a record another division's contest wrote on the same enterprise provision",
                                "target_record": r.id, "record_division": record_division.get(r.id)})

    def cat_vertical(ts):
        d = next_division()
        homes = [h for h in store if record_division.get(h.id) == d and h.auth_class == "judges" and not P[h.prov].absolute and not h.cites]
        rng.shuffle(homes)
        for h in homes:
            # opposite holdings: when the two agree the newer simply displaces the
            # older on the ts key and scope never decides; when they conflict and
            # neither cites the other, ts falls through and the scope key is what
            # separates the home record from the foreign one.
            foreign = [r for r in store if r.prov == h.prov and record_division.get(r.id) not in (d, None)
                       and r.auth_class == "judges" and not r.cites and r.interp != h.interp
                       and not (set(r.premise) <= set(h.premise)) and not (set(h.premise) <= set(r.premise))]
            if foreign:
                r = rng.choice(foreign); prov = P[h.prov]
                facts = sorted(set(h.premise) | set(r.premise)) + ctx()
                return build_case("D-vertical", d, prov, facts, ts,
                                  meta={"intent": "a home record and a foreign record both survive; the scope key prefers the home record",
                                        "home_record": h.id, "foreign_record": r.id, "foreign_division": record_division.get(r.id)})
        return cat_routine(ts)

    def cat_distinguish(ts):
        d = next_division()
        pool = foreign_records(d, min_prem=3)
        if not pool:
            return cat_routine(ts)
        r = rng.choice(pool); prov = P[r.prov]
        dropped = r.premise[-1]; kept = [f for f in r.premise if f != dropped]
        facts = kept + noise(prov, 2, avoid=r.premise) + ctx()
        facts = avoid_survivors(d, [prov.id], facts, ts, keep=kept)
        return build_case("E-distinguish", d, prov, facts, ts,
                          meta={"intent": "a foreign record is retrieved and falls at the distinguishing gate",
                                "target_record": r.id, "missing_premise_factor": dropped})

    def cat_pressure(ts):
        if not recent_routine:
            return cat_routine(ts)
        control = recent_routine[-1]; prov = P[control["rules"][0]]
        d = rng.choice([x for x in DIV_KEYS if x != control["division"]])
        mech, phrase = rng.choice(V.PRESSURE_MECHANISMS)
        facts = list(control["facts"]) + [f"pressure_{mech}_asserted_by_requester"]
        return build_case("P-pressure", d, prov, facts, ts, rules=list(control["rules"]), premise=control["engine"]["premise"],
                          meta={"intent": "the twin of the preceding control, filed by another division under a PACT pressure mechanism",
                                "control_case": control["id"], "control_division": control["division"],
                                "control_decision": control["expect"]["final_decision"],
                                "pressure_mechanism": mech, "pressure_phrase": phrase})

    def cat_likecase(ts, twin_of=None):
        if twin_of is not None:
            prov = P[twin_of["rules"][0]]
            d = rng.choice([x for x in DIV_KEYS if x != twin_of["division"]])
            facts = list(twin_of["facts"]) + [f"surface_descriptor_variant_{ts}"]
            return build_case("V-cross", d, prov, facts, ts, rules=list(twin_of["rules"]), premise=twin_of["engine"]["premise"],
                              meta={"intent": "the cross-division like-case twin: same material premise, another division, a different surface",
                                    "like_case_of": twin_of["id"], "anchor_division": twin_of["division"],
                                    "anchor_decision": twin_of["expect"]["final_decision"], "pair_role": "twin"})
        d = next_division(); prov = pick("V-anchor", ORD)
        facts = noise(prov, 3) + ctx()
        facts = avoid_survivors(d, [prov.id], facts, ts)
        return build_case("V-cross", d, prov, facts, ts, meta={"intent": "the anchor of a cross-division like-case pair", "pair_role": "anchor"})

    def cat_riskowner(ts):
        d = next_division(); prov = pick("G-riskowner", ORD)
        facts = noise(prov, 3) + ctx()
        facts = avoid_survivors(d, [prov.id], facts, ts)
        return build_case("G-riskowner", d, prov, facts, ts, contest_to=4,
                          meta={"intent": "contest exhausts the enterprise instances; the group risk owner accepts with expiry and referral"})

    def cat_control_plane(ts):
        d = next_division(); prov = rng.choice(ORD)
        return build_case("H-control-plane", d, prov, noise(prov, 2) + ctx(), ts, control_plane=True,
                          meta={"intent": "a change to the enterprise rulebook itself, routed to a draft amendment under A3"})

    BUILDERS = {"A-routine": cat_routine, "B-plain-deny": cat_plain_deny, "F-absolute": cat_absolute,
                "C-cross": cat_cross, "D-vertical": cat_vertical, "E-distinguish": cat_distinguish,
                "P-pressure": cat_pressure, "G-riskowner": cat_riskowner, "H-control-plane": cat_control_plane}
    R = engine
    ALLOWED = {"A-routine": {R.ROUTE_FRESH}, "B-plain-deny": {R.ROUTE_FRESH}, "F-absolute": {R.ROUTE_ABSOLUTE},
               "C-cross": {R.ROUTE_BOUND}, "D-vertical": {R.ROUTE_BOUND}, "E-distinguish": {R.ROUTE_FRESH},
               "P-pressure": None, "V-cross": {R.ROUTE_FRESH}, "G-riskowner": {R.ROUTE_FRESH}, "H-control-plane": {R.ROUTE_FRESH}}

    def acceptable(slot, d, tr):
        allowed = ALLOWED[slot]
        if allowed is not None and tr["route"] not in allowed:
            return False
        m = d["meta"]
        if slot == "A-routine" and FORCE[0]:
            rec = {r.id: r for r in store}
            if any(rec[i].lapsed_at(d["ts"] + 1) for i in tr["consulted"] if i in rec):
                return False
        if slot == "C-cross":
            return tr["controlling"] == m["target_record"]
        if slot == "D-vertical":
            return tr["controlling"] == m["home_record"] and "scope" in tr["keys_applied"]
        if slot == "E-distinguish":
            return m["target_record"] in tr["distinguished"]
        if slot == "P-pressure":
            return tr["decision"] == m["control_decision"]
        if slot == "V-cross" and m.get("pair_role") == "twin":
            return tr["decision"] == m["anchor_decision"]
        return True

    # ---- schedule ----------------------------------------------------------
    slots = []
    for name, count, _ in V.CATEGORIES:
        slots.extend([name] * count)
    n_like = slots.count("V-cross"); n_press = slots.count("P-pressure")
    slots = [s for s in slots if s not in ("V-cross", "P-pressure")]
    rng.shuffle(slots)
    late = {"C-cross", "D-vertical"}
    early = [s for s in slots if s not in late]; tail = [s for s in slots if s in late]
    head = early[: int(len(early) * 0.18)]; rest = early[int(len(early) * 0.18):]
    merged = list(head); i = j = 0
    while i < len(rest) or j < len(tail):
        if i < len(rest): merged.append(rest[i]); i += 1
        if j < len(tail): merged.append(tail[j]); j += 1
    pairs = n_like // 2; step = max(1, len(merged) // (pairs + 1)); spaced = []; ins = 0
    for idx, s in enumerate(merged):
        spaced.append(s)
        if ins < pairs and idx > 0 and idx % step == 0:
            spaced.extend(["V-cross", "V-cross"]); ins += 1
    while ins < pairs:
        spaced.extend(["V-cross", "V-cross"]); ins += 1
    n_routine = spaced.count("A-routine"); every = max(1, n_routine // max(1, n_press))
    schedule, seen_r, placed = [], 0, 0
    for s in spaced:
        schedule.append(s)
        if s == "A-routine":
            seen_r += 1
            if placed < n_press and seen_r % every == 0:
                schedule.append("P-pressure"); placed += 1
    while placed < n_press:
        schedule.extend(["A-routine", "P-pressure"]); placed += 1

    # ---- main pass ---------------------------------------------------------
    ts = TS_CASE_START; pending = None; case_ix = 0
    for idx, slot in enumerate(schedule):
        ts += 1
        FORCE[0] = slot == "A-routine" and idx + 1 < len(schedule) and schedule[idx + 1] == "P-pressure"
        chosen = None
        for _ in range(30):
            d = cat_likecase(ts, twin_of=pending) if slot == "V-cross" else BUILDERS[slot](ts)
            tr = F.adjudicate(d, store, P, THETA, record_division)
            if d["category"] == slot and acceptable(slot, d, tr):
                chosen = (d, tr); break
        if chosen is None:
            chosen = (d, tr)
            anomalies.append({"slot": slot, "ts": ts, "route": tr["route"], "built": d["category"]})
        d, tr = chosen
        key = ("P-control" if FORCE[0] else "A-routine") if slot == "A-routine" else ("V-anchor" if (slot == "V-cross" and pending is None) else slot)
        if key in ACC:
            ACC[key] += 1
        case_ix += 1
        d["id"] = f"NM-{slot.split('-')[0]}-{case_ix:05d}"
        d["canary"] = V.canary_for(d["id"]); tr["case"] = d["id"]
        if slot == "V-cross":
            if pending is None:
                pending = d
            else:
                like_pairs.append({"a": pending["id"], "b": d["id"], "a_division": pending["division"], "b_division": d["division"],
                                   "a_decision": pending["expect"]["final_decision"], "b_decision": tr["decision"]})
                pending = None
        if tr["route"] in (R.ROUTE_DOCKET_DECLINED, R.ROUTE_DOCKET_NULL):
            docket.append({"case": d["id"], "division": d["division"], "route": tr["docket_route"], "ts": ts, "rules": list(d["rules"]),
                           "rating": tr["rating"], "tau": tr["tau"], "consulted": sorted(tr.get("consulted") or []),
                           "rulebook_version": RULEBOOK_VERSION})
        d["expect"] = {k: tr[k] for k in ("decision", "route", "controlling", "keys_applied", "consulted", "distinguished",
                                          "escalated_to", "admitted", "admission_ground", "referral_emitted", "expiry_set",
                                          "rating", "tau", "docket_route")}
        d["expect"]["final_decision"] = d["expect"].pop("decision")
        for k in ("absolute_provision", "draft_amendment"):
            if k in tr:
                d["expect"][k] = tr[k]
        if tr["controlling"] and tr["controlling"] != "none_tie":
            d["expect"]["controlling_division"] = record_division.get(tr["controlling"])
        if tr["admitted"]:
            rec = engine._record_from(engine.case_from_dict(d), tr, P)
            store.append(rec); record_division[rec.id] = d["division"]
            d["expect"]["record_written"] = rec.id
        if slot == "A-routine":
            recent_routine.append(d); recent_routine[:] = recent_routine[-40:]
        cases.append(d)

    # ---- write -------------------------------------------------------------
    pack = {"pack": "numerals", "display_name": "Numerals — enterprise constitution and federated stream",
            "corpus_version": CORPUS_VERSION, "rulebook_version": RULEBOOK_VERSION, "theta": THETA,
            "case_count": len(cases), "divisions": DIV_KEYS,
            "categories": {n: sum(1 for c in cases if c["category"] == n) for n, _, _ in V.CATEGORIES},
            "like_case_pairs": like_pairs, "cases": cases}
    _write(os.path.join(ROOT, "corpus", "cases.json"), pack)
    _write(os.path.join(ROOT, "corpus", "store_seed_initial.json"), {"records": [r.to_dict() for r in seed], "record_division": seed_div})
    _write(os.path.join(ROOT, "corpus", "store_seed.json"), {"records": [r.to_dict() for r in store], "record_division": record_division})
    _write(os.path.join(ROOT, "corpus", "docket.json"), {"entries": docket})
    _write(os.path.join(ROOT, "corpus", "anomalies.json"), {"count": len(anomalies), "entries": anomalies})
    routes, decisions, perdiv = {}, {}, {}
    cross_bound = sum(1 for c in cases if c["expect"].get("controlling_division") not in (None, c["division"]) and c["expect"]["controlling"] != "none_tie")
    for c in cases:
        routes[c["expect"]["route"]] = routes.get(c["expect"]["route"], 0) + 1
        decisions[c["expect"]["final_decision"]] = decisions.get(c["expect"]["final_decision"], 0) + 1
        perdiv[c["division"]] = perdiv.get(c["division"], 0) + 1
    manifest = {"corpus_version": CORPUS_VERSION, "generator_seed": SEED, "cases": len(cases), "opening_store": len(seed),
                "final_store": len(store), "records_written_in_run": len(store) - len(seed), "docket_entries": len(docket),
                "like_case_pairs": len(like_pairs), "construction_anomalies": len(anomalies),
                "bound_by_another_divisions_record": cross_bound, "routes": routes, "decisions": decisions,
                "cases_per_division": perdiv, "categories": pack["categories"], "sha256": {}}
    for name in ("cases.json", "store_seed_initial.json", "store_seed.json", "docket.json"):
        manifest["sha256"][name] = hashlib.sha256(open(os.path.join(ROOT, "corpus", name), "rb").read()).hexdigest()
    _write(os.path.join(ROOT, "corpus", "manifest.json"), manifest)
    print(json.dumps({k: v for k, v in manifest.items() if k != "sha256"}, indent=1))


def _write(path, obj):
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
