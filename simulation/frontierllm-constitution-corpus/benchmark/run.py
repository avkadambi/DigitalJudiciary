"""Run the benchmark.

    python3 benchmark/run.py --cases 500 --runs 1 --k 1 --mode oracle
    python3 benchmark/run.py --cases 5000 --runs 3 --k 8 --mode dry --models opus,sonnet,haiku
    python3 benchmark/run.py --cases 500 --arms A,B --models sonnet --mode live --k 3

Modes: oracle (deterministic, offline), dry (cost projection only), live (API).
Live mode needs ANTHROPIC_API_KEY and will refuse to start without one.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))

def _portable_config(a):
    """argparse namespace as a dict, with filesystem paths made relative to the pack.

    Result files are shipped; they must not carry the build machine's directory layout."""
    cfg = dict(vars(a))
    for k, v in list(cfg.items()):
        if isinstance(v, str) and os.path.isabs(v):
            try:
                cfg[k] = os.path.relpath(v, os.path.dirname(HERE))
            except ValueError:
                pass
    return cfg

ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import engine   # noqa: E402
import config   # noqa: E402
import stream as streammod   # noqa: E402
import arms as armsmod       # noqa: E402
import judge as judgemod     # noqa: E402
import score as scoremod     # noqa: E402


def reference_run(built):
    """The executed reference trace, and the store as it grows.

    Every arm is scored against the SAME store trajectory, so no arm is
    advantaged by having seen a different case base. The store is grown by the
    reference engine because that is the only definition of the case base the
    architecture has; what an arm is SHOWN out of it is the manipulation.
    """
    out = engine.replay(built["stream"], built["seed_store"],
                        built["provisions"], built["theta"])
    return {t["case"]: t for t in out["traces"]}, out


def _wrap(text, indent, width):
    import textwrap
    return textwrap.wrap(text, width=width, initial_indent=" " * indent,
                         subsequent_indent=" " * (indent + 2)) or [" " * indent + text]


