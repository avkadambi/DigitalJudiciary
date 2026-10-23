"""
The dollar projection for an LLM-governed study (governance build v3, §6, H4).

    python3 simulation/ec/run_year.py ... --mode dry --project --roles-config <file>

reads the dry run it just wrote (measured token counts, chars/4, per role and per
level; the routing the dry stand-ins produced at `--dry-error-rate`) and prints:

  * USD per seat and per level for one company-year (arms C and D, each as a
    shadow-and-binding pair), and for the registered set (five companies);
  * L3 reasoning tokens at their upper bound (max_tokens minus visible output);
  * two agent lines, with and without the v1 cache (the shadow run of a pair
    replays the v1 agent calls from cache);
  * the L4 estimate, items per company-month by origin;
  * the routing shares with the EC-21 warnings.

Every figure is an estimate from a dry run and is labelled so.
"""

from __future__ import annotations

import json
import os

from . import calendar as cal

PACKS_IN_SET = 5
EC21_L2_MAX, EC21_L3_MAX, EC21_KAPPA_MAX, EC21_KAPPA_MIN_PANELS = 0.35, 0.08, 0.95, 50


def _runs(root: str) -> list:
    out = []
    for base, _dirs, files in os.walk(root):
        if "manifest.json" in files and "run.jsonl" in files:
            out.append(base)
    return sorted(out)


def _load(path: str):
    with open(path) as fh:
        return json.load(fh)


def _price(desc: dict) -> tuple:
    p = desc.get("price_per_mtok") or [0.0, 0.0]
    return float(p[0]), float(p[1])


def fleiss_kappa(votes: list):
    """Fleiss' kappa over panels; each item is the list of the seats' holdings."""
    items = [v for v in votes if v and len(v) >= 2]
    if not items:
        return None
    n = len(items[0])
    items = [v for v in items if len(v) == n]
    cats = sorted({x for v in items for x in v})
    if len(cats) < 2:
        return 1.0
    N = len(items)
    p_j = {c: sum(v.count(c) for v in items) / (N * n) for c in cats}
    P_i = [(sum(v.count(c) ** 2 for c in cats) - n) / (n * (n - 1)) for v in items]
    P_bar = sum(P_i) / N
    P_e = sum(p * p for p in p_j.values())
    if P_e >= 1.0:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def ec21_warnings(level_shares: dict, kappa, n_panels: int) -> list:
    w = []
    if (level_shares.get("L2+") or 0.0) > EC21_L2_MAX:
        w.append(f"EC-21: {level_shares['L2+']:.1%} of hearings reach L2 or above (warn above {EC21_L2_MAX:.0%})")
    if (level_shares.get("L3+") or 0.0) > EC21_L3_MAX:
        w.append(f"EC-21: {level_shares['L3+']:.1%} of hearings reach L3 or above (warn above {EC21_L3_MAX:.0%})")
    if kappa is not None and n_panels >= EC21_KAPPA_MIN_PANELS and kappa > EC21_KAPPA_MAX:
        w.append(f"EC-21: panel Fleiss kappa {kappa:.3f} over {n_panels} panels (warn above {EC21_KAPPA_MAX})")
    return w


def summarise(root: str) -> dict:
    """Per-role token counts and dollars, routing shares and L4 items from a dry run tree."""
    roles: dict = {}
    agent = {"input_tokens": 0, "output_tokens": 0, "calls": 0, "cost_usd": 0.0}
    hearings, levels, l4_items, panels, votes = 0, {"L1": 0, "L2": 0, "L3": 0, "L4": 0}, {}, 0, []
    company_days = 0
    n_runs = 0
    for d in _runs(root):
        man = _load(os.path.join(d, "manifest.json"))
        g = man.get("governance")
        if not g:
            continue
        n_runs += 1
        company_days += int(man.get("days") or 0)
        seats = g.get("seats") or {}
        flat = {}
        for r, desc in seats.items():
            if isinstance(desc, dict) and "seats" in desc:
                for i, sd in enumerate(desc["seats"]):
                    flat[f"dj_l2#{i + 1}"] = sd
            else:
                flat[r] = desc
        for role, u in (g.get("usage_by_role") or {}).items():
            desc = flat.get(role, {})
            pin, pout = _price(desc)
            row = roles.setdefault(role, {"model": desc.get("model"), "calls": 0, "input_tokens": 0,
                                          "output_tokens": 0, "usd": 0.0, "max_tokens": desc.get("max_tokens"),
                                          "reasoning": desc.get("reasoning")})
            row["calls"] += int(u.get("calls", 0))
            row["input_tokens"] += int(u.get("input_tokens", 0))
            row["output_tokens"] += int(u.get("output_tokens", 0))
            out_t = int(u.get("output_tokens", 0))
            if desc.get("reasoning") and desc.get("max_tokens"):
                # upper bound on thinking: max_tokens minus visible output, per call
                out_t = max(out_t, int(desc["max_tokens"]) * int(u.get("calls", 0)))
            row["usd"] += (int(u.get("input_tokens", 0)) * pin + out_t * pout) / 1e6
        summ = _load(os.path.join(d, "summary.json"))
        au = ((summ.get("agent_state") or {}).get("usage") or {})
        agent["input_tokens"] += int(au.get("input_tokens", 0))
        agent["output_tokens"] += int(au.get("output_tokens", 0))
        agent["calls"] += int(au.get("calls", 0))
        agent["cost_usd"] += float(au.get("cost_usd", 0.0))
        bl = _load(os.path.join(d, "bench_log.json"))
        for h in bl.get("hearings", []):
            if "final_level" not in h:
                continue
            hearings += 1
            lv = int(h.get("final_level") or 1)
            levels["L1"] += 1
            for k in range(2, lv + 1):
                levels[f"L{k}"] += 1
            l2 = (h.get("ladder") or {}).get("L2")
            if l2 and l2.get("votes"):
                panels += 1
                votes.append(list(l2["votes"]))
            if h.get("l4"):
                origin = h["l4"].get("origin", "other")
                l4_items[origin] = l4_items.get(origin, 0) + 1
    shares = {"L2+": (levels["L2"] / hearings) if hearings else None,
              "L3+": (levels["L3"] / hearings) if hearings else None,
              "L4": (levels["L4"] / hearings) if hearings else None}
    kappa = fleiss_kappa(votes) if votes else None
    return {"runs": n_runs, "company_days": company_days, "roles": roles, "agent": agent, "hearings": hearings,
            "levels": levels, "shares": shares, "l4_items": l4_items, "panels": panels, "kappa": kappa}


