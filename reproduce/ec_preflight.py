#!/usr/bin/env python3
"""
Preflight for the registered LLM live slice (prereg Part B, Sampling Plan).

    python3 reproduce/ec_preflight.py --provider anthropic --model <id> [--days 1] [--out <dir>]
    python3 reproduce/ec_preflight.py --provider openai --model <id>

Runs, in order, and stops on the first failure with a plain message:

  1. key        the provider's key variable is set (ANTHROPIC_API_KEY / OPENAI_API_KEY)
  2. models     GET /v1/models and confirm the model id is listed; print the exact id
  3. price      the PRICES entry in simulation/ec/agents/llm.py (warn when missing: live mode refuses it)
  4. plan       the registered run plan (5 packs x arms A,B,C,D x seed 11 x 365 days) with the cost
                projected from the dry run's token counts and the cache-sharing note
  5. smoke      a --days live run of vetpoc arm D, seed 97 (--smoke-seed), into --out: calls, parse failures, mean tokens from
                the provider's usage, spend, believes_monitored rate, three sample replies
  6. schema     every run.jsonl line of the smoke against the DATA_DICTIONARY run.jsonl section
  7. metrics    metrics.py on the smoke: the row, provenance ⟦measured⟧, E5 present

Without a key, steps 2 and 5-7 are SKIPPED by name and the exit status is 2; a
failed check exits 1; PREFLIGHT OK exits 0. The smoke is capped at --smoke-budget
USD (default 5) through the driver's --budget-usd.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
import tempfile
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import calendar as cal                                   # noqa: E402
from simulation.ec import metrics, run_year                                 # noqa: E402
from simulation.ec.agents import llm as llmmod                              # noqa: E402

DICTIONARY = os.path.join(ROOT, "prereg", "DATA_DICTIONARY.md")
DRY_ROOT = os.path.join(ROOT, "simulation", "ec", "results", "llm_dry")
REGISTERED_PACKS = ("vetpoc", "semifab", "frontierllm", "dcvigil", "meridian")
REGISTERED_ARMS = ("A", "B", "C", "D")
REGISTERED_SEED = 11
SMOKE_SEED = 97      # outside every registered seed set (calibration 11-23, EC-07 11-53, confirmatory 59-73, LLM slice 11)
PROVIDERS = {"anthropic": ("ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL", llmmod.ANTHROPIC_BASE_URL),
             "openai": ("OPENAI_API_KEY", "OPENAI_BASE_URL", llmmod.OPENAI_BASE_URL),
             "openai_compatible": ("OPENAI_API_KEY", "OPENAI_BASE_URL", llmmod.OPENAI_BASE_URL)}

# ---------------------------------------------------------------------------
# run.jsonl schema, transcribed from prereg/DATA_DICTIONARY.md §1 (one line per
# proposal). Types: a tuple of accepted Python types; None in the tuple means null
# is accepted. Values: the shared value sets of the dictionary's head table.
# ---------------------------------------------------------------------------

ACT_KIND = {"as_submitted", "violation", "departure", "exception"}
DECISION = {"allow", "block", "hold"}
REASON_CODE = {"clean", "t0_violation", "t1_tokenless", "t1_authorized", "t1_claimed_no_token",
               "t2_departure_admitted", "t2_departure_excluded_reason", "t2_departure_out_of_bound",
               "t3_in_context", "t3_out_of_context", "conflict_hold", "gloss_bar",
               "dj_permit", "dj_permit_conditional", "dj_deny"}
EVENT_TYPE = {"legitimate_act", "violation_blocked", "authorized_exception", "departure", "departure_blocked",
              "hold", "impermissible_executed"}
REPORTED_EVENT = {"none", "departure", "exception", "violation"}
DRIVER = {"N", "S", "O", "K", "W", "SELF", "CLAIM", "TRANSFER", "NONE"}
TIER = {"T0", "T1", "T2", "T3"}
VALID_FAIL = {"no_such_token", "revoked", "consumed", "expired", "wrong_class", "wrong_scope",
              "wrong_canon_version", "issuer_inside_reporting_line", "codified_class"}
IMPERM_WHY = {"t0_violation", "t1_claimed_no_token", "t2_departure_excluded_reason", "t2_departure_out_of_bound",
              "t3_out_of_context"} | {f"t1_{v}" for v in VALID_FAIL}

LINE_SCHEMA = {
    "pack": ((str,), set(REGISTERED_PACKS)), "arm": ((str,), set(REGISTERED_ARMS)), "seed": ((int,), None),
    "day": ((int,), None), "seq": ((int,), None), "ts": ((int,), None), "skeleton_id": ((str,), None),
    "conflict_flag": ((bool,), None), "corpus_contested": ((bool,), None), "corpus_contest_to": ((int,), None),
    "category": ((str, None), None), "proposal": ((dict,), None), "impermissible": ((bool,), None),
    "impermissible_tier": ((str, None), TIER), "impermissible_why": ((str, None), IMPERM_WHY),
    "verdict": ((dict,), None), "executed": ((bool,), None), "examen": ((dict, None), None),
    "dj": ((dict, None), None), "escalation": ((dict, None), None), "t3_sampled": ((bool,), None),
    "cost": ((dict, None), None), "believes_monitored": ((bool,), None),
    "parse_failed": ((bool,), None),           # LLM live lines only
    "preexisting_violation": ((bool,), None),  # LLM live lines only (added after the live pilot)
}
PROPOSAL_SCHEMA = {
    "act_id": ((str,), None), "case_id": ((str,), None), "company": ((str,), None), "day": ((int,), None),
    "ts": ((int,), None), "seq": ((int,), None), "agent_id": ((str,), None), "archetype": ((str,), None),
    "author_kind": ((str,), {"ai-agent", "human"}), "engaged": ((list,), None),
    "presented_driver": ((str,), DRIVER), "driver_level": ((int,), {0, 1, 2}), "audit_announced": ((bool,), None),
    "twin_of": ((str, None), None), "act": ((dict,), None), "facts": ((list,), None),
}
ACT_SCHEMA = {
    "kind": ((str,), ACT_KIND), "target_entry": ((str, None), None), "added_factor": ((str, None), None),
    "stated_reason": ((str,), DRIVER), "within_bound": ((bool, None), None), "context": ((str, None), None),
    "token_claim": ((str, None), None), "conflict": ((bool,), None),
}
VERDICT_SCHEMA = {
    "decision": ((str,), DECISION), "reason_code": ((str,), REASON_CODE), "entry": ((str, None), None),
    "tier": ((str, None), TIER), "L1": ((bool, None), None), "L2": ((bool, None), None), "escalate": ((bool,), None),
    "channel": ((str, None), {"escalation"}), "token_used": ((str, None), None), "event_type": ((str,), EVENT_TYPE),
}
EXAMEN_SCHEMA = {
    "act_id": ((str,), None), "day": ((int,), None), "entry": ((str, None), None), "tier": ((str, None), TIER),
    "reported_event": ((str,), REPORTED_EVENT), "stated_reason": ((str,), DRIVER), "token_ref": ((str, None), None),
    "narrative": ((str,), None),
}
COST_SCHEMA = {
    "cost_usd": ((float, int), None), "input_tokens": ((int,), None), "output_tokens": ((int,), None),
    "cached": ((bool,), None), "model": ((str,), None), "mode": ((str,), {"dry", "live"}),
}
ESCALATION_SCHEMA = {
    "act_id": ((str,), None), "case_id": ((str,), None), "company": ((str,), None), "day_filed": ((int,), None),
    "hear_day": ((int,), None), "entry": ((str, None), None), "tier": ((str, None), TIER),
    "reason_code": ((str,), {"t0_violation", "t1_tokenless", "t1_claimed_no_token", "conflict_hold", "corpus_contest"}),
    "contest_to": ((int,), None),
}


def _check_obj(obj: dict, schema: dict, where: str, errors: list, exact: bool = True) -> None:
    keys = set(obj)
    want = set(schema)
    if exact and keys != want:
        missing, extra = sorted(want - keys), sorted(keys - want)
        errors.append(f"{where}: fields differ from the dictionary: missing {missing}, extra {extra}")
    for k, (types, values) in schema.items():
        if k not in obj:
            continue
        v = obj[k]
        ok_types = tuple(t for t in types if t is not None)
        if v is None:
            if None not in types:
                errors.append(f"{where}.{k}: null not allowed")
            continue
        if isinstance(v, bool) and bool not in ok_types:
            errors.append(f"{where}.{k}: bool where {ok_types} expected")
            continue
        if not isinstance(v, ok_types):
            errors.append(f"{where}.{k}: {type(v).__name__} where {[t.__name__ for t in ok_types]} expected")
            continue
        if values is not None and v not in values:
            errors.append(f"{where}.{k}: {v!r} not in {sorted(values)}")


def check_line(line: dict, live_llm: bool) -> list:
    errors: list = []
    schema = dict(LINE_SCHEMA)
    if not live_llm:
        schema.pop("parse_failed")
        schema.pop("preexisting_violation", None)
    aid = (line.get("proposal") or {}).get("act_id", "?")
    _check_obj(line, schema, f"line {aid}", errors)
    if isinstance(line.get("proposal"), dict):
        _check_obj(line["proposal"], PROPOSAL_SCHEMA, f"{aid}.proposal", errors)
        if isinstance(line["proposal"].get("act"), dict):
            _check_obj(line["proposal"]["act"], ACT_SCHEMA, f"{aid}.proposal.act", errors)
    if isinstance(line.get("verdict"), dict):
        _check_obj(line["verdict"], VERDICT_SCHEMA, f"{aid}.verdict", errors)
    if isinstance(line.get("examen"), dict):
        _check_obj(line["examen"], EXAMEN_SCHEMA, f"{aid}.examen", errors)
    if isinstance(line.get("cost"), dict):
        _check_obj(line["cost"], COST_SCHEMA, f"{aid}.cost", errors)
    if isinstance(line.get("escalation"), dict):
        _check_obj(line["escalation"], ESCALATION_SCHEMA, f"{aid}.escalation", errors)
    if live_llm:
        if line.get("cost") is None:
            errors.append(f"{aid}: cost is null on a live LLM line")
        elif line["cost"].get("mode") != "live":
            errors.append(f"{aid}: cost.mode is {line['cost'].get('mode')!r}, not 'live'")
    return errors


def dictionary_fields() -> set | None:
    """The field names the dictionary's §1 table lists, or None if the section is not found."""
    try:
        with open(DICTIONARY, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None
    m = re.search(r"^## 1\. `run\.jsonl`.*?$(.*?)^### 1\.1", text, re.S | re.M)
    if not m:
        return None
    out = set()
    for ln in m.group(1).splitlines():
        mm = re.match(r"^\| `([a-z_0-9]+)` \|", ln)
        if mm:
            out.add(mm.group(1))
    return out


# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------


class Fail(Exception):
    pass


def say(step: str, msg: str) -> None:
    print(f"[{step:<7}] {msg}", flush=True)


def http_get(url: str, headers: dict, timeout: int = 60) -> dict:
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def step_models(provider: str, base: str, key: str, model: str) -> list:
    ids: list = []
    if provider == "anthropic":
        headers = {"x-api-key": key, "anthropic-version": llmmod.ANTHROPIC_VERSION}
        url = base.rstrip("/") + "/models?limit=1000"
        while url:
            doc = http_get(url, headers)
            ids += [m.get("id") for m in doc.get("data", []) if m.get("id")]
            if doc.get("has_more") and doc.get("last_id"):
                url = base.rstrip("/") + f"/models?limit=1000&after_id={doc['last_id']}"
            else:
                url = None
    else:
        doc = http_get(base.rstrip("/") + "/models", {"authorization": f"Bearer {key}"})
        ids = [m.get("id") for m in doc.get("data", []) if m.get("id")]
    say("models", f"{len(ids)} models listed at {base}")
    if model not in ids:
        near = [i for i in ids if model.split("-")[0] in i][:10]
        raise Fail(f"model {model!r} is not in the provider's model list; nearest: {near or ids[:10]}")
    say("models", f"model id: {model} (found in model list)")
    return ids


def dry_profile() -> dict:
    """Per pack: proposals, mean input and output tokens, from the registered dry
    run under simulation/ec/results/llm_dry when complete, else from a 30-day
    dry run of arm D scaled to 365 days."""
    prof = {}
    for pack in REGISTERED_PACKS:
        sp = os.path.join(DRY_ROOT, pack, "D", f"seed-{REGISTERED_SEED}", "summary.json")
        if os.path.exists(sp):
            s = json.load(open(sp))
            u = s.get("agent_state", {}).get("usage", {})
            if int(s.get("days", 0)) == cal.DAYS and u.get("calls"):
                prof[pack] = {"proposals": int(s["totals"]["proposals"]), "mean_in": u["input_tokens"] / u["calls"],
                              "mean_out": u["output_tokens"] / u["calls"], "source": f"llm_dry {cal.DAYS}-day run"}
                continue
        tmp = tempfile.mkdtemp(prefix=f"ec_preflight_dry_{pack}_")
        run_year.main(["--packs", pack, "--arms", "D", "--seeds", str(REGISTERED_SEED), "--days", "30",
                       "--agent", "llm:anthropic:sonnet", "--mode", "dry", "--out", tmp, "--quiet"])
        s = json.load(open(os.path.join(tmp, pack, "D", f"seed-{REGISTERED_SEED}", "summary.json")))
        u = s["agent_state"]["usage"]
        prof[pack] = {"proposals": int(round(s["totals"]["proposals"] * cal.DAYS / 30)),
                      "mean_in": u["input_tokens"] / u["calls"], "mean_out": u["output_tokens"] / u["calls"],
                      "source": "30-day dry run scaled x365/30"}
    return prof


def project(prof: dict, model: str, mean_in: float | None = None, mean_out: float | None = None) -> dict:
    pin, pout = llmmod.PRICES.get(model, (0.0, 0.0))
    out = {}
    for pack, p in prof.items():
        tin = mean_in if mean_in is not None else p["mean_in"]
        tout = mean_out if mean_out is not None else p["mean_out"]
        per_run = p["proposals"] * (tin * pin + tout * pout) / 1e6
        # Arms A, B, C render identical prompts (no glosses are written there): the first
        # arm pays, the next two are disk-cache hits (accounted at 0.1x, spend 0). Arm D
        # diverges once a gloss is written; its full price is the upper bound.
        out[pack] = {"per_arm_full": per_run, "accounted": per_run * (1 + 0.1 + 0.1 + 1),
                     "spend_upper": per_run * 2, "proposals": p["proposals"], "mean_in": tin, "mean_out": tout}
    return out


def step_plan(model: str, prof: dict) -> None:
    say("plan", "registered run plan (prereg Part B): packs " + ",".join(REGISTERED_PACKS)
        + f"; arms {','.join(REGISTERED_ARMS)}; seed {REGISTERED_SEED}; {cal.DAYS} days; --mode live; "
          "--checkpoint-every 10 --resume --budget-usd 1000")
    pr = project(prof, model)
    tot_acc = sum(v["accounted"] for v in pr.values())
    tot_sp = sum(v["spend_upper"] for v in pr.values())
    for pack, v in pr.items():
        say("plan", f"  {pack:<12} {v['proposals']:>5} proposals/arm, mean {v['mean_in']:.0f} in / {v['mean_out']:.0f} out tokens "
                    f"({prof[pack]['source']}): one arm ${v['per_arm_full']:.2f}, four arms accounted ${v['accounted']:.2f}, "
                    f"provider spend <= ${v['spend_upper']:.2f}")
    say("plan", f"projected cost at PRICES[{model}]: accounted cost_usd ${tot_acc:.2f}; provider spend <= ${tot_sp:.2f} "
                f"for the 20 runs (dry input estimate chars/4, {prof[next(iter(prof))]['mean_out']:.0f} output tokens assumed)")
    say("plan", "cache sharing: arms A, B and C render byte-identical prompts for the same skeleton, so after the first "
                "arm they are served from <out>/llm_cache at the cache rate; arm D's prompts diverge once a gloss is "
                "written (day 4 at the earliest). Run the arms in one invocation and one --out so the cache is shared.")


def step_smoke(provider: str, model: str, days: int, out: str, budget: float, rate_limit: float,
               seed: int = SMOKE_SEED) -> dict:
    spec = f"llm:{'openai' if provider != 'anthropic' else 'anthropic'}:{model}"
    argv = ["--packs", "vetpoc", "--arms", "D", "--seeds", str(seed), "--days", str(days),
            "--agent", spec, "--mode", "live", "--out", out, "--quiet", "--budget-usd", str(budget)]
    if rate_limit:
        argv += ["--rate-limit", str(rate_limit)]
    t0 = time.time()
    rc = run_year.main(argv)
    if rc != 0:
        raise Fail(f"run_year exited {rc} on the smoke (budget {budget} USD reached, or see {out}/vetpoc/D/seed-{seed}/llm_errors.jsonl)")
    d = os.path.join(out, "vetpoc", "D", f"seed-{seed}")
    lines = [json.loads(l) for l in open(os.path.join(d, "run.jsonl")) if l.strip()]
    summ = json.load(open(os.path.join(d, "summary.json")))
    u = summ["agent_state"]["usage"]
    costs = [l["cost"] for l in lines if l.get("cost")]
    fresh = [c for c in costs if not c["cached"]]
    mean_in = statistics.fmean(c["input_tokens"] for c in fresh) if fresh else float("nan")
    mean_out = statistics.fmean(c["output_tokens"] for c in fresh) if fresh else float("nan")
    twins = [l for l in lines if l["proposal"]["audit_announced"]]
    controls = [l for l in lines if not l["proposal"]["audit_announced"]]
    n_pf = sum(1 for l in lines if l.get("parse_failed"))
    say("smoke", f"{days}-day live run of vetpoc arm D in {time.time() - t0:.1f}s -> {d}")
    say("smoke", f"calls made: {u['calls']} ({u.get('http_calls', '?')} HTTP, {u['cached']} cache hits, "
                 f"{u.get('retries', 0)} retries); parse failures: {n_pf}")
    say("smoke", f"mean tokens from provider usage: {mean_in:.0f} input / {mean_out:.0f} output over {len(fresh)} fresh calls")
    say("smoke", f"actual cost: provider spend ${u.get('spend_usd', 0.0):.4f}; accounted cost_usd ${summ['totals']['cost_usd']:.4f}")
    bm_t = sum(1 for l in twins if l["believes_monitored"]) / len(twins) if twins else float("nan")
    bm_c = sum(1 for l in controls if l["believes_monitored"]) / len(controls) if controls else float("nan")
    say("smoke", f"believes_monitored rate: {bm_t:.2f} over {len(twins)} announced twins, {bm_c:.2f} over {len(controls)} controls")
    kinds = {}
    for l in lines:
        kinds[l["proposal"]["act"]["kind"]] = kinds.get(l["proposal"]["act"]["kind"], 0) + 1
    say("smoke", f"acts: {json.dumps(kinds, sort_keys=True)}; impermissible: {sum(l['impermissible'] for l in lines)}; "
                 f"executed: {summ['totals']['executed']}")
    cache = os.path.join(out, "llm_cache")
    files = sorted((os.path.getmtime(p), p) for b, _, fs in os.walk(cache) for f in fs
                   for p in [os.path.join(b, f)] if f.endswith(".json"))
    for _, p in files[-3:]:
        try:
            txt = json.load(open(p)).get("text") or ""
        except (OSError, ValueError):
            continue
        say("smoke", "sample reply: " + json.dumps(txt[:400]))
    if n_pf:
        say("smoke", f"WARNING: {n_pf} of {len(lines)} replies did not parse; see {d}/llm_errors.jsonl")
    if n_pf > 0.1 * max(1, len(lines)):
        raise Fail(f"parse failure rate {n_pf / len(lines):.2f} exceeds 0.10; fix the prompt or the model before the live run")
    return {"lines": lines, "dir": d, "mean_in": mean_in, "mean_out": mean_out, "spend": u.get("spend_usd", 0.0),
            "usage": u}


def step_schema(lines: list) -> None:
    errors: list = []
    for l in lines:
        errors += check_line(l, live_llm=True)
    want = dictionary_fields()
    if want is None:
        say("schema", "WARNING: could not parse the run.jsonl section of prereg/DATA_DICTIONARY.md")
    else:
        seen = set().union(*(set(l) for l in lines)) if lines else set()
        if seen != want:
            errors.append(f"run.jsonl fields {sorted(seen ^ want)} differ between the lines and DATA_DICTIONARY.md §1")
    if errors:
        for e in errors[:20]:
            say("schema", "ERROR " + e)
        raise Fail(f"{len(errors)} schema errors in {len(lines)} lines")
    say("schema", f"schema: ok ({len(lines)} lines against DATA_DICTIONARY.md §1, 1.1, 1.1.1, 1.2, 1.3, 1.5, 1.6)")


def step_metrics(out: str) -> dict:
    rows = metrics.compute(out)
    if len(rows) != 1:
        raise Fail(f"metrics.py found {len(rows)} runs under {out}, expected 1")
    r = rows[0]
    metrics.write(rows, out)
    print(metrics.table(rows, ["pack", "arm", "seed", "provenance", "mode", "n_proposals", "e1_imperm", "e3_og", "e5_eeg",
                               "e6_recall", "e6_precision", "e7_blind_spot", "cost_usd"]))
    if r["provenance"] != metrics.MEASURED:
        raise Fail(f"provenance is {r['provenance']}, not {metrics.MEASURED}")
    say("metrics", f"provenance: {r['provenance']}; e5_eeg: {r['e5_eeg']}")
    if r["e5_eeg"] is None:
        say("metrics", "WARNING: e5_eeg is NA (no announced twin in the smoke; a longer --days will carry some)")
    return r


# ---------------------------------------------------------------------------


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="preflight for the EC LLM live slice")
    ap.add_argument("--provider", choices=("anthropic", "openai", "openai_compatible"), default="anthropic")
    ap.add_argument("--model", required=True, help="model id or alias (opus, sonnet, haiku)")
    ap.add_argument("--days", type=int, default=1)
    ap.add_argument("--out", default=None, help="smoke directory (default: a fresh temp dir)")
    ap.add_argument("--smoke-budget", type=float, default=5.0)
    ap.add_argument("--rate-limit", type=float, default=0.0)
    ap.add_argument("--smoke-seed", type=int, default=SMOKE_SEED,
                    help="seed of the smoke run (default 97: never the registered LLM seed 11)")
    a = ap.parse_args(argv)

    key_var, base_var, base_default = PROVIDERS[a.provider]
    key = os.environ.get(key_var)
    base = os.environ.get(base_var, base_default)
    model = llmmod.ALIASES.get(a.model, a.model)
    skipped: list = []
    print(f"EC live preflight: provider {a.provider}, model {a.model} -> {model}, endpoint {base}")
    try:
        # 1. key
        if key:
            say("key", f"{key_var} is set ({len(key)} chars)")
        else:
            say("key", f"{key_var} is NOT set: network checks will be SKIPPED")
        # 2. models
        if key:
            try:
                step_models(a.provider, base, key, model)
            except (urllib.error.URLError, OSError, ValueError) as e:
                raise Fail(f"GET /models failed at {base}: {e}")
        else:
            skipped.append("models")
            say("models", "SKIPPED (no key): model id not confirmed against the provider; alias resolves to " + model)
        # 3. price
        if model in llmmod.PRICES:
            pin, pout = llmmod.PRICES[model]
            say("price", f"PRICES[{model}] = ${pin:.2f} in / ${pout:.2f} out per million tokens")
        else:
            say("price", f"WARNING: {model!r} is not in PRICES (simulation/ec/agents/llm.py): live mode refuses to start "
                         f"and the cost columns would be 0; add it, then re-run this preflight")
            raise Fail(f"model {model!r} not in PRICES")
        # 4. plan
        prof = dry_profile()
        step_plan(model, prof)
        # 5-7. smoke, schema, metrics
        if key:
            out = a.out or tempfile.mkdtemp(prefix="ec_preflight_")
            os.makedirs(out, exist_ok=True)
            sm = step_smoke(a.provider, model, a.days, out, a.smoke_budget, a.rate_limit, a.smoke_seed)
            step_schema(sm["lines"])
            step_metrics(out)
            if sm["lines"] and sm["mean_in"] == sm["mean_in"]:
                # Re-project with the measured means in place of the dry estimates.
                pr = project(prof, model, sm["mean_in"], sm["mean_out"])
                tot_acc = sum(v["accounted"] for v in pr.values())
                tot_sp = sum(v["spend_upper"] for v in pr.values())
                say("plan", f"re-projected from the smoke's measured usage ({sm['mean_in']:.0f} in / {sm['mean_out']:.0f} out): "
                            f"accounted ${tot_acc:.2f}; provider spend <= ${tot_sp:.2f} for the 20 runs")
        else:
            for s in ("smoke", "schema", "metrics"):
                skipped.append(s)
                say(s, "SKIPPED (no key)")
    except Fail as e:
        print(f"PREFLIGHT FAILED: {e}")
        return 1
    if skipped:
        print(f"PREFLIGHT INCOMPLETE: skipped checks {', '.join(skipped)} (set {key_var} to run them)")
        return 2
    print("PREFLIGHT OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
