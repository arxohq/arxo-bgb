# de.bgb.schuldrecht_at — BGB Buch 2 Abschnitte 1–7: Recht der Schuldverhältnisse, Allgemeiner Teil

Paket BG-04 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Geltungsbereich **§§ 241–432**:
245 geltende Paragraphen mit 749 Absätzen und zwei weggefallenen Positionen
(§ 279, § 419) auf den `legal_cutoff` 2026-09-17. Die Fragmente §194 liegen in
`sources/de-bgb-schuldrecht-at/` und sind aus dem Register DOKNR erzeugt —
nicht von Hand ändern (`corpus/tools/sources/sync/sync_de_bgb_packages.py`).

Importe: `de.bgb.core` (Personen, Anspruch, Schuldverhältnis, Gerichte) und
`de.bgb.fristen` (Eigentümer der Fristenberechnung, DECISION-0319 Р4).
Richtung `schuldrecht_at → fristen → core`, kein Rückimport.

## Aufbau

| Datei | Normen |
|---|---|
| `00-package.law` | Typen, gemeinsame Eingänge, Kalender §85, Politiken §86 |
| `abschnitt-01-titel-1-leistung.law` | §§ 241–279: Inhalt der Pflicht, Zinsen, Schadensersatz, Wahlschuld, Ort und Zeit der Leistung, Ausschluss der Leistungspflicht, Vertretenmüssen |
| `abschnitt-01-titel-1-verzug.law` | §§ 280–292: Pflichtverletzung, Verzug des Schuldners, Verzugszinsen; § 247 Abs. 1 |
| `abschnitt-01-titel-2-glaeubigerverzug.law` | §§ 293–304: Annahmeverzug und seine Wirkungen |
| `abschnitt-02-agb.law` | §§ 305–310: Einbeziehung, Auslegung, Inhaltskontrolle, Klauselverbote, Anwendungsbereich |
| `abschnitt-03-titel-1-begruendung-und-anpassung.law` | §§ 311–319: c.i.c., Form, Störung der Geschäftsgrundlage, Kündigung aus wichtigem Grund, Leistungsbestimmung |
| `abschnitt-03-titel-1-verbrauchervertraege.law` | §§ 312–312m: Anwendungsbereich, Entgeltgrenzen, Fernabsatz, elektronischer Geschäftsverkehr, Kündigungsschaltfläche |
| `abschnitt-03-titel-2-gegenseitiger-vertrag.law` | §§ 320–326: Einreden, Rücktritt wegen Leistungsstörung, Gegenleistung |
| `abschnitt-03-titel-2a-digitale-produkte.law` | §§ 327–327u: Bereitstellung, Mängel, Aktualisierungen, Verjährung, Rückgriff |
| `abschnitt-03-titel-3-4-dritter-draufgabe-strafe.law` | §§ 328–345: Vertrag zugunsten Dritter, Draufgabe, Vertragsstrafe |
| `abschnitt-03-titel-5-ruecktritt-widerruf.law` | §§ 346–361: Rücktritt und Widerrufsrecht bei Verbraucherverträgen |
| `abschnitt-04-erloeschen.law` | §§ 362–397: Erfüllung, Hinterlegung, Aufrechnung, Erlass |
| `abschnitt-05-06-uebertragung-und-schulduebernahme.law` | §§ 398–418: Abtretung, Schuldübernahme |
| `abschnitt-07-mehrheit.law` | §§ 420–432: Teilschuld, Gesamtschuld, Gesamtgläubiger |
| `basiszinssatz.lawparam.json` | A3-Parameter `Basiszinssatz` über die Achse `legal_time` (§ 247) |
| `analysis/saetze.json` | Matrix § → Absatz → Zustand (`tools/gen_saetze.py`) |

## Stand (17.09.2026)

| Maß | Wert |
|---|---|
| Tiefe §33.1 | **EXECUTABLE 245**, SOURCE_ONLY 2 (die weggefallenen §§ 279, 419, als Grenze mit Begründung erklärt), ANCHORED 0, UNEXPLAINED 0 |
| Absätze (`analysis/saetze.json`) | RULE 587, CHANNEL 55, EXTERNAL 69, DONE 38; POSITION 2 |
| Regeln | 492, davon 2 deontische Positionen (§ 241 Abs. 1, Abs. 2) |
| Szenarien | 15 in sechs Familien, beide Auswerter, Differential byteweise |
| Etiketten | Wörterbuch 1023, Normen 494, ohne Anker 0 |

