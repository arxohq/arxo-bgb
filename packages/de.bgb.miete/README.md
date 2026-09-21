# de.bgb.miete — BGB Buch 2 Abschnitt 8 Titel 5: Mietvertrag, Pachtvertrag, Landpachtvertrag (§§ 535–597)

## Pflichten / Positions

The deontic layer is added next to the existing institutional relations. The
first position family, `de.bgb.miete#positionen-535`, observes the four
contractual duties of § 535 with two scenarios: active before the supplied
performance facts and satisfied for the achievement duties after those facts
are supplied. The maintenance duty remains `ACTIVE` without a completeness
certificate, as required by § 124.

Paket BG-06 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Stand der Quelle: konsolidierter
Text von gesetze-im-internet.de, `legal_cutoff` 2026-09-17, 144 geltende
Paragraphen, 458 Absätze. Alle 144 Paragraphen sind mit einem Fragment
gepinnt; 142 sind EXECUTABLE nach §33.1, zwei sind als Grenze erklärt
(unten, „Was das Paket nicht tut und warum“).

## Karte des Titels

| Untertitel | §§ | Datei | Worum es geht |
|---|---|---|---|
| 1 Allgemeine Vorschriften | 535–548a | `untertitel-01-allgemeine-vorschriften.law` | Hauptpflichten, Mängelkette, Kündigung aus wichtigem Grund, stillschweigende Verlängerung, Verjährung |
| 2 Kapitel 1–2 Wohnraum | 549–556c | `untertitel-02-a-wohnraum-und-betriebskosten.law` | Anwendungsbereich, Schriftform, Kaution, Erhaltung und Modernisierung, Betriebskosten |
| 2 Unterkapitel 1a Miethöhe bei Mietbeginn | 556d–556g | `untertitel-02-b-mietpreisbremse.law` | 110 Prozent der ortsüblichen Vergleichsmiete, Vormiete, Modernisierung, Neubau, Rüge |
| 2 Unterkapitel 2 Miethöhe | 557–561 | `untertitel-02-c-mieterhoehung.law` | Staffel- und Indexmiete, Vergleichsmiete und Kappungsgrenze, Modernisierungsumlage, Betriebskostenänderung, Sonderkündigung |
| 2 Unterkapitel 3–5 | 562–567b | `untertitel-02-d-pfandrecht-eintritt-und-erwerb.law` | Vermieterpfandrecht, Eintritt beim Tod des Mieters, Kauf bricht nicht Miete |
| 2 Unterkapitel 5 Beendigung | 568–577a | `untertitel-02-e-kuendigung-wohnraum.law` | Form, wichtiger Grund bei Wohnraum, berechtigtes Interesse, Kündigungsfristen, Widerspruch, Zeitmietvertrag, Vorkaufsrecht, Sperrfrist |
| 3 Andere Sachen | 578–580a | `untertitel-03-andere-sachen.law` | Verweisungsketten für Grundstücke, Räume, Schiffe, digitale Produkte; sechs Kündigungsfristen |
| 4 Pacht | 581–584b | `untertitel-04-05-pacht-und-landpacht.law` | Fruchtgenuss, Inventar, Kündigung zum Schluss eines Pachtjahrs |
| 5 Landpacht | 585–597 | dieselbe Datei | Form, Beschreibung, Duldung, Verwendungen, Verjährung, Kündigungsfristen, Fortsetzung, Rückgabe |

## Ein Träger für drei Vertragstypen

Miete, Pacht und Landpacht sind im Text EIN Titel mit Verweisungsketten
(§ 581 Abs. 2, § 585 Abs. 2). Deshalb trägt das Paket ein einziges
`Mietverhaeltnis` mit der Art als Angabe des Falls (`vertragsart`), nicht drei
Entitäten: sonst müsste jede Regel des Untertitels 1 dreimal geschrieben
werden, und die Verweisung des § 581 Abs. 2 wäre nicht dieselbe Norm, sondern
eine Kopie (Ledger D-06-01).

## Fristen

