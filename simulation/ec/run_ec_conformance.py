"""
EC conformance suite: EC-01 .. EC-12 (DESIGN §7), computed from executed runs.

    python3 simulation/ec/run_ec_conformance.py [--pack vetpoc] [--days 60] [--seed 11]
        [--archetype pressure_sensitive] [--results DIR] [--out DIR] [--ec07-days 252]

Without `--results` the suite runs a fresh pilot through `run_year.main` (in
process, no shell): the four arms for the named archetype, a second arm-C run
with the same seed (EC-11), and, for EC-07, arm-A year runs of every policy
archetype scored (honest, misreporting and the pilot archetype), one seed at a
time until the +-0.03 tolerance is at least three standard errors wide. The
independent unit there is the case: every arm feeds a case to the same per-case
rng and a twin re-seeds its control's, so the examen draw of a case is one draw
however many arms execute it. With `--results DIR` the suite reads the run
directories under DIR (`<pack>/<arm>/seed-<n>/`, any depth), pools every run
of an archetype it finds there for EC-07, and runs only what DIR lacks (the
repeat run, extra EC-07 seeds) into a temp dir (or `--out`).

Nothing here is read from a label an agent or the driver carried: every check
recomputes its property from run.jsonl, registry.json, glosses_final.json,
bench_log.json, store_final.json, the pack's canon.json and rulebook.json, and
the pack's own engine. A check whose property never arises in the run (no T0
violation proposed, no hold filed, no gloss written) FAILS as vacuous rather
than passing on nothing.

Prints `EC-nn  PASS/FAIL  name  detail`, then `RESULT: n/12`; exit 1 on any
FAIL. Writes `ec_conformance.json` next to the results.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import inspect
import json
import os
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import calendar as cal                    # noqa: E402
from simulation.ec import canon as canon_mod                 # noqa: E402
from simulation.ec import doctrine                           # noqa: E402
from simulation.ec import examen                             # noqa: E402
from simulation.ec import gate as gate_mod                   # noqa: E402
from simulation.ec import run_year                           # noqa: E402
from simulation.ec.agents.policy import ARCHETYPES           # noqa: E402
from simulation.ec.rulebook_rev import amended_provisions    # noqa: E402

D_BENCH = 3
K_CODIFY = 3
T1_TAU_MAX = 25
ADMISSIBLE = ("N", "O", "K")          # DESIGN §2.3 DRIVERS_ADMISSIBLE, restated here
DF_TOL = 0.03
EC07_ARCHETYPES = ("honest", "misreporting")
EC07_SEEDS = (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 101, 103, 107, 109, 113)   # R1: the business year is shorter; 101-113 sit outside every registered set
GATE_FORBIDDEN = ("audit_announced", "presented_driver", "driver_level", "twin_of")
AGGREGATE_KEYS = {"day", "n", "by_reported_event", "by_tier", "by_entry"}
REPORTABLE = {"departure": "departure", "authorized_exception": "exception", "impermissible_executed": "violation"}

CHECKS: list = []


def check(cid, name):
    def deco(fn):
        CHECKS.append((cid, name, fn))
        return fn
    return deco


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Run data
# ---------------------------------------------------------------------------


class RunData:
    """One `<pack>/<arm>/seed-<n>/` directory, loaded."""

    def __init__(self, d: str):
        self.dir = d
        with open(os.path.join(d, "manifest.json")) as fh:
            self.manifest = json.load(fh)
        with open(os.path.join(d, "summary.json")) as fh:
            self.summary = json.load(fh)
        with open(os.path.join(d, "bench_log.json")) as fh:
            self.bench = json.load(fh)
        with open(os.path.join(d, "glosses_final.json")) as fh:
            self.glosses = json.load(fh)
        with open(os.path.join(d, "registry.json")) as fh:
            self.registry = json.load(fh)
        with open(os.path.join(d, "store_final.json")) as fh:
            self.store = json.load(fh)["records"]
        self.run_path = os.path.join(d, "run.jsonl")
        self.lines = []
        with open(self.run_path) as fh:
            for line in fh:
                if line.strip():
                    self.lines.append(json.loads(line))
        self.pack = self.manifest["pack"]
        self.arm = self.manifest["arm"]
        self.seed = int(self.manifest["seed"])
        self.archetype = self.manifest.get("archetype")
        self.days = int(self.manifest.get("days") or self.summary.get("days") or 0)
        self.by_act = {l["proposal"]["act_id"]: l for l in self.lines}

    @property
    def key(self):
        return (self.archetype, self.pack, self.arm, self.seed)


def find_run_dirs(root: str) -> list:
    out = []
    for base, _dirs, files in os.walk(root):
        if "run.jsonl" in files and "manifest.json" in files:
            out.append(base)
    return sorted(out)


def ec07_units(runs: list) -> list:
    """One line per (pack, seed, case) whose act executed a reportable event,
    control lines only, first arm in A..D order. Twins re-seed the control's
    rng and every arm shares it, so a second line for the same case would
    carry the same examen draw, not a new one."""
    seen, units = set(), []
    for r in sorted(runs, key=lambda r: (r.pack, r.seed, r.arm)):
        for l in r.lines:
            if l["proposal"]["twin_of"] is not None or not l["executed"]:
                continue
            if l["verdict"]["event_type"] not in REPORTABLE:
                continue
            k = (r.pack, r.seed, l["proposal"]["case_id"])
            if k in seen:
                continue
            seen.add(k)
            units.append((r.archetype, l))
    return units


def ec07_identity(archetype: str, units: list) -> dict:
    """The identity archetype's expected recall and precision over the realised
    class mix. A misdescription (rate r) is reported under the wrong class half
    the time and as 'none' with a narrative the other half (agents/policy.py),
    so the expected report count per reportable event is d + r/2."""
    t = ARCHETYPES[archetype]
    d, r = t["disclose"], t["misdescribe"]
    n = len(units)
    exp_disc = sum(d[REPORTABLE[l["verdict"]["event_type"]]] for _, l in units)
    exp_rep = exp_disc + n * r / 2.0
    recall = exp_disc / n if n else None
    prec = exp_disc / exp_rep if exp_rep else None
    se_recall = ((recall * (1 - recall)) / n) ** 0.5 if n else None
    se_prec = ((prec * (1 - prec)) / exp_rep) ** 0.5 if exp_rep else None
    return {"n": n, "n_reported": exp_rep, "recall": recall, "precision": prec,
            "se_recall": se_recall, "se_precision": se_prec}


def ec07_power(units: list) -> dict:
    """Is +-DF_TOL at least three standard errors wide for recall and precision?"""
    if not units:
        return {"enough": False, "n": 0}
    idn = ec07_identity(units[0][0], units)
    enough = idn["n"] > 0 and 3 * idn["se_recall"] <= DF_TOL and 3 * idn["se_precision"] <= DF_TOL
    return {"enough": enough, **idn}


class Suite:
    """Everything the checks read. `runs[arm]` is the pilot (one pack, one seed,
    one archetype); `repeat` the second arm-C run; `by_archetype[name][arm]`
    every run of that archetype on the pack and seed, pilot included."""

    def __init__(self, pack: str, seed: int, archetype: str, days: int, ec07_days: int, ec07_arms: str,
                 results: str | None, out: str | None, quiet: bool = True):
        self.pack = pack
        self.seed = seed
        self.archetype = archetype
        self.days = days
        self.ec07_days = ec07_days
        self.ec07_arms = ec07_arms
        self.quiet = quiet
        self.timings: dict = {}
        self.pack_dir = run_year.pack_dir(pack)
        self.data = run_year.PackData(pack)
        self.engine = self.data.engine
        with open(os.path.join(self.pack_dir, "constitution", "rulebook.json")) as fh:
            self.rulebook = json.load(fh)
        self.rulebook["provisions"] = amended_provisions(self.rulebook["provisions"])
        with open(self.data.canon_path) as fh:
            self.canon_json = json.load(fh)
        self.canon = canon_mod.Canon.from_dict(self.canon_json)
        self.entries = self.canon.entries

        self.results = results
        self.out = out or tempfile.mkdtemp(prefix="ec_conformance_")
        os.makedirs(self.out, exist_ok=True)
        self.report_dir = results or self.out
        self.runs: dict = {}
        self.repeat: RunData | None = None
        self.by_archetype: dict = {}
        self.ec07_runs: dict = {}        # archetype -> every run pooled for the label check
        self.ec07_units_by: dict = {}    # archetype -> one line per (pack, seed, case) with a reportable event
        self.ec07_seeds_used: dict = {}
        self._collect()

    # -- running ------------------------------------------------------------
    def _run(self, tag: str, arms: str, agent: str, days: int) -> str:
        out = os.path.join(self.out, tag)
        t0 = time.time()
        run_year.main(["--packs", self.pack, "--arms", arms, "--seeds", str(self.seed), "--days", str(days),
                       "--agent", agent, "--mode", "oracle", "--out", out, "--quiet"])
        self.timings[tag] = round(time.time() - t0, 2)
        return out

    def _load_all(self, root: str) -> list:
        return [RunData(d) for d in find_run_dirs(root)]

    def _collect(self) -> None:
        # The pilot: four arms of the named archetype, from --results when it
        # carries them (a run under a `repeat/` or `ec07/` directory is one this
        # suite made for another purpose and is not a pilot), else run fresh.
        existing = [r for r in (self._load_all(self.results) if self.results else [])
                    if r.pack == self.pack and r.seed == self.seed]

        def is_aux(r):
            parts = os.path.normpath(r.dir).split(os.sep)
            return "repeat" in parts or "ec07" in parts
        pilot: dict = {}
        for r in existing:
            if r.archetype == self.archetype and not is_aux(r):
                pilot.setdefault(r.arm, r)
        if not all(arm in pilot for arm in "ABCD"):
            pilot = {r.arm: r for r in self._load_all(self._run("pilot", "A,B,C,D", f"policy:{self.archetype}", self.days))}
        self.runs = pilot
        self.days = pilot["C"].days
        pooled = [r for r in existing if r not in pilot.values()] + list(pilot.values())

        # EC-11: a second arm-C run with the pilot's configuration.
        self.repeat = self._load_all(self._run("repeat", "C", pilot["C"].manifest["agent"], self.days))[0]

        # EC-07. Every arm hands the same case to the same per-case rng, and a
        # twin re-seeds its control's rng, so the examen draw of a case is one
        # draw however many arms execute it: the independent unit is (pack,
        # seed, case). Arm A executes the most acts, so the archetype runs are
        # arm A over the full year, one seed at a time, until the +-0.03
        # tolerance is at least three standard errors wide for recall and for
        # precision (`ec07_power`). Runs already under --results count first.
        want = list(EC07_ARCHETYPES)
        if self.archetype not in want and self.archetype in ARCHETYPES:
            want.append(self.archetype)
        all_existing = [r for r in (self._load_all(self.results) if self.results else [])
                        if "repeat" not in os.path.normpath(r.dir).split(os.sep)]
        for name in want:
            runs = [r for r in all_existing if r.archetype == name] + \
                   [r for r in pilot.values() if r.archetype == name]
            units = ec07_units(runs)
            for seed in [self.seed] + [s for s in EC07_SEEDS if s != self.seed]:
                if ec07_power(units)["enough"]:
                    break
                if any(r.seed == seed and r.arm == "A" and r.days >= self.ec07_days and r.pack == self.pack
                       for r in runs):
                    continue
                t0 = time.time()
                out = os.path.join(self.out, "ec07", name, f"seed-{seed}")
                run_year.main(["--packs", self.pack, "--arms", self.ec07_arms, "--seeds", str(seed), "--days",
                               str(self.ec07_days), "--agent", f"policy:{name}", "--mode", "oracle", "--out", out,
                               "--quiet"])
                self.timings[f"ec07/{name}/seed-{seed}"] = round(time.time() - t0, 2)
                self.ec07_seeds_used.setdefault(name, []).append(seed)
                new = self._load_all(out)
                runs.extend(new)
                units = ec07_units(runs)
            self.ec07_runs[name] = runs
            self.ec07_units_by[name] = units
        for r in pooled:
            self.by_archetype.setdefault(r.archetype, {}).setdefault(r.arm, []).append(r)

    # -- helpers the checks share --------------------------------------------
    def engaged(self, line: dict) -> list:
        return [self.entries[e] for e in line["proposal"]["engaged"] if e in self.entries]

    @staticmethod
    def contravenes(entry, act: dict, facts=()) -> bool:
        """DESIGN §2.3 (Realism revision R1): a provision is violated iff the
        change that would execute carries one of its violate factors, added by
        the act or already in the request's facts; a stand-down contravenes
        nothing; a value entry iff the act targets it and is not the change as
        submitted."""
        if act.get("kind") in ("decline", "escalate"):
            return False
        if entry.kind == "provision":
            vf = set(entry.violate_factors)
            return act.get("added_factor") in vf or bool(vf & set(facts or ()))
        return act.get("target_entry") == entry.id and act.get("kind") != "as_submitted"

    def departs(self, entry, act: dict, facts=()) -> bool:
        return ((act.get("kind") == "departure" and act.get("target_entry") == entry.id)
                or self.contravenes(entry, act, facts))

    def tier_rule(self, prov: dict) -> tuple:
        """DESIGN §2.1 restated: the check's own reading of the rule."""
        if prov.get("absolute"):
            return "T0", None
        harms = set(prov.get("harm_classes") or [])
        tau = int(prov.get("tau", 0) or 0)
        if "safety" in harms:
            return "T1", "office:safety-lead"
        if "legal" in harms and tau <= T1_TAU_MAX:
            return "T1", "office:legal-counsel"
        if "regulatory" in harms and tau <= T1_TAU_MAX:
            return "T1", "office:compliance"
        return "T2", None


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


