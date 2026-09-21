# de.bgb.dienst_werk — Bürgerliches Gesetzbuch, Buch 2 Abschnitt 8 Titel 8–9

Paket BG-07 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Der Zuschnitt trägt **§§ 611–651y**
(Dienstvertrag, Behandlungsvertrag, Werkvertrag, Bauvertrag,
Verbraucherbauvertrag, Architekten- und Ingenieurvertrag, Bauträgervertrag,
Pauschalreisevertrag), Stand `legal_cutoff` 2026-09-17 (Quelle: `sources.law`,
erzeugt aus dem Register DOKNR; konsolidierter Text von
gesetze-im-internet.de, amtliche Verkündung im Bundesgesetzblatt Teil I).
**Der aktuelle Positions-Schnitt ist vollständig abgesenkt.** Die
Paketvollständigkeit nach §33.1 und die Vollständigkeit des deontischen
Inventars sind davon getrennte Aussagen.

| Maß | Wert |
|---|---|
| Paragraphen im Paket (§§ 611–651y) | 106 |
| Tiefe §33.1 | **103 EXECUTABLE** von 106 (97 %) |
| Rest | 3 SOURCE_ONLY: §§ 611b, 641a (weggefallen), § 651 (Fundstellenangabe „jetzt § 650") — Grenzen mit Grund |
| Regeln | 347 (strict 325, defeasible 22 aus elf `presumption`) |
| Pflichten §18 | 54 `duty`, 1 `prohibition`, 44 `external judgment relation` |
| Szenarien | 209 PASS in 37 Familien, beide Auswerter, Differential byteweise gleich (Schnitt `304238ad6c9b93eae434b1ea8d5c250f5c181a95`) |

## Karte der Dateien

| Untertitel | §§ | Datei | Familien |
|---|---|---|---|
| T8 U1 Dienstvertrag | 611–630 | `untertitel-01-dienstvertrag.law` | `grundpflichten`, `betriebsuebergang`, `verguetung-bei-leistungsstoerung`, `fuersorge`, `beendigung-und-kuendigungsfristen`, `ausserordentliche-kuendigung`, `nachwirkungen`, `kuendigung-621-rest` |
| T8 U2 Behandlungsvertrag | 630a–630h | `untertitel-02-behandlungsvertrag.law` | `behandlungsvertrag`, `behandlungsfehler-beweislast` |
| T9 U1 Kap. 1 Werkvertrag | 631–650 | `untertitel-03-a-werkvertrag.law` | `werkvertrag-grundlagen`, `werkmaengel-und-abnahme`, `werkverjaehrung` |
| T9 U1 Kap. 2 Bauvertrag | 650a–650h | `untertitel-03-b-bauvertrag.law` | `bauvertrag` |
| T9 U1 Kap. 3 Verbraucherbauvertrag | 650i–650o | `untertitel-03-c-verbraucherbauvertrag.law` | `verbraucherbauvertrag` |
| T9 U2 Architekten-/Bauträgervertrag | 650p–651 | `untertitel-04-architekt-und-bautraeger.law` | `architekten-und-bautraegervertrag` |
| T9 U3 Pauschalreisevertrag | 651a–651y | `untertitel-05-pauschalreise.law` | `pauschalreise-begriff-und-preis`, `pauschalreise-maengel`, `pauschalreise-sicherung-und-vermittlung` |

Vier Träger: `Dienstverhaeltnis`, `Behandlungsverhaeltnis`, `Werkvertrag`,
`Pauschalreisevertrag`. Jeder Untertitel läuft über seinen eigenen; die
Verweisungsnormen (§§ 630b, 650, 650q, 650u, 651u) werden als
institutionelle Schlüsse abgesenkt, nicht durch doppelte Regeln (Ledger
D-07-10).

## Sieben Mechaniken

**1. § 622 Abs. 1: zwei Termine, kein Datumskonstruktor.** Die Grundfrist
„vier Wochen zum Fünfzehnten oder zum Ende eines Kalendermonats" braucht den
15. des Monats, in dem die Vierwochenfrist abläuft. Ein Konstruktor
`date_of(Jahr, Monat, Tag)` ist bewusst abgelehnt (Errata E-0084); der 15.
wird `add_calendar_period(month_start_of(Grenze), 14 calendar_day)` gerechnet.
Zwei sich ausschließende Regeln wählen den frühesten zulässigen Termin;
Zeugen `t30`/`t31`.

**2. Absatz 1 und Absatz 2 des § 622 dürfen nicht gleichzeitig feuern**
(Ledger D-07-04): je zwei Varianten der Absatz-1-Regeln
(Arbeitnehmerkündigung immer, Arbeitgeberkündigung nur unterhalb der
Zweijahresschwelle) statt eines Schlüsselkonflikts bei `key(d)`. Zeugen
`t32`–`t34`.

**3. `not` über eine wertungsabhängige Relation bleibt unentschieden**
(Ledger D-07-06) und `not` über einen ABGELEITETEN Schluss feuert überhaupt
nicht (Ledger D-07-14, gemessen an `t133`). Beide Fälle sind durch
ausdrückliche positive Relationen des Falls ersetzt
(`kein_arbeitsverhaeltnis_im_sinne_des_622`,
`abhilfe_nicht_verweigerbar_651k` und dreißig weitere). Die Verneinung EINER
Relation, die der Fall direkt und ausdrücklich negativ beantwortet, bleibt
unproblematisch.

**4. Elf Vermutungen als `presumption … unless`.** § 630h Abs. 1, 2, 3
(zweimal), 4, 5 (zweimal) sowie § 648 Satz 3, § 650c Abs. 2, § 650f Abs. 5
Satz 3 und § 650g Abs. 3. Jede trägt ihren Gegenbeweis als `unless`-Klausel,
die SÄMTLICHE Variablen des Kopfes bindet (§ 190); der Gegenbeweis ist stets
eine ausdrückliche Eingabe des Falls. Zeugen mit beiden Seiten: `t65`/`t66`,
`t67`/`t68`, `t78`/`t79`, `t104`/`t104a`.

**5. „Vor dem Ereignis" wird VORWÄRTS gerechnet** (Ledger D-07-09). Die
Abstände „sieben Tage vor Reisebeginn" (§ 651e), „20 Tage vor Reisebeginn"
(§§ 651f, 651g, 651h) und „zwei Wochen vor Antritt" (§ 651u) werden nicht als
negativer Kalenderschritt vom Reisebeginn aus gerechnet — ein negativer
`calendar_day`-Schritt kompiliert, führt aber nicht aus. Sie werden vom Tag
der Erklärung an vorwärts gerechnet und mit dem Reisebeginn verglichen.
Zeugen `t126`/`t126a`, `t127`/`t127a`, `t130`, `t143`.

**6. § 193 wird nur dort gerechnet, wo der Text eine Erklärung INNERHALB der
Frist verlangt.** Das ist bei § 650g Abs. 4 Satz 3 (begründete Einwendungen)
und § 650r Abs. 1 Satz 2 (Sonderkündigung) der Fall; gerechnet wird
`add_business_days(kalendarisches Ende, 1 business_day)` über
`KALENDER_BUNDESWEIT` des Eigentümerpakets `de.bgb.fristen` — derselbe
Ausdruck wie dessen Regel `Verlegung193`. Alle übrigen Termine dieses Pakets
werden durch bloßen Zeitablauf wirksam. Zeugen mit beiden Seiten:
`t105` (Sonnabend → Montag) und `t105a` (Werktag bleibt).

**7. § 621 Nr. 2 und Nr. 4 rechnen über den Kalender und das Quartal**
(Ledger D-07-12). Der Wochenanfang und der Quartalsanfang sind — wie bei
`de.bgb.miete` (D-06-08) — Angaben des Falls, weil §258 für sie keinen Term
kennt; der erste Werktag der Woche wird mit `add_business_days` bestimmt, der
Sonnabend als fünfter Tag nach dem Wochenanfang, das Quartalsende mit zwei
Monatsschritten und `month_end_of`. Zeugen `t112`/`t112a`, `t113`/`t113a`.

## Fristen

Eine Politik `BGB_DIENST_WERK_KALENDER` für das ganze Paket (§ 168.2), mit
demselben Feldsatz wie `BGB_FRISTEN_KALENDER` (Ledger D-07-01). Alle Zeilen —
`docs/foundations/de-bgb/DEADLINES.json`, Abschnitt BG-07.

Tage: §§ 621 Nr. 1, 650b Abs. 2, 650g Abs. 4, 651e Abs. 1, 651f Abs. 1,
651h Abs. 4, 5. Wochen: §§ 617 Abs. 1, 621 Nr. 4, 5, 622 Abs. 1, 3, 626
Abs. 2, 650r Abs. 1, 651u Abs. 3. Monate: §§ 613a Abs. 6, 622 Abs. 2, 624.
Jahre: §§ 630f Abs. 3 (zehn), 634a Abs. 1 (zwei und fünf), 651j (zwei).
Die regelmäßige Verjährungsfrist des § 634a Abs. 1 Nr. 3 und Abs. 3 rechnet
`de.bgb.fristen` (§§ 195, 199 Abs. 1) und wird von dort QUALIFIZIERT gelesen.

**Stunden sind in diesem Paket keine Frist** (Ledger D-07-11): die
Stundengrenzen der §§ 651a Abs. 5 Nr. 2, 651c Abs. 1 Nr. 3, 651h Abs. 4
Satz 1 Nr. 1 Buchst. c, 651k Abs. 5 Nr. 2 und 651w Abs. 1 Satz 1 Nr. 2 sind
ausdrückliche Angaben des Falls; die Politik §86 zählt Tage, Wochen, Monate
und Jahre nach §§ 187 f. Die Zeilen stehen mit `BOUNDARY` in `DEADLINES.json`.

## Geld (Rundung)

Der Untertitel 1 führt keine Division: §§ 615 und 616 rechnen je EINE
Subtraktion (Ledger D-07-03). Die Untertitel 3 bis 5 rechnen Anteile, und
zwar GENAU EINMAL je Größe, gerundet auf den Cent —
`div_round(Wert × z, n × 1.0, 2, "HALF_UP")` (Ledger D-07-07):

| Norm | Größe |
|---|---|
| § 638 Abs. 3, § 651m Abs. 1 | Verhältnis der Werte — als PAAR GANZER ZAHLEN, weil ein Produkt zweier Money-Größen in v1 nicht definiert ist (§58) |
| § 641 Abs. 3 | das Doppelte der Mängelbeseitigungskosten (Multiplikation ohne Rundung) |
| §§ 648 Satz 3, 650f Abs. 5 Satz 3 | 5 Prozent des nicht erbrachten Teils |
| § 650c Abs. 3 | 80 Prozent der angebotenen Mehrvergütung |
| § 650f Abs. 1 | 10 Prozent Nebenforderungen |
| § 650m Abs. 1, 2, 4 | 90, 5, 10 und 20 Prozent der Gesamtvergütung |
| § 651g Abs. 1 | 8 Prozent des Reisepreises |
| § 651p Abs. 1 | dreifacher Reisepreis (Multiplikation ohne Rundung) |

Prozentsätze sind LITERALE des Textes, keine Parameter.

## Bewertende Merkmale (DECISION-0194)

**WERTUNG** (`external judgment relation … { authority Court; }`) — 44
Merkmale, darunter: Gesamtbetrachtung aller Umstände (§ 611a Abs. 1),
grobe Fahrlässigkeit (§ 617 Abs. 1), wichtiger Grund (§§ 626, 627, 648a),
allgemein anerkannter fachlicher Standard (§ 630a Abs. 2), Entbehrlichkeit
von Information und Aufklärung (§§ 630c Abs. 4, 630e Abs. 3), mutmaßlicher
Wille (§ 630d Abs. 1 Satz 4), Rechtzeitigkeit und Verständlichkeit der
Aufklärung (§ 630e Abs. 2), Unverzüglichkeit der Einsichtgewährung (§ 630g
Abs. 1), volle Beherrschbarkeit des Risikos und hypothetische Einwilligung
(§ 630h Abs. 1, 2), grober Behandlungsfehler (§ 630h Abs. 5), übliche
Beschaffenheit (§ 633 Abs. 2), unverhältnismäßige Kosten (§§ 635 Abs. 3,
651k Abs. 1), Fehlschlagen und Unzumutbarkeit (§§ 636, 637), Unwesentlichkeit
des Mangels und Angemessenheit der Abnahmefrist (§ 640), angemessene
Entschädigung (§§ 642, 651h), wesentliche Überschreitung des Kostenanschlags
(§ 649), wesentliche Bedeutung des Werks (§ 650a Abs. 2), Zumutbarkeit der
Änderung (§ 650b), Prüffähigkeit der Schlussrechnung (§ 650g Abs. 4),
erhebliche Vertragsänderung (§ 651g), unvermeidbare außergewöhnliche
Umstände (§ 651h Abs. 3), erhebliche Beeinträchtigung (§§ 651l, 651n Abs. 2).

**FESTGESTELLTE TATSACHE** (`kind empirical`, im Fall `origin adjudicated`):
Kenntnis der kündigungserheblichen Tatsachen (§ 626 Abs. 2), Vertretenmüssen
(§ 619a), Betriebsübergang (§ 613a), Einwilligungsunfähigkeit (§ 630d Abs. 1
Satz 2), erkennbare Behandlungsfehlerumstände (§ 630c Abs. 2 Satz 2),
fehlende Befähigung (§ 630h Abs. 4), arglistiges Verschweigen (§§ 634a
Abs. 3, 639) — letzteres wie bei `de.bgb.kauf` im Tatsachenkanal, nicht im
Wertungskanal (Ledger D-07-05).

**LESARTEN** (`interpretation … any_of`): in diesem Paket nicht gebraucht —
der Text stellt an keiner Stelle zwei konkurrierende Auslegungen zur
Formalisierung, die der Fall wählen müsste.

## Was dieses Paket nicht tut (Grenzen aus dem Text)

1. **§§ 611b, 641a** sind weggefallen, **§ 651** ist seit dem 1. Januar 2018
   eine Fundstellenangabe („jetzt § 650") — drei erklärte Grenzen, die
   `check_formalization_depth.py` als SOURCE_ONLY mit Grund führt.
2. **Verweise in Nachbarpakete** werden als institutionelle Schlüsse
   abgesenkt, nie als doppelte Regel (Ledger D-07-10): §§ 249 ff., 275, 280,
   281, 283, 284, 311a, 312, 314, 323, 326, 346–348, 355, 442, 447, 842–846
   und Abschnitt 3 Titel 2a gehören `de.bgb.schuldrecht_at` und
   `de.bgb.kauf`; § 218 und die regelmäßige Verjährungsfrist gehören
   `de.bgb.fristen`.
3. **Fremde Ordnungen** sind benannt, nicht formalisiert
   (`SOURCES.json`, `external`): EGBGB Art. 244, 249, 250, 251, 252,
   Honorarordnung für Architekten und Ingenieure, Zivilprozessordnung
   (§ 650d), Grundbuch- und Schiffsregisterrecht (§§ 647a, 650e),
   Aufsichtsrecht der Kreditinstitute und Kreditversicherer sowie das
   Reisesicherungsfondsgesetz (§§ 632a Abs. 2, 650f Abs. 2, 651r Abs. 2, 3),
   Strafprozessordnung § 52 (§ 630c Abs. 2 Satz 3), EG-Fahrzeuggenehmigungs-
   und Fahrerlaubnis-Verordnung (§ 651a Abs. 3), Gewerbeordnung und
   Richtlinie (EU) 2015/2302 (§ 651s), die fünf Fahrgastrechteverordnungen
   (§ 651p Abs. 3), Kündigungsschutz-, Betriebsverfassungs- und Teilzeit- und
   Befristungsgesetz (§§ 620, 622).
4. **Institutionelle Tatsachen ohne eigene Schlussfolgerungskette**: § 613a
   Abs. 1 Satz 2–4, Abs. 2 Satz 2, Abs. 3, Abs. 5 (kein Bemessungsschlüssel),
   § 642 Abs. 2 (zwei Richtungen ohne Schlüssel), § 651l Abs. 2 (Aufteilung
   des Reisepreises ohne Schlüssel), § 651w Abs. 5. Die vollständige
   Absatz-Karte mit je einem Grund steht in `analysis/saetze.json`
   (217 RULE-, 47 ANCHORED-, 3 BOUNDARY-Absätze).
5. **Stundenfristen** — siehe oben, Ledger D-07-11.
6. **Der Wortlaut geht der Erwartung vor** (Ledger D-07-13): § 651r trägt in
   der geltenden Fassung nicht die im Sitzungsauftrag genannten 110 Prozent
   und 22 Millionen Euro, sondern den Absicherungsvertrag nach dem
   Reisesicherungsfondsgesetz.

## Unabhängige Erwartung

`sources/egbgb-art-229-uebergang/` hält den Wortlaut der beiden
Übergangsnormen **Art. 229 § 39 und § 42 EGBGB** fest (gesetze-im-internet.de,
abgerufen am 18.09.2026, `PINS.sha256`). Sie stehen in einem ANDEREN Gesetz
als der Snapshot dieses Pakets und bestätigen die beiden Korridore
unabhängig: neues Bauvertragsrecht ab dem 1. Januar 2018, neues Reiserecht ab
dem 1. Juli 2018. Zeugen auf beiden Seiten jedes Korridors: `t99a`/`t99b`,
`t119a`, `t121a`/`t121b`. Zeile: `SOURCES.json.expectations`.

## Stab-Ketten (Auditurteil)

`audit.py --fast` nennt 31 von 347 Regeln als „Posten in eine Richtung", fast
alle mit dem Hinweis „Schwelle in der Marke der Prämisse". Das ist bei diesem
Paket kein Warteschlangenlager: die Prämissen sind ausdrückliche Eingaben des
Falls (positive Gegenfakten nach D-07-06 und D-07-14) und Wertungen des
Gerichts nach DECISION-0194 — beide haben definitionsgemäß keinen Produzenten
im Paket. Vier Paragraphen mit viel Text je Norm (§§ 650 Abs. 2–4, 651p
Abs. 2, 3, 651r Abs. 2, 3, 651w Abs. 3, 5) hängen an fremden Ordnungen; ob
sie Brücken oder erklärte Grenzen werden, ist als `V7-07-03` offen.

## Prüfung

```sh
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
./law engine lock corpus/laws/de/bgb/dienst-werk --clir corpus/clir --write
python3 corpus/laws/de/bgb/fristen/tools/gen_kalender.py        # Kalenderzeile im Lock
./law engine check corpus/laws/de/bgb/dienst-werk
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-dienst-werk.lawir.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.dienst_werk#bauvertrag"
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.dienst_werk#bauvertrag"
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-07 --check
```

Die Familien `werkverjaehrung`, `bauvertrag`, `kuendigung-621-rest` und
`architekten-und-bautraegervertrag` deklarieren
`world = ["de.bgb.dienst_werk", "de.bgb.fristen", "de.bgb.core"]`: sie
brauchen die regelmäßige Verjährungsfrist beziehungsweise den Kalender
`KALENDER_BUNDESWEIT` des Eigentümerpakets im Programm §267.1.