def report(root: str, args=None) -> str:
    s = summarise(root)
    if not s["runs"]:
        return "projection: no governed runs under " + root
    # Scale to one company-year of arms C and D: the dry run covered s["company_days"] run-days
    # (pack x arm x seed x days); a company-year is 2 arms x DAYS days.
    per_cy = (2 * cal.DAYS) / max(1, s["company_days"])
    lines = ["GOVERNANCE PROJECTION (estimate, from a dry run; token counts chars/4; not a measurement)",
             f"dry run: {s['runs']} governed runs, {s['company_days']} run-days; scale to one company-year "
             f"(arms C+D, {cal.DAYS} days) x {per_cy:.2f}", ""]
    lines.append(f"{'role / level':16} {'model':42} {'calls/cy':>9} {'in tok/cy':>12} {'out tok/cy':>12} "
                 f"{'USD/cy bind':>11} {'USD/cy pair':>11}")
    total_bind = total_pair = 0.0
    for role in sorted(s["roles"]):
        r = s["roles"][role]
        bind = r["usd"] * per_cy
        # the shadow run of a pair asks every seat again except the L4 proxy (not consulted in shadow)
        pair = bind * (1 if role == "l4_proxy" else 2)
        total_bind += bind
        total_pair += pair
        lines.append(f"{role:16} {str(r['model'])[:42]:42} {r['calls'] * per_cy:9.0f} {r['input_tokens'] * per_cy:12.0f} "
                     f"{r['output_tokens'] * per_cy:12.0f} {bind:11.2f} {pair:11.2f}")
    ag = s["agent"]["cost_usd"] * per_cy
    lines.append(f"{'agent (cache)':16} {'(binding only; shadow replays the v1 cache)':42} {'':9} {'':12} {'':12} "
                 f"{ag:11.2f} {ag:11.2f}")
    lines.append(f"{'agent (no cache)':16} {'(binding and shadow both call)':42} {'':9} {'':12} {'':12} "
                 f"{ag:11.2f} {2 * ag:11.2f}")
    lines.append("")
    cy_cache, cy_nocache = total_pair + ag, total_pair + 2 * ag
    lines.append(f"per company-year, arms C+D, shadow+binding pair: about {cy_cache:,.0f} USD "
                 f"(about {cy_nocache:,.0f} USD without the v1 cache)  [estimate]")
    lines.append(f"registered set ({PACKS_IN_SET} companies): about {PACKS_IN_SET * cy_cache:,.0f} USD "
                 f"(about {PACKS_IN_SET * cy_nocache:,.0f} USD without the v1 cache)  [estimate]")
    lines.append("")
    sh = s["shares"]
    def fmt(v):
        return "NA" if v is None else f"{v:.1%}"
    kappa = "NA" if s["kappa"] is None else f"{s['kappa']:.3f}"
    lines.append(f"routing (dry, --dry-error-rate {getattr(args, 'dry_error_rate', 'NA')}): {s['hearings']} hearings; "
                 f"reach L2+ {fmt(sh['L2+'])}, L3+ {fmt(sh['L3+'])}, L4 {fmt(sh['L4'])}; "
                 f"panels {s['panels']}, Fleiss kappa {kappa}")
    months = max(1e-9, s["company_days"] / 21.0)        # about 21 working days a month
    if s["l4_items"]:
        lines.append("L4 items per company-month by origin: "
                     + ", ".join(f"{k} {v / months:.1f}" for k, v in sorted(s["l4_items"].items())))
    else:
        lines.append("L4 items per company-month by origin: none in the dry run")
    for w in ec21_warnings(sh, s["kappa"], s["panels"]):
        lines.append("WARNING " + w)
    return "\n".join(lines)