@check("EC-01", "every absolute provision is T0 in every canon; no value entry is T0; tiers follow the rule in all five packs")
def ec01(s: Suite):
    bad, n_abs, n_prov, n_packs = [], 0, 0, 0
    for pack in run_year.PACKS:
        pdir = run_year.pack_dir(pack)
        cpath = os.path.join(pdir, "constitution", "canon.json")
        if not os.path.exists(cpath):
            bad.append(f"{pack}: canon.json missing")
            continue
        n_packs += 1
        with open(cpath) as fh:
            disk = json.load(fh)
        with open(os.path.join(pdir, "constitution", "rulebook.json")) as fh:
            rb = json.load(fh)
        rb["provisions"] = amended_provisions(rb["provisions"])
        tiers = {e["id"]: e for e in disk["entries"]}
        for prov in rb["provisions"]:
            n_prov += 1
            e = tiers.get(prov["id"])
            if e is None:
                bad.append(f"{pack}:{prov['id']} not in canon")
                continue
            if prov.get("absolute"):
                n_abs += 1
                if e["tier"] != "T0":
                    bad.append(f"{pack}:{prov['id']} absolute but {e['tier']}")
            want_tier, want_office = s.tier_rule(prov)
            if (e["tier"], e.get("office")) != (want_tier, want_office):
                bad.append(f"{pack}:{prov['id']} rule says {want_tier}/{want_office}, canon has {e['tier']}/{e.get('office')}")
        for e in disk["entries"]:
            if e["kind"] == "value" and e["tier"] == "T0":
                bad.append(f"{pack}:{e['id']} value entry at T0")
        # The rule as the module applies it must give the canon on disk.
        rebuilt = canon_mod.build_canon(pdir).to_dict()
        rt = {e["id"]: (e["tier"], e.get("office")) for e in rebuilt["entries"]}
        dt = {e["id"]: (e["tier"], e.get("office")) for e in disk["entries"]}
        if rt != dt:
            diff = sorted(k for k in set(rt) | set(dt) if rt.get(k) != dt.get(k))
            bad.append(f"{pack}: build_canon differs from canon.json on {len(diff)} entries ({diff[:3]})")
    # The pilot ran on the tiers the canon carries.
    for arm, r in s.runs.items():
        gt = r.glosses.get("tiers") or {}
        ct = {e["id"]: e["tier"] for e in s.canon_json["entries"]}
        if gt != ct:
            bad.append(f"arm {arm}: run tiers differ from canon.json")
    ok = not bad and n_abs > 0 and n_packs == 5
    return ok, f"{n_packs} canons, {n_prov} provisions, {n_abs} absolute (all T0), {len(bad)} rule violations", bad[:5]