Familien: `#verzug` (4), `#widerruf` (3), `#mehrheit` (2), `#schadensersatz` (2),
`#agb` (2), `#erloeschen` (2).

## Die vier Mechaniken dieses Pakets

### 1. Fristen — gerechnet in `de.bgb.fristen`

Dieses Paket schreibt Ereignis und Dauer in die Köpfe des Eigentümers
(`frist_ereignis`, `frist_dauer_tage`, `frist_ende_kalender`) und liest das
Ende (`frist_ende`); die Verlegung des § 193 rechnet dort die Regel
`Verlegung193`. Die POLITIK des Falls muss im Programm des Falls erklärt sein
(LDC-E1332), deshalb trägt das Paket eigene Politiken mit denselben Feldern:
`BGB_SCHULDRECHT_AT_TAG` (Tagesfrist, § 187 Abs. 1, § 188 Abs. 1, § 193 als
Roll) und `BGB_SCHULDRECHT_AT_KALENDER` (Wochen, Monate, Jahre; § 193
ausdrücklich). **Eine Politik je Fall** (§168.2): die Tagesfristen (§ 286
Abs. 3: 30 Tage; § 355 Abs. 2: 14 Tage; § 357 Abs. 1, § 327n Abs. 4: 14 Tage;
§ 357b Abs. 1, § 327r Abs. 3: 30 Tage) und die Kalenderfristen (§ 356 Abs. 4:
zwölf Monate und 14 Tage; § 318 Abs. 2 und § 382: 30 Jahre; § 416 Abs. 1:
sechs Monate; § 327j: zwei Jahre, zwölf und vier Monate; § 327u Abs. 2: sechs
Monate) gehören in getrennte Fälle. Jede Zeile steht in
`docs/foundations/de-bgb/DEADLINES.json` unter `BG-04`.

Der Verzug des § 286 Abs. 3 wird mit dem **Ablauf** des Fristendes benannt und
nicht mit dem folgenden Tag: einen Tagesschritt lässt die Tagespolitik des
Falls nicht zu (MISSING_POLICY, gemessen 17.09.2026), und einen zweiten Schritt
nennt der Text nicht (Ledger D-04-08).

### 2. Basiszinssatz (§ 247) — Parameter und Rechnung

Der **geltende** Satz ist der A3-Parameter `Basiszinssatz` über die Achse
`legal_time`: 49 bekanntgemachte Werte vom 1. Juli 2002 bis zum 1. Juli 2026
aus dem Schnappschuss `sources/bundesbank-basiszinssatz/` (Bekanntmachungen der
Deutschen Bundesbank nach § 247 Abs. 2; Hash in `PINS.sha256`, Eintrag in
`SOURCES.json.external`). Vor dem 1. Juli 2002 antwortet das Paket nicht
(`MISSING_PARAMETER_VALUE`), es füllt die Lücke nicht mit Null.

Die **Rechnung** des Absatzes 1 Satz 2 und 3 ist eine Regel: der Satz verändert
sich zum 1. Januar und 1. Juli um die Veränderung der Bezugsgröße (Zinssatz der
jüngsten Hauptrefinanzierungsoperation der EZB). Zeuge `v03`: 2,27 + 2,15 −
3,15 = 1,27 Prozent zum 1. Juli 2025 — derselbe Wert, den die Bundesbank
bekanntgemacht hat (unabhängige Erwartung).

### 3. Rundung — Politik des Pakets, keine Norm

