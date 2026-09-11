# Release notes — 5.5 (review experience)

**Nothing below the presentation layer changed.** The Kernel, the Challenge
Gate, the axioms, the ledger, the connectors, the HTTP surface, the routes,
the workers and every conformance suite are untouched. 5.5 rewrites
`app/reviewui.py` only. The 5.4 screens are preserved verbatim at
`app/reviewui_v54_legacy.py` if you need to diff or revert.

## Why

Two findings from the pilot:

1. **It read as a system for people who already understood it.** Screens led
   with provision ids, tiers, dispositions and holdings. A risk owner needed
   the architecture in their head before they could act.
2. **It could not be used on a phone.** The one job that is genuinely urgent
   and genuinely mobile — a named person signing off a blocked change — was a
   desktop-only, multi-column docket sheet.

## What changed

### Plain language, same rigour

The vocabulary is now the reader's, not the paper's. Every guarantee is
unchanged and still stated — just in words that tell you what to do.

| Was | Now |
|---|---|
| Your desk / Legislature / Ledger / Rulebook / Analytics | Your work / Rule changes / Past rulings / Rules / Cost |
| "This decision is not yours to make" | "You can read this, but not sign it" — and the account's powers are now stated on sign-in, before you spend three clicks |
| "Provision engaged" + provision text | "What the rule says", quoted, with the id as a footnote |
| Tier ladder with chain stamps | "Automatic check → Looked at again → You" |
| `blocked_absolute`, "an absolute floor" | "There is no way around this one" / "cannot be waived by anyone" |
| "challenge", "request a human" | "say the rule does not apply", "ask a person" |

### The queue is an inbox

`queue_page` groups by whether the decision is yours, gives every row one
sentence of plain English derived from the provision, and makes the age the
loudest thing on a row older than five days.

### One decision, one screen

`task_page` is restructured as **the question → what happened → what the rule
says → how it reached you → your decision**. Identifiers, precedent consulted
and provenance move into a disclosure drawer: they are evidence, not the
argument.

Two refusals that carry constitutional weight are unchanged:

* when Proposition 2 bars an acceptance, the accept control is **absent**, not
  disabled;
* the end date sits **inside the sentence being signed**, because A7 makes it
  constitutive of the act. It now also offers 7 / 30 / 90-day presets which
  set the same `expiry` field — the server contract is identical.

### The blocked engineer gets routes, not a disposition

`change_page` leads with **Ways forward**, numbered, each labelled with what
it costs ("fastest", "minutes", "usually days"). The lanes are still read from
`lanes_for`, the same function that annotates GitHub, so the screen cannot
offer an exit the architecture does not. When the rule is absolute there is
one panel saying so plainly, and no controls.

### Every desk gets the theme

`desk_page` (all four roles including the auditor), `ledger_page`,
`changes_page`, `amendments_page`, `impact_page`, `analytics_page`,
`activity_page`, `judge_activity_page`, the rulebook pages and the simulator
console all pick up the new type, palette, section headings, rounded cards,
44px controls and mobile behaviour. Their markup is largely unchanged — 5.4's
class names were retained and restyled — with page titles, subnav labels and
the shared lane vocabulary rewritten in plain language.

### Usable on a phone

* A five-item bottom tab bar under 760px; the full desk row above it.
* Single-column decision, change and record screens.
* 44px minimum touch targets on every control; full-width actions.
* The `.reg` register rows (ledger, changes, activity, the desk, clause-by-
  clause) stack instead of starving their flexible column to zero.
* Sticky identity bar, safe-area padding, filters that wrap to full width.

### Sign-in states the powers

`login_page` says what the account can do before you use it, in one sentence,
instead of after you have read a whole case. The live-run panel and the
development roster are unchanged in behaviour.

## Compatibility

* Every function signature in `reviewui.py` is unchanged. `httpapi.py` was not
  touched.
* Every route, form action, field name and CSRF contract is unchanged.
* `BRANCH_LABEL` is retained; `ROLE_CAN`, `_ago()`, `_plain_why()` and `grp()`
  are added.
* 5.4 CSS class names are retained and restyled, so any screen not listed
  above still renders correctly.
* `run_conformance.py`, `run_interface_conformance.py` and
  `run_extension_conformance.py` assert on traces and the interface contract,
  not on markup, and are unaffected.

## Still to do

* Notifications: a signed decision should reach the requesting engineer
  without them polling a page.
* The impact desk would read better with the one-sentence answer generated
  from the metrics rather than assembled in the template.
* Batch decisions for the risk owner: eleven near-identical waivers on the
  same rule are one decision, not eleven.
