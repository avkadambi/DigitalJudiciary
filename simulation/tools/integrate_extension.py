#!/usr/bin/env python3
"""Integrate a pack's scenario extension into its generator, harness and benchmark.

    python3 tools/integrate_extension.py <pack-dir>

Idempotent: every patch is guarded by a marker and asserted to apply exactly
once. What it does, per pack:

  constitution/scenarios.json      copied from simulation/scenarios.json
  harness/coverage.py              scenario coverage (VC-50) — from tools/templates
  benchmark/human.py               arm C, the priced human desk — from tools/templates
  generator/vocab.py               CATEGORIES rescaled to 6,000 (identical in all packs);
                                   merge shim appending ext_vocab (families, provisions,
                                   tau, amendments, scenario/harm metadata)
  generator/changes.py             merge shim appending ext_changes
  generator/build_constitution.py  status/origin/scenarios/harm_classes on every provision,
                                   TAU for new families, readiness status, amendments written
                                   from vocab, corpus version 2.0.0, scenario catalogue block
  generator/build_corpus.py        coverage queues (every provision gets a compliant touch, a
                                   plain violation, a pressure twin, a like-case anchor, and
                                   every absolute a floor case and a compliant touch), risk-
                                   owner pool extended to the new ordinary families, pack
                                   name fixed
  generator/build_explorer.py, build_simulation.py   gzip mtime=0 so the HTML is byte-stable
  generator/build_docs.py          readiness status in the status table; scenario matrix
  harness/run_conformance.py       VC-50
  harness/mutation_matrix.py       M25 (breaks coverage.py; VC-50's self-test kills it)
  benchmark/config.py, run.py      default stream 6,000; --human flag
  reproduce/run_all.sh             banner
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
TPL = os.path.join(HERE, "templates")

CATEGORIES_6000 = {
    "A-routine": 696, "B-plain-deny": 372, "C-precedent": 576, "D-ordering": 204,
    "E-distinguish": 300, "F-absolute": 348, "G-riskowner": 300, "H-control-plane": 150,
    "I-lapsed": 102, "J-novel": 102, "K-tie": 48, "P-pressure": 222, "L-consolidated": 198,
    "M-supersession": 180, "N-standing": 144, "Q-docket": 312, "R-reporter": 108,
    "S-acknowledgement": 132, "T-audit-register": 96, "U-renewal": 156, "V-likecase": 480,
    "W-crossjurisdiction": 240, "X-coldstart": 144, "Y-adversarial": 210, "Z-inexpressibility": 180,
}
assert sum(CATEGORIES_6000.values()) == 6000

MARK = "# --- scenario extension (corpus 2.0.0) ---"


def read(p):
    return open(p).read()


def write(p, s):
    open(p, "w").write(s)


def patch(path, old, new, count=1, flags=0, regex=False):
    s = read(path)
    if regex:
        s2, n = re.subn(old, new, s, flags=flags)
    else:
        n = s.count(old)
        s2 = s.replace(old, new)
    if n != count:
        raise SystemExit(f"{os.path.basename(path)}: expected {count} match(es) for {old[:60]!r}, found {n}")
    write(path, s2)


def already(path):
    return MARK in read(path)


# --------------------------------------------------------------------------

VOCAB_SHIM = '''

''' + MARK + '''
# Merge of generator/ext_vocab.py: the scenario extension. Additive only —
# nothing above this line is edited by it. See tools/EXTENSION_AUTHORING_SPEC.md.
import json as _json
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ext_vocab as _ext  # noqa: E402

_BASE_LEN = len(PROVISIONS[0])
_BASE_IDS = {p[0] for p in PROVISIONS}
FAMILIES.update(_ext.FAMILIES)
TAU_EXT = dict(_ext.TAU)
EXT_FAMILIES = set(_ext.FAMILIES)
EXT_IDS = {p["id"] for p in _ext.PROVISIONS}
for _p in _ext.PROVISIONS:
    _row = (_p["id"], _p["family"], _p["title"], _p["absolute"], _p["citation"],
            _p["source_status"], _p["status"], _p["origin"])
    PROVISIONS.append(_row[:_BASE_LEN])

with open(_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                        "constitution", "scenarios.json")) as _fh:
    SCENARIO_CATALOGUE = _json.load(_fh)
_SCEN_HARM = {s["id"]: s["harm_classes"] for s in SCENARIO_CATALOGUE["scenarios"]}


def _harm_for(scenarios):
    out = []
    for s in scenarios:
        for h in _SCEN_HARM.get(s, []):
            if h not in out:
                out.append(h)
    return out


PROVISION_META = {}
for _row in PROVISIONS:
    _pid, _fam = _row[0], _row[1]
    if _pid in EXT_IDS:
        _e = next(p for p in _ext.PROVISIONS if p["id"] == _pid)
        PROVISION_META[_pid] = {"status": _e["status"], "origin": _e["origin"],
                                "scenarios": list(_e["scenarios"]),
                                "harm_classes": list(_e["harm_classes"])}
    else:
        _status = _row[6] if _BASE_LEN >= 7 else "in_force"
        _origin = _row[7] if _BASE_LEN >= 8 else "base"
        _sc = list(getattr(_ext, "PROVISION_SCENARIOS", {}).get(_pid)
                   or _ext.FAMILY_SCENARIOS.get(_fam, []))
        PROVISION_META[_pid] = {"status": _status, "origin": _origin,
                                "scenarios": _sc, "harm_classes": _harm_for(_sc)}

ABSOLUTE_IDS = {p[0] for p in PROVISIONS if p[3]}
try:
    PROPOSED_AMENDMENTS = list(PROPOSED_AMENDMENTS) + list(_ext.PROPOSED_AMENDMENTS)
except NameError:
    PROPOSED_AMENDMENTS = list(_ext.PROPOSED_AMENDMENTS)
try:
    FLOOR_FACING_FAMILIES = set(FLOOR_FACING_FAMILIES) | set(getattr(_ext, "FLOOR_FACING_FAMILIES", set()))
except NameError:
    pass
SCENARIO_CATALOGUE_META = {
    "version": SCENARIO_CATALOGUE["version"],
    "harm_classes": SCENARIO_CATALOGUE["harm_classes"],
    "scenario_count": len(SCENARIO_CATALOGUE["scenarios"]),
    "note": ("Every provision carries `scenarios` (ids from constitution/scenarios.json) and "
             "`harm_classes` (computed from the catalogue, never authored per provision). "
             "harness/coverage.py and VC-50 compute coverage from the executed corpus."),
}
'''

CHANGES_SHIM = '''

''' + MARK + '''
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ext_changes as _ext  # noqa: E402
FAMILY_CONTEXT.update(_ext.FAMILY_CONTEXT)
COMPLIANT_CHANGES.update(_ext.COMPLIANT_CHANGES)
VIOLATION_CHANGES.update(_ext.VIOLATION_CHANGES)
'''

CORPUS_QUEUES = '''
''' + MARK + '''
# Coverage by construction. The architect's catalogue (constitution/scenarios.json)
# names, per scenario class, the mechanisms in which it must be exercised. A
# random draw from GENERAL does not guarantee that every provision — and so
# every scenario — receives a compliant touch, a plain violation, a pressure
# twin, a like-case anchor and a risk-owner acceptance, nor that every absolute
# receives a floor case AND a compliant touch (A6's conjunction: touching a
# floor is not violating it). So the first draws of each of those categories
# walk a shuffled queue over the provisions before the draw becomes random,
# and VC-50 verifies the property on the corpus as built rather than trusting
# this code.
EXT_G_POOL = [p for p in GENERAL if p.family in vocab.EXT_FAMILIES]


def _shuffled(xs):
    xs = list(xs)
    rng.shuffle(xs)
    return xs


def _violation_pairs(provs):
    """One (provision, violating factor) pair per provision first, so that every
    ordinary provision is plainly denied at least once whatever its factors
    share with its siblings (corpus 2.1.0: a provision whose violating factors
    were all claimed by earlier siblings could otherwise miss its scenario's B
    cell), then one pair per still-unseen violating factor."""
    seen, out = set(), []
    for p in provs:
        vs = [v for v in p.violate_factors if v in changes.VIOLATION_CHANGES] or list(p.violate_factors)
        if vs:
            seen.add(vs[0])
            out.append((p, vs[0]))
    for p in provs:
        for v in p.violate_factors:
            if v in changes.VIOLATION_CHANGES and v not in seen:
                seen.add(v)
                out.append((p, v))
    return _shuffled(out)


COVERAGE_QUEUE = {
    "A-routine": _shuffled(GENERAL) + _shuffled(ABSOLUTE),
    "P-control": _shuffled(GENERAL) + _shuffled(ABSOLUTE),
    "V-anchor": _shuffled(GENERAL),
    "G-riskowner": _shuffled(GENERAL),
    "B-plain-deny": _violation_pairs(GENERAL),
    "F-absolute": _violation_pairs(ABSOLUTE),
}
ACCEPTED = {k: 0 for k in COVERAGE_QUEUE}


def _pick(key, pool):
    q = COVERAGE_QUEUE[key]
    i = ACCEPTED[key]
    if i < len(q):
        return q[i]
    return rng.choice(pool)


def _pick_pair(key, pool):
    q = COVERAGE_QUEUE[key]
    i = ACCEPTED[key]
    if i < len(q):
        return q[i]
    prov = rng.choice(pool)
    return prov, rng.choice(prov.violate_factors)


def _queue_key(slot, anchor):
    if slot == "A-routine":
        return "P-control" if FORCE_UNCONTESTED_ROUTINE[0] else "A-routine"
    if slot == "V-likecase":
        return "V-anchor" if anchor else None
    return slot if slot in COVERAGE_QUEUE else None

'''

VC50 = '''
@check("VC-50", "Scenario coverage — every class in the architect's catalogue is exercised in every mechanism it requires")
def vc50(r):
    """The architect's catalogue (constitution/scenarios.json) lists the legal,
    compliance, reputational and safety scenario classes the simulation exists
    to exercise, and for each the mechanisms — compliant touch, plain violation,
    floor short-circuit, pressure twin, like-case pair, risk-owner acceptance,
    cross-jurisdiction, control plane — in which it must appear. Every
    provision carries its scenario ids. This check computes, from the corpus
    as built, the scenario x mechanism matrix and fails on any required cell
    that is empty. A floor mechanism is demanded only where the pack maps an
    absolute provision to the scenario; where the catalogue expects a floor and
    the constitution supplies none, that is reported as a constitution gap.

    The checker is held to its own specification (harness/coverage.py
    `spec_selftest`): a synthetic corpus missing a required mechanism must be
    reported, and a complete one must not. M25 breaks that and this check
    kills it. Without the self-test a checker that reports nothing would pass.
    """
    import coverage as COV
    catalogue = COV.load_catalogue(ROOT)
    gaps = COV.missing(r.rulebook, r.cases, catalogue)
    spec_ok, spec = COV.spec_selftest()
    counts, applicable = COV.matrix(r.rulebook, r.cases, catalogue)
    notes = COV.constitution_notes(r.rulebook, catalogue)
    cells = sum(1 for s in counts for m in counts[s] if counts[s][m] > 0)
    return (not gaps and spec_ok,
            f"{len(applicable)} scenario classes apply to this constitution; "
            f"{cells} scenario x mechanism cells populated; {len(gaps)} required "
            f"cells empty; checker self-test {'passes' if spec_ok else 'FAILS'} {spec}; "
            f"constitution notes for the lawmakers: {notes or 'none'}",
            [f"{s}:{m} {why}" for s, m, why in gaps][:6])

'''

RUN_HUMAN = '''
    if a.human:
        import human as humanmod
        est = humanmod.estimate(built["stream"], ref_traces, built["provisions"])
        all_results.append(est)
        print(humanmod.summarise(est))
'''


def integrate(pack):
    pack = os.path.abspath(pack)
    g = lambda *xs: os.path.join(pack, *xs)  # noqa: E731

    # ---- files copied in --------------------------------------------------
    shutil.copy(os.path.join(SIM, "scenarios.json"), g("constitution", "scenarios.json"))
    shutil.copy(os.path.join(TPL, "coverage.py"), g("harness", "coverage.py"))
    shutil.copy(os.path.join(TPL, "human.py"), g("benchmark", "human.py"))

    # ---- vocab.py ----------------------------------------------------------
    vp = g("generator", "vocab.py")
    if not already(vp):
        for name, n in CATEGORIES_6000.items():
            patch(vp, r'\("%s", \d+, ' % re.escape(name), '("%s", %d, ' % (name, n), regex=True)
        patch(vp, "assert sum(c[1] for c in CATEGORIES) == 5000", "assert sum(c[1] for c in CATEGORIES) == 6000")
        write(vp, read(vp).rstrip("\n") + VOCAB_SHIM)

    # ---- changes.py --------------------------------------------------------
    cp = g("generator", "changes.py")
    if not already(cp):
        write(cp, read(cp).rstrip("\n") + CHANGES_SHIM)

    # ---- build_constitution.py --------------------------------------------
    bc = g("generator", "build_constitution.py")
    if not already(bc):
        s = read(bc)
        # loop header, all three tuple shapes
        s, n = re.subn(
            r"for idx, \((pid, fam, title, absolute, citation, source(?:, status)?(?:, origin)?)\) in enumerate\(vocab\.PROVISIONS\):\n",
            "for idx, _row in enumerate(vocab.PROVISIONS):\n"
            "        pid, fam, title, absolute, citation, source = _row[:6]\n"
            "        _meta = vocab.PROVISION_META[pid]\n"
            "        status, origin = _meta[\"status\"], _meta[\"origin\"]\n", s)
        assert n == 1, "loop header"
        # status check present in every pack
        if "cannot be absolute" not in s:
            s = s.replace(
                "        f = vocab.FAMILIES[fam]\n",
                "        if status not in STATUSES:\n"
                "            raise SystemExit(f\"{pid}: unknown status {status!r}\")\n"
                "        if absolute and status != \"in_force\":\n"
                "            raise SystemExit(f\"{pid}: a {status} provision cannot be absolute\")\n"
                "        f = vocab.FAMILIES[fam]\n", 1)
        if "STATUSES = (" not in s:
            s = s.replace("def slice_pool(", "STATUSES = (\"in_force\", \"deferred\", \"advisory\", \"readiness\")\n\n\ndef slice_pool(", 1)
        else:
            s = re.sub(r"STATUSES = \([^)]*\)", "STATUSES = (\"in_force\", \"deferred\", \"advisory\", \"readiness\")", s, count=1)
        # provision dict: uniform status/origin/scenarios/harm_classes after risk_framework
        s = re.sub(r'\n\s*"status": status,\n', "\n", s)
        s = re.sub(r'\n\s*"origin": origin,\n', "\n", s)
        s, n = re.subn(r'("risk_framework": f\["risk"\],\n)',
                       r'\1                "status": status,\n'
                       r'                "origin": origin,\n'
                       r'                "scenarios": _meta["scenarios"],\n'
                       r'                "harm_classes": _meta["harm_classes"],\n', s)
        assert n == 1, "risk_framework"
        # counts block: uniform
        s = re.sub(r'\n\s*"(in_force|deferred|advisory|readiness|shipped|extension)": sum\(1 for p in provisions if p\["(status|origin)"\] == "[a-z_]+"\),', "", s)
        s, n = re.subn(r'("families": len\(vocab\.FAMILIES\),\n)',
                       r'\1            "in_force": sum(1 for p in provisions if p["status"] == "in_force"),\n'
                       r'            "deferred": sum(1 for p in provisions if p["status"] == "deferred"),\n'
                       r'            "advisory": sum(1 for p in provisions if p["status"] == "advisory"),\n'
                       r'            "readiness": sum(1 for p in provisions if p["status"] == "readiness"),\n'
                       r'            "shipped": sum(1 for p in provisions if p["origin"] == "shipped"),\n'
                       r'            "base": sum(1 for p in provisions if p["origin"] == "base"),\n'
                       r'            "extension": sum(1 for p in provisions if p["origin"] == "extension"),\n'
                       r'            "scenario_extension": sum(1 for p in provisions if p["id"] in vocab.EXT_IDS),\n'
                       r'            "scenario_extension_absolute": sum(1 for p in provisions if p["id"] in vocab.EXT_IDS and p["absolute"]),\n', s)
        assert n == 1, "counts"
        s, n = re.subn(r'CORPUS_VERSION = "[0-9.]+"', 'CORPUS_VERSION = "2.0.0"', s)
        assert n == 1
        s, n = re.subn(r"\ndef build\(\):\n", "\nTAU.update(vocab.TAU_EXT)\n\n\ndef build():\n", s)
        assert n == 1
        # amendments + catalogue block written from vocab, before the rulebook write
        amend = ('    _write(os.path.join(OUT, "proposed_amendments.json"),\n'
                 '           {"note": ("Findings against existing provisions, filed as draft "\n'
                 '                     "amendments rather than applied. Under Axiom A3 the only route "\n'
                 '                     "from a case — or from a corpus author — to a rule change is a "\n'
                 '                     "draft amendment the legislative process may adopt or reject."),\n'
                 '            "amendments": vocab.PROPOSED_AMENDMENTS})\n')
        if 'proposed_amendments.json' in s:
            s = re.sub(r'    _write\(os\.path\.join\(OUT, "proposed_amendments\.json"\),\n(?:.*\n)*?\s*"amendments": vocab\.PROPOSED_AMENDMENTS\}\)\n', "", s, count=1)
        s, n = re.subn(r'(    _write\(os\.path\.join\(OUT, "rulebook\.json"\), rulebook\)\n)',
                       amend + '    rulebook["scenario_catalogue"] = vocab.SCENARIO_CATALOGUE_META\n' + r"\1", s)
        assert n == 1, "rulebook write"
        s = s.rstrip("\n") + "\n" + MARK + "\n"
        write(bc, s)

    # ---- build_corpus.py ----------------------------------------------------
    bcp = g("generator", "build_corpus.py")
    if not already(bcp):
        s = read(bcp)
        s = s.replace("5,000 adjudication cases", "6,000 adjudication cases", 1)
        # queues before the first builder
        s, n = re.subn(r"\n(# Set when the next scheduled slot is a pressure twin\.)", "\n" + CORPUS_QUEUES + r"\n\1", s)
        assert n == 1, "queue insert"
        # routine
        s, n = re.subn(r"def cat_routine\(ts\):\n    prov = rng\.choice\(GENERAL\)\n",
                       "def cat_routine(ts):\n"
                       "    prov = _pick(\"P-control\" if FORCE_UNCONTESTED_ROUTINE[0] else \"A-routine\", GENERAL)\n", s)
        assert n == 1, "cat_routine"
        # a compliant touch on an absolute provision is never contested: no
        # precedent is written on a floor by this category
        s, n = re.subn(r"contest_to=\(0 if FORCE_UNCONTESTED_ROUTINE\[0\]\n",
                       "contest_to=(0 if (FORCE_UNCONTESTED_ROUTINE[0] or prov.absolute)\n", s)
        assert n == 1, "routine contest"
        # plain deny
        s, n = re.subn(r"def cat_plain_deny\(ts\):\n    prov = rng\.choice\(GENERAL\)\n    v = rng\.choice\(prov\.violate_factors\)\n",
                       "def cat_plain_deny(ts):\n    prov, v = _pick_pair(\"B-plain-deny\", GENERAL)\n", s)
        assert n == 1, "cat_plain_deny"
        # absolute
        s, n = re.subn(r"def cat_absolute\(ts\):\n    prov = rng\.choice\(ABSOLUTE\)\n    other = rng\.choice\(GENERAL\)\n    v = rng\.choice\(prov\.violate_factors\)\n",
                       "def cat_absolute(ts):\n    prov, v = _pick_pair(\"F-absolute\", ABSOLUTE)\n    other = rng.choice(GENERAL)\n", s)
        assert n == 1, "cat_absolute"
        # risk owner pool
        s, n = re.subn(r"(def cat_riskowner\(ts\):\n(?:    #.*\n)*)    prov = rng\.choice\((\[p for p in GENERAL if p\.family in \([^\]]*\])\)\n",
                       "\\1    prov = _pick(\"G-riskowner\", \\2 + EXT_G_POOL)\n", s)
        assert n == 1, "cat_riskowner"
        # like-case anchor
        s, n = re.subn(r"    prov = rng\.choice\(GENERAL\)\n(    facts = noise\(prov, 3\) \+ ctx\(1\)\n    facts, _ = avoid_survivors\(\[prov\.id\], facts, ts\)\n    return build_case\(\"V-likecase\")",
                       "    prov = _pick(\"V-anchor\", GENERAL)\n\\1", s)
        assert n == 1, "cat_likecase"
        # a pressure control must face the same store its twin will: reject a
        # control whose consulted set holds a record that lapses one tick later
        s, n = re.subn(r"\ndef acceptable\(slot, d, tr\):\n    allowed = ALLOWED_ROUTES\[slot\]\n",
                       "\ndef acceptable(slot, d, tr):\n    allowed = ALLOWED_ROUTES[slot]\n"
                       "    if slot == \"A-routine\" and FORCE_UNCONTESTED_ROUTINE[0]:\n"
                       "        _rec = {r.id: r for r in store}\n"
                       "        if any(_rec[i].lapsed_at(d[\"ts\"] + 1) for i in tr[\"consulted\"] if i in _rec):\n"
                       "            return False\n", s)
        assert n == 1, "acceptable"
        # accepted counter
        s, n = re.subn(r"\n        d, tr = chosen\n",
                       "\n        d, tr = chosen\n"
                       "        _qk = _queue_key(slot, pending_like is None)\n"
                       "        if _qk is not None:\n"
                       "            ACCEPTED[_qk] += 1\n", s)
        assert n == 1, "accepted"
        # G-riskowner queue only counts when the slot really was G (the key maps 1:1); fine.
        # pack name
        pname = {"vetpoc": "vetpoc", "semifab": "semifab", "frontierllm": "frontierllm",
                 "dcvigil": "dcvigil", "meridian": "meridian"}[next(k for k in ("vetpoc", "semifab", "frontierllm", "dcvigil", "meridian") if k in os.path.basename(pack))]
        s, n = re.subn(r'"pack": "[a-z]+",', f'"pack": "{pname}",', s)
        assert n == 1, "pack name"
        s = s.rstrip("\n") + "\n" + MARK + "\n"
        write(bcp, s)

    # ---- byte-stable html ---------------------------------------------------
    for f in ("build_explorer.py", "build_simulation.py"):
        p = g("generator", f)
        if "gzip.compress(raw, 9)" in read(p):
            patch(p, "gzip.compress(raw, 9)", "gzip.compress(raw, 9, mtime=0)")

    # ---- build_docs.py ------------------------------------------------------
    bd = g("generator", "build_docs.py")
    if not already(bd):
        s = read(bd)
        s = re.sub(r'for st in \("in_force", "deferred", "advisory"(?:, "readiness")?\):',
                   'for st in ("in_force", "deferred", "advisory", "readiness"):', s, count=1)
        s = s.rstrip("\n") + "\n" + MARK + "\n"
        write(bd, s)

    # ---- conformance --------------------------------------------------------
    rc = g("harness", "run_conformance.py")
    if "VC-50" not in read(rc):
        patch(rc, "\ndef s_leak(block, case):", VC50 + "\ndef s_leak(block, case):")

    mm = g("harness", "mutation_matrix.py")
    if "M25" not in read(mm):
        patch(mm, 'CHANGES = os.path.join(ROOT, "generator", "changes.py")\n',
              'CHANGES = os.path.join(ROOT, "generator", "changes.py")\n'
              'COVERAGE = os.path.join(HERE, "coverage.py")\n')
        patch(mm, '"justification": JUSTIFICATION, "changes": CHANGES}',
              '"justification": JUSTIFICATION, "changes": CHANGES,\n           "coverage": COVERAGE}')
        patch(mm, "for target in (ENGINE, EXTENSIONS, DISCRIMINATING, JUSTIFICATION, CHANGES):",
              "for target in (ENGINE, EXTENSIONS, DISCRIMINATING, JUSTIFICATION, CHANGES, COVERAGE):")
        # append M25 as the last mutant entry (before the closing bracket of MUTANTS)
        s = read(mm)
        m = re.search(r"\nMUTANTS = \[\n", s)
        end = s.index("\n]\n", m.end())
        m25 = ('    ("M25", "fault",\n'
               '     "            if counts[s][m] == 0:",\n'
               '     "            if False:",\n'
               '     "the scenario-coverage checker reports no empty cell; VC-50\'s self-test kills it",\n'
               '     "coverage"),\n')
        s = s[:end + 1] + m25 + s[end + 1:]
        write(mm, s)

    # ---- benchmark ----------------------------------------------------------
    cfg = g("benchmark", "config.py")
    if '"cases": 5000,' in read(cfg):
        patch(cfg, '"cases": 5000,', '"cases": 6000,')
    rp = g("benchmark", "run.py")
    if "--human" not in read(rp):
        patch(rp, '    ap.add_argument("--out", default=',
              '    ap.add_argument("--human", action="store_true",\n'
              '                    help="add arm C: a priced human review desk that reads every "\n'
              '                         "arrival against the rulebook with no case base. Estimation-"\n'
              '                         "only: no decisions, no model calls; every input is a stated "\n'
              '                         "⟦PROJECTED⟧ parameter in benchmark/human.py.")\n'
              '    ap.add_argument("--out", default=')
        patch(rp, "\n    os.makedirs(a.out, exist_ok=True)\n", RUN_HUMAN + "\n    os.makedirs(a.out, exist_ok=True)\n")
        patch(rp, 'total_cost = sum(r["usage"]["cost_usd"] for r in all_results)',
              'total_cost = sum(r["usage"]["cost_usd"] for r in all_results if "usage" in r)')
        s = read(rp).replace("The 5,000-case corpus is always", "The 6,000-case corpus is always")
        write(rp, s)
    sc = g("benchmark", "score.py")
    if "def summarise" in read(sc) and '"usage" in r' not in read(sc):
        s = read(sc)
        # summarise iterates results; skip the human row, which has no score
        s = re.sub(r"(def summarise\(results\):\n)", r'\1    results = [r for r in results if r.get("score") is not None or r.get("arm") != "C"]\n', s, count=1)
        write(sc, s)

    ra = g("reproduce", "run_all.sh")
    s = read(ra).replace("corpus (5,000 cases, one chronological pass)", "corpus (6,000 cases, one chronological pass)")
    write(ra, s)
    print(f"integrated: {os.path.basename(pack)}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        integrate(p)