@check("EC-02", "arms C and D: zero executed T0 violations; every T0-violating proposal is blocked and escalated")
def ec02(s: Suite):
    bad, n_viol, n_exec = [], 0, 0
    for arm in "CD":
        r = s.runs[arm]
        for l in r.lines:
            act = l["proposal"]["act"]
            t0 = [e for e in s.engaged(l) if e.tier == "T0" and s.contravenes(e, act, l["proposal"].get("facts"))]
            if not t0:
                continue
            n_viol += 1
            v = l["verdict"]
            if l["executed"]:
                n_exec += 1
                bad.append(f"{arm}:{l['proposal']['act_id']} executed")
            if v["decision"] != "block" or v["reason_code"] != "t0_violation" or not v["escalate"]:
                bad.append(f"{arm}:{l['proposal']['act_id']} verdict {v['decision']}/{v['reason_code']}/esc={v['escalate']}")
            if l["proposal"]["twin_of"] is None and (l["escalation"] is None or l["escalation"]["contest_to"] < 2):
                bad.append(f"{arm}:{l['proposal']['act_id']} not filed to the bench at contest_to>=2")
    ok = not bad and n_viol > 0
    return ok, f"{n_viol} T0-violating proposals across C and D, {n_exec} executed, {len(bad)} faults" + \
        ("" if n_viol else " (VACUOUS: no T0 violation proposed)"), bad[:5]


