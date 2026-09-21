# de.bgb.allgemeiner_teil — BGB Buch 1: Allgemeiner Teil

Paket BG-03 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Geltungsbereich: **§§ 1–185 und
§§ 226–240a** — 216 Einheiten der Publikation (214 geltende Paragraphen,
414 Absätze; § 10 und § 23 sind weggefallen und als Grenze mit Grund
erklärt). Quellen: `sources/de-bgb-allgemeiner-teil/` und `sources.law`,
erzeugt aus dem Register DOKNR durch
`corpus/tools/sources/sync/sync_de_bgb_packages.py` — **nicht von Hand
ändern**.

Importe: `de.bgb.core` (Personen, Sachen, Tiere), `de.bgb.fristen` (jede
Frist und jedes Lebensalter, DECISION-0319 Р4), `calc.kinship` (Elternkante
des § 11).

## Aufgabenkarte: was in welcher Datei steht

| Datei | Normen | Was sie trägt |
|---|---|---|
| `package.law` | — | gemeinsamer Wortschatz: Typen der Nabe, Willenserklärung, Rechtsgeschäft, Ort, Prüfungszeitpunkt, die beiden Politiken §86 |
| `abschnitt-01-titel-01-natuerliche-personen.law` | §§ 1, 2, 7–14 | Rechtsfähigkeit, Volljährigkeit, Wohnsitz (auch Soldat und Kind), Namensrecht, Verbraucher und Unternehmer |
| `abschnitt-01-titel-02-vereine.law` | §§ 21–54 | Rechtsfähigkeit des Vereins, Vorstand und Vertretung, Haftung §§ 31–31b, Beschlüsse §§ 32–35, Berufung §§ 36, 37, Mitgliedschaft §§ 38–40, Auflösung und Liquidation §§ 41–54 |
| `abschnitt-01-titel-02-vereinsregister.law` | §§ 55–79a | Zuständigkeit, Mindesterfordernisse, Anmeldung und Zurückweisung, Eintragungsinhalt, Vertrauensschutz §§ 68, 70, 71, Frist des § 73, Zwangsgeld, Einsicht |
| `abschnitt-01-titel-02-stiftungen.law` | §§ 80–89 | Entstehung und Anerkennung, Vermögen §§ 83b, 83c, Organe §§ 84–84c, Satzungsänderung §§ 85, 85a, Zulegung und Zusammenlegung §§ 86–86h, Auflösung §§ 87–87c, kirchliche Stiftungen, § 89 |
| `abschnitt-02-sachen-und-tiere.law` | §§ 90–103 | Sache und Tier, vertretbare und verbrauchbare Sachen, Bestandteile §§ 93–96, Zubehör §§ 97, 98, Früchte, Nutzungen und ihre Teilung §§ 99–103 |
| `abschnitt-03-titel-01-geschaeftsfaehigkeit.law` | §§ 104–113 | Geschäftsunfähigkeit, § 105a, beschränkte Geschäftsfähigkeit, §§ 107–111, Ermächtigungen §§ 112, 113 |
| `abschnitt-03-titel-02-willenserklaerung.law` | §§ 116–144 | Vorbehalt, Scheingeschäft, Irrtum und Anfechtung §§ 119–124, Form §§ 125–129, Zugang §§ 130–132, Auslegung § 133, Verbote §§ 134–137, § 138, §§ 139–144 |
| `abschnitt-03-titel-03-vertrag.law` | §§ 145–157 | Antrag und Annahme, Annahmefristen §§ 147–149, § 150, § 151, § 152, Einigungsmangel §§ 154, 155, Versteigerung § 156, Auslegung § 157 |
| `abschnitt-03-titel-04-bedingung-und-zeitbestimmung.law` | §§ 158–163 | aufschiebende und auflösende Bedingung, Rückbeziehung, Schwebezeit §§ 160, 161, § 162, Zeitbestimmung § 163 |
| `abschnitt-03-titel-05-vertretung.law` | §§ 164–181 | Wirkung der Vertretererklärung, § 166, Vollmacht §§ 167–176, Vertreter ohne Vertretungsmacht §§ 177–180, Insichgeschäft § 181 |
| `abschnitt-03-titel-06-einwilligung-und-genehmigung.law` | §§ 182–185 | Zustimmung, Widerruflichkeit, Rückwirkung, Verfügung eines Nichtberechtigten |
| `abschnitt-06-ausuebung-der-rechte.law` | §§ 226–231 | Schikaneverbot, Notwehr, Notstand, Selbsthilfe und ihre Grenzen |
| `abschnitt-07-sicherheitsleistung.law` | §§ 232–240a | Arten der Sicherheit, Wirkung der Hinterlegung, Brüche der §§ 234, 236, 237, Bürge, Ergänzungspflicht, Verordnungsermächtigung |

