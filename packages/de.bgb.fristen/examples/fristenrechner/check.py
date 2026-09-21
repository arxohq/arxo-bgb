#!/usr/bin/env python3
"""Fristenrechner: status, rule, anchor, Rust/Python, replay."""
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
CLOSED = {"truth": "NEITHER"}

TAG = {
    "truth": "TRUE_ONLY",
    "rule": FR + "TagesfristEnde",
    "anchor": FR + "BGB_P187",
}
VERLEGUNG = {
    "truth": "TRUE_ONLY",
    "rule": FR + "Verlegung193",
    "anchor": FR + "BGB_P193",
}
KALENDER = {
    "truth": "TRUE_ONLY",
    "rule": FR + "KalenderfristEnde",
    "anchor": FR + "BGB_P188",
}
OHNE = {
    "truth": "TRUE_ONLY",
    "rule": FR + "VerjaehrungOhneHemmung",
    "anchor": FR + "BGB_P209",
}
MINDEST = {
    "truth": "TRUE_ONLY",
    "rule": FR + "VerjaehrungMitMindestfristMassgeblich",
    "anchor": FR + "BGB_P203",
}
KLAGE = {
    "truth": "TRUE_ONLY",
    "rule": FR + "VerjaehrungNachHemmungDurchRechtsverfolgung",
    "anchor": FR + "BGB_P204",
}
HOECHST = {
    "truth": "TRUE_ONLY",
    "rule": FR + "HoechstfristLebenKoerperGesundheitFreiheit",
    "anchor": FR + "BGB_P199",
}
ALTER = {
    "truth": "TRUE_ONLY",
    "rule": FR + "LebensjahrVollendet",
    "anchor": FR + "BGB_P187",
}

EXPECTED = {
    "Ereignisfrist14": {
        "ende-2026-03-20": TAG,
        "ende-2026-03-21": CLOSED,
    },
    "Samstag193": {
        "ende-2026-03-23": TAG,
        "ende-2026-03-21": CLOSED,
    },
    "UltimoMonatsfrist": {
        "kalender-2026-02-28": KALENDER,
        "ende-2026-03-02": VERLEGUNG,
        "ende-2026-02-28": CLOSED,
    },
    "VerjaehrungUltimo": {
        "verjaehrt-2023-12-31": OHNE,
        "verjaehrt-2023-12-30": CLOSED,
    },
    "Verhandlungen203": {
        "verjaehrt-2024-02-15": MINDEST,
        "verjaehrt-2024-01-15": CLOSED,
    },
    "Klageerhebung204": {
        "verjaehrt-2024-03-01": KLAGE,
        "verjaehrt-2023-12-31b": CLOSED,
    },
    "HoechstfristKoerper": {
        "hoechst-2040-05-01": HOECHST,
        "hoechst-2040-05-02": CLOSED,
    },
    "LebensjahrSchalt": {
        "alter-2025-02-27": ALTER,
        "alter-2025-02-28": CLOSED,
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "fristenrechner"))
