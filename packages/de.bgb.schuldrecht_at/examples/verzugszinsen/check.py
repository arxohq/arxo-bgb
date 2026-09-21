#!/usr/bin/env python3
"""Verzugszinsen: five cases, Rust/Python identity and replay."""
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

SR = "urn:de:corpus:clir:bgb-schuldrecht-at#"
TRUE = {"truth": "TRUE_ONLY"}

EXPECTED = {
    "VerbraucherFuenfPunkte": {
        "v01-6-52": {**TRUE, "rule": SR + "VerzugszinssatzFuenfProzentpunkteUeberDemBasiszinssatz", "anchor": SR + "BGB_P288"},
        "v01-652-euro": {**TRUE, "rule": SR + "VerzugszinsenFuerEinVollesJahr", "anchor": SR + "BGB_P288"},
    },
    "UnternehmerNeunPunkte": {
        "v02-10-52": {**TRUE, "rule": SR + "VerzugszinssatzNeunProzentpunkteBeiEntgeltforderungenOhneVerbraucher", "anchor": SR + "BGB_P288"},
        "v02-526-euro": {**TRUE, "rule": SR + "VerzugszinsenFuerEinVollesJahr", "anchor": SR + "BGB_P288"},
    },
    "PauschaleVierzigEuro": {
        "v03-40-euro": {**TRUE, "rule": SR + "PauschaleVierzigEuroBeiEntgeltforderung", "anchor": SR + "BGB_P288"},
        "v03-110-euro": {**TRUE, "rule": SR + "PauschaleWirdAufRechtsverfolgungskostenAngerechnet", "anchor": SR + "BGB_P288"},
    },
    "HalbjahrwechselBasiszinssatz": {
        "v04-6-27": {**TRUE, "rule": SR + "VerzugszinssatzFuenfProzentpunkteUeberDemBasiszinssatz", "anchor": SR + "BGB_P288"},
    },
    "VerzugOhneMahnung": {
        "v05-verzug-ab-1-august": {**TRUE, "rule": SR + "VerzugOhneMahnungBeiKalendermaessigerLeistungszeit", "anchor": SR + "BGB_P286"},
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "verzugszinsen"))
