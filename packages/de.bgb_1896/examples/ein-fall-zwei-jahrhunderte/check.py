#!/usr/bin/env python3
"""Ein Fall, zwei Jahrhunderte: status, rule, anchor, Rust/Python, replay."""
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

OLD = "urn:de:corpus:clir:bgb-1896#"
FRISTEN = "urn:de:corpus:clir:bgb-fristen#"
NEITHER = {"truth": "NEITHER"}

V4_NOCH_NICHT = {
    "truth": "FALSE_ONLY",
    "rule": OLD + "RegelmaessigeVerjaehrungNochNicht",
    "anchor": OLD + "BGB_P195",
}
V4_HEUTE = {
    "truth": "TRUE_ONLY",
    "rule": FRISTEN + "RegelmaessigeVerjaehrungsfrist",
    "anchor": FRISTEN + "BGB_P195",
}
V31_ALT = {
    "truth": "TRUE_ONLY",
    "rule": OLD + "RegelmaessigeVerjaehrung",
    "anchor": OLD + "BGB_P195",
}
V31_EINREDE = {
    "truth": "TRUE_ONLY",
    "rule": OLD + "LeistungVerweigern",
    "anchor": OLD + "BGB_P222",
}
V31_HEUTE = {
    "truth": "TRUE_ONLY",
    "rule": FRISTEN + "RegelmaessigeVerjaehrungsfrist",
    "anchor": FRISTEN + "BGB_P195",
}
GELEISTET = {
    "truth": "TRUE_ONLY",
    "rule": OLD + "GeleistetesNichtZurueck",
    "anchor": OLD + "BGB_P222",
}

EXPECTED = {
    "VierJahre_1896": {
        "v4-1896-vollendet": V4_NOCH_NICHT,
        "v4-heute-verjaehrt": NEITHER,
    },
    "VierJahre_Heute": {
        "v4-1896-vollendet": NEITHER,
        "v4-heute-verjaehrt": V4_HEUTE,
    },
    "EinunddreissigJahre_1896": {
        "v31-1896-vollendet": V31_ALT,
        "v31-1896-einrede": V31_EINREDE,
        "v31-heute-verjaehrt": NEITHER,
    },
    "EinunddreissigJahre_Heute": {
        "v31-1896-vollendet": NEITHER,
        "v31-1896-einrede": NEITHER,
        "v31-heute-verjaehrt": V31_HEUTE,
    },
    "NachLeistung_1896": {
        "geleistet-1896": GELEISTET,
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "ein fall zwei jahrhunderte"))