Zeilen: `docs/foundations/de-bgb/DEADLINES.json`, Abschnitt BG-06. Die Politik
`BGB_MIETE_KALENDER` trägt denselben Feldsatz wie `BGB_FRISTEN_KALENDER`
(`same_day`, `include_end`, `no_roll`, `last_day_of_month`) — eine Politik je
Fall (§168.2). § 193 wird nicht gerollt, sondern dort ausdrücklich gerechnet,
wo der Text eine Erklärung INNERHALB der Frist verlangt: § 545 Satz 1 (zwei
Wochen), § 556 Abs. 3 Satz 2 und Satz 5 (je zwölf Monate), § 558b Abs. 2
(Zustimmung), § 561 Abs. 1 (Sonderkündigung), § 562b Abs. 2 (Pfandrecht),
§ 563 Abs. 3 (Ablehnung des Eintritts).

Der „dritte Werktag“ der §§ 556b, 573b, 573c, 573d, 575a, 576, 579 Abs. 2,
580a, 584 und 594a wird mit `add_business_days` über dem Kalender
`KALENDER_BUNDESWEIT` aus `de.bgb.fristen` gezählt (Lock-Zeile im eigenen
`law.lock`, `lockVersion` 0.2 — D-09-07).

**Abstände „N Monate VOR“** (§ 555c Abs. 1, § 556c Abs. 2, § 574b Abs. 2,
§ 575 Abs. 2) werden VORWÄRTS vom Tag der Erklärung an gerechnet und mit dem
Bezugstag verglichen: ein negativer Kalenderschritt lässt die Auswertung
NON_EXECUTABLE werden (Ledger D-06-07, gemessen).

## Rundung

Beträge sind `EUR`. Jede Division steht GENAU EINMAL je Anspruch und rundet
kaufmännisch auf den Cent, `div_round(…, n × 1.0, 2, "HALF_UP")`:

| Norm | Rechnung |
|---|---|
| § 536 Abs. 1 Satz 2 | Miete × (Nenner − Zähler) / Nenner — die Quote gibt das Gericht |
| § 551 Abs. 2 Satz 1 | Sicherheit / 3 (drei gleiche Teilzahlungen) |
| § 556d Abs. 1 | Vergleichsmiete × 110 / 100 |
| § 558 Abs. 3 | Miete vor drei Jahren × 120 / 100, in den bestimmten Gebieten × 115 / 100 |
| § 559 Abs. 1 | Kosten × 8 / 1200 (8 Prozent jährlich, auf den Monat) |
| § 559 Abs. 3a | 3,00 €, 2,00 € oder 0,50 € je Quadratmeter Wohnfläche |
| § 559a Abs. 2 | (Erhöhungsbetrag × 12 − Zinsermäßigung) / 12 |
| § 559c Abs. 1 Satz 2 | Kosten × 30 / 100 |
| § 559e Abs. 1 | Kosten × 10 / 1200 |
| § 559f Abs. 2 | Kosten / 2 |

Der Höchstbetrag der Kaution (§ 551 Abs. 1: Nettomiete × 3) und die
Zwei-Monats-Schwellen (§ 543 Abs. 2 Nr. 3 Buchst. b, § 569 Abs. 2a) sind
exakte Multiplikationen ohne Rundung.

## Bewertende Merkmale (DECISION-0194)

Jeder Fall ist nach dem WORTLAUT des Paragraphen einem Kanal zugeordnet.
Wertungen des Gerichts (`external judgment relation … { authority Court; }`):
§ 536 Abs. 1 Satz 2 und 3 (Minderungsquote, unerhebliche Minderung), § 536c
Abs. 1 (unverzüglich), § 543 Abs. 1 Satz 2 (Unzumutbarkeit), § 543 Abs. 2
Nr. 3 Buchst. a (nicht unerheblicher Teil), § 543 Abs. 3 Satz 2 (Entbehrlichkeit),
§ 552 Abs. 1 und § 553 Abs. 1 (berechtigtes Interesse), § 553 Abs. 1 Satz 2 und
§ 554 Abs. 1 Satz 2 (Unzumutbarkeit), § 555d Abs. 2, § 559 Abs. 4, § 574 Abs. 1
und 2, § 588 Abs. 2, § 595 Abs. 1 (Härte), § 559d Satz 2 (nachvollziehbarer
objektiver Grund), § 573 Abs. 1 Satz 1 (berechtigtes Interesse).

