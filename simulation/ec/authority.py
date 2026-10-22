"""
Who may lift a provision, read from who owns it (Realism revision R2).

R2 replaces the R1 tier rule, which read waiver authority off a provision's
harm tags and charging threshold. A normal company decides who may grant an
exception from *who owns the policy*. The rule here therefore reads a frozen
family-to-owner table and whether the provision's citation names a binding
instrument (prereg/REALISM_REVIEW.md §R2; consolidated external review of
22 October 2026, four reviewers). It is deterministic and reads only released
rulebook fields (absolute, harm_classes, tau, family, citation, status) plus
the R2 overlays in `rulebook_rev.py`:

  1. status advisory -> T3 (contexts internal-prototype, spike);
     deferred | readiness -> T2
  2. absolute -> T0
  3. a released absolute overlaid non-absolute -> T1, office = owner's office
     (an engineering, apparatus or accessibility owner maps to safety if S, else
     compliance; an agent owner to safety if the citation says "safety", else security)
  4. harm ∩ {legal, regulatory, safety} = ∅ -> T2
  5. owner = FAMILY_OWNER[company][family]; any WCAG citation -> accessibility
  6. binding citation:
       security | legal | compliance -> T1, that office
       safety -> T1 safety if S, else T1 compliance
       agent -> T1 safety if the citation says "safety", else T1 compliance
       engineering | apparatus -> T1 compliance if L or R, else T2
       accessibility -> T2
  7. internal citation:
       security | agent -> T1 security (safety if the citation says "safety") if tau <= 30
       safety -> T1 safety if S and tau <= 30
       legal | compliance -> T1 that office if tau <= 25
       engineering | apparatus | accessibility -> T2
     anything else -> T2

The two tau cut-offs (30 for security and safety owners, 25 for legal and
compliance) apply to internal standards only; they are design choices,
disclosed. The office set is security (the CISO), compliance, safety, legal
and accessibility, all on the governance reporting line by default
(`CISO_LINE` can move security to the engineering line for the registered
sensitivity).
"""

from __future__ import annotations

import re

OFFICE_SECURITY = "office:security"
OFFICE_COMPLIANCE = "office:compliance"
OFFICE_SAFETY = "office:safety-lead"
OFFICE_LEGAL = "office:legal-counsel"
OFFICE_ACCESSIBILITY = "office:accessibility-lead"
OFFICE_OF = {"security": OFFICE_SECURITY, "compliance": OFFICE_COMPLIANCE, "safety": OFFICE_SAFETY,
             "legal": OFFICE_LEGAL, "accessibility": OFFICE_ACCESSIBILITY}

TAU_RISK = 30        # internal standards owned by security or safety
TAU_LEGAL = 25       # internal standards owned by legal or compliance

# company prefix -> family -> owner. Frozen from the consolidated review (Table "Family owners").
FAMILY_OWNER = {
    "VP": {"RB": "security", "SC": "security", "AS": "security",
           "VC": "safety", "PO": "safety", "AW": "safety", "PS": "safety", "PH": "safety",
           "CS": "compliance", "RR": "compliance", "DR": "compliance",
           "PD": "legal", "BN": "legal", "CC": "legal",
           "AI": "agent", "HA": "engineering", "GV": "apparatus", "AX": "accessibility"},
    "SF": {"RP": "security", "SS": "security", "CR": "security", "AS": "security", "OT": "security",
           "EH": "safety",
           "EX": "compliance", "WI": "compliance", "NC": "compliance", "IT": "compliance", "SO": "compliance",
           "RS": "compliance", "QS": "compliance",
           "DS": "legal", "AG": "agent", "SG": "engineering", "RT": "engineering", "TQ": "engineering",
           "GV": "apparatus"},
    "FL": {"MB": "security", "LS": "security", "SC": "security", "AS": "security", "WX": "security",
           "SF": "safety", "BS": "safety", "CS": "safety", "CB": "safety", "UH": "safety",
           "TR": "compliance",
           "TD": "legal", "PI": "legal", "IP": "legal", "PV": "legal",
           "AG": "agent", "EV": "engineering", "IN": "engineering", "FG": "engineering", "GV": "apparatus"},
    "DV": {"SC": "security", "TI": "security", "EV": "security", "TG": "security", "AP": "security",
           "OT": "security", "SV": "security",
           "AC": "safety", "LS": "safety",
           "EN": "compliance", "TC": "compliance",
           "DR": "legal", "LA": "legal", "CT": "legal",
           "AG": "agent", "QA": "engineering", "OP": "engineering", "AI": "engineering", "TL": "engineering",
           "KS": "engineering", "RS": "engineering", "GV": "apparatus", "AX": "accessibility"},
    "MF": {"PD": "security", "SS": "security", "SP": "security",
           "FC": "compliance", "FL": "compliance", "AI": "compliance", "EV": "compliance", "CP": "compliance",
           "RE": "compliance", "PS": "compliance", "FR": "compliance", "CN": "compliance", "FP": "compliance",
           "MP": "compliance", "VA": "compliance",
           "DP": "legal", "DA": "legal", "AG": "agent", "CQ": "engineering", "LG": "engineering",
           "PR": "engineering", "GV": "apparatus"},
}