def discriminating_report(built, ref_traces, results, answers_by_arm,
                          reader="naive", mode="oracle"):
    """One row per scenario family, one column per arm, tier-ordered.

    Two things are reported, because two things differ. The disposition is what
    the arm answered. The route is how it got there — and a family can agree on
    the answer while disagreeing on everything that matters about it, which is
    S2: the architecture sees two decisions that tie and escalates; a reader
    that takes the newest record as current gets the same word without ever
    noticing the older one was never superseded.
    """
    import collections
    by_scn = collections.OrderedDict()
    for c in built["stream"]:
        m = c["meta"]
        by_scn.setdefault(m["scenario_id"], {"tier": m["tier"], "cases": [],
                                             "expected": m["dj_expected"],
                                             "trap": m["monolith_trap"],
                                             "title": m.get("title", ""),
                                             "why": m.get("why", ""),
                                             "hook": m.get("pact_hook", "")})
        by_scn[m["scenario_id"]]["cases"].append(c["id"])

    arms_seen = [k[1] for k in answers_by_arm]
    seen, arm_cols = set(), []
    for x in arms_seen:
        if x not in seen:
            seen.add(x); arm_cols.append(x)
    ref_col = "B" if "B" in arm_cols else arm_cols[0]

    def cell(col, case_id):
        key = next(k for k in answers_by_arm if k[1] == col)
        a0 = (answers_by_arm[key].get(case_id) or [{}])[0]
        return a0

    w = "{:<36}{:<11}" + "{:<20}" * len(arm_cols) + "{}"
    lines = [w.format("scenario", "tier", *arm_cols, "diverges from " + ref_col),
             "-" * (48 + 20 * len(arm_cols) + 16)]
    diverging = 0
    for tier in ("structural", "measured", "adverse"):
        for sid, d in by_scn.items():
            if d["tier"] != tier:
                continue
            rep = d["cases"][0]
            base = cell(ref_col, rep).get("disposition")
            row, off = [sid, tier], []
            for col in arm_cols:
                a0 = cell(col, rep)
                dd = a0.get("disposition") or "(docketed)"
                if len(d["cases"]) > 1:
                    dd += f" (x{len(d['cases'])})"
                row.append(dd)
                if col != ref_col and a0.get("disposition") != base:
                    off.append(col)
            if off:
                diverging += 1
            lines.append(w.format(*row, ", ".join(off) if off else "—"))

    lines.append("")
    lines.append(f"{diverging} of {len(by_scn)} families answer differently under {ref_col} "
                 f"than under at least one other arm.")
    lines.append("")
    lines.append("How each family was reached, arm by arm (the answer is not the whole of it —")
    lines.append("S2 is a family where the words agree and the reasoning does not):")
    lines.append("")
    for tier in ("structural", "measured", "adverse"):
        for sid, d in by_scn.items():
            if d["tier"] != tier:
                continue
            rep = d["cases"][0]
            lines.append(f"  {sid}  [{tier}]  {d['title']}")
            for line in _wrap("PACT: " + d["hook"], 6, 92):
                lines.append(line)
            for col in arm_cols:
                a0 = cell(col, rep)
                calls = sum(1 for cid in d["cases"]
                            if (cell(col, cid) or {}).get("called_model"))
                tail = (f"   [{calls}/{len(d['cases'])} arrivals cost a model call]"
                        if len(d["cases"]) > 1 else "")
                lines.append(f"      {col:<6} {str(a0.get('disposition') or '(docketed)'):<20}"
                             f"{a0.get('route', '—')}{tail}")
            for line in _wrap("trap: " + d["trap"], 6, 92):
                lines.append(line)
            exp, b0 = d["expected"], cell(ref_col, rep)
            if exp is None:
                verdict = "no single disposition is expected: the representative decides " \
                          "and the members are disposed by citation"
            elif exp == "none_tie":
                ok = str(b0.get("route", "")).startswith("tie")
                verdict = ("architecture expected to find a TIE and refer: "
                           + ("met" if ok else "NOT met"))
            else:
                ok = b0.get("disposition") == exp
                verdict = f"architecture expected to answer {exp}: " + ("met" if ok else "NOT met")
            for line in _wrap(verdict, 6, 92):
                lines.append(line)
            lines.append("")

    lines.append("structural = the monolith cannot get this right in principle; the information")
    lines.append("             it would need is state, and no larger context window supplies it")
    lines.append("measured   = it could; PACT measures that it frequently does not")
    lines.append("adverse    = the architecture does no better, or worse — reported for the same")
    lines.append("             reason as the rest")
    lines.append("")
    if mode == "oracle" and reader == "perfect":
        lines.append("Reader: perfect. Every arm is answered by a reasoner that applies the gate")
        lines.append("and the ordering itself, so the arms agree by construction and the")
        lines.append("disposition column shows nothing. Re-run with --oracle-reader naive, or")
        lines.append("--mode live. The route block above is still informative.")
    elif mode == "oracle":
        lines.append("Reader: naive. Arm B is decided by the engine; the arms nothing binds are")
        lines.append("read by a stand-in for three measured PACT behaviours. This is a lower")
        lines.append("bound on the arm and is not evidence about any model — --mode live is.")
    else:
        lines.append("Reader: live models. Each cell is one model's answer on the first case of")
        lines.append("the family; k>1 attempts are summarised in the scored results file.")
    return "\n".join(lines)


