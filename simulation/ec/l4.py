"""
L4, the final authority above the court (governance build v3, §3.3, §5.7).

    llm-proxy    a named frontier model decides for the risk owner (registered);
                 recorded decided_by "llm-proxy", never reported as a human
    queue        pilots: the item is written to <out>/human_queue.jsonl and a
                 person decides it with tools/human_review.py, which appends to
                 <out>/human_decisions.jsonl. Items beyond `human_cap` go to the
                 proxy, labelled so. With the shadow proxy on (the default in
                 queue mode) the proxy also decides every human item, logged only,
                 for the proxy-versus-owner agreement measure
    interactive  queue, decided at the terminal (a TTY is required)
    rule         the engine's risk-owner rule: permit_conditional

Hearings are synchronous: a queue item with no decision on file either stops
the run for the person (`--human-wait`: the run checkpoints and exits 4; rerun
to resume once decided) or lapses to deny, flagged and counted. Lapse-to-deny is
stricter than a real executive and is reported as such.

A6 limits L4: no decision may permit while affirming an absolute violation. A
decision may overturn the finding (`absolute_finding_overturned: true`) and then
decide on the merits. Proxy fail-safe: lapse to deny, flagged and counted.
"""

from __future__ import annotations

import json
import os
import sys

from . import governance as gov

HOLDINGS = ("permit", "permit_conditional", "deny")
SCHEMA = {"holding": "|".join(HOLDINGS), "absolute_finding_overturned": "true|false",
          "conditions": "<= 300 characters or null", "reasons": "<= 800 characters", "confidence": "0-100"}
QUEUE_FILE, DECISIONS_FILE = "human_queue.jsonl", "human_decisions.jsonl"


class HumanWaitNeeded(RuntimeError):
    """A queue item has no decision on file and the run was asked to wait."""


def validate_decision(d: dict, a6_found: bool) -> str | None:
    if d.get("holding") not in HOLDINGS:
        return f"holding must be one of {HOLDINGS}"
    if a6_found and d["holding"] != "deny" and not d.get("absolute_finding_overturned"):
        return "a permit may not affirm an absolute violation: overturn the finding or deny"
    return None


def render_item(item: dict) -> str:
    """What the proxy (and the person) sees: the case file, every opinion, the
    prosecutor's call, the conscience's decision and the A6 notice."""
    u = [item["case_file"], "", "THE LADDER"]
    for lv, op in (item.get("ladder") or {}).items():
        if lv == "L2":
            u.append(f"- L2 panel votes {op.get('votes')} (majority {op.get('majority')})")
            for o in op.get("opinions") or []:
                u.append(f"  - {o.get('stance')}: {o.get('holding')}; {str(o.get('reasons') or '')[:300]}")
        else:
            u.append(f"- {lv}: {op.get('holding')}; controlling {op.get('controlling')}; "
                     f"{str(op.get('reasons') or '')[:400]}")
    pr = item.get("prosecutor")
    if pr is not None:
        u.append(f"- the prosecutor {'charged' if pr.get('charge') else 'declined'}")
    u.append(f"- the conscience's decision on the change: {item.get('conscience') or 'none'}")
    if item.get("a6_found"):
        u += ["", "NOTICE: the court found that the change breaks an absolute provision. You may not permit it "
                  "while that finding stands."]
    u.append(f"Why it reached you: {item.get('origin')}")
    return "\n".join(u)


