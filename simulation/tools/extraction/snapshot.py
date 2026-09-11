"""One document in, one three-valued case out — and what that does to the trace.

`extract_case` is the seam: backend proposes, calibration decides, the
contract refuses a silent factor that keeps its value. `replay_with_snapshot`
then runs the pack's engine over the extracted facts and compares every trace
against the reference, which is how the Evaluator's epsilon stops being an
identity and becomes a measured quantity per pack:

    binds_kept            bound in both, same controlling record
    binds_broken_by_silence   reference bound; extracted abstained with premise_not_established
    binds_broken_otherwise    reference bound; extracted abstained for another cause
    false_binds           extracted bound where the reference did not, or on another record
    decisions_changed     final disposition differs
    floors_missed         an absolute short-circuit the extracted facts did not trigger
                          (a floor violation that went through unnoticed — the dangerous error)
    floors_referred_on_silence   the extracted facts were unrecorded on a floor's factor and the
                          engine refused and referred (A6 under silence, 5.11.0) instead of proceeding
    floors_invented       an absolute short-circuit the reference did not take

The pack's engine is imported from the pack directory: nothing here is
imported by the packs, and torch never enters the process unless a model
backend is asked for.
"""
from __future__ import annotations

import collections
import hashlib
import importlib.util
import json
import os
import sys

from .abstain import Calibration, span_confidence
from .contract import ABSENT, ABSTAINED, CARRIED, OBSERVED, ExtractedCase, FieldValue, Span


def load_pack(pack_dir: str):
    """(engine module, rulebook, params, cases, seed) for a pack; roster loaded."""
    pack_dir = os.path.abspath(pack_dir)
    spec = importlib.util.spec_from_file_location("dj_pack_engine", os.path.join(pack_dir, "harness", "engine.py"))
    engine = importlib.util.module_from_spec(spec)
    sys.modules["dj_pack_engine"] = engine
    spec.loader.exec_module(engine)
    rb = json.load(open(os.path.join(pack_dir, "constitution", "rulebook.json")))
    params = json.load(open(os.path.join(pack_dir, "constitution", "parameters.json")))
    cases = json.load(open(os.path.join(pack_dir, "corpus", "cases.json")))["cases"]
    seed = json.load(open(os.path.join(pack_dir, "corpus", "store_seed_initial.json")))["records"]
    engine.load_roster(os.path.join(pack_dir, "constitution", "organizations.json"))
    dims = os.path.join(pack_dir, "constitution", "dimensions.json")
    provisions = {p["id"]: engine.Provision.from_dict(p) for p in rb["provisions"]}
    if os.path.exists(dims):
        engine.load_dimensions(dims, provisions)
    return engine, rb, params, cases, seed, provisions


def vocabulary_for(case: dict, rulebook_by_id: dict) -> list:
    """The factors an extractor is asked about: those of the engaged provisions."""
    out = set()
    for pid in case.get("rules", []):
        p = rulebook_by_id.get(pid)
        if p:
            out.update(p["factors"]["comply"])
            out.update(p["factors"]["violate"])
    return sorted(out)


def extract_case(document: str, case: dict, vocabulary: list, backend, cal: Calibration,
                 provenance_extra: dict | None = None) -> ExtractedCase:
    proposed = {r.factor: r for r in backend.score(document, vocabulary)}
    fields = []
    vocab = set(vocabulary)
    for name in vocabulary:
        floor = cal.floor_for(name)
        r = proposed.get(name)
        if r is None:
            fields.append(FieldValue(name, ABSENT, floor=floor))
            continue
        conf = span_confidence(r.token_probs, cal.aggregation)
        status = OBSERVED if conf >= floor else ABSTAINED
        fields.append(FieldValue(name, status, confidence=conf, floor=floor, span=Span(r.start, r.end, r.text)))
    # Facts outside the vocabulary are not the extractor's business.
    for f in case["facts"]:
        if f not in vocab:
            fields.append(FieldValue(f, CARRIED))
    prov = {"backend": backend.identity(), "calibration": cal.as_dict(),
            "document_sha256": hashlib.sha256(document.encode()).hexdigest(), "extracted": True}
    prov.update(provenance_extra or {})
    return ExtractedCase(case["id"], tuple(fields), prov)


