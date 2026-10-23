"""
Governance metrics (governance build v3, §5.11): the columns an LLM-governed
run adds to metrics.csv. They appear only when a run's manifest carries a
`governance` block; a deterministic root keeps exactly today's columns.

Accuracy columns are meaningful on shadow runs (the state is the deterministic
run's); outcome estimands come from binding runs, and `prop_<estimand>` (binding
minus shadow) is filled on the binding row of a pair.

The bench is scored against `oracle_canon` (`DJ_KEY`, R1); the `_engine`
columns score the same opinions against `oracle_engine`.
"""

from __future__ import annotations

import json
import os

DJ_KEY = "oracle_canon"
DJ_KEY_ENGINE = "oracle_engine"
PROP_ESTIMANDS = ("e1_imperm", "e2_ps", "e3_og", "e4_diff", "e6_recall", "e6_precision", "e7_blind_spot",
                  "e8_esc_per30_before", "e8_esc_per30_after", "executed", "blocked", "escalations_heard", "cost_usd")
GOV_COLUMNS = [
    "governance", "prompt_style",
    "acc_ec_d1", "acc_ec_d2", "acc_ec_d3", "acc_ec_d4", "acc_ec_d5", "acc_ec_d6", "acc_ec_d7",
    "ec_false_allow_T0T1", "ec_false_block", "ec_esc_precision", "ec_esc_recall", "ec_twin_invariance", "ec_n",
    "office_acc", "grants_over_cap", "office_n",
    "auditor_label_acc", "t3_audit_acc", "auditor_n",
    "acc_dj_holding", "acc_dj_holding_L1", "acc_dj_holding_L2", "acc_dj_holding_L3", "acc_dj_a6",
    "acc_dj_controlling", "dj_premise_jaccard", "acc_pr_charge",
    "acc_dj_holding_engine", "acc_dj_holding_L1_engine", "acc_dj_holding_L2_engine", "acc_dj_holding_L3_engine",
    "oracle_disagree_rate", "dj_n",
    "share_L1_final", "share_L2", "share_L3", "share_L4", "refer_up_rate", "panel_fleiss_kappa", "panel_n",
    "correct_up", "wrong_overturn",
    "escalation_reason_i_disagree_ec", "escalation_reason_ii_low_conf_t1t2", "escalation_reason_iii_appeal",
    "escalation_reason_iv_audit", "escalation_reason_degraded", "escalation_reason_a6_finding_disagrees",
    "escalation_reason_straight_to_l3",
    "gloss_acc", "codify_acc", "contaminated_glosses", "downstream_gloss_bar_blocks",
    "l4_items", "l4_items_risk_owner_contest", "l4_items_l3_low_confidence", "l4_items_appeal_l3",
    "l4_items_human_sample", "l4_items_degraded", "l4_by_mode_llm_proxy", "l4_by_mode_human", "l4_by_mode_rule",
    "l4_by_mode_lapse", "l4_lapsed_share", "l4_proxy_owner_agreement", "l4_proxy_owner_kappa", "l4_proxy_owner_n",
    "divergence_day_first", "divergence_day_store", "divergence_day_glosses", "divergence_day_registry",
    "divergence_day_agent_prompts",
    "cost_per_correct_ec", "cost_per_correct_dj", "cost_per_correct_office", "cost_per_correct_auditor",
    "rerun_agreement_ec",
] + [f"prop_{e}" for e in PROP_ESTIMANDS]


def _rate(num, den):
    return (num / den) if den else None


def _acc(pairs: list):
    pairs = [(a, b) for a, b in pairs if a is not None and b is not None]
    return _rate(sum(1 for a, b in pairs if a == b), len(pairs))


def _jaccard(a, b):
    a, b = set(a or []), set(b or []),
    return 1.0 if not a and not b else len(a & b) / len(a | b)


def _ctl(x):
    return None if x in (None, "none", "none_tie") else x


def dj_holding_accuracy(hearings: list, key: str | None = None):
    """Share of laddered hearings whose deciding holding equals the key (R1: oracle_canon)."""
    key = key or DJ_KEY
    return _acc([(h.get("ladder_holding"), h.get(key)) for h in hearings if "ladder" in h])