class L4Authority:
    def __init__(self, mode: str, out_dir: str, deadline_days: int = 10, wait: bool = False, human_cap: int = 40,
                 proxy_client=None, shadow_proxy: bool = False, flip=None, style: str = "canon"):
        self.mode, self.out_dir, self.deadline_days, self.wait = mode, out_dir, int(deadline_days), bool(wait)
        self.human_cap, self.proxy, self.shadow_proxy, self.flip, self.style = int(human_cap), proxy_client, \
            bool(shadow_proxy), flip, style
        self.human_items = 0
        self.counts = {"items": 0, "by_mode": {}, "by_origin": {}, "lapsed": 0, "proxy_failures": 0}
        self.agreement: list = []         # (owner holding, shadow proxy holding)

    # -- the proxy ------------------------------------------------------------
    def _proxy(self, item: dict) -> dict:
        system = gov.load_prompt("l4_proxy", self.style) + "\n\n" + gov.schema_text(SCHEMA)
        user = render_item(item)
        a6 = bool(item.get("a6_found"))
        if self.proxy.mode != "live":
            self.proxy.account_dry(system, user, gov.DRY_OUT_TOKENS["l4_proxy"])
            want = item.get("oracle_canon") or "permit_conditional"
            if a6:
                want = "deny"
            out = {"holding": want, "absolute_finding_overturned": False, "dry_flipped": False}
            key = "l4|" + str(item.get("case_id")) + "|" + str(item.get("act_id"))
            if self.flip is not None and self.flip.flip(key) and not a6:
                out["holding"], out["dry_flipped"] = self.flip.choice(key, [h for h in HOLDINGS if h != want]), True
            out["cost"] = dict(self.proxy.last_cost or {})
            return out
        parsed, meta = self.proxy.call_json(system, user, validate=lambda d: validate_decision(d, a6))
        if parsed is None:
            self.counts["proxy_failures"] += 1
            self.counts["lapsed"] += 1
            return {"holding": "deny", "lapsed": True, "fail_safe": "lapse_to_deny", "cost": dict(self.proxy.last_cost or {})}
        return {"holding": parsed["holding"], "absolute_finding_overturned": bool(parsed.get("absolute_finding_overturned")),
                "conditions": parsed.get("conditions"), "reasons": str(parsed.get("reasons") or "")[:800],
                "confidence": parsed.get("confidence"), "repaired": meta["repaired"], "cost": dict(self.proxy.last_cost or {})}

    # -- the human queue ------------------------------------------------------
    def _decisions(self) -> dict:
        path = os.path.join(self.out_dir, DECISIONS_FILE)
        out = {}
        if os.path.exists(path):
            with open(path) as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        d = json.loads(line)
                        out[d["item"]] = d
        return out

    def _enqueue(self, item_id: str, item: dict) -> None:
        path = os.path.join(self.out_dir, QUEUE_FILE)
        queued = set()
        if os.path.exists(path):
            with open(path) as fh:
                queued = {json.loads(x)["item"] for x in fh if x.strip()}
        if item_id in queued:
            return
        with open(path, "a") as fh:
            fh.write(json.dumps({"item": item_id, "case_id": item.get("case_id"), "origin": item.get("origin"),
                                 "a6_found": bool(item.get("a6_found")), "text": render_item(item)}, sort_keys=True) + "\n")

    def _interactive(self, item_id: str, item: dict) -> dict:
        if not sys.stdin.isatty():
            raise RuntimeError("--l4 interactive needs a terminal")
        print("\n" + render_item(item))
        while True:
            h = input(f"[{item_id}] holding ({'/'.join(HOLDINGS)}): ").strip()
            ov = item.get("a6_found") and h != "deny" and input("overturn the absolute finding? (y/n): ").strip() == "y"
            d = {"item": item_id, "holding": h, "absolute_finding_overturned": bool(ov)}
            err = validate_decision(d, bool(item.get("a6_found")))
            if err is None:
                with open(os.path.join(self.out_dir, DECISIONS_FILE), "a") as fh:
                    fh.write(json.dumps(d, sort_keys=True) + "\n")
                return d
            print(err)

    # -- one item ---------------------------------------------------------------
    def decide(self, item: dict) -> dict:
        item_id = str(item.get("act_id"))
        origin = item.get("origin", "other")
        self.counts["items"] += 1
        self.counts["by_origin"][origin] = self.counts["by_origin"].get(origin, 0) + 1
        out = {"origin": origin, "item": item_id}
        if self.mode == "rule":
            out.update(holding="deny" if item.get("a6_found") else "permit_conditional", decided_by="rule", l4_mode="rule")
        elif self.mode == "llm-proxy" or self.human_items >= self.human_cap:
            over = self.mode != "llm-proxy"
            out.update(self._proxy(item), decided_by="llm-proxy", l4_mode=self.mode,
                       over_human_cap=over)
        else:
            self.human_items += 1
            dec = self._decisions().get(item_id)
            if dec is None and self.mode == "interactive":
                dec = self._interactive(item_id, item)
            if dec is None:
                self._enqueue(item_id, item)
                if self.wait:
                    self.human_items -= 1
                    self.counts["items"] -= 1
                    self.counts["by_origin"][origin] -= 1
                    raise HumanWaitNeeded(f"L4 item {item_id} awaits a decision in {QUEUE_FILE}")
                self.counts["lapsed"] += 1
                out.update(holding="deny", decided_by="lapse", lapsed=True, l4_mode=self.mode)
            else:
                out.update(holding=dec["holding"], decided_by="human", l4_mode=self.mode,
                           absolute_finding_overturned=bool(dec.get("absolute_finding_overturned")),
                           note=dec.get("note"))
            if self.shadow_proxy and self.proxy is not None:
                sp = self._proxy(item)
                out["shadow_proxy"] = sp
                if out["decided_by"] == "human":
                    self.agreement.append([out["holding"], sp["holding"]])
        m = out["decided_by"]
        self.counts["by_mode"][m] = self.counts["by_mode"].get(m, 0) + 1
        return out

    def state(self) -> dict:
        return {"human_items": self.human_items, "counts": self.counts, "agreement": self.agreement}

    def restore(self, d: dict) -> None:
        self.human_items = int(d.get("human_items", 0))
        self.counts = d.get("counts") or self.counts
        self.agreement = list(d.get("agreement") or [])


def cohen_kappa(pairs: list):
    """Cohen's kappa for (owner, proxy) holdings."""
    if not pairs:
        return None
    n = len(pairs)
    cats = sorted({x for p in pairs for x in p})
    po = sum(1 for a, b in pairs if a == b) / n
    pe = sum((sum(1 for a, _ in pairs if a == c) / n) * (sum(1 for _, b in pairs if b == c) / n) for c in cats)
    return 1.0 if pe >= 1.0 else (po - pe) / (1 - pe)
