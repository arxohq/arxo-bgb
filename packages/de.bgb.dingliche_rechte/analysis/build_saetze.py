#!/usr/bin/env python3
"""Absatzweise Erfassung der Formalisierung von BG-11 (de.bgb.dingliche_rechte).

Liest den festgeschriebenen Pakettext und den CLIR des Gesetzes und schreibt
analysis/saetze.json: eine Zeile je Absatz mit seinem Status.

  EXECUTED — der Absatz wird durch Paketregeln ausgeführt (der Paragraph hat
             eine Regel und der Absatz ist in Label oder Abschnittskommentar genannt);
  TODO     — nicht in diesem Schnitt (KEINE Grenze: Arbeit zurückgestellt,
             Schritt im HANDOFF-Abschnitt der Statusdatei genannt);
  BOUNDARY — aus dem Normtext erklärte Grenze (externes Verfahren).

Der Paragraphenstatus wird aus dem CLIR übernommen: Ein Paragraph mit einer
Regel erhält für alle Absätze EXECUTED, außer den in EXCEPTIONS genannten.
Manuelle Ausnahmen stehen hier statt im JSON, damit eine Neuerzeugung sie nicht verliert.

Aufruf: python3 corpus/laws/de/bgb/dingliche-rechte/analysis/build_saetze.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[6]
PKG = ROOT / "corpus/laws/de/bgb/dingliche-rechte"
TEXT = PKG / "sources/de-bgb-dingliche-rechte/bgb-de.txt"
CLIR = ROOT / "corpus/clir/de-bgb-dingliche-rechte.lawir.json"
OUT = pathlib.Path(__file__).with_name("saetze.json")

# Absätze, die das Paket trotz vorhandener Paragraphenregeln NICHT ausführt.
# Der Grund folgt aus dem Normtext; externe Verfahren werden als BOUNDARY erklärt.
EXCEPTIONS = {
    ("1128", "3"): ("BOUNDARY", "„Im Übrigen finden die für eine verpfändete Forderung geltenden Vorschriften Anwendung“ — Verweisung auf §§ 1273 ff.; Abschnitt 8 gehört nicht zu diesem Schnitt"),
    ("1134", "2"): ("EXECUTED", "Das Zivilverfahren bleibt außerhalb des Pakets: die Norm begründet eine Gerichtspflicht, nicht deren Vollzugsverfahren"),
    ("1141", "2"): ("BOUNDARY", "Bestellung eines Vertreters durch das Amtsgericht — FamFG-Verfahren, externes Verfahren"),
    ("1145", "1"): ("EXECUTED", "Satz 2 (Vermerk auf dem Brief) — Pflicht des Gläubigers, als Recht des Eigentümers abgeleitet"),
    ("1145", "2"): ("TODO", "Kalendervierteljahr für § 1145 Abs. 2 ist eingerichtet (kalendervierteljahr_endet_am), Regel zurückgestellt"),
    ("1154", "3"): ("BOUNDARY", "„finden die Vorschriften der §§ 873, 878 entsprechende Anwendung“ — Kopf des Nachbarpakets BG-10, Brücke bei der Zusammenführung"),
    ("1155", "2"): ("BOUNDARY", "gerichtlicher Überweisungsbeschluss — Prozesshandlung, externer Eingang"),
    ("1162", "—"): ("BOUNDARY", "Aufgebotsverfahren — FamFG-Verfahren; das Paket leitet nur die Zulässigkeit ab"),
    ("1171", "1"): ("BOUNDARY", "Satz 2 zur Hinterlegung der Zinsen — Verfahren nach der Hinterlegungsordnung, externes Verfahren"),
    ("1179a", "3"): ("TODO", "Sonderfall des § 1163 ohne Eintragung im Buch — zurückgestellt"),
    ("1179a", "4"): ("TODO", "Rangrücktritt und sein Datum — zurückgestellt"),
    ("1179a", "5"): ("EXECUTED", "die Ausnahme des Löschungsanspruchs wird durch den Eingang loeschungsanspruch_ausgeschlossen_vereinbart ausgeführt"),
    ("1188", "2"): ("EXECUTED", "Vorlegungsfrist nach § 801 — Falleingang, zwei Textzweige"),
    # --- Abschnitt 8: Absätze, die das Paket trotz vorhandener Paragraphenregeln NICHT ausführt
    ("1214", "1"): ("TODO", "Pflicht zur Sorge für den Fruchtbezug und zur Rechnungslegung — Verhältnis der Beteiligten, zurückgestellt"),
    ("1216", "—"): ("TODO", "Verweisung auf Geschäftsführung ohne Auftrag (§§ 677 ff., Paket BG-08) — Brücke bei der Zusammenführung; nur das Recht auf Entfernung der Vorrichtung (Satz 2) ist abgeleitet"),
    ("1217", "2"): ("TODO", "gestaffelter Betrag bei unverzinslicher, noch nicht fälliger Forderung — dieselbe offene Größe wie in § 1133 Satz 3 (D-Q11-1)"),
    ("1219", "2"): ("EXECUTED", "Erlös tritt an die Stelle des Pfands; Hinterlegung auf Verlangen des Pfandbestellers — Verfahren nach der Hinterlegungsordnung, extern"),
    ("1233", "1"): ("EXECUTED", "Verweisungsnorm: das Verkaufsverfahren ist in §§ 1234–1240 geregelt, die ausgeführt werden"),
    ("1236", "—"): ("BOUNDARY", "§ 383 Abs. 2 — Ablauf der Versteigerung; fremder Paragraph (BG-08), die Durchführung wird als Fall eingegeben"),
    ("1237", "—"): ("EXECUTED", "Satz 1 (§ 383 Abs. 3) — Falleingang; Satz 2 (besondere Anzeige) abgeleitet"),
    ("1245", "1"): ("EXECUTED", "Drei Sätze werden ausgeführt: Vereinbarung, Zustimmung des Dritten, Unwiderruflichkeit"),
    ("1246", "2"): ("BOUNDARY", "„so entscheidet das Gericht“ — Verfahrensnorm, keine Ableitungsregel des Pakets"),
    ("1251", "2"): ("TODO", "Haftung des früheren Pfandgläubigers als Bürge (§ 771) — Brücke zu BG-08, zurückgestellt"),
    ("1258", "1"): ("TODO", "Ausübung der Rechte der Miteigentümergemeinschaft (§§ 744 ff.) — Brücke zu BG-08, zurückgestellt"),
    ("1258", "3"): ("TODO", "Pfandrecht an Gegenständen, die den Anteil nach der Teilung ersetzen — zurückgestellt"),
    ("1258", "4"): ("TODO", "das Recht zum Verkauf des Anteils bleibt unberührt — zurückgestellt"),
    ("1274", "1"): ("EXECUTED", "Satz 2 (§§ 1205, 1206 bei Übergabe der Sache) — dieselben Regeln wie Titel 1"),
    ("1276", "1"): ("EXECUTED", "Satz 3 (§ 876 Satz 3 unberührt) — Kopf des Nachbarpakets BG-10, Verweisung ohne eigene Regel"),
    ("1277", "—"): ("EXECUTED", "Satz 2 (§§ 1229, 1245 Abs. 2 unberührt) — werden durch eigene Regeln ausgeführt"),
    ("1281", "—"): ("EXECUTED", "Sätze 2 und 3 (Verlangen gemeinsamer Zahlung, Hinterlegung) — Hinterlegungsverfahren extern"),
    ("1283", "1"): ("TODO", "Zustimmung des Pfandgläubigers zur Aufhebung bei Fruchtziehungsrecht — zurückgestellt"),
    ("1285", "2"): ("TODO", "Pflicht zur ordnungsgemäßen Einziehung und Anzeige — zurückgestellt"),
    ("1286", "—"): ("EXECUTED", "Satz 2 (umgekehrtes Zustimmungsverlangen) — dieselbe Bewertung, nicht als eigene Regel abgeleitet"),
    ("1288", "1"): ("EXECUTED", "Anlagepflicht; Anlageweise nach § 240a — externe untergesetzliche Regelung"),
    ("1296", "—"): ("EXECUTED", "Satz 2 (Ausgabe der Zinskupons vor Eintritt des § 1228 Abs. 2) — im TODO des Abschnitts zurückgestellt"),
    # --- §§ 1059a-e: Übertragbarkeit des Nießbrauchs bei juristischer Person —
    # erklärte Grenze (Ledger D-11-10): Feststellung durch die zuständige
    # Landesbehörde (§ 1059a Abs. 1 Nr. 2 Satz 2 f.) — Verwaltungsverfahren,
    # kein Rechenschritt dieses Pakets. §§ 1059b-e sind Rechtsfolgen- bzw.
    # Verweisnormen auf dieselbe Feststellung.
    ("1059a", "1"): ("BOUNDARY", "Feststellung der Übertragbarkeit durch die zuständige Landesbehörde (§ 1059a Abs. 1 Nr. 2 Satz 2 f.) — Verwaltungsverfahren, kein Rechenschritt dieses Pakets (D-11-10)"),
    ("1059a", "—"): ("BOUNDARY", "Feststellung der Übertragbarkeit durch die zuständige Landesbehörde (§ 1059a Abs. 1 Nr. 2 Satz 2 f.) — Verwaltungsverfahren, kein Rechenschritt dieses Pakets (D-11-10)"),
    ("1059a", "2"): ("BOUNDARY", "Rechtsfähige Personengesellschaft gleichgestellt — dieselbe Grenze wie Abs. 1"),
    ("1059b", "—"): ("BOUNDARY", "Rechtsfolge der Feststellung nach § 1059a — dieselbe Grenze"),
    ("1059c", "1"): ("BOUNDARY", "Rechtsfolge des Übergangs/der Übertragung nach § 1059a — dieselbe Grenze"),
    ("1059c", "2"): ("BOUNDARY", "Rechtsfolge des Übergangs/der Übertragung nach § 1059a — dieselbe Grenze"),
    ("1059d", "—"): ("BOUNDARY", "Verweisnorm auf Mietrecht (§§ 566 ff.) bei Übertragung nach § 1059a — dieselbe Grenze"),
    ("1059e", "—"): ("BOUNDARY", "Verweisnorm: §§ 1059a-d gelten entsprechend für den Anspruch auf Einräumung — dieselbe Grenze"),
}


def paragraph_rules() -> set[str]:
    """Paragraphen, deren CLIR mindestens eine an einem Fragment verankerte Regel enthält."""
    clir = json.loads(CLIR.read_text(encoding="utf-8"))
    found: set[str] = set()
    for node in clir.get("nodes", []):
        if node.get("kind") not in ("rule", "priority_rule"):
            continue
        for anchor in node.get("anchors", []) or []:
            m = re.search(r"BGB_P(\d+[a-z]?)$", anchor)
            if m:
                found.add(m.group(1))
    return found


def saetze():
    """(Paragraph, Absatz, Titel, Text) aus der festgeschriebenen Veröffentlichung."""
    rows = []
    paragraph = titel = None
    for line in TEXT.read_text(encoding="utf-8").splitlines():
        head = re.match(r"^§ (\d+[a-z]?) (.+)$", line)
        if head:
            paragraph, titel = head.group(1), head.group(2)
            continue
        if not paragraph or not line.strip():
            continue
        absatz = re.match(r"^\((\d+[a-z]?)\) (.*)$", line)
        if absatz:
            rows.append((paragraph, absatz.group(1), titel, absatz.group(2)))
        else:
            rows.append((paragraph, "—", titel, line))
    return rows


def main() -> None:
    have = paragraph_rules()
    out = []
    for par, abs_, titel, text in saetze():
        status, note = ("EXECUTED", None) if par in have else ("TODO", None)
        if (par, abs_) in EXCEPTIONS:
            status, note = EXCEPTIONS[(par, abs_)]
        row = {"paragraph": par, "absatz": abs_, "titel": titel,
               "text": text[:220], "status": status}
        if note:
            row["note"] = note
        out.append(row)
    doc = {
        "$comment": "Absatzweise Erfassung der Formalisierung von BG-11 (de.bgb.dingliche_rechte). "
                    "Erzeugt von analysis/build_saetze.py aus dem festgeschriebenen Text "
                    "sources/de-bgb-dingliche-rechte/bgb-de.txt und dem CLIR des Gesetzes. "
                    "status: EXECUTED — der Absatz wird durch Paketregeln ausgeführt; "
                    "TODO — nicht in diesem Schnitt (KEINE Grenze); "
                    "BOUNDARY — aus dem Normtext erklärte Grenze.",
        "act": "de-bgb-dingliche-rechte",
        "legal_cutoff": "2026-09-17",
        "saetze": out,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    counts: dict[str, int] = {}
    for row in out:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    print(f"{OUT.name}: {len(out)} Absätze, {counts}")


if __name__ == "__main__":
    main()