Weder § 288 noch § 426 nennen eine Rundung. Wo aus einem Satz oder einem Bruch
ein Geldbetrag wird, rundet das Paket **einmal je Anspruch** auf den Cent,
kaufmännisch: `div_round(Betrag × Zähler, Nenner als Decimal, 2, "HALF_UP")`.
Zeugen: `v01` (6,52 % von 10 000,00 EUR = 652,00 EUR), `v04` (10,52 % von
5 000,00 EUR = 526,00 EUR), `m01` (10 000,00 / 3 = 3 333,33 EUR), `s01`
(9 000,00 × 2/3 = 6 000,00 EUR). Anteile selbst sind exakt: `1 / n` zweier
Integer gibt den `Rational` (§18), und der Anteil des Mitverschuldens kommt vom
Gericht als Paar ganzer Zahlen (Ledger D-04-05).

### 4. Bewertende Merkmale — 55 Absätze auf dem Kanal des Gerichts

Jede Wertung ist **pro Paragraph** als `external judgment relation … { authority
Court; }` erklärt (DECISION-0194, Kanal §47.3), nie als flache Tatsache des
Falls: Treu und Glauben (§ 242), Unverhältnismäßigkeit (§ 251 Abs. 2, § 275
Abs. 2, § 327l Abs. 2), Wahrscheinlichkeit des entgangenen Gewinns (§ 252),
billige Entschädigung (§ 253), Mitverschulden und sein Anteil (§ 254),
angemessene Fristen (§ 250, § 264, § 281, § 321, § 323, § 350), grobe
Unbilligkeit (§ 271a), überraschende Klausel (§ 305c), unzumutbare Härte
(§ 306), unangemessene Benachteiligung (§ 307), die Klauselverbote MIT
Wertungsmöglichkeit (§ 308), Störung der Geschäftsgrundlage (§ 313), wichtiger
Grund (§ 314), Billigkeit der Leistungsbestimmung (§ 315, § 319), Unerheblichkeit
der Pflichtverletzung und des Mangels (§ 323 Abs. 5, § 327m Abs. 2), Herabsetzung
der Vertragsstrafe (§ 343), Schwere des Mangels (§ 327m Abs. 1 Nr. 4), Minderung
(§ 327n) und jedes „unverzüglich“ (§ 318, § 352, § 353, § 355 Abs. 3, § 374,
§ 384, § 396, § 410) — ein bewertendes Merkmal, keine Frist von null Tagen.

Prüfung des Kanals zweistufig: `a02` fragt ohne Antwort des Gerichts
(`REQUIRES_JUDGMENT` mit `judgment_request`), `s01` und `a01` rechnen mit der
Antwort (`origin adjudicated`, `judgment_requests(0)`).

## Was das Paket nicht tut und warum

- **Der Inhalt der Informationspflichten steht im EGBGB** (Artikel 246, 246a,
  246b, 246c, 246d, 247, 249) und ist nicht Gegenstand dieses Pakets: der Fall
  sagt, ob der Unternehmer unterrichtet hat (`informationspflicht_nach_246a_erfuellt`,
  `unterrichtung_ueber_das_widerrufsrecht_am`), die Rechtsfolge der Unterlassung
  steht hier (§ 312e, § 356 Abs. 3, § 312m Abs. 2). 69 Absätze sind deshalb
  `EXTERNAL` in `analysis/saetze.json` — mit Nennung des fremden Gesetzes.
- **Fremde Gesetze bleiben Eingänge**: ZPO (Rechtshängigkeit § 291,
  Beschlagnahme § 392, Unpfändbarkeit §§ 394, 400, rechtskräftiges Urteil
  § 407 Abs. 2, Schätzung § 287), InsO (§ 377 Abs. 2, § 401 Abs. 2, § 418
  Abs. 2), HGB (§ 327u Abs. 5), KWG/WpIG/ZAG/KAGB/BörsG (§ 310 Abs. 1a),
  TKG (§ 327 Abs. 6, § 327r Abs. 6), PBefG (§ 309 Nr. 7), GWB (§ 271a Abs. 2).
- **Nachbarpakete**: die Begriffe des Verbrauchers und des Unternehmers
  (§§ 13, 14) gehören `de.bgb.allgemeiner_teil`; bis es seine Köpfe
  veröffentlicht, sind `verbraucher` und `unternehmer` eigene Eingänge dieses
  Pakets (Ledger D-04-01). § 441 Abs. 3 (Minderung), §§ 438, 439 gehören
  `de.bgb.kauf`; §§ 482 ff., 492 ff., 506, 514 gehören
  `de.bgb.sonstige_vertraege`; § 650i gehört `de.bgb.dienst_werk`; §§ 987 ff.
  (§ 292) gehören `de.bgb.besitz_eigentum`. Die Verjährung selbst (§§ 194–218)
  gehört `de.bgb.fristen` — § 390 liest von dort `verjaehrung_eingetreten_am`
  (Zeuge `e02`).
