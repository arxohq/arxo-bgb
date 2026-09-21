#!/usr/bin/env python3
"""Ein Fall, drei Kodizes: status, rule, anchor, Rust/Python, replay."""
from pathlib import Path
import sys

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE
while not (ROOT / "packs" / "examples" / "cases" / "collection_check.py").is_file():
    if ROOT.parent == ROOT:
        raise SystemExit("repository root not found")
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / "packs" / "examples" / "cases"))
from collection_check import main  # noqa: E402

FR = "urn:de:corpus:clir:bgb-fristen#"
IP = "urn:de:corpus:clir:bgb-ius-privatum#"
CC = "urn:fr:corpus:clir:code-civil#"
PICC = "urn:org:unidroit:clir:picc-limitation#"
NEITHER = {"truth": "NEITHER"}

BGB_2013 = {
    "truth": "TRUE_ONLY",
    "rule": FR + "RegelmaessigeVerjaehrungsfrist",
    "anchor": FR + "BGB_P195",
}
# Living BGB proves the day Verjährung enters, not that a wrong day is false
# (`so01` expects NEITHER the day before). No negative rule is added here:
# that would rebuild de.bgb.fristen and the ten ZPO snapshots.
BGB_2016_OFFEN = {"truth": "NEITHER"}
CC_JA = {
    "truth": "TRUE_ONLY",
    "rule": CC + "ActionPrescriteApresEcheance",
    "anchor": CC + "CC_POST_ART2219",
}
CC_NEIN = {
    "truth": "FALSE_ONLY",
    "rule": CC + "ActionNonPrescriteAvantOuAEcheance",
    "anchor": CC + "CC_POST_ART2219",
}
IUS_BGB = {
    "truth": "TRUE_ONLY",
    "rule": IP + "EinredeExcludit",
}
IUS_CC = {
    "truth": "TRUE_ONLY",
    "rule": CC + "PrescriptionExcludit",
    "anchor": CC + "CC_POST_ART2219",
}
IUS_PICC = {
    "truth": "TRUE_ONLY",
    "rule": PICC + "ExpiryExcludit",
    "anchor": PICC + "PICC_ART10_9_EN",
}

EXPECTED = {
    "FuenfJahre_BGB": {
        "bgb-2013-12-31": BGB_2013,
        "cc-prescrite": NEITHER,
        "remedium-exclusum": IUS_BGB,
    },
    "FuenfJahre_CC": {
        "bgb-2013-12-31": NEITHER,
        "cc-prescrite": CC_JA,
        "remedium-exclusum": IUS_CC,
    },
    "FuenfJahre_PICC": {
        "bgb-2013-12-31": NEITHER,
        "cc-prescrite": NEITHER,
        "remedium-exclusum": IUS_PICC,
    },
    "ZweiJahre_BGB": {
        "bgb-2016-12-31": BGB_2016_OFFEN,
        "cc-prescrite": NEITHER,
        "remedium-exclusum": NEITHER,
    },
    "ZweiJahre_CC": {
        "bgb-2016-12-31": NEITHER,
        "cc-prescrite": CC_NEIN,
        "remedium-exclusum": NEITHER,
    },
    "ZweiJahre_PICC": {
        "bgb-2016-12-31": NEITHER,
        "cc-prescrite": NEITHER,
        "remedium-exclusum": NEITHER,
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "ein fall drei kodizes"))