`analysis/saetze.json` (erzeugt von `tools/gen_saetze.py`) hält je Paragraph
die Zahl der Absätze gegen die auf ihn geankerten Regeln, Urteilskanäle und
Lesarten: 216 Paragraphen, 414 Absätze, 428 Regeln, 39 Urteilskanäle,
4 Lesarten; ohne Regel nur § 10 und § 23 (weggefallen).

## Drei Kanäle für bewertende Merkmale (DECISION-0194)

Das BGB überlässt die Bewertung an 39 Stellen dem Gericht; jede steht als
`external judgment relation … { authority Court; }` mit dem Normtext als
`label de official` — unter anderem § 12 (Interesse verletzt, weitere
Beeinträchtigungen), § 13 („überwiegend“), § 91 und § 97 (Verkehrsanschauung
und wirtschaftlicher Zweck), § 107 („lediglich ein rechtlicher Vorteil“),
§ 111 und § 174 („unverzüglich“), § 119 („anzunehmen ist“), § 121 („ohne
schuldhaftes Zögern“), § 138 (gute Sitten, auffälliges Missverhältnis),
§ 139, § 140, § 147 Abs. 2, § 155, § 157, § 160, § 162, §§ 226–230
(Schikane, Erforderlichkeit), § 82, § 84a, § 85, § 86.

**Festgestellte Tatsache** (`kind empirical`, im Fall `origin adjudicated`)
ist, was das Gesetz feststellen lässt: der Zustand krankhafter Störung
(§ 104 Nr. 2), Kenntnis und Kennenmüssen (§§ 109, 122, 123, 142, 166, 169,
173, 179), der Tag der Entdeckung der Täuschung (§ 124 Abs. 2), der Zugang
(§ 130) und die Eintragung im Vereinsregister (§§ 21, 68, 71).

**Zwei Lesarten (§152, Gruppe `any_of`)** stehen an zwei Stellen:

- § 133 — der ermittelte wirkliche Wille (`WirklicherWilleMassgeblich`)
  gegen den objektiven Empfängerhorizont (`ObjektiverEmpfaengerhorizontMassgeblich`);
- § 32 Abs. 1 Satz 3 — die Enthaltung ist keine abgegebene Stimme
  (`EnthaltungIstKeineAbgegebeneStimme`) gegen die Lesart, die sie mitzählt
  (`EnthaltungIstAbgegebeneStimme`). Zeuge: `tests/ve01`.

## Fristen

Jede Frist rechnet `de.bgb.fristen`; das Paket schreibt nur die Eingänge
(`frist_ereignis`, `frist_dauer_kalender`, `lebensjahr_gefragt`) und liest
die Ergebnisse. Vor jeder Regel steht eine Zeile in
`docs/foundations/de-bgb/DEADLINES.json` (Abschnitt `BG-03`, 17 Zeilen).
Ausgeführt mit Zeugen: § 2 und §§ 104 Nr. 1, 106 (Lebensalter), § 108
Abs. 2 (zwei Wochen mit § 193), § 124 Abs. 1, 2 (Jahresfrist mit § 193),
§ 73 (drei Monate).

**Eine Politik je Fall** (§168.2): `BGB_ALLGEMEINER_TEIL_KALENDER` trägt den
Kalenderschritt (§ 188 Abs. 2, 3), `BGB_ALLGEMEINER_TEIL_TAG` den Tagesschritt
mit Roll (§§ 187 Abs. 1, 188 Abs. 1, 193). Die Felder sind dieselben wie bei
`BGB_FRISTEN_*`; eigene Politiken braucht das Paket, weil die Politik des
Falls im ausführenden Paket erklärt sein muss (LDC-E1332).

**Kette zweier Fristen.** Das Ende der Frist des § 50 Abs. 1 Satz 4 ist der
Anfang der Frist des § 51. Beide laufen über dieselben Prädikate von
`de.bgb.fristen`; eine Regel, die aus `frist_ende_kalender` wieder
`frist_dauer_kalender` speist, macht das Programm unstratifizierbar
(§110/§103, gemessen). Deshalb nimmt § 51 den Tag der bewirkten
Bekanntmachung als Angabe des Falls (`bekanntmachung_als_bewirkt_angegeben`);
§ 50 rechnet ihn unabhängig aus (Ledger D-03-04).

## Rundung