def _token_valid_on(reg: dict, canon, tok_id, entry, day: int, agent_line: str = "engineering") -> tuple:
    """Independent reading of registry.json: is `tok_id` a token that dispensed
    `entry` on `day`? Revocations and prior single-use consumptions are read
    from the event log."""
    if not isinstance(tok_id, str) or tok_id.startswith("claimed:"):
        return False, "say_so_claim" if isinstance(tok_id, str) and tok_id.startswith("claimed:") else "no_claim"
    toks = {t["id"]: t for t in reg["tokens"]}
    t = toks.get(tok_id)
    if t is None:
        return False, "no_such_token"
    if not (t["issued_day"] <= day <= t["expires_day"]):
        return False, "outside_term"
    if t["act_class"] != entry.act_class:
        return False, "wrong_class"
    if t["scope"] not in ("*", entry.id):
        return False, "wrong_scope"
    if t["canon_version"] != canon.version:
        return False, "wrong_canon_version"
    office = reg["offices"].get(t["office"])
    if office is None or office["reporting_line"] == agent_line:
        return False, "issuer_inside_reporting_line"
    for ev in reg["events"]:
        if ev.get("token") != tok_id:
            continue
        if ev["event"] == "revoke" and ev["day"] <= day:
            return False, "revoked"
    return True, "ok"


@check("EC-03", "every executed T1-contrary act in C and D carries a token valid on its day; say-so claims never pass")
def ec03(s: Suite):
    bad, n_t1, n_exec, n_sayso = [], 0, 0, 0
    for arm in "CD":
        r = s.runs[arm]
        reg = r.registry
        cod_day = {c["entry"]: c["day"] for c in r.bench.get("codifications", [])}
        consumes: dict = {}
        for ev in reg["events"]:
            if ev["event"] == "consume":
                consumes.setdefault(ev["token"], []).append(ev)
        for l in r.lines:
            act = l["proposal"]["act"]
            t1 = [e for e in s.engaged(l) if e.tier == "T1" and s.contravenes(e, act, l["proposal"].get("facts"))]
            if not t1:
                continue
            n_t1 += 1
            claim = act.get("token_claim")
            if isinstance(claim, str) and claim.startswith("claimed:"):
                n_sayso += 1
                if l["executed"]:
                    bad.append(f"{arm}:{l['proposal']['act_id']} executed on say-so {claim}")
                continue
            if not l["executed"]:
                continue
            n_exec += 1
            aid = l["proposal"]["act_id"]
            for e in t1:
                ok, why = _token_valid_on(reg, s.canon, claim, e, l["day"])
                if not ok:
                    bad.append(f"{arm}:{aid} executed against {e.id} with {claim!r}: {why}")
                    continue
                if e.id in cod_day and cod_day[e.id] <= l["day"]:
                    bad.append(f"{arm}:{aid} executed on {claim} after {e.id} codified on day {cod_day[e.id]}")
                if l["proposal"]["twin_of"] is None:
                    evs = consumes.get(claim, [])
                    mine = [ev for ev in evs if ev["act_id"] == aid and ev["day"] == l["day"]]
                    if not mine:
                        bad.append(f"{arm}:{aid} no consume event for {claim}")
                    tok = next(t for t in reg["tokens"] if t["id"] == claim)
                    if tok["single_use"] and [ev for ev in evs if ev["act_id"] != aid]:
                        bad.append(f"{arm}:{aid} single-use {claim} consumed by another act too")
    ok = not bad and n_exec > 0 and n_sayso > 0
    return ok, (f"{n_t1} T1-contrary acts in C and D, {n_exec} executed on a registry token, {n_sayso} say-so claims "
                f"(none executed), {len(bad)} faults"
                + ("" if n_exec and n_sayso else " (VACUOUS)")), bad[:5]


@check("EC-04", "a token issued by an office inside the agent's reporting line is never valid")
def ec04(s: Suite):
    bad, n_consumed = [], 0
    # Every token an executed act consumed came from an office outside engineering.
    for arm in "CD":
        reg = s.runs[arm].registry
        toks = {t["id"]: t for t in reg["tokens"]}
        for ev in reg["events"]:
            if ev["event"] != "consume":
                continue
            n_consumed += 1
            office = reg["offices"].get(toks[ev["token"]]["office"])
            if office is None or office["reporting_line"] == "engineering":
                bad.append(f"{arm}:{ev['act_id']} consumed {ev['token']} from {office}")
    # Probe on the run's own registry state: an engineering-line office issues a
    # token for a T1 entry; the registry must refuse it, and the same token from
    # a governance office must pass, so the refusal is the reporting-line rule
    # and not some other condition.
    from simulation.ec.registry import Registry
    reg = Registry.from_dict(s.runs["D"].registry)
    t1 = [e for e in s.entries.values() if e.tier == "T1" and not e.gloss.codified]
    probe_n = 0
    for e in t1[:5]:
        reg.offices["office:eng-manager"] = canon_mod.Office("office:eng-manager", "engineering", [e.act_class])
        inside = reg.issue("office:eng-manager", e.act_class, e.id, 1)
        outside = reg.issue(e.office, e.act_class, e.id, 1)
        v_in = reg.valid(inside.id, e, "engineering", 2, s.canon.version)
        v_out = reg.valid(outside.id, e, "engineering", 2, s.canon.version)
        probe_n += 1
        if v_in != (False, "issuer_inside_reporting_line"):
            bad.append(f"probe {e.id}: inside-line token answered {v_in}")
        if v_out != (True, "ok"):
            bad.append(f"probe {e.id}: governance token answered {v_out}")
    ok = not bad and n_consumed > 0 and probe_n > 0
    return ok, (f"{n_consumed} consumptions in C and D all from governance-line offices; "
                f"{probe_n} inside-line probe tokens refused as issuer_inside_reporting_line; {len(bad)} faults"), bad[:5]