def apply_snapshot(cases: list, extracted: dict) -> list:
    """Cases with facts/unrecorded replaced by the snapshot's; others untouched."""
    out = []
    for c in cases:
        e = extracted.get(c["id"])
        if e is None:
            out.append(c)
            continue
        d = dict(c)
        d.update(e.to_case_patch())
        out.append(d)
    return out


def replay_with_snapshot(engine, cases: list, extracted: dict, seed: list, provisions: dict, theta: float) -> dict:
    ref = engine.replay(cases, seed, provisions, theta)
    got = engine.replay(apply_snapshot(cases, extracted), seed, provisions, theta)
    k = collections.Counter()
    examples = collections.defaultdict(list)
    for a, b in zip(ref["traces"], got["traces"]):
        cid = a["case"]
        ra, rb = a["route"], b["route"]
        unresolved = getattr(engine, "ROUTE_FLOOR_UNRESOLVED", "floor_unresolved")
        if rb == unresolved:
            k["floors_referred_on_silence"] += 1
            if ra != engine.ROUTE_ABSOLUTE:
                k["floors_referred_where_reference_proceeded"] += 1
                examples["floors_referred_where_reference_proceeded"].append(cid)
        elif ra == engine.ROUTE_ABSOLUTE and rb != engine.ROUTE_ABSOLUTE:
            k["floors_missed"] += 1
            examples["floors_missed"].append(cid)
        elif rb == engine.ROUTE_ABSOLUTE and ra != engine.ROUTE_ABSOLUTE:
            k["floors_invented"] += 1
            examples["floors_invented"].append(cid)
        a_bound = a["gate_outcome"] == engine.GOVERNED
        b_bound = b["gate_outcome"] == engine.GOVERNED
        if a_bound and b_bound and a["controlling"] == b["controlling"]:
            k["binds_kept"] += 1
        elif a_bound and b_bound:
            k["false_binds"] += 1
            examples["false_binds"].append(cid)
        elif a_bound and not b_bound:
            key = "binds_broken_by_silence" if b["gate_outcome"] == engine.PREMISE_NOT_ESTABLISHED else "binds_broken_otherwise"
            k[key] += 1
            examples[key].append(cid)
        elif b_bound and not a_bound:
            k["false_binds"] += 1
            examples["false_binds"].append(cid)
        if a["decision"] != b["decision"]:
            k["decisions_changed"] += 1
            examples["decisions_changed"].append(cid)
        if b["gate_outcome"] == engine.PREMISE_NOT_ESTABLISHED:
            k["premise_not_established"] += 1
        if b.get("record_withheld"):
            k["records_withheld"] += 1          # 5.14.0: no law on facts nobody established
        if b_bound and not a_bound:
            k["false_binds:where_reference_abstained"] += 1
    n_ref_binds = sum(1 for a in ref["traces"] if a["gate_outcome"] == engine.GOVERNED)
    return {"cases": len(cases), "reference_binds": n_ref_binds, "counts": dict(k),
            "bind_retention": round(k["binds_kept"] / n_ref_binds, 6) if n_ref_binds else None,
            "decision_agreement": round(1 - k["decisions_changed"] / len(cases), 6) if cases else None,
            "examples": {kk: v[:5] for kk, v in examples.items()},
            "records_written_reference": len(ref["records_written"]),
            "records_written_extracted": len(got["records_written"])}


def write_snapshot(path: str, extracted: dict, meta: dict) -> None:
    out = {"meta": meta, "cases": {cid: e.to_case_patch() for cid, e in sorted(extracted.items())},
           "audit": [e.audit() for _, e in sorted(extracted.items())]}
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