Festgestellte Tatsachen (`kind empirical`, im Fall `origin adjudicated`): die
Kenntnis des Mieters vom Mangel (§ 536b), die Arglist (§ 536b, § 536d), die
Tage der Überlassung, der Rückgabe, des Zugangs, der Veräußerung und des Todes.

Lesarten §152 werden nicht gebraucht: wo der Text auseinandergeht, delegiert
er selbst an das Gericht (§ 574a Abs. 2, § 591 Abs. 3, § 595 Abs. 6).

## Was das Paket nicht tut und warum

1. **Zwei Paragraphen sind erklärte Grenzen** (`sources/de-bgb-miete/articles.json`,
   `declared`): § 558c (Begriff des Mietspiegels und Ermächtigung der
   Bundesregierung) und § 558e (Begriff der Mietdatenbank). Beide richten sich
   an Behörden und den Verordnungsgeber und tragen keine Rechtsfolge für ein
   Mietverhältnis; Mietspiegel und Datenbankauskunft kommen als Eingabe des
   Falls herein (§ 558a Abs. 2 Nr. 1 und 2). Die Grenze folgt dem TEXT, nicht
   dem Arbeitsumfang.
2. **Schadensersatz, Verzug und Rücktritt** (§§ 280, 286, 323, 326) gehören
   `de.bgb.schuldrecht_at` (BG-04); §§ 536a, 546a, 571 stellen hier nur fest,
   DASS und WOFÜR gehaftet wird. Ebenso liegen die Vorschriften über digitale
   Produkte (§§ 327 ff.), auf die § 548a und § 578b verweisen, bei BG-04.
3. **Rechtsverordnungen der Länder** — Gebiete mit angespanntem Wohnungsmarkt
   (§ 556d Abs. 2), Kappungsgrenzengebiet (§ 558 Abs. 3 Satz 3), verlängerte
   Sperrfrist (§ 577a Abs. 2) — sind kein Bundesrecht und werden nicht
   erfunden: der Fall gibt Gebiet und Zeitraum an (Ledger D-06-02). Dasselbe
   gilt für Betriebskostenverordnung, Telekommunikationsgesetz,
   Gebäudemodernisierungsgesetz, Wohnraumförderungsgesetz, ZPO und das
   Landwirtschaftsgericht.
4. **Das Verfahren** — Klage auf Zustimmung (§ 558b Abs. 2), Räumungsklage
   (§ 569 Abs. 3 Nr. 2), Urteil über die Fortsetzung (§ 574a Abs. 2) — wird
   nicht nachgebildet: das Paket rechnet die FRISTEN dieser Schritte und nimmt
   ihr Ergebnis als festgestellte Tatsache.
5. **Ein Fall trägt genau ein streitiges Mietverhältnis** und darin höchstens
   einen Mangel, eine Kündigung, eine Mieterhöhung und eine Abrechnung: die
   Schlüssel sind das Verhältnis oder der jeweilige Träger (Ledger D-06-03).
6. **Der Quartalsanfang und der Wochenbeginn** (§ 580a Abs. 1 Nr. 2, Abs. 2,
   § 584 Abs. 1, § 594a Abs. 1) kommen als Angabe des Falls: einen Term dafür
   nennt die Fläche v1 nicht (Ledger D-06-08). Dasselbe gilt für das Pachtjahr,
   weil der Vertrag ein anderes als das Kalenderjahr bestimmen kann
   (§ 594a Abs. 1 Satz 2).

## Szenarien

Fünf Familien, 13 Szenarien, alle mit beiden Auswertern und byteweisem
Differential (`de.bgb.miete#maengel`, `#betriebskosten`, `#mieterhoehung`,
`#kuendigung`, `#pacht`). Beide Seiten jeder Schwelle: § 584 Abs. 1 (letzter
Tag und einen Tag zu spät), § 573c Abs. 1 (drei Stufen und ein Zeuge „minus
ein Subjekt“), § 558 Abs. 3 (Kappungsgrenze überschritten), § 559 Abs. 3a
(Kappung gewahrt).

## Prüfung

```sh
./law engine check corpus/laws/de/bgb/miete
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-miete.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-bg06.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.miete#kuendigung"
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.miete#kuendigung"
```
