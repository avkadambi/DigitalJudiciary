You run doctrine.write_gloss(canon, entry_id, holding, day): append {day, case, holding, act_class (default the entry's), outcome (default the holding)} to gloss.holdings; on a T1 entry with holding deny, add act_class to gloss.no_waiver_classes if absent; bump gloss.version. Tier, violate_factors, kind, office and canon_version never change.
Answer with one JSON object and nothing else.