_NOT_BINDING = re.compile(r"NIST SP|\bISO\b|ISO/IEC|SOC 2|SLSA|OpenSSF|\bCWE\b|benchmark|floor|practice policy|"
                          r"risk architecture|Chapter 5|commitment|threat model", re.I)
_BINDING = re.compile(r"U\.S\.C|\bUSC\b|\bCFR\b|\bArts?(icle)?\.? ?\d|Regulation \(EU\)|Reg\. \(EU\)|Directive|"
                      r"\bCode\b ?§|Pub\. ?L|\bGDPR\b|PCI DSS|contract|agreement|\bActs?\b|\blaws?\b|ILCS|NYCRR|"
                      r"\b[SA]B \d+|Stat\.|\bFR \d|OSHA|Rule \d|\bSR \d+-\d+|OCC Bulletin", re.I)


def company_of(pid: str) -> str:
    return pid.split("-", 1)[0]


def owner_of(prov: dict) -> str:
    if re.search(r"WCAG", prov.get("citation") or ""):
        return "accessibility"
    return FAMILY_OWNER.get(company_of(prov["id"]), {}).get(prov["family"], "engineering")


def binding(citation: str) -> bool:
    """A citation is binding when it names a statute, regulation, supervisory rule,
    PCI DSS, or a customer contract or agreement."""
    return bool(_BINDING.search(citation or ""))


def tier_of(prov: dict) -> tuple:
    """(tier, office, reason)."""
    status = prov.get("status", "in_force")
    if status == "advisory":
        return "T3", None, "status advisory"
    if status in ("deferred", "readiness"):
        return "T2", None, f"status {status}"
    if prov.get("absolute"):
        return "T0", None, "absolute"
    harms = set(prov.get("harm_classes") or [])
    S, L, R = "safety" in harms, "legal" in harms, "regulatory" in harms
    owner = owner_of(prov)
    cit = prov.get("citation") or ""
    says_safety = bool(re.search(r"safety", cit, re.I))
    if prov.get("released_absolute"):
        if owner in ("engineering", "apparatus", "accessibility"):
            return "T1", OFFICE_SAFETY if S else OFFICE_COMPLIANCE, "demoted absolute, T1 floor"
        if owner == "agent":
            return "T1", OFFICE_SAFETY if says_safety else OFFICE_SECURITY, "demoted absolute, T1 floor"
        return "T1", OFFICE_OF[owner], "demoted absolute, T1 floor"
    if not (S or L or R):
        return "T2", None, "no legal, regulatory or safety harm"
    tau = int(prov.get("tau", 0) or 0)
    if binding(cit):
        if owner in ("security", "legal", "compliance"):
            return "T1", OFFICE_OF[owner], f"binding citation, {owner}-owned"
        if owner == "safety":
            return "T1", OFFICE_SAFETY if S else OFFICE_COMPLIANCE, "binding citation, safety-owned"
        if owner == "agent":
            return "T1", OFFICE_SAFETY if says_safety else OFFICE_COMPLIANCE, "binding citation, agent rule"
        if owner in ("engineering", "apparatus"):
            return (("T1", OFFICE_COMPLIANCE, f"binding citation, {owner}-owned, legal or regulatory harm")
                    if (L or R) else ("T2", None, f"{owner}-owned"))
        return "T2", None, f"{owner}-owned"
    if owner in ("security", "agent") and tau <= TAU_RISK:
        return "T1", OFFICE_SAFETY if says_safety else OFFICE_SECURITY, f"internal standard, {owner}-owned, tau <= {TAU_RISK}"
    if owner == "safety" and S and tau <= TAU_RISK:
        return "T1", OFFICE_SAFETY, f"internal standard, safety-owned, tau <= {TAU_RISK}"
    if owner in ("legal", "compliance") and tau <= TAU_LEGAL:
        return "T1", OFFICE_OF[owner], f"internal standard, {owner}-owned, tau <= {TAU_LEGAL}"
    return "T2", None, f"internal standard, {owner}-owned"


__all__ = ["FAMILY_OWNER", "OFFICE_OF", "tier_of", "owner_of", "binding", "TAU_RISK", "TAU_LEGAL",
           "OFFICE_SECURITY", "OFFICE_COMPLIANCE", "OFFICE_SAFETY", "OFFICE_LEGAL", "OFFICE_ACCESSIBILITY"]