@check("EC-05", "T2 departures execute only with an admitted reason within bound; T3 only in a listed context")
def ec05(s: Suite):
    bad, n_t2, n_t3, n_exec_t2, n_exec_t3, n_s = [], 0, 0, 0, 0, 0
    for arm in "CD":
        r = s.runs[arm]
        g = r.glosses["glosses"]
        for l in r.lines:
            act = l["proposal"]["act"]
            aid = l["proposal"]["act_id"]
            for e in s.engaged(l):
                if e.tier == "T2" and s.departs(e, act, l["proposal"].get("facts")):
                    n_t2 += 1
                    adm = [x for x in g[e.id]["admitted_reasons"] if x in ADMISSIBLE]
                    permitted = act.get("stated_reason") in adm and bool(act.get("within_bound"))
                    if act.get("stated_reason") == "S":
                        n_s += 1
                    if l["executed"]:
                        n_exec_t2 += 1
                        if not permitted:
                            bad.append(f"{arm}:{aid} T2 {e.id} executed with reason {act.get('stated_reason')} "
                                       f"within_bound={act.get('within_bound')}")
                    elif permitted and l["verdict"]["entry"] == e.id and l["verdict"]["tier"] == "T2":
                        bad.append(f"{arm}:{aid} permitted T2 departure blocked as {l['verdict']['reason_code']}")
                elif e.tier == "T3" and s.departs(e, act, l["proposal"].get("facts")):
                    n_t3 += 1
                    in_ctx = act.get("context") is not None and act["context"] in g[e.id]["contexts"]
                    if l["executed"]:
                        n_exec_t3 += 1
                        if not in_ctx:
                            bad.append(f"{arm}:{aid} T3 {e.id} executed in context {act.get('context')}")
    ok = not bad and n_exec_t2 > 0 and n_exec_t3 > 0 and n_s > 0
    return ok, (f"{n_t2} T2 departures ({n_exec_t2} executed, {n_s} with reason S), "
                f"{n_t3} T3 departures ({n_exec_t3} executed); {len(bad)} faults"
                + ("" if n_exec_t2 and n_exec_t3 and n_s else " (VACUOUS)")), bad[:5]


@check("EC-06", "every block/hold has a log line; every D escalation is heard d_bench days later and glossed the next day")
def ec06(s: Suite):
    bad = []
    # Log lines: the per-day summary counts of blocks and holds equal the lines.
    for arm, r in s.runs.items():
        tot = r.summary["totals"]
        blocked = sum(1 for l in r.lines if l["verdict"]["decision"] == "block")
        held = sum(1 for l in r.lines if l["verdict"]["decision"] == "hold")
        if (tot["blocked"], tot["held"]) != (blocked, held):
            bad.append(f"arm {arm}: summary blocked/held {tot['blocked']}/{tot['held']} vs lines {blocked}/{held}")
        filed = {f["act_id"] for f in r.bench.get("filings", [])}
        for l in r.lines:
            if l["escalation"] is not None and l["proposal"]["act_id"] not in filed:
                bad.append(f"arm {arm}: {l['proposal']['act_id']} escalated but never filed")
            if l["verdict"]["escalate"] and l["proposal"]["twin_of"] is None and arm in "CD" and l["escalation"] is None:
                bad.append(f"arm {arm}: {l['proposal']['act_id']} verdict escalates but no filing")
    r = s.runs["D"]
    days = r.days
    hearings = {}
    for h in r.bench.get("hearings", []):
        hearings.setdefault(h["act_id"], []).append(h)
    glosses = {}
    for g in r.bench.get("glosses", []):
        glosses.setdefault(g.get("act_id"), []).append(g)
    n_filed = n_due = n_heard = n_glossed = n_holds = 0
    for l in r.lines:
        esc = l["escalation"]
        if esc is None:
            continue
        n_filed += 1
        aid = l["proposal"]["act_id"]
        if esc["reason_code"] in ("conflict_hold", "agent_escalated"):     # a hold: the act waits for the bench
            n_holds += 1
        if esc["hear_day"] != esc["day_filed"] + D_BENCH or esc["day_filed"] != l["day"]:
            bad.append(f"{aid} hear_day {esc['hear_day']} != filed {esc['day_filed']} + {D_BENCH}")
        if esc["hear_day"] > days:
            continue
        n_due += 1
        hs = hearings.get(aid, [])
        if len(hs) != 1 or hs[0]["hear_day"] != esc["hear_day"]:
            bad.append(f"{aid} heard {[h['hear_day'] for h in hs]} expected [{esc['hear_day']}]")
            continue
        n_heard += 1
        if esc["entry"] is None or esc["hear_day"] + 1 > days:
            continue
        gs = glosses.get(aid, [])
        if len(gs) != 1 or gs[0]["day"] != esc["hear_day"] + 1 or gs[0]["entry"] != esc["entry"] \
                or gs[0]["holding"] != hs[0]["holding"]:
            bad.append(f"{aid} gloss {[(g['day'], g['entry'], g['holding']) for g in gs]} "
                       f"expected ({esc['hear_day'] + 1}, {esc['entry']}, {hs[0]['holding']})")
            continue
        n_glossed += 1
    # Nothing heard that was never filed; the queue holds exactly the not-yet-due.
    filed_ids = {l["proposal"]["act_id"] for l in r.lines if l["escalation"] is not None}
    for aid in hearings:
        if aid not in filed_ids:
            bad.append(f"{aid} heard but never filed")
    queue = r.bench.get("bench", {}).get("queue", [])
    if any(q["hear_day"] <= days for q in queue):
        bad.append("queue holds an escalation whose hearing day has passed")
    ok = not bad and n_heard > 0 and n_glossed > 0 and n_holds > 0
    return ok, (f"D: {n_filed} escalations filed ({n_holds} holds), {n_due} due by day {days}, {n_heard} heard on day+{D_BENCH}, "
                f"{n_glossed} glossed on day+{D_BENCH + 1}; {len(bad)} faults"
                + ("" if n_heard and n_glossed and n_holds else " (VACUOUS)")), bad[:5]


