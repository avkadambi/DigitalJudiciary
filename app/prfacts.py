"""L5 Inbound translation: GitHub pull-request signals -> constitutional facts.

This is the layer the paper has to be most careful about, because it is the
only place where the outside world becomes a case. Three properties are
enforced here and checked by the interface conformance suite:

  1. **Deterministic.** Same payload + same map => same factor set, same
     provision list, same ordering. No model, no clock, no network.
  2. **Versioned and pinned.** `extractor_version` and a content hash of the
     map are written into every `pr_session`, exactly as the rulebook version
     is pinned at intake (CC-04). A session is replayable forever.
  3. **Attributed.** A factor that came from a CI signal and a factor the PR
     author simply claimed in the description are both recorded, but they are
     distinguishable (`self_asserted`). An auditor should never have to guess
     which facts the machine actually observed.

The extractor emits facts; it never emits outcomes. Interpretation of those
facts against a provision belongs to the Kernel and nowhere else.
"""
from __future__ import annotations

import fnmatch
import json
import os
import re

from .kernel import canonical, sha256

DEFAULT_MAP = os.path.join(os.path.dirname(__file__), "..", "seed",
                           "github_factor_map.json")


def map_path() -> str:
    return os.environ.get("DJ_FACTOR_MAP") or DEFAULT_MAP

# Which webhook events are adjudicable at all. Anything else is recorded as
# 'ignored' — the judiciary does not have an opinion about a closed PR.
ADJUDICABLE = {
    ("pull_request", "opened"),
    ("pull_request", "reopened"),
    ("pull_request", "synchronize"),
    ("pull_request", "ready_for_review"),
    ("check_suite", "completed"),
    ("simulator", "submit"),
}