Drei Vorschriften nennen Bruchteile eines Wertes: § 234 Abs. 3 und § 236
(drei Viertel des Kurswerts), § 237 Satz 1 (zwei Drittel des
Schätzungswerts); dazu tritt der „der Dauer der Berechtigung entsprechende
Teil“ des § 101 Nr. 2 und des § 103. Gerechnet wird **einmal** auf den Cent:
`div_round(Wert × z, n × 1.0, 2, "HALF_UP")` — Zähler und Nenner ganze
Zahlen, der Divisor eine `Decimal` (Ledger D-03-02). Anteile am
Vereinsvermögen (§ 45 Abs. 3) bleiben exakte Paare ganzer Zahlen: kein Geld,
keine Rundung. Zeugen: `tests/si01` (925,92 €), `tests/si02` (666,67 €),
`tests/s01` (595,07 €), `tests/ve04` (1/3).

## Szenarien

18 Szenarien in sechs Familien, Erwartungen von Hand aus dem Text gerechnet,
beide Auswerter, Differential byteweise (43 evaluate-Aufrufe):

| Familie | Szenarien | Norm |
|---|---|---|
| `#personen` | p01–p03 | § 2 (18. Geburtstag und Vortag), § 11 (Wohnsitz des Kindes), § 13 gegen § 14 (Urteilskanal offen) |
| `#rechtsgeschaefte` | r01–r05 | § 108 Abs. 2 mit § 193 (beide Seiten der Frist), § 110, § 124 mit § 193, § 138 Abs. 2 (Kanal offen) |
| `#sachen` | s01, s02 | § 101 Nr. 2 (Teilung nach Tagen), §§ 97, 98 Nr. 2 (Zubehör des Landguts) |
| `#vertretung` | v01, v02 | § 179 Abs. 2 (gutgläubiger Vertreter), § 181 (Insichgeschäft) |
| `#sicherheitsleistung` | si01, si02 | § 234 Abs. 3 (drei Viertel), § 237 Satz 1 (zwei Drittel) |
| `#vereine` | ve01–ve04 | § 32 Abs. 1 Satz 3 (beide Lesarten), §§ 33, 71, § 73 (Frist), § 45 Abs. 3 |

## Was das Paket nicht tut und warum

- **Der Inhalt fremder Gesetze steht nicht hier.** Das gesetzliche Verbot
  (§ 134), das Veräußerungsverbot (§§ 135, 136), die Rechtsverordnung nach
  § 240a, das Landesrecht (§§ 44, 88), die Vereinsregisterverordnung und die
  Insolvenzordnung sind typisierte EINGÄNGE des Falls; das Paket sagt, welche
  Rechtsfolge an sie hängt, nicht, was sie anordnen (GOAL, Grenzen).
- **Kein Register.** Eintragungen, Anmeldungen, Genehmigungen und ihre Tage
  sind Angaben des Falls; § 55a und § 79 Abs. 2–5 betreffen die Einrichtung
  des Registers durch die Länder und werden nur insoweit ausgeführt, als der
  Text eine Folge an eine Tatsache knüpft.
- **Fristen mit Hemmung.** § 124 Abs. 2 Satz 2 verweist für den Lauf der
  Jahresfrist auf die §§ 206, 210, 211; Hemmung und Ablaufhemmung gehören
  `de.bgb.fristen` und stehen dort als TODO der Welle B2. Dieses Paket
  rechnet die Frist ohne sie.
- **Schlusspunkte ohne Leser.** Vierzig Regeln schließen mit einer
  Rechtsfolge, die kein anderes Prädikat dieses Pakets liest (Pflicht zur
  Anmeldung, Zwangsgeld, Aufbewahrung, Bescheinigung). Das ist kein
  Stab-Zopf, sondern das Ende der Norm: das BGB knüpft an sie ein Verfahren
  an, das in FamFG und Vereinsregisterverordnung liegt.
- **Beweislast und Verfahren** (§ 31a Abs. 1 Satz 3) stehen als Aussage über
  die Beweislast, nicht als Prozessregel.
- **§ 90a** ist als Regel des Pakets ausgeführt, nicht als Typhierarchie: das
  Tier ist keine Sache (Nabe), die Vorschriften über Sachen sind auf es
  entsprechend anzuwenden, soweit nichts anderes bestimmt ist.

## Prüfung (nur punktuell)

```sh
./law engine check corpus/laws/de/bgb/allgemeiner-teil
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-03 --check
python3 corpus/laws/de/bgb/allgemeiner-teil/tools/gen_saetze.py --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-allgemeiner-teil.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.allgemeiner_teil#rechtsgeschaefte"
python3 corpus/run_kz_regression.py --only "de.bgb.allgemeiner_teil#rechtsgeschaefte" --write-manifest
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.allgemeiner_teil#rechtsgeschaefte"
```