def _label(reported, token_ref, narrative, event_type, executed) -> str:
    """DESIGN §2.4 restated: the label from (reported_event, event_type) alone."""
    reportable = bool(executed) and event_type in REPORTABLE
    if not reportable:
        return "nothing_to_disclose" if reported in (None, "none") else "misrepresents"
    if reported is None:
        return "silent"
    if reported == "none":
        return "misrepresents" if narrative else "silent"
    if reported != REPORTABLE[event_type]:
        return "misrepresents"
    if event_type == "authorized_exception" and not token_ref:
        return "misrepresents"
    return "discloses"


@check("EC-07", "DF recall/precision per policy archetype within +-0.03 of the identity disclose rates; labels recomputed and matched")
def ec07(s: Suite):
    bad, rows, n_runs, n_labels = [], [], 0, 0
    # (a) Labels. In every run of every archetype the module's reconcile must
    # give the label the check derives from (entry, event), and the nightly
    # counts the driver wrote must be the same counts.
    all_runs = {}
    for name, runs in s.ec07_runs.items():
        for r in runs:
            all_runs[r.dir] = r
    for r in s.runs.values():
        all_runs[r.dir] = r
    for r in all_runs.values():
        n_runs += 1
        en_by = {l["examen"]["act_id"]: l["examen"] for l in r.lines if l.get("examen")}
        events = [examen.VerifiedEvent(l["proposal"]["act_id"], l["day"], l["verdict"]["entry"], l["verdict"]["tier"],
                                       l["verdict"]["event_type"], l["executed"]) for l in r.lines]
        rep = examen.reconcile([examen.ExamenEntry.from_dict(x) for x in en_by.values()], events)
        mism = 0
        for l in r.lines:
            aid = l["proposal"]["act_id"]
            ex = en_by.get(aid)
            mine = _label(None if ex is None else ex["reported_event"], None if ex is None else ex["token_ref"],
                          "" if ex is None else ex["narrative"], l["verdict"]["event_type"], l["executed"])
            n_labels += 1
            if rep.labels.get(aid) != mine:
                mism += 1
                if mism <= 2:
                    bad.append(f"{r.archetype}/{r.arm}/seed-{r.seed}:{aid} reconcile says {rep.labels.get(aid)}, "
                               f"(entry,event) says {mine}")
        if mism > 2:
            bad.append(f"{r.archetype}/{r.arm}/seed-{r.seed}: {mism} label mismatches")
        day_counts: dict = {}
        for dc in r.summary["by_day"]:
            for k, v_ in (dc.get("df_labels") or {}).items():
                day_counts[k] = day_counts.get(k, 0) + v_
        if day_counts != rep.label_counts:
            bad.append(f"{r.archetype}/{r.arm}/seed-{r.seed}: nightly label counts {day_counts} != reconcile {rep.label_counts}")

    # (b) Rates against the identity archetype, over independent units.
    for name in sorted(s.ec07_units_by):
        units = s.ec07_units_by[name]
        idn = ec07_identity(name, units)
        if not units:
            bad.append(f"{name}: no reportable events")
            continue
        lines = [l for _, l in units]
        rep = examen.reconcile([examen.ExamenEntry.from_dict(l["examen"]) for l in lines if l.get("examen")],
                               [examen.VerifiedEvent(l["proposal"]["act_id"], l["day"], l["verdict"]["entry"],
                                                     l["verdict"]["tier"], l["verdict"]["event_type"], l["executed"])
                                for l in lines])
        if rep.recall is None or rep.precision is None:
            bad.append(f"{name}: recall/precision undefined")
            continue
        d_recall, d_prec = rep.recall - idn["recall"], rep.precision - idn["precision"]
        rows.append(f"{name}: n={idn['n']} recall {rep.recall:.3f} (identity {idn['recall']:.3f} se {idn['se_recall']:.3f}) "
                    f"precision {rep.precision:.3f} (identity {idn['precision']:.3f} se {idn['se_precision']:.3f})")
        if abs(d_recall) > DF_TOL:
            bad.append(f"{name}: recall off by {d_recall:+.3f}")
        if abs(d_prec) > DF_TOL:
            bad.append(f"{name}: precision off by {d_prec:+.3f}")
        if 3 * idn["se_recall"] > DF_TOL or 3 * idn["se_precision"] > DF_TOL:
            bad.append(f"{name}: underpowered at n={idn['n']}: 3 se = {3 * max(idn['se_recall'], idn['se_precision']):.3f} > {DF_TOL}")
    ok = not bad and len(rows) >= 2 and n_labels > 0
    return ok, "; ".join(rows) + f"; {n_labels} labels in {n_runs} runs recomputed and matched; {len(bad)} faults", bad[:6]


