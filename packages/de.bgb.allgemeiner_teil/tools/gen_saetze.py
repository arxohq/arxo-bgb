#!/usr/bin/env python3
"""Absatzinventar des Pakets BG-03: welche Inhalte jeder Paragraph des Umfangs trägt.

Für jeden Paragraphen des Registers (`sources/<act>/articles.json` und der
festgeschriebene Text) werden Absätze und Sätze gezählt sowie Regeln,
Urteilskanäle nach § 47.3 und Lesarten nach § 152 gesammelt, die in den
`.law`-Dateien des Pakets daran verankert sind. Die Ausgabe ist
`analysis/saetze.json`. Verankerungen werden aus den Quellen (`@source(...)`
über der Deklaration), nicht aus dem CLIR gelesen; dadurch bleibt die Aufzeichnung
auch vor einer erneuten CLIR-Erzeugung korrekt.

    python3 corpus/laws/de/bgb/allgemeiner-teil/tools/gen_saetze.py          # schreiben
    python3 corpus/laws/de/bgb/allgemeiner-teil/tools/gen_saetze.py --check  # prüfen
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PKG = Path(__file__).resolve().parents[1]
ACT = "de-bgb-allgemeiner-teil"
TEXT = PKG / "sources" / ACT / "bgb-de.txt"
ARTICLES = PKG / "sources" / ACT / "articles.json"
REGISTRY = PKG.parents[4] / "docs/foundations/de-bgb/registry/DOKNR.json"
OUT = PKG / "analysis" / "saetze.json"

PARAGRAPH = re.compile(r"^§ (\d+[a-z]?) (.*)$")
ABSATZ = re.compile(r"^\((\d+)\)")
ANCHOR = re.compile(r"^@source\(([^)]*)\)\s*$")
DECL = re.compile(r"^(?:pub )?(rule|external judgment relation|interpretation|definition)\s+(\w+)")
PUB_JUDGMENT = re.compile(r"^pub external judgment relation (\w+)")


def paragraphs() -> dict[str, dict]:
    """Absätze und Sätze jedes Paragraphen aus dem festgeschriebenen Text."""
    text = TEXT.read_text(encoding="utf-8").splitlines()
    out: dict[str, dict] = {}
    current: dict | None = None
    for line in text:
        head = PARAGRAPH.match(line)
        if head:
            current = {"paragraph": head.group(1), "title": head.group(2).strip(),
                       "absaetze": 0, "saetze": 0, "regeln": [], "urteilskanaele": [],
                       "lesarten": []}
            out[head.group(1)] = current
            continue
        if current is None or not line.strip():
            continue
        if ABSATZ.match(line):
            current["absaetze"] += 1
        current["saetze"] += len(re.findall(r"[.!?](?:\s|$)", line))
    # Die Zahl der Absätze nimmt das Register (eine Zeile je Absatz); der
    # gerenderte Text zählt Aufzählungen sonst als eigene Absätze.
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    for norm in registry.get("norms", []):
        number = norm.get("number")
        if number in out and norm.get("status") == "in_force":
            out[number]["absaetze"] = len(norm.get("lines", []))
    return out


def anchors(rows: dict[str, dict]) -> None:
    """Regeln, Kanäle und Lesarten, die in den Quellen am Paragraphen verankert sind."""
    for law in sorted(PKG.glob("*.law")):
        if law.name == "sources.law":
            continue
        pending: list[str] = []
        for line in law.read_text(encoding="utf-8").splitlines():
            anchor = ANCHOR.match(line.strip())
            if anchor:
                pending = [frag.strip() for frag in anchor.group(1).split(",")]
                continue
            stripped = line.strip()
            judgment = PUB_JUDGMENT.match(stripped)
            decl = DECL.match(stripped)
            interpretation = stripped.startswith("interpretation ")
            if not (judgment or decl or interpretation):
                continue
            targets = pending
            pending = []
            if not targets:
                continue
            name = (judgment.group(1) if judgment
                    else stripped.split()[1] if interpretation
                    else decl.group(2))
            bucket = ("urteilskanaele" if judgment
                      else "lesarten" if interpretation
                      else "regeln")
            for frag in targets:
                number = frag.replace("BGB_P", "")
                row = rows.get(number)
                if row is not None and name not in row[bucket]:
                    row[bucket].append(name)
    # Lesarten nach § 152 werden innerhalb von `interpretation … of` ohne @source erklärt.
    pattern = re.compile(r"^interpretation (\w+) of BGB_P(\d+[a-z]?)")
    for law in sorted(PKG.glob("*.law")):
        for line in law.read_text(encoding="utf-8").splitlines():
            match = pattern.match(line.strip())
            if match and match.group(2) in rows:
                row = rows[match.group(2)]
                if match.group(1) not in row["lesarten"]:
                    row["lesarten"].append(match.group(1))


def build() -> dict:
    rows = paragraphs()
    anchors(rows)
    declared = {}
    articles = json.loads(ARTICLES.read_text(encoding="utf-8"))
    for edition in articles.get("editions", []):
        declared.update(edition.get("declared", {}))
    for number, reason in declared.items():
        if number in rows:
            rows[number]["boundary"] = reason
    return {
        "$comment": "Absatzinventar von BG-03: Absätze und Sätze jedes Paragraphen "
                    "gegenüber den daran verankerten Regeln, Urteilskanälen nach § 47.3 "
                    "und Lesarten nach § 152. Erzeugt von tools/gen_saetze.py — nicht manuell bearbeiten.",
        "act": ACT,
        "legal_cutoff": articles.get("legal_cutoff"),
        "counts": {
            "paragraphs": len(rows),
            "absaetze": sum(row["absaetze"] for row in rows.values()),
            "regeln": sum(len(row["regeln"]) for row in rows.values()),
            "urteilskanaele": sum(len(row["urteilskanaele"]) for row in rows.values()),
            "lesarten": sum(len(row["lesarten"]) for row in rows.values()),
            "ohne_regel": sorted(number for number, row in rows.items() if not row["regeln"]),
        },
        "paragraphs": [rows[key] for key in sorted(rows, key=lambda n: (int(re.sub(r"\D", "", n)), n))],
    }


def main() -> int:
    data = build()
    rendered = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        if not OUT.is_file() or OUT.read_text(encoding="utf-8") != rendered:
            print(f"gen_saetze: {OUT} weicht von der Quelle ab")
            return 1
        print("gen_saetze: OK")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(rendered, encoding="utf-8")
    print(f"gen_saetze: geschrieben {OUT.relative_to(PKG)}: "
          f"{data['counts']['paragraphs']} Paragraphen, {data['counts']['absaetze']} Absätze, "
          f"{data['counts']['regeln']} Regeln, {data['counts']['urteilskanaele']} Kanäle, "
          f"{data['counts']['lesarten']} Lesarten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
