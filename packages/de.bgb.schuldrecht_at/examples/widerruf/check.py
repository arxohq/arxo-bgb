#!/usr/bin/env python3
"""Widerruf: sechs Fälle, Rust/Python identity and replay."""
from pathlib import Path
import sys
PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE
while not (ROOT / "packs" / "examples" / "cases" / "collection_check.py").is_file():
    if ROOT.parent == ROOT: raise SystemExit("repository root not found")
    ROOT = ROOT.parent
sys.path.insert(0, str(ROOT / "packs" / "examples" / "cases"))
from collection_check import main
NS = "urn:de:corpus:clir:bgb-schuldrecht-at#"
FS = "urn:de:corpus:clir:bgb-fristen#"
TRUE = {"truth": "TRUE_ONLY"}
EXPECTED = {
    "WiderrufAmLetztenTag": {
        "widerruf-am-letzten-tag-ende": {**TRUE, "rule": NS + "DauerDerWiderrufsfristVierzehnTage", "anchor": NS + "BGB_P355"},
        "widerruf-am-letzten-tag-fristgerecht": {**TRUE, "rule": NS + "WiderrufIstFristgerecht", "anchor": NS + "BGB_P355"},
    },
    "WiderrufEinenTagZuSpaet": {
        "widerruf-einen-tag-zu-spaet-ende": {**TRUE, "rule": NS + "DauerDerWiderrufsfristVierzehnTage", "anchor": NS + "BGB_P355"},
        "widerruf-einen-tag-zu-spaet-fristgerecht": {"truth": "NEITHER"},
    },
    "WiderrufNachWochenende": {
        "widerruf-nach-wochenende-ende": {**TRUE, "rule": NS + "DauerDerWiderrufsfristVierzehnTage", "anchor": NS + "BGB_P355"},
        "widerruf-nach-wochenende-fristgerecht": {**TRUE, "rule": NS + "WiderrufIstFristgerecht", "anchor": NS + "BGB_P355"},
    },
    "WiderrufWerktag": {
        "widerruf-werktag-ende": {**TRUE, "rule": NS + "DauerDerWiderrufsfristVierzehnTage", "anchor": NS + "BGB_P355"},
        "widerruf-werktag-fristgerecht": {**TRUE, "rule": NS + "WiderrufIstFristgerecht", "anchor": NS + "BGB_P355"},
    },
    "WiderrufNachSpaeterUnterrichtung": {
        "widerruf-nach-spaeter-unterrichtung-ende": {**TRUE, "rule": NS + "DauerDerWiderrufsfristVierzehnTage", "anchor": NS + "BGB_P355"},
        "widerruf-nach-spaeter-unterrichtung-fristgerecht": {**TRUE, "rule": NS + "WiderrufIstFristgerecht", "anchor": NS + "BGB_P355"},
    },
    "WiderrufNachSpaeterUnterrichtungZuSpaet": {
        "widerruf-nach-spaeter-unterrichtung-zu-spaet-ende": {**TRUE, "rule": NS + "DauerDerWiderrufsfristVierzehnTage", "anchor": NS + "BGB_P355"},
        "widerruf-nach-spaeter-unterrichtung-zu-spaet-fristgerecht": {"truth": "NEITHER"},
    },
}
if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "widerruf"))