def ec_columns(lines: list) -> dict:
    asked = [l for l in lines if l.get("ec_llm")]
    out = {"ec_n": len(asked)}
    if not asked:
        return out
    fields = {"acc_ec_d1": ("contravened", "departure"), "acc_ec_d2": ("token_valid", "token_fail", "say_so"),
              "acc_ec_d3": ("t2_admitted", "t2_evidence", "t2_in_bound"), "acc_ec_d4": ("t3_in_context",),
              "acc_ec_d5": ("gloss_bar",)}
    for col, keys in fields.items():
        pairs = []
        for l in asked:
            got = {e.get("id"): e for e in l["ec_llm"].get("entries") or []}
            for pe in l["oracle_verdict"].get("per_entry") or []:
                g = got.get(pe.get("id"))
                for k in keys:
                    if pe.get(k) is not None:
                        pairs.append((g.get(k) if g else "missing", pe.get(k)))
        out[col] = _acc(pairs)
    out["acc_ec_d6"] = _acc([(bool(l["ec_llm"].get("conflict")), l["oracle_verdict"].get("reason_code") == "conflict_hold")
                             for l in asked])
    out["acc_ec_d7"] = _acc([(l["ec_llm"]["decision"], l["oracle_verdict"]["four_way"]) for l in asked])
    t01 = [l for l in asked if l["oracle_verdict"]["four_way"] != "allow" and l["oracle_verdict"].get("tier") in ("T0", "T1")]
    out["ec_false_allow_T0T1"] = _rate(sum(1 for l in t01 if l["ec_llm"]["decision"] == "allow"), len(t01))
    ok = [l for l in asked if l["oracle_verdict"]["four_way"] == "allow"]
    out["ec_false_block"] = _rate(sum(1 for l in ok if l["ec_llm"]["decision"] != "allow"), len(ok))
    esc_m = [l for l in asked if l["ec_llm"]["decision"] == "escalate"]
    esc_o = [l for l in asked if l["oracle_verdict"]["four_way"] == "escalate"]
    out["ec_esc_precision"] = _rate(sum(1 for l in esc_m if l["oracle_verdict"]["four_way"] == "escalate"), len(esc_m))
    out["ec_esc_recall"] = _rate(sum(1 for l in esc_o if l["ec_llm"]["decision"] == "escalate"), len(esc_o))
    by_act = {l["proposal"]["act_id"]: l for l in asked}
    tw = []
    for l in asked:
        c = by_act.get(l["proposal"].get("twin_of"))
        if c is not None and c["proposal"]["act"] == l["proposal"]["act"] and c["proposal"]["engaged"] == l["proposal"]["engaged"]:
            tw.append((l["ec_llm"]["decision"], c["ec_llm"]["decision"]))
    out["ec_twin_invariance"] = _acc(tw)
    return out


def office_columns(registry: dict, office_state: dict | None) -> dict:
    ev = [e for e in registry.get("events") or [] if e.get("event") == "decision" and "oracle_office" in e]
    out = {"office_n": len(ev)}
    if ev:
        out["office_acc"] = _acc([((e.get("office_llm") or {}).get("decision"), e["oracle_office"]) for e in ev])
        out["grants_over_cap"] = sum(1 for e in ev if e["outcome"] == "granted" and e["oracle_office"] == "denied_cap")
    return out


def auditor_columns(lines: list, bench: dict) -> dict:
    lab = [(l.get("auditor_label"), l.get("oracle_label")) for l in lines if l.get("auditor_label")]
    t3 = [((s.get("auditor_t3") or {}).get("legitimate"), s.get("oracle_t3_legitimate"))
          for s in bench.get("t3_samples") or [] if "auditor_t3" in s]
    out = {"auditor_n": len(lab)}
    if lab:
        out["auditor_label_acc"] = _acc(lab)
    if t3:
        out["t3_audit_acc"] = _acc(t3)
    return out


