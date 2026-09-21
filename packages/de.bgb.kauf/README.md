# de.bgb.kauf — Bürgerliches Gesetzbuch, Buch 2 Abschnitt 8 Titel 1: Kauf, Tausch

Paket BG-05 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Es trägt **§§ 433–480** in fünf
Untertiteln, Stand `legal_cutoff` 2026-09-17 (Quelle: sources.law, erzeugt aus
dem Register DOKNR; konsolidierter Text von gesetze-im-internet.de, amtliche
Verkündung im Bundesgesetzblatt Teil I).

| Maß | Wert |
|---|---|
| Paragraphen | 63 |
| Absätze (`analysis/saetze.json`) | 134 — 120 RULE, 11 CHANNEL, 3 EXTERNAL |
| Tiefe §33.1 | **63 EXECUTABLE**, 0 ANCHORED, 0 SOURCE_ONLY |
| Regeln | 228 (strict 195, defeasible 17, defeater 13) |
| Szenarien | 31 in sieben Familien, beide Auswerter, Differential byteweise gleich |
| Pflichten / Positions | 3 duty (§433), 1 duty (§439), 2 power (§§437, 441), 2 duty (§448), 2 duty (§475), 7 duty (§§454, 457–458, 466–467, 479); 40 positions scenarios in `#positions-p1` |

P1 kauf geschlossen: 21 `POSITION`, 20 `EXISTING`, 0 `BOUNDARY`; alle Zeilen
durch Paarszenarien `evaluate positions()` geprüft.

## Karte der Aufgaben

| Untertitel | §§ | Datei |
|---|---|---|
| 1 Allgemeine Vorschriften — Pflichten, Sachmangel, Rechtsmangel, Rechte des Käufers | 433–437, 442–445 | `untertitel-01-a-pflichten-und-mangel.law` |
| 1 — Verjährung, Nacherfüllung, Minderung, Rückgriff | 438–441, 445a–445c | `untertitel-01-b-rechtsbehelfe-und-verjaehrung.law` |
| 1 — Gefahr- und Lastenübergang, Kosten, Eigentumsvorbehalt, Rechtskauf | 446–453 | `untertitel-01-c-gefahruebergang-und-nebenbestimmungen.law` |
| 2 Besondere Arten des Kaufs — Kauf auf Probe, Wiederkauf, Vorkauf | 454–473 | `untertitel-02-besondere-arten-des-kaufs.law` |
| 3 Verbrauchsgüterkauf | 474–479 | `untertitel-03-verbrauchsgueterkauf.law` |
| 4 Reparaturverpflichtung des Herstellers | 479a–479g | `untertitel-04-reparaturverpflichtung.law` |
| 5 Tausch und der Korridor 2022 | 480 | `untertitel-05-tausch-und-uebergang-2022.law` |

## Die fünf Mechaniken

**1. Der Mangel ist negativ bestimmt.** § 434 sagt, wann die Sache *frei von
Sachmängeln* ist. Deshalb trägt jede Anforderung der Absätze 2 bis 4 eine
eigene POSITIVE Eingabe, und der Mangel folgt aus ihrer AUSDRÜCKLICHEN
Verneinung durch den Fall (`not vereinbarte_beschaffenheit_vorhanden(k)`).
Das Schweigen des Falls schaltet keine Norm frei. Jede Nummer des
geschlossenen Katalogs hat ihre eigene Regel: eine Disjunktion im Regelkörper
sänke zu Regeln `Name/alt/N` ab, auf die kein `applied(Name)` je passt.

