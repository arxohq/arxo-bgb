#!/usr/bin/env python3
"""Erbfolge und Pflichtteil: status, rule, anchor, Rust/Python, replay."""
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

ERB = "urn:de:corpus:clir:bgb-erbfolge#"
VERF = "urn:de:corpus:clir:bgb-verfuegungen#"
CLOSED = {"truth": "NEITHER"}

BRUCH = {"truth": "TRUE_ONLY"}
SUMME = {
    "truth": "TRUE_ONLY",
    "rule": ERB + "ErbschaftVollstaendigVerteilt",
    "anchor": ERB + "BGB_P1922",
}
AUSGESCHLAGEN = {
    "truth": "TRUE_ONLY",
    "rule": ERB + "AusschlagungWirksam",
    "anchor": ERB + "BGB_P1945",
}
FRIST = {
    "truth": "TRUE_ONLY",
    "rule": ERB + "AusschlagungsfristVerstrichen",
    "anchor": ERB + "BGB_P1944",
}
ANGENOMMEN = {
    "truth": "TRUE_ONLY",
    "rule": ERB + "FristablaufGiltAlsAnnahme",
    "anchor": ERB + "BGB_P1943",
}
QUOTE = {
    "truth": "TRUE_ONLY",
    "rule": VERF + "PflichtteilsquoteAlsBruch",
    "anchor": VERF + "BGB_P2303",
}
GELD = {
    "truth": "TRUE_ONLY",
    "rule": VERF + "PflichtteilAlsGeld",
    "anchor": VERF + "BGB_P2311",
}
GERICHT = {
    "truth": "NEITHER",
    "evaluation": "REQUIRES_JUDGMENT",
}

EXPECTED = {
    "StammZweiKinder": {
        "teil-s-halb": BRUCH,
        "teil-c1-viertel": BRUCH,
        "teil-g1-achtel": BRUCH,
        "teil-s-drittel": CLOSED,
        "teil-c1-drittel": CLOSED,
        "summe-eins": SUMME,
    },
    "GuetertrennungZweiKinder": {
        "teil-s-halb": CLOSED,
        "teil-c1-viertel": CLOSED,
        "teil-g1-achtel": CLOSED,
        "teil-s-drittel": BRUCH,
        "teil-c1-drittel": BRUCH,
        "summe-eins": SUMME,
    },
    "ZugewinnEltern": {
        "teil-s-dreiviertel": BRUCH,
        "teil-m-achtel": BRUCH,
        "teil-v-halb": CLOSED,
        "summe-eins": SUMME,
    },
    "ZweiteOrdnung": {
        "teil-s-dreiviertel": CLOSED,
        "teil-m-achtel": CLOSED,
        "teil-v-halb": BRUCH,
        "teil-b-viertel": BRUCH,
        "teil-n-viertel": BRUCH,
        "summe-eins": SUMME,
    },
    "AusschlagungStamm": {
        "ausgeschlagen-c1": AUSGESCHLAGEN,
        "teil-g1-halb": {"truth": "TRUE_ONLY"},
        "frist-verstrichen": CLOSED,
        "gilt-angenommen": CLOSED,
    },
    "AusschlagungZuSpaet": {
        "ausgeschlagen-c1": CLOSED,
        "teil-g1-halb": CLOSED,
        "frist-verstrichen": FRIST,
        "gilt-angenommen": ANGENOMMEN,
    },
    "PflichtteilTochter": {
        "pflichtteilsquote-c1": QUOTE,
        "pflichtteil-c1": GELD,
    },
    "EntziehungOffen": {
        "entziehbar-c1": GERICHT,
    },
}

if __name__ == "__main__":
    raise SystemExit(main(
        PACKAGE, EXPECTED, "erbfolge und pflichtteil",
        position_ns=ERB,
    ))
