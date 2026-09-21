#!/usr/bin/env python3
"""Absatzweise Erfassung der Formalisierung von BG-16 (de.bgb.verfuegungen, §§ 2064–2385).

Liest `sources.law` (Absatzgliederung je Paragraph aus dem amtlichen Text)
und alle `.law`-Module des Pakets (Regeln mit `label de official`, die
§-Nummer und optional "Abs. N" zitieren) und schreibt `analysis/saetze.json`:
eine Zeile je Absatz mit Status.

  RULE     — der Absatz wird von mindestens einer Regel ausdrücklich zitiert
             (Zeuge: die zitierenden Regelnamen).
  ANCHORED — der Paragraph trägt Regeln, aber keine nennt diesen Absatz
             ausdrücklich (Verweisung, Verfahren, Wiederholung — Näheres in
             `note`, wo bekannt).
  TODO     — der Paragraph trägt noch keine Regel (SOURCE_ONLY nach §33.1);
             offene Aufgabe, keine fachliche Grenze.

Manuelle Ausnahmen (BOUNDARY, abweichende Notizen) stehen in EXCEPTIONS
unten, nicht in der JSON — eine Neugenerierung verliert sie sonst.

Aufruf: python3 corpus/laws/de/bgb/verfuegungen/analysis/build_saetze.py
"""
import json
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[6]
PKG = ROOT / "corpus/laws/de/bgb/verfuegungen"
OUT = pathlib.Path(__file__).with_name("saetze.json")

# (Paragraph, Abs. als String wie im Text — "—" wenn ohne Gliederung) -> (Status, Note)
EXCEPTIONS = {
    # § 2109 (package.law, BG-15/BG-16-Vorbild): dreißigjährige Frist als
    # bloße Eingabe statt Kalenderrechnung — bewusst NICHT umgeschrieben
    # (Koordinatoranweisung 18.09.2026); § 2162 rechnet dagegen kalendarisch.
    # Kein EXCEPTIONS-Eintrag nötig: § 2109 bleibt RULE mit seinem Zeugen.
}


def load_abs_structure():
    """§ -> Liste der Abs.-Nummern (aus dem amtlichen Text, Muster '(N)' am Zeilenanfang)."""
    text = (PKG / "sources.law").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(
        r'@id\("[^"]*#BGB_P(\w+)"\).*?text de official """(.*?)"""', text, re.S
    ):
        para, body = m.group(1), m.group(2)
        abs_nums = sorted(set(re.findall(r"^\((\d+)\)", body, re.M)), key=int)
        out[para] = abs_nums or ["—"]
    return out


def load_rule_citations():
    """§ + Abs. -> Liste der Regelnamen, deren amtliches Label sie zitiert."""
    citations = {}
    for law_file in sorted(PKG.glob("*.law")):
        if law_file.name == "sources.law":
            continue
        text = law_file.read_text(encoding="utf-8")
        # Regel-/Vermutungsköpfe mit ihrem direkt folgenden amtlichen Label.
        for m in re.finditer(
            r'\b(?:rule|presumption)\s+(\w+)\s*\([^)]*\)\s*(?:strict\s*)?\{\s*'
            r'label de official "([^"]*)"',
            text,
        ):
            name, label = m.group(1), m.group(2)
            for pm in re.finditer(r"§\s*(\d+[a-z]?)(?:\s*Abs\.\s*(\d+))?", label):
                para, absn = pm.group(1), pm.group(2) or "—"
                citations.setdefault((para, absn), []).append(name)
    return citations


def load_paragraphs_with_any_rule():
    """§ -> True, wenn IRGENDEINE Regel/Vermutung im Paket ihn per @source trägt."""
    has_source = set()
    for law_file in sorted(PKG.glob("*.law")):
        if law_file.name == "sources.law":
            continue
        text = law_file.read_text(encoding="utf-8")
        for m in re.finditer(r"@source\(BGB_P(\w+)\)", text):
            has_source.add(m.group(1))
    return has_source


def main():
    abs_structure = load_abs_structure()
    citations = load_rule_citations()
    anchored = load_paragraphs_with_any_rule()

    out = {
        "$comment": (
            "Absatz-Karte des ganzen Pakets (§§ 2064-2385) mit Regelzeugen. "
            "RULE — mindestens eine Regel zitiert den Absatz ausdruecklich im "
            "amtlichen Label; ANCHORED — der Paragraph traegt Regeln, aber "
            "keine nennt diesen Absatz ausdruecklich (Verweisung, Verfahren, "
            "Wiederholung); TODO — der Paragraph traegt noch keine Regel "
            "(SOURCE_ONLY nach Mass 33.1, offene Aufgabe, keine Grenze). "
            "Generiert von analysis/build_saetze.py — Handkorrekturen stehen "
            "im Skript (EXCEPTIONS), nicht hier."
        )
    }

    for para in sorted(abs_structure, key=lambda p: (int(re.match(r"\d+", p).group()), p)):
        abs_list = abs_structure[para]
        para_entry = {}
        for absn in abs_list:
            key = (para, absn)
            if key in EXCEPTIONS:
                status, note = EXCEPTIONS[key]
            elif key in citations:
                status, note = "RULE", ""
            elif para in anchored:
                status, note = "ANCHORED", "Paragraph traegt Regeln, dieser Absatz wird von ihrem Text nicht ausdruecklich genannt (Verweisung, Verfahren oder Wiederholung)"
            else:
                status, note = "TODO", "noch nicht formalisiert (SOURCE_ONLY, Mass 33.1) — offene Aufgabe, keine fachliche Grenze"
            witness = ";".join(citations.get(key, []))
            para_entry[absn] = {"status": status, "witness": witness, "note": note}
        out[para] = para_entry

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total = sum(len(v) for k, v in out.items() if k != "$comment")
    rule = sum(1 for k, v in out.items() if k != "$comment" for e in v.values() if e["status"] == "RULE")
    anch = sum(1 for k, v in out.items() if k != "$comment" for e in v.values() if e["status"] == "ANCHORED")
    todo = sum(1 for k, v in out.items() if k != "$comment" for e in v.values() if e["status"] == "TODO")
    print(f"saetze.json: {len(out) - 1} Paragraphen, {total} Absaetze — RULE {rule}, ANCHORED {anch}, TODO {todo}")


if __name__ == "__main__":
    main()