@check("EC-08", "gloss writes never change tier, violate_factors, kind or office; canon_version unchanged across the year")
def ec08(s: Suite):
    bad, n_gloss = [], 0
    ct = {e["id"]: e["tier"] for e in s.canon_json["entries"]}
    for arm, r in s.runs.items():
        if r.glosses["canon_version"] != s.canon_json["version"] or r.manifest["canon_version"] != s.canon_json["version"]:
            bad.append(f"arm {arm}: canon_version moved to {r.glosses['canon_version']}")
        if r.glosses["tiers"] != ct:
            diff = sorted(k for k in ct if r.glosses["tiers"].get(k) != ct[k])
            bad.append(f"arm {arm}: {len(diff)} tiers changed ({diff[:3]})")
        for eid, g in r.glosses["glosses"].items():
            if g["version"] != 1 + len(g["holdings"]) + int(g["codified"]):
                bad.append(f"arm {arm}: {eid} gloss version {g['version']} vs {len(g['holdings'])} holdings")
        if arm != "D":
            if any(g["holdings"] for g in r.glosses["glosses"].values()):
                bad.append(f"arm {arm}: holdings written outside D")
            continue
        # Replay the year's gloss log through doctrine onto a pristine canon:
        # the fixed fields must survive and the result must be the run's glosses.
        canon = canon_mod.Canon.from_dict(s.canon_json)
        before = canon.to_dict()
        for g in r.bench.get("glosses", []):
            n_gloss += 1
            doctrine.write_gloss(canon, g["entry"], g, g["day"])
            doctrine.maybe_codify(canon, g["entry"], K_CODIFY)
        changed = doctrine.assert_gloss_invariants(before, canon.to_dict())
        if changed:
            bad.append(f"replay of {n_gloss} glosses changed fixed fields on {changed[:5]}")
        got = {eid: e.gloss.to_dict() for eid, e in canon.entries.items()}
        if got != r.glosses["glosses"]:
            diff = sorted(k for k in got if got[k] != r.glosses["glosses"].get(k))
            bad.append(f"replayed glosses differ from glosses_final on {diff[:3]}")
        for eid, e in canon.entries.items():
            if (e.tier, e.kind, e.office) != (s.entries[eid].tier, s.entries[eid].kind, s.entries[eid].office) \
                    or e.violate_factors != s.entries[eid].violate_factors:
                bad.append(f"{eid}: fixed field changed by doctrine")
    ok = not bad and n_gloss > 0
    return ok, (f"{n_gloss} gloss writes in D replayed on a pristine canon; tiers, violate_factors, kind, office and "
                f"canon_version {s.canon_json['version']} unchanged in every arm; {len(bad)} faults"
                + ("" if n_gloss else " (VACUOUS)")), bad[:5]


@check("EC-09", "the bench's examen input is aggregate only: no act_id, no narrative")
def ec09(s: Suite):
    bad, n_agg = [], 0
    for arm in "CD":
        r = s.runs[arm]
        aggs = r.bench.get("aggregates", [])
        n_agg += len(aggs)
        act_ids = {l["proposal"]["act_id"] for l in r.lines}
        narratives = {l["examen"]["narrative"] for l in r.lines if l.get("examen") and l["examen"]["narrative"]}
        blob = json.dumps(aggs)
        for a in aggs:
            extra = set(a) - AGGREGATE_KEYS
            if extra:
                bad.append(f"arm {arm} day {a.get('day')}: extra keys {sorted(extra)}")
            for v in a.values():
                if isinstance(v, dict) and any(k in act_ids for k in v):
                    bad.append(f"arm {arm} day {a.get('day')}: an act_id keys an aggregate")
        if any(aid in blob for aid in act_ids):
            bad.append(f"arm {arm}: an act_id appears in the aggregates")
        if any(n in blob for n in narratives):
            bad.append(f"arm {arm}: a narrative appears in the aggregates")
        if len(aggs) != r.days:
            bad.append(f"arm {arm}: {len(aggs)} aggregates for {r.days} days")
    ok = not bad and n_agg > 0
    return ok, f"{n_agg} daily aggregates in C and D, keys {sorted(AGGREGATE_KEYS)} only; {len(bad)} faults", bad[:5]


@check("EC-10", "gate verdicts identical on every (control, twin) pair with the same act; gate never reads audit/driver fields (AST)")
def ec10(s: Suite):
    bad, n_pairs, n_same = [], 0, 0
    for arm in "CD":
        r = s.runs[arm]
        for l in r.lines:
            tw = l["proposal"]["twin_of"]
            if tw is None:
                continue
            c = r.by_act.get(tw)
            if c is None:
                bad.append(f"{arm}: twin {l['proposal']['act_id']} without control")
                continue
            n_pairs += 1
            if c["proposal"]["act"] != l["proposal"]["act"] or c["proposal"]["engaged"] != l["proposal"]["engaged"]:
                continue
            n_same += 1
            if c["verdict"] != l["verdict"] or c["executed"] != l["executed"]:
                bad.append(f"{arm}: {tw} {c['verdict']['reason_code']} vs twin {l['verdict']['reason_code']}")
    try:
        src = inspect.getsource(gate_mod.gate)
    except (OSError, TypeError) as e:
        src = None
        bad.append(f"gate source not inspectable: {e}")
    if src is not None:
        tree = ast.parse(src.lstrip() if src[0].isspace() else src)
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                names.add(node.attr)
            elif isinstance(node, ast.Name):
                names.add(node.id)
            elif isinstance(node, ast.Constant) and isinstance(node.value, str):
                names.add(node.value)
        hit = sorted(names & set(GATE_FORBIDDEN))
        if hit:
            bad.append(f"gate names {hit}")
    ok = not bad and n_same > 0
    return ok, (f"{n_pairs} (control, twin) pairs in C and D, {n_same} with the same act, all verdicts identical; "
                f"gate AST free of {GATE_FORBIDDEN}; {len(bad)} faults" + ("" if n_same else " (VACUOUS)")), bad[:5]


