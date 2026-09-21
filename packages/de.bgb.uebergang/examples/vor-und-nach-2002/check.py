#!/usr/bin/env python3
"""Vor und nach 2002: Erwartungen aus den Fällen, Rust/Python und replay."""
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

UEBERGANG = "urn:de:corpus:clir:bgb-uebergang#"

TRUE = {"truth": "TRUE_ONLY"}
FALSE = {"truth": "NEITHER"}
KORRIDOR = {
    "truth": "TRUE_ONLY",
    "rule": UEBERGANG + "KorridorAnwendbar",
    "anchor": UEBERGANG + "EGBGB_ART229_P6",
}
KUERZER = {
    "truth": "TRUE_ONLY",
    "rule": UEBERGANG + "NeueFristKuerzer",
    "anchor": UEBERGANG + "EGBGB_ART229_P6",
}
LAENGER = {
    "truth": "TRUE_ONLY",
    "rule": UEBERGANG + "NeueFristLaenger",
    "anchor": UEBERGANG + "EGBGB_ART229_P6",
}
ENDE = {
    "truth": "TRUE_ONLY",
    "rule": UEBERGANG + "VollendungMitKuerzererNeuerFrist",
    "anchor": UEBERGANG + "EGBGB_ART229_P6",
}
ALT = {
    "truth": "TRUE_ONLY",
    "rule": UEBERGANG + "VollendungMitFrueherAblaufenderAlterFrist",
    "anchor": UEBERGANG + "EGBGB_ART229_P6",
}
NEU = {
    "truth": "TRUE_ONLY",
    "rule": UEBERGANG + "VollendungBeiLaengererNeuerFrist",
    "anchor": UEBERGANG + "EGBGB_ART229_P6",
}

EXPECTED = {
    "NeueFristAbStichtag": {
        "a01-korridor": KORRIDOR,
        "a01-kuerzer": KUERZER,
        "a01-ende": ENDE,
    },
    "AlteFristFrueher": {
        "a02-kuerzer": KUERZER,
        "a02-ende": ALT,
    },
    "AnspruchNachStichtag": {
        "a03-no-korridor": FALSE,
    },
    "NeueFristLaenger": {
        "a04-laenger": LAENGER,
        "a04-ende": NEU,
    },
}

if __name__ == "__main__":
    raise SystemExit(main(
        PACKAGE,
        EXPECTED,
        "vor und nach 2002",
        position_ns=UEBERGANG,
    ))