**2. Die Fristen.** §§ 438, 445b, 455, 462, 469, 475, 475c, 475e und 477
rechnen mit dem Kalenderschritt des § 188 Abs. 2 unter der Politik
`BGB_KAUF_KALENDER` (`start_count same_day`, `include_end true`,
`roll no_roll`, `month_end last_day_of_month`) — demselben Feldsatz wie
`BGB_FRISTEN_KALENDER`. **§ 193 wird nur dort gerechnet**, wo der Text eine
Erklärung INNERHALB der Frist verlangt: bei den Ausschlussfristen der §§ 462
und 469 Abs. 2 (Ausübung des Wiederkaufs- und des Vorkaufsrechts) durch
`add_business_days(Ende, 1 business_day)`. Die Verjährung der §§ 438 und 445b
wird NICHT verlegt: sie tritt mit Zeitablauf ein und verlangt von niemandem
eine Handlung (dasselbe Kriterium hat BG-10 gemessen, Ledger D-10-05). Die
regelmäßige Verjährungsfrist des § 438 Abs. 3 rechnet `de.bgb.fristen`
(§§ 195, 199 Abs. 1 mit dem Ultimo).

**3. Rundung.** Beträge sind `EUR`. Das Paket teilt an genau zwei Stellen:
§ 441 Abs. 3 (Herabsetzung des Kaufpreises im Verhältnis der beiden Werte)
und § 467 Satz 1 (verhältnismäßiger Teil des Gesamtpreises). Beide Male sind
die Werte ganze Zahlen in Cent — der Text nennt weder Einheit noch
Bewertungsverfahren, und `Money / Money` ist in §58 nicht genannt —, und
gerechnet wird EINMAL je Anspruch:
`div_round(Betrag × Zähler, Nenner × 1.0, 2, "HALF_UP")`. Ein Zinssatz, ein
Schwellenwert oder eine Rundung, die der Text nicht nennt, ist hier nicht
erfunden.

**4. Bewertende Merkmale (DECISION-0194).** Elf Absätze führen einen der drei
Kanäle, gewählt nach dem Wortlaut des Paragraphen:

- **Wertung** (`external judgment relation … { authority Court; }`) — „üblich
  … und die der Käufer erwarten kann“ (§ 434 Abs. 3 Nr. 2), „deren Erhalt der
  Käufer erwarten kann“ (Nr. 4), „unverhältnismäßige Kosten“ (§ 439 Abs. 4),
  „unzumutbar“ und „fehlgeschlagen“ (§ 440), „Schätzung“ (§ 441 Abs. 3
  Satz 2), „grobe Fahrlässigkeit“ (§ 442 Abs. 1 Satz 2), „angemessene Frist“
  (§§ 455, 475 Abs. 6), **„unverzüglich“ (§ 469 Abs. 1)** — eine Wertung,
  keine Frist von null Tagen —, „Zeitraum, den der Verbraucher erwarten kann“
  (§ 475b Abs. 4 Nr. 2), „derart schwerwiegend“ (§ 475d Abs. 1 Nr. 3),
  „mit der Art der Ware unvereinbar“ (§ 477 Abs. 1), „angemessener Zeitraum“
  und „angemessenes Entgelt“ (§ 479b), „angemessener Preis“ (§ 479c).
- **Festgestellte Tatsache** (`relation kind empirical`, im Fall
  `origin adjudicated`) — Kenntnis des Mangels bei Vertragsschluss (§ 442
  Abs. 1 Satz 1), arglistiges Verschweigen (§§ 438 Abs. 3, 442, 444, 445),
  die Tage der Ablieferung und der Übergabe.
- **Lesarten** (`interpretation … any_of`) — nicht gebraucht: dieser Titel
  streitet über Wertungen, nicht über den Wortsinn. § 434 Abs. 3 Satz 3 nennt
  seine drei Ausnahmen selbst und ist deshalb eine Defeater-Schicht.

**5. Der Korridor 2022.** Art. 229 § 58 EGBGB stellt auf den **Tag des
Vertragsschlusses** ab. Das ist eine Tatsache des Falls, nicht die legal time
der Auswertung; ein `effective`-Fenster (§87) prüft aber die legal time und
gäbe für jeden 2026 ausgewerteten Fall dieselbe Antwort. Der Korridor ist
deshalb ein Garde über `vertragsschluss_am` (`neues_kaufrecht_anwendbar`).
Zeugen: `u01` (1.1.2022), `u02` (31.12.2021), `u03` (2.1.2022).