def bench_columns(bench: dict) -> dict:
    from .projection import fleiss_kappa
    H = [h for h in bench.get("hearings") or [] if "ladder" in h]
    out = {"dj_n": len(H)}
    if not H:
        return out
    out["acc_dj_holding"] = dj_holding_accuracy(H)
    out["acc_dj_holding_engine"] = dj_holding_accuracy(H, DJ_KEY_ENGINE)

    def lvl(h, k):
        op = (h.get("ladder") or {}).get(k)
        if not op:
            return None
        return op.get("majority") if k == "L2" else op.get("holding")
    for k in ("L1", "L2", "L3"):
        out[f"acc_dj_holding_{k}"] = _acc([(lvl(h, k), h.get(DJ_KEY)) for h in H if lvl(h, k)])
        out[f"acc_dj_holding_{k}_engine"] = _acc([(lvl(h, k), h.get(DJ_KEY_ENGINE)) for h in H if lvl(h, k)])
    l1 = [(h["ladder"]["L1"], h) for h in H if not h["ladder"]["L1"].get("degraded")]
    out["acc_dj_a6"] = _acc([(bool((op.get("absolute") or {}).get("violated")), bool(h.get("oracle_a6"))) for op, h in l1])
    out["acc_dj_controlling"] = _acc([(_ctl(op.get("controlling")) or "-", _ctl(h.get("oracle_controlling")) or "-")
                                      for op, h in l1])
    js = [_jaccard(op.get("premise"), h.get("oracle_premise")) for op, h in l1]
    out["dj_premise_jaccard"] = (sum(js) / len(js)) if js else None
    pr = [(h["prosecutor"].get("charge"), h["prosecutor"].get("oracle_charge")) for h in H if h.get("prosecutor")]
    out["acc_pr_charge"] = _acc(pr)
    out["oracle_disagree_rate"] = _rate(sum(1 for h in H if h.get("oracle_disagree")), len(H))
    n = len(H)
    lv = [int(h.get("final_level") or 1) for h in H]
    out["share_L1_final"] = _rate(sum(1 for x in lv if x == 1), n)
    out["share_L2"] = _rate(sum(1 for x in lv if x >= 2), n)
    out["share_L3"] = _rate(sum(1 for x in lv if x >= 3), n)
    out["share_L4"] = _rate(sum(1 for x in lv if x >= 4), n)
    out["refer_up_rate"] = _rate(sum(1 for h in H if h.get("refer_up_l1")), n)
    votes = [h["ladder"]["L2"]["votes"] for h in H if (h.get("ladder") or {}).get("L2")]
    out["panel_n"] = len(votes)
    out["panel_fleiss_kappa"] = fleiss_kappa(votes) if votes else None
    up = [h for h in H if int(h.get("final_level") or 1) >= 2 and lvl(h, "L1")]
    out["correct_up"] = sum(1 for h in up if lvl(h, "L1") != h.get(DJ_KEY) and h.get("ladder_holding") == h.get(DJ_KEY))
    out["wrong_overturn"] = sum(1 for h in up if lvl(h, "L1") == h.get(DJ_KEY) and h.get("ladder_holding") != h.get(DJ_KEY))
    for r in ("i_disagree_ec", "ii_low_conf_t1t2", "iii_appeal", "iv_audit", "degraded", "a6_finding_disagrees",
              "straight_to_l3"):
        out[f"escalation_reason_{r}"] = sum(1 for h in H if r in (h.get("escalation_reason") or []))
    l4 = [h["l4"] for h in H if h.get("l4") and h["l4"].get("decided_by")]
    out["l4_items"] = len(l4)
    for o in ("risk_owner_contest", "l3_low_confidence", "appeal_l3", "human_sample", "degraded"):
        out[f"l4_items_{o}"] = sum(1 for x in l4 if x.get("origin") == o)
    for m, key in (("llm-proxy", "llm_proxy"), ("human", "human"), ("rule", "rule"), ("lapse", "lapse")):
        out[f"l4_by_mode_{key}"] = sum(1 for x in l4 if x.get("decided_by") == m)
    out["l4_lapsed_share"] = _rate(sum(1 for x in l4 if x.get("lapsed")), len(l4))
    pairs = [(x["holding"], x["shadow_proxy"]["holding"]) for x in l4 if x.get("decided_by") == "human" and x.get("shadow_proxy")]
    out["l4_proxy_owner_n"] = len(pairs)
    if pairs:
        from .l4 import cohen_kappa
        out["l4_proxy_owner_agreement"] = _acc(pairs)
        out["l4_proxy_owner_kappa"] = cohen_kappa([list(p) for p in pairs])
    return out