- **Der Zinsbetrag für einen Zeitraum, der kein volles Jahr ist**, wird nicht
  gerechnet: § 288 nennt den Satz „für das Jahr“ und keine Zinsmethode
  (actual/365, actual/360, 30/360). Die Zahl der Tage je Jahr steht nicht im
  Text — Frage `D-Q04-1` im Ledger, keine erfundene Methode.
- **§ 366 Abs. 2** rechnet nur die erste Stufe der Reihenfolge (die fällige
  Schuld); Sicherheit, Lästigkeit, Alter und die verhältnismäßige Tilgung sind
  `TODO` des Ledgers, keine Grenze.
- **§ 426 Abs. 1 Satz 2** verteilt den Ausfall EINES Schuldners; mehrere
  Ausfälle in Folge brauchen einen zweiten Durchgang über das Ergebnis des
  ersten (`stage` §111.1) und sind Grenze dieses Pakets (Zeuge des einen
  Ausfalls: `m02`).
- **Deontische Positionen** trägt nur § 241 (Leistungspflicht, Rücksichtnahme).
  Die übrigen Pflichten dieses Abschnitts sind Schlussfolgerungen mit eigenem
  Kopf; ihre Verletzung ist eine festgestellte Tatsache (§ 280 Abs. 1) und
  nicht `VIOLATED` einer Position. Die Migration weiterer Pflichten in
  Positionen ist Aufgabe der Welle B5, nicht dieser Wellen.
- **Verdikt zu den 63 „Posílki v odin konec“ des Audits**: sie entstehen dort,
  wo die Voraussetzung der Norm eine Beschreibung des Vertragsinhalts oder
  eine Zahl des Textes im Etikett trägt (§ 309 Nummern, § 312 Abs. 2,
  § 327 Abs. 6). Das ist kein Stab: die Zahl steht im Gesetz und die
  Beschreibung ist die Tatsache, die das Gesetz verlangt — die Kette endet
  beim Fall, weil sie beim Fall enden soll.

## Prüfung (nur punktuell — PARALLEL.md §2)

## Pflichten / Positions

Die deontische Schicht P2 ergänzt die bestehenden relations um normative
Positionen: §241 bleibt `EXISTING`; die Familien
`positionen-271-280`, `positionen-281-286`, `positionen-312d-355`,
`positionen-320-387` und `positionen-321-391` enthalten neue duty-, liberty-
und power-Formen. §346 ist `EXISTING`: Die Rückgewährpflicht wird durch
`RueckgewaehrNachRuecktritt` in
`abschnitt-03-titel-5-ruecktritt-widerruf.law` hergeleitet; die Szenarien
der Familie `positionen-321-391` prüfen die verbundenen Rückgewährzustände.

```sh
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-04 --check
./law engine check corpus/laws/de/bgb/schuldrecht-at
python3 corpus/laws/de/bgb/schuldrecht-at/tools/gen_kalender.py --check
python3 corpus/laws/de/bgb/schuldrecht-at/tools/gen_saetze.py --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-schuldrecht-at.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-bg04.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.schuldrecht_at#verzug"
python3 corpus/run_kz_regression.py --only "de.bgb.schuldrecht_at#verzug" --write-manifest
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.schuldrecht_at#verzug"
python3 verify/ci/gates/sources/check_source_pinning.py --only corpus/laws/de/bgb/schuldrecht-at
python3 .claude/skills/audit-formalization/scripts/audit.py de-bgb-schuldrecht-at --fast
```

Dieselben Befehle für `#widerruf`, `#mehrheit`, `#schadensersatz`, `#agb` und
`#erloeschen`. Zahl der ausgeführten Fälle je Prüfung:
`docs/foundations/de-bgb/CHECKS.json`, Zeilen `CHK-04-NN`.
