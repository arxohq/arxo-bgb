# de.bgb.betreuung — BGB Buch 4 Abschnitt 3 (§§ 1773–1888/1921)

Paket BG-14 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Es senkt Buch 4 Abschnitt 3 in
der Nummerierung ab 1.1.2023 (Reform des Vormundschafts- und
Betreuungsrechts) ab: Titel 1 Vormundschaft (§§ 1773–1808), Titel 2
Pflegschaft für Minderjährige (§§ 1809–1813), Titel 3 Rechtliche Betreuung
(§§ 1814–1881), Titel 4 Sonstige Pflegschaft (§§ 1882–1888). Quellen:
`sources.law`, erzeugt aus dem Register DOKNR, Stand `legal_cutoff`
2026-09-17: 116 Paragraphen, 12 deontische Positionen (§§ 1773, 1775–1781,
1783–1786) und 1 Bereichsposition, 116 gepinnte Fragmente,
text coverage 99,3 %.

Tiefe § 33.1 (`check_formalization_depth.py`): **EXECUTABLE 114** Einheiten,
ANCHORED 2, SOURCE_ONLY 0, UNEXPLAINED 0 — alle 116 Paragraphen adressiert.
265 Regeln/Relationen (`check_label_coverage.py`: Wörterbuch 510/0, Normen
265/0, ohne Anker 0). 82 Szenarien in zwölf Familien, beide Auswerter,
`evaluate`-Aufrufe byteweise identisch (`check_kz_differential.py`).

## Nummerierung nach dem Register, nicht nach der Paraphrase (D-14-02)

Der Sitzungsauftrag benannte Paragraphen nach einer älteren Erinnerung an die
Nummerierung; der gepinnte Text zeigt andere Inhalte an denselben Nummern —
namentlich hat § 1868 KEINE turnusmäßige gerichtliche Überprüfung (das ist
§ 294 FamFG, Verfahrensrecht außerhalb dieses Pakets); die echten
Ausschlussfristen der Vergütung stehen in § 1877 Absatz 4 (15 Monate,
Aufwendungsersatz) und § 1878 Absatz 4 (6 Monate, Aufwandspauschale), nicht in
§ 1876. Einzelheiten und die vollständige Gegenüberstellung: Ledger D-14-02.

## Ein Prädikat für drei Ämter (Ledger D-14-01)

Titel 1 verweist mehrfach mit „gilt entsprechend“ auf die Maschinerie des
Titel 3 (§ 1798 Abs. 2, § 1799 Abs. 1, § 1800 Abs. 2, § 1801, § 1802 Abs. 2,
§ 1807, § 1808 Abs. 2); Titel 2 auf Titel 1 (§ 1813); Titel 4 auf Titel 3
(§ 1888). Nach dem Muster D-11-07 (eine `Pfandrecht`-Entität für zwei Titel)
trägt EIN Prädikat `gesetzlicher_vertreter(vertreter, vertretene)` alle drei
Ämter (Vormund/Mündel, Betreuer/Betreuter, Pfleger/Pflegling); die
Vermögenssorge-, Genehmigungs-, Aufsichts- und Vergütungsmaschinerie ist
EINMAL geschrieben (in den Titel-3-Dateien) und wird von den „gilt
entsprechend“-Normen der übrigen Titel wiederverwendet — keine
Zwillingsmaschinerie.

## Kalender §85 und Fristen (Ledger D-04-03-Muster)

Wie `de.bgb.schuldrecht_at` bindet dieses Paket den gemeinsamen
Feiertagsdatensatz (Ledger D-03) mit einem eigenen Knoten
`KALENDER_BUNDESWEIT` (`tools/gen_kalender.py`, nicht `law engine lock
--write`); ein Fall dieses Pakets wählt ihn ausdrücklich mit `calendar
KALENDER_BUNDESWEIT;`, weil zwei Kalenderknoten im verbundenen Weltbild sonst
`AMBIGUOUS_CALENDAR` geben. Drei Politiken:

- `BGB_BETREUUNG_TAG` (§ 187 Abs. 1 Ereignistag nicht mitgerechnet, § 193
  Verlegung) für Tagesfristen, in denen eine Erklärung GEGENÜBER dem Gericht
  geschuldet ist: § 1781 Abs. 2 (zwei Wochen, Mitteilung des
  Vormundschaftsvereins), § 1783 Abs. 1 Nr. 5 (vier Wochen, Bereiterklärung
  der benannten Person).