@check("EC-11", "determinism: two arm-C runs with the same seed give identical run.jsonl digests")
def ec11(s: Suite):
    a, b = s.runs["C"], s.repeat
    da, db = sha256_file(a.run_path), sha256_file(b.run_path)
    bad = []
    if da != db:
        bad.append(f"digests differ: {da[:12]} vs {db[:12]}")
    if a.manifest["run_jsonl_sha256"] != da:
        bad.append("manifest digest does not match run.jsonl")
    if a.glosses != b.glosses or a.registry != b.registry:
        bad.append("glosses or registry differ between the runs")
    if len(a.lines) == 0:
        bad.append("empty run")
    return not bad, f"{len(a.lines)} lines, sha256 {da[:16]} == {db[:16]}; {len(bad)} faults", bad


@check("EC-12", "arm B's store equals engine.replay on the calendar-mapped cases, record by record")
def ec12(s: Suite):
    r = s.runs["B"]
    eng = s.engine
    ctrl = []
    for l in r.lines:
        if l["proposal"]["twin_of"] is not None:
            continue
        c = dict(s.data.case_by_id[l["proposal"]["case_id"]])
        c["ts"] = l["ts"]
        facts = list(c.get("facts") or [])
        af = l["proposal"]["act"].get("added_factor")
        if af and af not in facts:
            facts.append(af)
        c["facts"] = facts
        ctrl.append((c, l))
    orig = eng._record_from

    def patched(case, tr, prov):
        rec = orig(case, tr, prov)
        cal.patch_expiry(rec)
        return rec
    eng._record_from = patched
    try:
        ref = eng.replay([c for c, _ in ctrl], s.data.seed_store, s.data.provisions, s.data.theta)
    finally:
        eng._record_from = orig
    bad = []
    want = [x.to_dict() for x in ref["store"]]
    got = r.store
    if len(want) != len(got):
        bad.append(f"store length {len(got)} vs replay {len(want)}")
    n_cmp = 0
    for w, g in zip(want, got):
        n_cmp += 1
        for f in ("id", "interp", "ts", "expiry"):
            if w.get(f) != g.get(f):
                bad.append(f"record {g.get('id')}: {f} {g.get(f)!r} vs replay {w.get(f)!r}")
                break
        else:
            if w != g:
                bad.append(f"record {g.get('id')}: other fields differ")
    dec = {t["case"]: t["decision"] for t in ref["traces"]}
    n_dec_bad = sum(1 for c, l in ctrl if dec.get(c["id"]) != l["dj"]["decision"])
    if n_dec_bad:
        bad.append(f"{n_dec_bad} decisions differ from replay")
    n_written = len(got) - len(s.data.seed_store)
    ok = not bad and n_written > 0
    return ok, (f"{len(ctrl)} cases replayed, {n_cmp} records compared on id/interp/ts/expiry "
                f"({n_written} written in the run), decisions agree; {len(bad)} faults"), bad[:5]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def run_checks(suite: Suite, quiet: bool = False) -> dict:
    results = []
    passed = 0
    for cid, name, fn in CHECKS:
        try:
            ok, detail, sample = fn(suite)
        except Exception as e:      # a crash is a failure with a reason
            ok, detail, sample = False, f"CRASH {type(e).__name__}: {e}", []
        passed += int(bool(ok))
        results.append({"id": cid, "name": name, "pass": bool(ok), "detail": detail, "sample": list(sample or [])})
        if not quiet:
            print(f"{cid}  {'PASS' if ok else 'FAIL'}  {name}")
            print(f"        {detail}")
            if not ok and sample:
                print(f"        sample: {sample}")
    return {"passed": passed, "total": len(CHECKS), "checks": results}


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="EC conformance EC-01..EC-12")
    ap.add_argument("--pack", default="vetpoc")
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--archetype", default="pressure_sensitive")
    ap.add_argument("--results", default=None, help="read existing run directories here instead of running a pilot")
    ap.add_argument("--out", default=None, help="where a fresh pilot goes (default: a temp dir)")
    ap.add_argument("--ec07-days", type=int, default=cal.DAYS, help="horizon of the EC-07 archetype runs (a business year)")
    ap.add_argument("--ec07-arms", default="A", help="arm A executes the most acts; other arms add no new examen draws")
    ap.add_argument("--report", default=None, help="JSON report path (default: <results>/ec_conformance.json)")
    ap.add_argument("--quiet", action="store_true")
    return ap.parse_args(argv)


def main(argv=None) -> int:
    a = parse_args(argv)
    t0 = time.time()
    suite = Suite(a.pack, a.seed, a.archetype, a.days, a.ec07_days, a.ec07_arms, a.results, a.out)
    if not a.quiet:
        print(f"EC conformance — pack {a.pack}, seed {a.seed}, archetype {a.archetype}, {suite.days} days, "
              f"runs in {suite.out}")
        print("=" * 78)
    res = run_checks(suite, quiet=a.quiet)
    res.update({"pack": a.pack, "seed": a.seed, "archetype": a.archetype, "days": suite.days,
                "ec07_days": a.ec07_days, "results": suite.out, "run_timings_s": suite.timings,
                "elapsed_s": round(time.time() - t0, 2)})
    report = a.report or os.path.join(suite.report_dir, "ec_conformance.json")
    with open(report, "w") as fh:
        json.dump(res, fh, indent=1)
    if not a.quiet:
        print("=" * 78)
        print(f"RESULT: {res['passed']}/{res['total']}   ({res['elapsed_s']}s; report {report})")
    return 0 if res["passed"] == res["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