## Urteilskanal und Schließung

Urteilsanfragen folgen der SCHLIESSUNG des gefragten Kopfes. Deshalb hat der
Sachmangel einer Ware mit digitalen Elementen (§ 475b Abs. 2) einen EIGENEN
Kopf `sachmangel_der_ware_mit_digitalen_elementen`, der erst in `mangel`
einmündet: sonst zöge jede Frage nach dem Sachmangel des § 434 das Urteil über
den erwartbaren Aktualisierungszeitraum mit (dasselbe Prinzip wie Ledger
D-10-07). **Gemessen 17.09.2026:** anders als bei einem `unless` einer
poraussierbaren Regel STELLT der `unless` einer `presumption` die Urteilsfrage
— die Vermutung des § 477 verlangt die Antwort des Gerichts zur
Unvereinbarkeit, bevor das Dokument COMPUTED wird (Ledger D-05-07).

## Was das Paket nicht tut und warum

1. **Rücktritt, Schadensersatz und Fristsetzung** (§§ 280, 281, 283, 284,
   311a, 323, 326 Abs. 5, 346–348, 218) gehören `de.bgb.schuldrecht_at`
   (BG-04). § 437 nennt hier nur, WELCHES Recht dem Käufer zusteht; ob der
   Rücktritt wirksam erklärt ist, entscheidet das Nachbarpaket. Die wenigen
   Voraussetzungen, die BG-05 selbst braucht (`ruecktritt_vom_vertrag_erklaert`,
   `ruecktritt_nach_218_unwirksam`, `annahmeverzug_des_kaeufers_am`), sind
   bis zur Brücke eigene Eingaben (Ledger D-05-02).
2. **Digitale Produkte** (Abschnitt 3 Titel 2a, §§ 327 ff.), an deren Stelle
   die §§ 445c, 453 Abs. 1 Satz 2 und 475a verweisen, liegen ebenfalls bei
   BG-04. BG-05 stellt nur FEST, dass die kaufrechtlichen Vorschriften nicht
   anzuwenden sind.
3. **Verbraucher und Unternehmer** (§§ 13, 14) gehören
   `de.bgb.allgemeiner_teil` (BG-03). Deren Köpfe hängen dort am
   Rechtsgeschäft; BG-05 erklärt eigene Eingänge mit Anker auf § 474 Abs. 1
   und wird sie ohne Änderung der lesenden Regeln durch die Brücke ersetzen
   (Ledger D-05-05).
4. **Fremde Gesetze** — § 377 HGB (Rügeobliegenheit, § 445a Abs. 4), ZPO und
   InsO (§§ 450, 471), Anhang II der Richtlinie (EU) 2024/1799 und Artikel 2
   Nummer 20 der Verordnung (EU) 2024/1781 (§§ 479a, 479b) — kommen als
   typisierte Eingabe des Falls herein und werden nicht formalisiert.
5. **Ein Fall trägt genau einen streitigen Mangel je Kaufvertrag.** Die
   Mangelprädikate haben den Vertrag als Schlüssel; mehrere Mängel desselben
   Vertrags sind mehrere Fälle (Ledger D-05-01).
6. **Das bis zum 31. Dezember 2021 geltende Kaufrecht** ist nicht Teil dieses
   Schnitts. Für frühere Verträge schweigt das Paket; es behauptet nicht, die
   Vermutung greife nicht (Zeuge `u02`).

## Prüfung

```sh
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
./law engine check corpus/laws/de/bgb/kauf
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-kauf.lawir.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.kauf#sachmangel" …
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.kauf#sachmangel" …
```

Die sieben Familien: `#sachmangel` (8), `#verjaehrung-438` (6), `#minderung`
(3), `#verbrauchsgueterkauf` (5), `#uebergang-2022` (3), `#besondere-arten`
(4), `#reparatur` (2).

## Sprache

In `.law`, `.lawtest`, Kommentaren, `label` und diesem README nur Deutsch und
Englisch (DECISION-0319, Р7).