- `BGB_BETREUUNG_KALENDER` (§ 188 Abs. 2, 3; die cross-package Regel
  `de.bgb.fristen::Verlegung193` verlegt aus `frist_ende_kalender`) für
  Monats-/Jahresfristen: § 1781 Abs. 3 (drei/sechs Monate, Bestellungsfrist),
  § 1856 Abs. 2 (zwei Monate, Mitteilung der Genehmigung), § 1863 Abs. 3
  (ein Jahr, Jahresbericht — Szenario j03 zeigt die Verlegung eines Sonntags
  auf Montag), § 1877 Abs. 4 (15 Monate, Aufwendungsersatz), § 1878 Abs. 4
  (6 Monate, Aufwandspauschale).

- `BGB_BETREUUNG_TAG_ROLLFREI` (D-14-06 Block 7): reine Wartefrist ohne
  Adressaten einer Erklärung, § 193 passt nicht (Muster D-10-05) — § 1830
  Abs. 2 Satz 2 (zwei Wochen, Sterilisation frühestens nach Wirksamkeit der
  Genehmigung). Szenarien m56/m57 zeigen den Unterschied zu den anderen
  Politiken konkret: Genehmigung wirksam an einem Sonntag, Fristende bleibt
  auf dem Sonntag — OHNE die Verlegung, die `BGB_BETREUUNG_TAG` an derselben
  Stelle vornähme.

Szenarien m58/m59 zeigen zusätzlich, dass dieselbe § 1863-Abs.-3-Maschinerie
ohne eigene Kopie auch für den Ergänzungspfleger (Titel 2, § 1813) und den
sonstigen Pfleger (Titel 4, § 1888 Abs. 1) greift (D-14-01).

## Bewertende Merkmale (DECISION-0194)

Kanal §47.3 (`external judgment relation … { authority Court; }`): Eignung
und Auswahl des Vormunds (§§ 1778, 1779, 1785) und des Betreuers (§§ 1816,
1819), Amtsführung zum Wohl (§ 1790), freier Wille (§ 1814 Abs. 2 — Szenario
b02b zeigt `REQUIRES_JUDGMENT` ohne Antwort), Erforderlichkeit der Betreuung
(§ 1814 Abs. 3), Einwilligungsvorbehalt (§ 1825 Abs. 1), Wünsche und
mutmaßlicher Wille des Betreuten (§ 1821 Abs. 4, § 1827 Abs. 2), Übereinstimmung
mit dem Willen bei ärztlichen Maßnahmen (§ 1829 Abs. 3). Festgestellte
Tatsachen mit `origin adjudicated`: Krankheit/Behinderung (§ 1814 Abs. 1),
Bestellung von Vormund/Betreuer, Unterbringungs- und
Zwangsmaßnahmengenehmigung (§§ 1831 f., 1832 Abs. 2). Ein flacher Fall-Fakt
„ist betreuungsbedürftig“ kommt im Paket nicht vor.

## Genehmigungsschwellen in Euro

§ 1849 Abs. 2 S. 1 Nr. 1 Buchst. a (3 000 €, Geldleistungsanspruch) und
§ 1854 Nr. 6 (6 000 €, Vergleich/Schiedsvereinbarung) sind im Text selbst
genannte Zahlen, keine Annahmen des Pakets; beide Seiten der 3 000-Euro-
Schwelle sind Szenario (g01/g02).

## Was das Paket nicht tut und warum

Nach sieben Blöcken (D-14-06) trägt jeder der 116 Paragraphen des Pakets
entweder eine Ableitungsregel (114, `analysis/saetze.json` Status `RULE`)
oder ist bewusst als reiner Wertungskanal (§ 1778, `JUDGMENT`) bzw. als
Festlegung ohne eigene Rechtsfolge (§ 1780, `FACT`) klassifiziert — keine
Norm bleibt ohne Adresse oder ohne Grund SOURCE_ONLY. `TASKS.json
BG-14-TODO-1` ist DONE: die dritte, rollfreie Fristenpolitik (§ 1830 Absatz 2)
und die Titel-2/4-Brückenszenarien für die generische Fristenmaschinerie
sind seit Block 7 mit eigenen Fallpaaren ausgeführt (m56–m59). Offen bleibt
nur, was der Text selbst als externen Eingang markiert:

- Verfahrensrecht (FamFG, Betreuungsorganisationsgesetz, VBVG) bleibt
  externer Eingang (`SOURCES.json.external`); die Anwendbarkeit des VBVG
  selbst ist als Dispatcher in § 1875 Absatz 2 formalisiert.
- Titel 2/4 haben nur je eine Brückenszenario-Instanz (Jahresbericht); weitere
  Titel-3-Maschinerie (Genehmigungen, Vermögensverwaltung usw.) greift nach
  demselben Muster automatisch über `gesetzlicher_vertreter`, ohne dass
  jede einzelne Kombination hier separat vorgeführt wurde.

## Prüfung

```sh
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json  # lokal, siehe PARALLEL.md §2
./law engine check corpus/laws/de/bgb/betreuung
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-betreuung.lawir.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.betreuung#vormundschaft"
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.betreuung#vormundschaft"
```
