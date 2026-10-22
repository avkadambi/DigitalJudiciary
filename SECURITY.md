# Security policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 5.15.x (current release) | Yes |
| Earlier releases | Best effort |

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security reports.

Email: **avkadambi@gmail.com**

Include:

* description of the issue and impact
* steps to reproduce or a proof of concept
* affected version / commit if known

You should receive an acknowledgement within a few business days.

## Scope notes for this system

* The **Challenge Gate** is the only component authorised to write precedent.
* Inbound webhooks must be HMAC-verified (`DJ_GITHUB_WEBHOOK_SECRET`).
* Break-glass is audited and does **not** create tier-1 precedent (Def. 7).
* API keys grant authority; treat them as secrets. Prefer OIDC in a later release.
* LLM judge keys must come from the environment / secret manager when `profile` is `enterprise` or `gcp`.

## Safe disclosure

We ask that you give us reasonable time to fix issues before public disclosure.
