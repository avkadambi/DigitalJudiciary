"""Benchmark configuration: models, prices, arms, and the defaults.

Prices are per million tokens, read from the Claude pricing page on
6 September 2026. They are data, not constants of nature — check them before
quoting a cost figure in a paper.
"""

PRICES = {
    # model id                      (input $/MTok, output $/MTok)
    "claude-opus-5":                (5.00, 25.00),
    "claude-sonnet-5":              (2.00, 10.00),
    "claude-haiku-4-5":             (1.00,  5.00),
}

ALIASES = {"opus": "claude-opus-5", "sonnet": "claude-sonnet-5", "haiku": "claude-haiku-4-5"}

CACHE_READ_MULT = 0.10     # a cache hit costs 0.1x base input
CACHE_WRITE_MULT = 1.25    # a 5-minute cache write costs 1.25x base input
BATCH_MULT = 0.50          # the batch API is 50% off input and output

# --------------------------------------------------------------------------
# The arms.
#
# Every arm answers the same question about the same case: what is the
# disposition, and which record controls. What differs is what the arm is
# allowed to see and whether a retrieved record BINDS it.
#
#   sees_constitution   the full rulebook in the prompt
#   store_view          none | topk | gated | log
#   binds               does a controlling record determine the disposition
#                       without a model call
#   k_records           how many records the prompt carries
# --------------------------------------------------------------------------

ARMS = {
    "A": {
        "label": "Monolith — whole constitution, no case base",
        "sees_constitution": True, "store_view": "none", "binds": False, "k_records": 0,
        "note": ("The frontier-model-per-case baseline. It has the rules and the "
                 "change and nothing else, so it cannot cite and cannot be bound. "
                 "This is the arm that answers 'why not just use a big model'."),
    },
    "A+": {
        "label": "Monolith + retrieval — constitution and the top-k records, ungated",
        "sees_constitution": True, "store_view": "topk", "binds": False, "k_records": 40,
        "note": ("The fair RAG comparison: the same records the judiciary would "
                 "retrieve, but unordered and ungated, and advisory. It must pick "
                 "the controlling record itself."),
    },
    "B_mem": {
        "label": "Advisory memory — gated survivors shown as advice",
        "sees_constitution": True, "store_view": "gated", "binds": False, "k_records": 8,
        "note": ("Chapter 5 Definition 13. Retrieval and the gate are the "
                 "architecture's own, so the comparison isolates bindingness "
                 "rather than confounding it with retrieval quality."),
    },
    "B_gov": {
        "label": "Governed exception log — attribution without precedent",
        "sees_constitution": True, "store_view": "log", "binds": False, "k_records": 3,
        "note": ("Chapter 5 Definition 12. The log says who accepted what. It "
                 "holds no relation between cases, so no earlier decision can "
                 "control this one."),
    },
    "B": {
        "label": "Digital Judiciary — engine retrieves, gates and orders",
        "sees_constitution": False, "store_view": "gated", "binds": True, "k_records": 6,
        "note": ("The model is asked only where the architecture asks anyone: a "
                 "fresh interpretation when no record controls. Absolutes, "
                 "citations and docketed arrivals never reach it, which is what "
                 "R7 predicts and what this harness measures."),
    },
}

DEFAULTS = {
    "cases": 6000,
    "runs": 1,
    "k": 1,                      # attempts per case; Chapter 6 uses 8 for pass^8
    "arms": ["A", "A+", "B_mem", "B_gov", "B"],
    "models": ["claude-sonnet-5"],
    "mode": "oracle",
    "batch": True,
    "cache": True,
    "seed": 20260906,
}

# Tokens per character, for the dry-run estimator. Measured against this
# corpus's own JSON, which is denser than prose.
CHARS_PER_TOKEN = 3.7