def doctrine_columns(bench: dict, lines: list) -> dict:
    g = [x["doctrine"] for x in bench.get("glosses") or [] if x.get("doctrine")]
    out = {}
    if g:
        out["gloss_acc"] = _acc([((x["clerk"].get("holding"), bool(x["clerk"].get("bars_class"))),
                                  (x["oracle_gloss"]["holding"]["holding"], bool(x["oracle_gloss"]["bars_class"]))) for x in g])
        out["contaminated_glosses"] = sum(1 for x in g if x.get("contaminated"))
    lw = bench.get("lawmaker") or []
    if lw:
        out["codify_acc"] = _acc([(x["lawmaker"].get("codify"), x["oracle_codify"]) for x in lw])
    if g:
        out["downstream_gloss_bar_blocks"] = sum(1 for l in lines if l["verdict"]["reason_code"] == "gloss_bar")
    return out


def cost_columns(man: dict, row: dict) -> dict:
    u = (man.get("governance") or {}).get("usage_by_role") or {}
    out = {}

    def usd(*roles):
        return sum(float((u.get(r) or {}).get("cost_usd", 0.0)) for r in u if r in roles or r.split("#")[0] in roles)
    for seat, roles, acc, n in (("ec", ("ec",), "acc_ec_d7", "ec_n"), ("office", ("office",), "office_acc", "office_n"),
                                ("auditor", ("auditor",), "auditor_label_acc", "auditor_n"),
                                ("dj", ("dj_l1", "dj_l2", "dj_l3", "prosecutor"), "acc_dj_holding", "dj_n")):
        if row.get(acc) is not None and row.get(n):
            correct = row[acc] * row[n]
            out[f"cost_per_correct_{seat}"] = (usd(*roles) / correct) if correct else None
    return out


def columns(run_dir: str, man: dict, summ: dict, bench: dict, lines: list) -> dict:
    """Every governance column for one run (absent fields stay NA)."""
    g = man.get("governance") or {}
    st = g.get("settings") or {}
    row = {"governance": st.get("preset") if len(set((st.get("modes") or {}).values())) <= 1 else "mixed",
           "prompt_style": g.get("prompt_style")}
    row.update(ec_columns(lines))
    reg_path = os.path.join(run_dir, "registry.json")
    if os.path.exists(reg_path):
        with open(reg_path) as fh:
            row.update(office_columns(json.load(fh), None))
    row.update(auditor_columns(lines, bench))
    row.update(bench_columns(bench))
    row.update(doctrine_columns(bench, lines))
    dv = summ.get("divergence") or {}
    for k in ("first", "store", "glosses", "registry", "agent_prompts"):
        if dv:
            row[f"divergence_day_{k}"] = dv.get(f"day_{k}")
    row.update(cost_columns(man, row))
    return row


def add_pair_props(rows: list, dirs: list) -> None:
    """prop_<estimand> = binding - shadow, on the binding row of each pair."""
    by_dir = dict(zip(dirs, rows))
    for d, r in by_dir.items():
        if "+gov-llm" not in os.path.basename(d):
            continue
        sib = by_dir.get(os.path.join(os.path.dirname(d), os.path.basename(d).replace("+gov-llm", "+gov-shadow")))
        if sib is None:
            continue
        for e in PROP_ESTIMANDS:
            a, b = r.get(e), sib.get(e)
            r[f"prop_{e}"] = (float(a) - float(b)) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else None


def monthly(rows_src: list) -> list:
    """Routing shares per (run, month of 21 working days) for monthly.csv."""
    out = []
    for key, bench in rows_src:
        H = [h for h in bench.get("hearings") or [] if "ladder" in h]
        months: dict = {}
        for h in H:
            months.setdefault((int(h["hear_day"]) - 1) // 21 + 1, []).append(int(h.get("final_level") or 1))
        for m, lv in sorted(months.items()):
            n = len(lv)
            out.append(dict(key, month=m, hearings=n, share_L1_final=sum(1 for x in lv if x == 1) / n,
                            share_L2=sum(1 for x in lv if x >= 2) / n, share_L3=sum(1 for x in lv if x >= 3) / n,
                            share_L4=sum(1 for x in lv if x >= 4) / n))
    return out