def preflight(a):
    """Say where the key came from, then prove it works with one small call."""
    src = judgemod.key_source()
    if not src:
        print(judgemod.NO_KEY_MESSAGE)
        return 1
    print(f"key found in: {src}")
    model = config.ALIASES.get(a.models.split(",")[0].strip(), a.models.split(",")[0].strip())
    print(f"testing {model} with one short call ...")
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=judgemod.find_api_key())
        r = client.messages.create(
            model=model, max_tokens=16,
            messages=[{"role": "user", "content": "Reply with the single word: ready"}])
        txt = r.content[0].text.strip() if r.content else ""
        pin, pout = config.PRICES[model]
        spent = (r.usage.input_tokens*pin + r.usage.output_tokens*pout)/1e6
        print(f"  reply: {txt!r}")
        print(f"  tokens: {r.usage.input_tokens} in, {r.usage.output_tokens} out  "
              f"(${spent:.6f})")
        print("\nthe key works. Price the run you want before you start it:")
        print("  python3 benchmark/run.py --cases 500 --k 3 --mode dry --models sonnet")
        return 0
    except Exception as e:
        print(f"  FAILED: {type(e).__name__}: {e}")
        print("\nCommon causes: the key is revoked or mistyped; the account has no "
              "credit; the model id is not enabled for this account.")
        return 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Digital Judiciary benchmark")
    ap.add_argument("--cases", type=int, default=config.DEFAULTS["cases"],
                    help="X — total changes. The 6,000-case corpus is always "
                         "included first; the remainder is a random overlay.")
    ap.add_argument("--runs", type=int, default=config.DEFAULTS["runs"], help="Y — independent runs")
    ap.add_argument("--k", type=int, default=config.DEFAULTS["k"],
                    help="attempts per case (Chapter 6 uses 8 for pass^8)")
    ap.add_argument("--arms", default=",".join(config.DEFAULTS["arms"]))
    ap.add_argument("--models", default=",".join(config.DEFAULTS["models"]))
    ap.add_argument("--mode", choices=("oracle", "dry", "live"), default=config.DEFAULTS["mode"])
    ap.add_argument("--no-batch", action="store_true", help="price without the 50%% batch discount")
    ap.add_argument("--no-cache", action="store_true", help="price without prompt caching")
    ap.add_argument("--seed", type=int, default=config.DEFAULTS["seed"])
    ap.add_argument("--p-violate", type=float, default=0.18)
    ap.add_argument("--p-contest", type=float, default=0.08)
    ap.add_argument("--p-clean", type=float, default=0.25)
    ap.add_argument("--discriminating", action="store_true",
                    help="run only the discriminating scenario suite: eight families, "
                         "built from what PACT cannot pose because it has no store. "
                         "Five structural, two measured, one the architecture loses.")
    ap.add_argument("--justify", type=int, default=0,
                    help="attach author justifications: N twin items (N/2 pairs) "
                         "in which the same change is filed twice, once with a "
                         "plain note and once with a note that claims "
                         "compliance, admits the breach, or says truthfully of a "
                         "clean change what the first says falsely of a dirty "
                         "one. Scores the disclosure axis.")
    ap.add_argument("--guard", type=int, default=0,
                    help="add N non-binding guard items: the change reads like a "
                         "violation and the facts do not trigger it. Measures "
                         "rule-scope discernment, PACT's sixth axis.")
    ap.add_argument("--oracle-reader", choices=("perfect", "naive"), default=None,
                    help="who reads the records for the non-binding arms in oracle "
                         "mode. 'perfect' applies the gate and the ordering itself, "
                         "which hands every arm the architecture's work and makes "
                         "them agree; 'naive' substitutes the three behaviours PACT "
                         "measures (recency for supersession, clearance at face "
                         "value, similarity for premise containment). Defaults to "
                         "naive under --discriminating, perfect otherwise. Neither "
                         "is evidence about a model.")
    ap.add_argument("--realism", choices=("native", "stripped", "announced"),
                    default="native",
                    help="native strips the corpus's own test scaffolding from what "
                         "the arm sees; the other two reproduce PACT's Appendix L "
                         "probe so the evaluation-awareness effect can be measured "
                         "on this corpus rather than assumed from theirs.")
    ap.add_argument("--human", action="store_true",
                    help="add arm C: a priced human review desk that reads every "
                         "arrival against the rulebook with no case base. Estimation-"
                         "only: no decisions, no model calls; every input is a stated "
                         "⟦PROJECTED⟧ parameter in benchmark/human.py.")
    ap.add_argument("--out", default=os.path.join(ROOT, "benchmark", "results"))
    ap.add_argument("--check", action="store_true",
                    help="preflight: report where the key was found and make one "
                         "cheap call to prove it works, then stop. Costs a fraction "
                         "of a cent and spends nothing else.")
    a = ap.parse_args(argv)

    if a.check:
        return preflight(a)

    arm_names = [x.strip() for x in a.arms.split(",") if x.strip()]
    for n in arm_names:
        if n not in config.ARMS:
            raise SystemExit(f"unknown arm {n!r}; known: {sorted(config.ARMS)}")
    models = [config.ALIASES.get(m.strip(), m.strip()) for m in a.models.split(",") if m.strip()]

    reader = a.oracle_reader or ("naive" if a.discriminating else "perfect")

    if a.discriminating:
        import discriminating as disc
        rb0 = json.load(open(os.path.join(ROOT, "constitution", "rulebook.json")))
        params0 = json.load(open(os.path.join(ROOT, "constitution", "parameters.json")))
        prov0 = {p["id"]: engine.Provision.from_dict(p) for p in rb0["provisions"]}
        engine.load_roster(os.path.join(ROOT, "constitution", "organizations.json"))
        seeds, scn = disc.build(prov0, rb0)
        built = {"stream": scn, "corpus_n": 0, "random_n": 0, "guard_n": 0,
                 "provisions": prov0, "seed_store": [r.to_dict() for r in seeds],
                 "theta": params0["theta"], "rulebook": rb0,
                 "arrival_model": {"suite": "discriminating"}}
    else:
        built = streammod.build(a.cases, a.seed, a.p_violate, a.p_contest, a.p_clean,
                                guard=a.guard, justify=a.justify)
    ref_traces, ref_out = reference_run(built)
    pack_header = json.load(open(os.path.join(ROOT, "corpus", "cases.json")))
    pack_header = {k: v for k, v in pack_header.items() if k != "cases"}
    rulebook = built["rulebook"]

    print(f"stream: {len(built['stream']):,} changes "
          f"({built['corpus_n']:,} stratified corpus + {built['random_n']:,} random overlay"
          + (f" + {built['guard_n']:,} non-binding guard items" if built.get('guard_n') else "")
          + (f" + {built['justify_n']:,} justification twins" if built.get('justify_n') else "")
          + f"); realism={a.realism}")
    print(f"arrival model for the overlay: {built['arrival_model']}")
    print(f"arms: {', '.join(arm_names)}   models: {', '.join(models)}   "
          f"runs: {a.runs}   attempts/case: {a.k}   mode: {a.mode}")
    if a.mode == "oracle" and reader == "perfect":
        print("NOTE  oracle mode answers as a perfect reader of what each arm was\n"
              "      shown. It is an upper bound on the arm, not a prediction about\n"
              "      any model. Use it to exercise the harness, never to make a claim.")
    elif a.mode == "oracle":
        print("NOTE  oracle mode, naive reader: arm B is decided by the engine; the\n"
              "      arms nothing binds are read by a stand-in for the three\n"
              "      behaviours PACT measures (recency for supersession, clearance\n"
              "      at face value, similarity for containment). A lower bound on\n"
              "      the arm, not a prediction about any model. --mode live settles it.")
    print()

    all_results = []
    answers_by_arm = {}
    t0 = time.time()
    for model in models:
        for arm_name in arm_names:
            arm = config.ARMS[arm_name]
            j = judgemod.Judge(model, mode=a.mode, batch=not a.no_batch,
                               cache=not a.no_cache, realism=a.realism,
                               oracle_reader=reader)
            answers, no_call, total = {}, 0, 0
            # Dry mode is pure accounting: one pass over the stream, scaled by
            # runs x attempts. Simulating 120,000 identical arrivals to add up
            # the same token counts is only a way of spending an afternoon.
            eff_runs, eff_k, scale = (1, 1, a.runs * a.k) if a.mode == "dry" else (a.runs, a.k, 1)
            for run_i in range(eff_runs):
                # the store trajectory, replayed identically for every arm
                store = [engine.Record.from_dict(r) if isinstance(r, dict) else r
                         for r in built["seed_store"]]
                for case in built["stream"]:
                    atts = answers.setdefault(case["id"], [])
                    for _ in range(eff_k):
                        ans, called = armsmod.decide(
                            arm_name, arm, case, store, built["provisions"],
                            built["theta"], j, rulebook)
                        total += 1
                        no_call += (0 if called else 1)
                        if ans is not None:
                            ans["called_model"] = called
                            atts.append(ans)
                    t = ref_traces.get(case["id"])
                    if t and t.get("admitted"):
                        store.append(engine._record_from(
                            engine.case_from_dict(case), t, built["provisions"]))
            if scale != 1:
                j.usage.input *= scale; j.usage.cached *= scale
                j.usage.output *= scale; j.usage.calls *= scale
                no_call *= scale; total *= scale
            s = (scoremod.score_arm(arm_name, answers, built["stream"], pack_header,
                                    ref_traces, built["provisions"], a.k)
                 if a.mode != "dry" else None)
            answers_by_arm[(model, arm_name)] = answers
            all_results.append({
                "arm": arm_name, "model": model,
                "label": arm["label"], "note": arm["note"],
                "usage": j.usage.as_dict(model, batch=not a.no_batch),
                "no_call_fraction": no_call / total if total else 0.0,
                "arrivals_scored": total,
                "score": s,
            })
            u = j.usage
            print(f"  {model:20} {arm_name:6} calls {u.calls:>8,}  "
                  f"no-call {100*(no_call/total if total else 0):5.1f}%  "
                  f"${u.cost(model, batch=not a.no_batch):>10,.2f}")

    if a.human:
        import human as humanmod
        est = humanmod.estimate(built["stream"], ref_traces, built["provisions"])
        all_results.append(est)
        print(humanmod.summarise(est))

    os.makedirs(a.out, exist_ok=True)
    tag = f"{a.mode}-x{a.cases}-y{a.runs}-k{a.k}"
    path = os.path.join(a.out, f"benchmark-{tag}.json")
    json.dump({
        "config": _portable_config(a), "stream": {"total": len(built["stream"]),
                                      "corpus": built["corpus_n"],
                                      "random": built["random_n"],
                                      "guard": built.get("guard_n", 0),
                                      "justify": built.get("justify_n", 0),
                                      "arrival_model": built["arrival_model"]},
        "prices_per_mtok": config.PRICES,
        "elapsed_s": round(time.time() - t0, 1),
        "results": all_results,
    }, open(path, "w"), indent=2)

    if a.discriminating and a.mode != "dry":
        print()
        print(discriminating_report(built, ref_traces, all_results, answers_by_arm,
                                    reader=reader, mode=a.mode))
    elif a.mode != "dry":
        print()
        print(scoremod.summarise(all_results))
        print()
        print("consist. = like-case pairs agreeing (no ground truth needed) — the primary endpoint")
        print("scope    = guard items correctly permitted; denying one is over-application")
        print("disclos. = justification twins holding their control's answer — the same change,")
        print("           filed twice with different author notes. An identity for arm B, which")
        print("           reads factors and never the note; a measurement for every other arm")
        print("transp.  = permitted violations the arm disclosed as violations (the ARM's own")
        print("           account; silence and misrepresentation are split in the results file)")
        print("floors   = absolute provisions upheld;  pressure = twins holding their control's answer")
        print("interp.acc = agreement with the reference engine on cases where no record")
        print("           controls — the only cross-arm accuracy figure that is not circular")
        print("falsebind = the binding gate (5.11.0): citations of a record that does not govern,")
        print("           or of the wrong record, over all citations, with the exact 95% upper")
        print("           bound; a dash means the arm never cited a controlling record")
    total_cost = sum(r["usage"]["cost_usd"] for r in all_results if "usage" in r)
    print(f"\ntotal measured cost: ${total_cost:,.2f}    results: {os.path.relpath(path, os.path.dirname(os.path.dirname(os.path.dirname(HERE))))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
