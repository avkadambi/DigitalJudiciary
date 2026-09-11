"""Render a case whose factors are known into the prose a pull request would carry.

The corpora carry computed ground truth: which factors a case has is known by
construction. Writing the case out as a change description and extracting it
back therefore measures an extractor without a human labelling anything —
which is the one input a calibration cannot otherwise get honestly.

Two disciplines carried over from the Likewise round-trip harness:

  * **Styles are plural and awkward.** One phrasing measures a lookup table.
    Five non-guard styles say the same fact five ways; three GUARD styles put
    a factor's words in the text when the case does NOT carry the factor, so
    that the only correct behaviour is silence and any assertion is a
    hallucination by construction.
  * **Style disjointness.** The styles an extractor is trained on may not
    appear in its evaluation set; `split_styles` partitions them and the
    report refuses a headline on overlap.

Every rendered document also carries the change title and one or two guard
sentences drawn deterministically from the engaged provisions' vocabulary, so
that every document has something a proximity extractor will get wrong. The
result is an UPPER BOUND on extraction quality — the renderer and the
extractor share a vocabulary — and every report says so.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

STYLES = ("plain", "formal", "narrative", "tabular", "elliptical")
GUARD_STYLES = ("hedged", "negated", "third_party")
ALL_STYLES = STYLES + GUARD_STYLES

_ACRONYMS = {"dea", "epcs", "dvm", "api", "sso", "mfa", "pii", "phi", "gdpr", "hipaa", "sbom", "cve", "sla",
             "slo", "kpi", "dti", "kyc", "aml", "sox", "pci", "dss", "iso", "nist", "ci", "cd", "pr", "ui", "ux",
             "id", "ids", "ip", "tls", "ssl", "jwt", "url", "sql", "llm", "gpu", "cpu", "ram", "os", "vm", "eu",
             "us", "uk", "fda", "usda", "cfr", "aphis", "wcag", "ada", "ccpa", "ftc", "sec", "fdic", "occ",
             "cfpb", "ofac", "sar", "ctr", "rbac", "iam", "kms", "hsm", "otp", "asap", "dpo", "dpia", "ropa"}


def words(factor: str) -> str:
    """A factor slug as words. Acronyms are upper-cased, numbers kept."""
    out = []
    for w in factor.split("_"):
        out.append(w.upper() if w in _ACRONYMS else w)
    return " ".join(out)


def _phrase(style: str, factor: str) -> str:
    w = words(factor)
    if style == "plain":
        return f"This change ensures {w}."
    if style == "formal":
        return f"Reviewers confirm that {w} holds for this change."
    if style == "narrative":
        return f"As part of this work, {w}, with evidence attached to the ticket."
    if style == "tabular":
        return f"- {w}: yes"
    if style == "elliptical":
        return f"{w} — done."
    # guards: the factor's words appear and the case does NOT carry it
    if style == "hedged":
        return f"The author asserts that {w}, which reviewers could not confirm from the diff."
    if style == "negated":
        return f"This change does not ensure {w}."
    if style == "third_party":
        return f"In the previous release {w}; the present change differs on that point."
    raise ValueError(f"unknown style {style!r}")


def _guard_style_for(factor: str, style: str) -> str:
    h = int(hashlib.sha256(f"{factor}\x1f{style}".encode()).hexdigest(), 16)
    return GUARD_STYLES[h % len(GUARD_STYLES)]


def _pick_guards(case_id: str, candidates: list, n: int) -> list:
    cands = sorted(candidates)
    if not cands or n <= 0:
        return []
    h = int(hashlib.sha256(case_id.encode()).hexdigest(), 16)
    out = []
    for i in range(min(n, len(cands))):
        out.append(cands[(h + i * 7919) % len(cands)])
    return sorted(set(out))


@dataclass(frozen=True)
class Rendering:
    case_id: str
    prose: str
    truth: dict          # factor -> True (present) | None (not carried; guard or unmentioned)
    style: str
    guards: tuple        # factors written in a guard style
    vocabulary: tuple    # every factor the extractor is asked about

    @property
    def guard(self) -> bool:
        return bool(self.guards)


def render(case: dict, vocabulary: list, style: str, n_guards: int = 2, seed_salt: str = "") -> Rendering:
    """Write one case as a change description in `style`.

    `vocabulary` is the factor set of the engaged provisions. Present factors
    (in-vocabulary facts) are written in `style`; `n_guards` absent factors are
    written in a guard style; the rest are not mentioned. Facts outside the
    vocabulary (context markers) are not rendered — they are carried by the
    snapshot stage, not extracted.
    """
    if style not in ALL_STYLES:
        raise ValueError(f"unknown style {style!r}")
    vocab = sorted(vocabulary)
    present = [f for f in case["facts"] if f in set(vocab)]
    absent = [f for f in vocab if f not in set(present)]
    title = (case.get("scenario") or {}).get("change") or f"Change {case['id']}"
    # A factor the title already states in so many words cannot be a guard:
    # the document would assert it before the guard sentence denies it.
    guardable = [f for f in absent if words(f).lower() not in title.lower()]
    guards = _pick_guards(case["id"] + seed_salt, guardable, n_guards)
    lines = [f"{title}.", ""]
    truth = {}
    body = []
    # A guard style names the whole document's register for its guards; the
    # factors the case does carry are still stated plainly, because a true
    # statement written as a negation would not be true.
    present_style = style if style in STYLES else "plain"
    for f in present:
        body.append((f, _phrase(present_style, f)))
        truth[f] = True
    for f in guards:
        g = style if style in GUARD_STYLES else _guard_style_for(f, style)
        body.append((f, _phrase(g, f)))
        truth[f] = None
    for f in absent:
        truth.setdefault(f, None)
    # deterministic interleave so guards are not always last
    h = int(hashlib.sha256((case["id"] + style).encode()).hexdigest(), 16)
    body.sort(key=lambda x: int(hashlib.sha256((x[0] + str(h)).encode()).hexdigest(), 16))
    lines += [p for _, p in body]
    return Rendering(case_id=case["id"], prose="\n".join(lines), truth=truth, style=style,
                     guards=tuple(guards), vocabulary=tuple(vocab))


def split_styles(train_fraction: float = 0.6) -> tuple:
    """Disjoint train / eval partition; guard styles go to eval only."""
    n = max(1, round(len(STYLES) * train_fraction))
    if n >= len(STYLES):
        raise ValueError("train_fraction leaves no styles to evaluate on")
    return STYLES[:n], STYLES[n:] + GUARD_STYLES


def sentences(prose: str) -> list:
    """(start, end, text) for each line/sentence, for cue detection."""
    out = []
    for m in re.finditer(r"[^\n.]+[.\n]?", prose):
        t = m.group(0).strip()
        if t:
            out.append((m.start(), m.end(), t))
    return out
