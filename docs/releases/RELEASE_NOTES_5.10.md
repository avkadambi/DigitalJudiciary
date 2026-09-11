# Release 5.10.0 — Numerals, the parent company (federation 1.0.0)

7 September 2026. Additive to 5.9.0. The five division packs are unchanged in
constitution, corpus, stores, docket and every conformance figure; their pack
version moves to 2.0.1 for one harness fix described below.

## What the release adds

**An enterprise constitution.** `simulation/numerals/` introduces Numerals, the
invented parent of VetPOC, SemiFab, FrontierLLM, DCVigil and Meridian. Thirty-three
enterprise provisions in six families (governance of the rulebook, agent-authored
change, application security, secrets and supply chain, change control and
resilience, people/privacy/accessibility/statutory clocks), each carrying
`level: enterprise` and a curated, id-level `implemented_by` map into the five
division constitutions as shipped. The recurring blocks the 5.9.0 survey found
copy-pasted across packs now have one home.

**Inheritance as minimum harmonisation.** A division may tighten an enterprise
provision and may never loosen one; an enterprise absolute is a floor in every
division. The build enforces the corollary the other way too: the enterprise may
not impose a floor over a frozen division constitution. Where the author requested
a floor and a division states the duty ordinarily, the provision is held ordinary
with `proposed_absolute: true` and a draft amendment is filed against the loosening
division provisions. Six floors stand; four are proposed and pending. That is A3
across levels.

**The inheritance survey's findings**, filed as 26 draft amendments and applied
nowhere: change control is under-provisioned outside Meridian (no other division
forbids self-approval; SemiFab and FrontierLLM have no rollback or freeze-window
provision), and CWE-level application security is absent from DCVigil and
Meridian. `docs/INHERITANCE.md` is the full map.

**A federated stream.** 3,000 changes filed by the five divisions against the
enterprise constitution and one shared store, with computed ground truth. Records
on enterprise provisions bind across divisions; a division's own record is
presented one scope step narrower than a foreign one, so the ordering rule's
existing scope key yields Chapter 4 §8's thin vertical precedent — one line in
`harness/federation.py`, and mutant MF1 shows it is the line that matters. Two new
categories: C-cross (bound by another division's record, 400 cases) and D-vertical
(home and foreign records both survive; home wins on scope, 100 cases); 200
cross-division like-case pairs; 250 cross-division pressure twins. Ten federation
checks, 6/6 faults killed, 2/2 controls survived, zero construction anomalies,
deterministic rebuild.

**A federated benchmark, offline.** Beside the monolith and advisory memory, a
division-local judiciary (`B_div`, five judiciaries that do not share a store) and
the federated judiciary (`B`). Under the oracle reader dispositions agree
everywhere; what separates the arms is structural — only an arm holding the
enterprise store cites the record another division wrote, and only the federated
judiciary does it without a model call (26.7% no-call against 14.9%).

## Harness fix (pack version 2.0.1)

`benchmark/arms.py` in every pack rated an arrival against τ before retrieving;
`engine.adjudicate` retrieves, gates and orders first and rates only when nothing
survives. The federated stream exposed it: arm B docketed two cross-division cases
the reference bound to a live record. Fixed in all six copies. No corpus,
conformance or mutation figure depends on the arm code.

## What it means for the papers

Chapter 7 lists federated jurisprudence under heterogeneous constitutions as
future work with no artefact; there is one now. Paper 4 §3.2 already presents the
five worlds to the human panel as product lines of one company; the federated
stream gives that framing a corpus and a new consistency endpoint — cross-division
pairs, disposition and citation — that the route-profile agreement of RQ3 does not
supply. The independent packs remain the RQ3 instrument; the federated stream is
reported beside them, never pooled with them.
