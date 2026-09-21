#!/usr/bin/env python3
"""Karte der Rechtsbehelfe: Rust/Python identity and replay."""
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

NS = "urn:de:corpus:clir:bgb-schuldrecht-at#"
TRUE = {"truth": "TRUE_ONLY"}

EXPECTED = {
    "Fristsetzung": {
        "fristsetzung": {
            **TRUE,
            "rule": NS + "RuecktrittNachErfolgloserFristsetzung",
            "anchor": NS + "BGB_P323",
        },
    },
    "Unmoeglichkeit": {
        "unmoeglichkeit": {
            **TRUE,
            "rule": NS + "WegfallDerGegenleistungBeiAusschlussDerLeistungspflicht",
            "anchor": NS + "BGB_P326",
        },
    },
    "KaufmangelNacherfuellung": {
        "kaufmangel-nacherfuellung": {
            **TRUE,
            "rule": NS + "RuecktrittOhneFristBeiErnsthafterVerweigerung",
            "anchor": NS + "BGB_P323",
        },
    },
    "KaufmangelMinderung": {
        "kaufmangel-minderung": {
            **TRUE,
            "rule": NS + "RuecktrittOhneFristBeiWesentlicherTermintreue",
            "anchor": NS + "BGB_P323",
        },
    },
    "RuecktrittRueckgewaehr": {
        "ruecktritt-rueckgewaehr": {
            **TRUE,
            "rule": NS + "RueckgewaehrNachVertraglichemRuecktritt",
            "anchor": NS + "BGB_P346",
        },
    },
    "Werkmangel": {
        "werkmangel": {
            **TRUE,
            "rule": NS + "RuecktrittBeiAusschlussDerLeistungspflicht",
            "anchor": NS + "BGB_P326",
        },
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "rechtsbehelfe"))