class FactorMap:
    """The loaded, hashed extraction map."""

    def __init__(self, path: str | None = None):
        with open(path or map_path()) as fh:
            self.raw = json.load(fh)
        self.version = self.raw["extractor_version"]
        self.hash = sha256(canonical(self.raw))
        self._body_pattern = re.compile(
            self.raw["self_assertion"]["body_pattern"])
        # Absolutes-first ordering is decided by the constitution at runtime,
        # but within a class the order is the map's declaration order, which
        # is stable because JSON objects preserve insertion order in CPython.
        self.trigger_order = [k for k in self.raw["provision_triggers"]
                              if k != "note"]

    # -- predicate primitives -------------------------------------------
    @staticmethod
    def _paths(pr: dict) -> list[str]:
        return [f.get("filename", "") for f in pr.get("files", [])]

    @staticmethod
    def _labels(pr: dict) -> set[str]:
        out = set()
        for lab in pr.get("labels", []):
            out.add(lab["name"] if isinstance(lab, dict) else str(lab))
        return out

    @staticmethod
    def _checks(pr: dict) -> list[dict]:
        return pr.get("check_runs", [])

    def _atom(self, atom: dict, pr: dict) -> bool:
        if "any" in atom:
            return any(self._atom(a, pr) for a in atom["any"])
        if "all" in atom:
            return all(self._atom(a, pr) for a in atom["all"])
        if "none" in atom:
            return not any(self._atom(a, pr) for a in atom["none"])
        if "path_glob" in atom:
            globs = atom["path_glob"]
            paths = self._paths(pr)
            return any(_glob(p, g) for g in globs for p in paths)
        if "label" in atom:
            return bool(set(atom["label"]) & self._labels(pr))
        if "title_regex" in atom:
            return bool(re.search(atom["title_regex"], pr.get("title", "")))
        if "body_regex" in atom:
            return bool(re.search(atom["body_regex"], pr.get("body") or ""))
        if "check" in atom:
            want = atom["check"]
            for c in self._checks(pr):
                if c.get("name") == want["name"] and \
                        c.get("conclusion") == want["conclusion"]:
                    return True
            return False
        if "base_ref_regex" in atom:
            return bool(re.search(atom["base_ref_regex"],
                                  pr.get("base_ref", "")))
        if "draft" in atom:
            return bool(pr.get("draft")) == bool(atom["draft"])
        raise ValueError(f"unknown predicate atom: {sorted(atom)}")

    def _rule_holds(self, rule: dict, pr: dict) -> bool:
        ok = True
        if "any" in rule:
            ok = ok and any(self._atom(a, pr) for a in rule["any"])
        if "all" in rule:
            ok = ok and all(self._atom(a, pr) for a in rule["all"])
        if "none" in rule:
            ok = ok and not any(self._atom(a, pr) for a in rule["none"])
        return ok

    # -- extraction ------------------------------------------------------
    def extract(self, pr: dict) -> dict:
        """Return the full, auditable extraction result for one PR."""
        observed, provenance = [], {}
        for rule in self.raw["rules"]:
            if self._rule_holds(rule, pr):
                observed.append(rule["factor"])
                provenance[rule["factor"]] = "observed"

        asserted = []
        for m in self._body_pattern.finditer(pr.get("body") or ""):
            f = m.group(1)
            asserted.append(f)
            provenance.setdefault(f, "self_asserted")

        factors = sorted(set(observed) | set(asserted))
        return {
            "extractor_version": self.version,
            "factor_map_hash": self.hash,
            "factors": factors,
            "observed": sorted(set(observed)),
            "self_asserted": sorted(set(asserted) - set(observed)),
            "provenance": provenance,
        }

    def is_control_plane(self, pr: dict) -> bool:
        """A3: does this PR target the rulebook itself?"""
        globs = self.raw["control_plane"]["path_globs"]
        return any(_glob(p, g) for g in globs for p in self._paths(pr))

    def provisions_engaged(self, factors: list[str]) -> list[str]:
        """Provisions whose trigger set intersects the extracted factors.
        Returned in map-declaration order; the caller re-sorts absolutes
        first using the live constitution."""
        fs = set(factors)
        triggers = self.raw["provision_triggers"]
        return [pid for pid in self.trigger_order if set(triggers[pid]) & fs]

    def scope(self, pr: dict) -> dict:
        cfg = self.raw["scope"]
        out: dict[str, str] = {}
        paths = self._paths(pr)
        for entry in cfg.get("service_from_path", []):
            for p in paths:
                if _glob(p, entry["glob"]):
                    parts = p.split("/")
                    idx = entry["capture"]
                    if len(parts) > idx:
                        out["service"] = parts[idx]
                    break
            if "service" in out:
                break
        for entry in cfg.get("domain_from_path", []):
            if any(_glob(p, entry["glob"]) for p in paths):
                out["domain"] = entry["domain"]
                break
        prefix = cfg.get("team_from_label_prefix")
        if prefix:
            for lab in sorted(self._labels(pr)):
                if lab.startswith(prefix):
                    out["team"] = lab[len(prefix):]
                    break
        return out


def _glob(path: str, pattern: str) -> bool:
    """fnmatch with '**' semantics: '**/x' also matches a top-level 'x'."""
    if fnmatch.fnmatch(path, pattern):
        return True
    if pattern.startswith("**/"):
        return fnmatch.fnmatch(path, pattern[3:])
    return False


def normalize_event(event_type: str, payload: dict) -> dict:
    """Flatten a GitHub webhook payload into the shape the extractor reads.

    `files` and `check_runs` are not in the webhook body; GitHub requires
    separate API calls. The adapter supplies them under `dj_context` (from
    the enricher, or from the simulator during benchmark runs), so the
    extractor itself stays a pure function of its input.
    """
    pr = payload.get("pull_request") or {}
    ctx = payload.get("dj_context") or {}
    repo = (payload.get("repository") or {}).get("full_name", "unknown/unknown")
    return {
        "repo": repo,
        "number": pr.get("number") or payload.get("number") or 0,
        "title": pr.get("title", ""),
        "body": pr.get("body") or "",
        "labels": pr.get("labels", []),
        "draft": bool(pr.get("draft")),
        "base_ref": (pr.get("base") or {}).get("ref", ""),
        "head_sha": (pr.get("head") or {}).get("sha", ""),
        "author": (pr.get("user") or {}).get("login", "unknown"),
        "files": ctx.get("files", []),
        "check_runs": ctx.get("check_runs", []),
        "event_type": event_type,
        "action": payload.get("action", ""),
    }
