#!/usr/bin/env python3
"""Kündigung und Mieterhöhung: six cases, Rust/Python identity and replay."""
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

MIETE = "urn:de:corpus:clir:bgb-miete#"
TRUE = {"truth": "TRUE_ONLY"}
NEITHER = {"truth": "NEITHER"}
GRUND = {**TRUE, "rule": MIETE + "Stufe573cGrundfrist", "anchor": MIETE + "BGB_P573c"}
FUENF = {**TRUE, "rule": MIETE + "Stufe573cFuenfJahre", "anchor": MIETE + "BGB_P573c"}
ACHT = {**TRUE, "rule": MIETE + "Stufe573cAchtJahre", "anchor": MIETE + "BGB_P573c"}
WERKTAG = {**TRUE, "rule": MIETE + "DritterWerktag573cAbs1Satz1", "anchor": MIETE + "BGB_P573c"}
KAPPUNG = {**TRUE, "rule": MIETE + "Kappungsgrenze558Abs3Satz1", "anchor": MIETE + "BGB_P558"}
ANSPRUCH = {**TRUE, "rule": MIETE + "Zustimmungsanspruch558Abs1", "anchor": MIETE + "BGB_P558"}

EXPECTED = {
    "KuendigungGrundstufe": {
        "grundstufe": GRUND,
        "fuenf-jahre": NEITHER,
        "acht-jahre": NEITHER,
        "dritter-werktag": WERKTAG,
        "ende": {**TRUE, "rule": MIETE + "Beendigungstag573cGrundstufe", "anchor": MIETE + "BGB_P573c"},
    },
    "KuendigungFuenfJahre": {
        "grundstufe": NEITHER,
        "fuenf-jahre": FUENF,
        "acht-jahre": NEITHER,
        "ende-fuenf": {**TRUE, "rule": MIETE + "Beendigungstag573cFuenfJahre", "anchor": MIETE + "BGB_P573c"},
    },
    "KuendigungAchtJahre": {
        "grundstufe": NEITHER,
        "fuenf-jahre": NEITHER,
        "acht-jahre": ACHT,
        "dritter-werktag-acht": WERKTAG,
        "ende-acht": {**TRUE, "rule": MIETE + "Beendigungstag573cAchtJahre", "anchor": MIETE + "BGB_P573c"},
    },
    "MieterhoehungBisKappungsgrenze": {
        "wartefrist": {**TRUE, "rule": MIETE + "Wartefrist558Abs1Satz1", "anchor": MIETE + "BGB_P558"},
        "kappung": KAPPUNG,
        "anspruch": ANSPRUCH,
        "ueberschritten": NEITHER,
    },
    "MieterhoehungUeberKappungsgrenze": {
        "kappung": KAPPUNG,
        "ueberschritten": {**TRUE, "rule": MIETE + "KappungsgrenzeUeberschritten558Abs3", "anchor": MIETE + "BGB_P558"},
        "anspruch": NEITHER,
    },
    "ZustimmungVerspaetet": {
        "fristende": {**TRUE, "rule": MIETE + "Zustimmungsfrist558bVerlegung193", "anchor": MIETE + "BGB_P558b"},
        "verspaetet": NEITHER,
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "kündigung und mieterhöhung"))
