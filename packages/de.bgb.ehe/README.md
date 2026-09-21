# de.bgb.ehe — BGB Buch 4, Abschnitt 1: Ehe und eheliches Güterrecht

Paket BG-12 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Geltungsbereich §§ 1297–1588
(214 Paragraphen als Fragmente §194, `sources/de-bgb-ehe/`, generiert aus dem
Register DOKNR, `legal_cutoff` 2026-09-17). Importe: `de.bgb.core` (Personen
und Gerichte), `de.bgb.fristen` (§§ 186–193 und die vollendeten Lebensjahre),
`calc.kinship` (§ 1307).

**Richtung der Abhängigkeit: `erbfolge → ehe`.** Dieses Paket veröffentlicht
den Güterstand, die Erhöhung des Erbteils (§ 1371 Abs. 1) und die Folgen der
fortgesetzten Gütergemeinschaft; es importiert `de.bgb.erbfolge` und
`de.bgb.verfuegungen` NICHT. Wo der Text des Abschnitts das Erbrecht liest —
„wird nicht Erbe“ (§ 1371 Abs. 2), „bei gesetzlicher Erbfolge als Erben
berufen“ (§ 1483 Abs. 1 Satz 2), der Anteil der gesetzlichen Erbfolge
(§ 1503 Abs. 1), der fiktive Pflichtteil (§ 1586b Abs. 1 Satz 3) —, ist das
Ergebnis ein ausdrücklicher EINGANG des Falls; ein Rückimport gäbe einen
Zyklus (Ledger D-12-07, D-12-13).

## Tiefe

| Maß §33.1 | Zahl |
|---|---|
| EXECUTABLE (aus der Einheit wird etwas abgeleitet) | 208 von 214 |
| Grenze mit Grund im Text (`(weggefallen)`) | 6 — §§ 1300, 1354, 1370, 1389, 1458, 1508 |
| UNEXPLAINED | 0 |

463 Normen, alle mit Anker; Wörterbuch 666 Marken, keine ohne Anker.
Einheit-für-Einheit-Nachweis: `analysis/saetze.json` (Status, Zeugenregeln,
Szenario).

## Aufbau

| Datei | Bereich |
|---|---|
| `package.law` | Typen, Kalender §85, Politik §86, Kern des Güterstands (§§ 1353, 1363, 1371 Abs. 1, 1408, 1414) |
| `titel-01-verloebnis.law` | §§ 1297–1302 Verlöbnis |
| `titel-02-eingehung.law` | §§ 1303–1312 Eingehung der Ehe |
| `titel-03-aufhebung.law` | §§ 1313–1320 Aufhebung |
| `titel-04-wirkungen.law` | §§ 1353–1362 Wirkungen der Ehe, Eigentumsvermutung |
| `titel-06-01-zugewinngemeinschaft.law` | §§ 1363–1390 Zugewinngemeinschaft und Zugewinnausgleich |
| `titel-06-02-vertragliches-gueterrecht.law` | §§ 1408–1414, 1519 Ehevertrag |
| `titel-06-03-guetergemeinschaft.law` | §§ 1415–1482 Gütergemeinschaft |
| `titel-06-04-fortgesetzte-guetergemeinschaft.law` | §§ 1483–1518 fortgesetzte Gütergemeinschaft |
| `titel-07-01-scheidung.law` | §§ 1564–1568b Scheidung, Ehewohnung, Haushaltsgegenstände |
| `titel-07-02-nachehelicher-unterhalt.law` | §§ 1569–1588 nachehelicher Unterhalt, Versorgungsausgleich, kirchliche Verpflichtungen |

## Die vier Mechaniken

### 1. Fristen §86 — EINE Politik, zwei Enden

Der Abschnitt kennt KEINE nach Tagen bestimmte Frist. Jede Frist ist nach
Wochen, Monaten oder Jahren bestimmt, daher trägt das Paket nur
`BGB_EHE_KALENDER` (Ledger D-12-02); eine Tagespolitik wäre auf keiner Norm
belegbar. Welches Ende eine Norm liest, sagt die Norm (Ledger D-12-03):

* `frist_ende` **mit** der Verlegung des § 193 — dort, wo am Ende eine
  Erklärung abzugeben oder ein Antrag zu stellen ist: §§ 1309 Abs. 1 Satz 3,
  1317, 1320, 1366 Abs. 3, 1568a Abs. 6, 1585b Abs. 3. Zeuge `s05`: der
  11.04.2026 ist ein Samstag, der Anspruch erlischt erst mit Ablauf des
  Montags, 13.04.2026.
* `frist_ende_kalender` **ohne** § 193 — dort, wo die Frist VERSTRICHENE ZEIT
  misst und es keinen Adressaten der Handlung gibt: §§ 1310 Abs. 3, 1315
  Abs. 2, 1358 Abs. 3 Nr. 4, 1361b Abs. 4, 1375 Abs. 3, 1385 Nr. 1, 1565
  Abs. 2, 1566, 1570 Abs. 1. Zeuge `s01`: der 01.03.2025 ist ein Samstag und
  bleibt das Fristende.

Der Kalenderknoten `KALENDER_BUNDESWEIT` trägt denselben Datensatz wie
`de.bgb.fristen` (Ledger D-04-03); der Fall nennt ihn als Achse.

### 2. Geld und Rundung

Vermögen, Zugewinn und Überschuss sind `Money` und werden nur addiert und
subtrahiert — exakte Arithmetik. Geteilt wird genau EINMAL je Forderung,
kaufmännisch auf den Cent (`div_round(…, n * 1.0, 2, "HALF_UP")`, Ledger
D-12-06, Muster D-04-04 und D-07):

* § 1378 Abs. 1 — die Hälfte des Überschusses (Zeuge `z01`: 140 000,01 / 2 =
  70 000,01);
* § 1476 Abs. 1 — der Überschuss des Gesamtguts zu gleichen Teilen (`gg02`);
* § 1478 Abs. 1 — der Fehlbetrag nach dem Verhältnis des Eingebrachten
  (`gg03`); das Verhältnis wird in Cent gerechnet, weil §58 kein Produkt
  zweier Geldbeträge kennt (Ledger D-12-10);
* § 1503 Abs. 1 und § 1505 — der Anteil und der halbe Anteilswert (`gg04`).

**Kein negativer Zugewinn** (§ 1373) und **keine Überschreitung der
Obergrenze** (§ 1378 Abs. 2) werden durch ZWEI Regeln mit sich
ausschließenden Garden ausgedrückt, nicht durch `max` oder `min`: die Garde
ist der Text, ein Extremum wäre eine Erfindung (Zeugen `z02`, `z03`, `z04`).

### 3. Drei Kanäle für die Wertung (DECISION-0194)

Der Abschnitt ist voller Wertungen, und keine wird als flacher Tatsachen-Kopf
geführt. 49 `external judgment relation` mit `authority Court` tragen sie —
darunter „gescheitert“ (§ 1565 Abs. 1 Satz 2), „unzumutbare Härte“
(§ 1565 Abs. 2), „grob unbillig“ (§§ 1381, 1579), „angemessene
Erwerbstätigkeit“ (§ 1574 Abs. 2), „Vermögen im Ganzen“ (§ 1365 Abs. 1).
Die Antwort des Gerichts darf VERNEINEND sein: `u02` belegt es mit
`assert not verlaengerung_der_betreuung_billig … { origin adjudicated; }`.
Bleibt sie aus, so steht im Dokument NEITHER mit dem evaluation status
REQUIRES_JUDGMENT (`s02`) — das ist nicht „nein“, sondern „das Gericht ist
gefragt“.

**§ 1365 „Vermögen im Ganzen“ hat KEINE Prozentschwelle** (Ledger D-12-08),
und **§ 1579 Nr. 1 „Ehe von kurzer Dauer“ KEINE Zahl von Jahren**
(Ledger D-12-12): der Text nennt keine, und das Paket erfindet keine.

### 4. Vermutungen §146 und ihr Gegenteil

Echte Vermutungen mit Gegenbeweis stehen als `presumption`: § 1301 Satz 2,
§ 1360b, § 1362 Abs. 1 und 2, § 1377 Abs. 1 und 3, § 1380 Abs. 1 Satz 2,
§ 1568b Abs. 2. **Unwiderlegbare** Vermutungen sind das Gegenteil davon und
stehen als strikte REGELN: § 1566 („wird unwiderlegbar vermutet“) und
§ 1361b Abs. 4 („wird unwiderleglich vermutet“) — Ledger D-12-11.

## Was das Paket nicht tut und warum

* **Die sechs `(weggefallen)`-Paragraphen** (§§ 1300, 1354, 1370, 1389, 1458,
  1508) tragen im geltenden Text keine Norm. Sie sind Positionen des
  Inventars und als Grenze mit dem Grund aus der Publikation selbst erklärt
  (`articles.json`, `declared`), nicht „nicht geschafft“.
* **Verweisungen in andere Pakete werden nicht nachgebaut**, sondern
  festgestellt und in der Marke benannt: das Bereicherungsrecht (§§ 1301,
  1434, 1457 → `de.bgb.bereicherung_delikt`), die §§ 1613–1615 und 1605,
  1609, 1610a (§§ 1360a Abs. 3, 1578a, 1580, 1582 →
  `de.bgb.verwandtschaft`), die §§ 406–408 (§ 1473 →
  `de.bgb.schuldrecht_at`), die §§ 1943–1959, 1990, 1991 und das
  Pflichtteilsrecht (§§ 1484, 1480, 1505, 1509, 1513, 1517 →
  `de.bgb.erbfolge`, `de.bgb.verfuegungen`).
* **Äußere Gesetze** bleiben außen: das Versorgungsausgleichsgesetz
  (§§ 1408 Abs. 2, 1587), das FamFG, Artikel 13 EGBGB (§§ 1305, 1309), das
  Verschollenheitsgesetz (§ 1494 Abs. 2), § 2049 (§ 1515 Abs. 2). Die
  Regeln stellen fest, DASS verwiesen wird.
* **Namen rechnet das Paket nicht** (§§ 1355–1355b, Muster D-13-07): welcher
  String am Ende im Register steht, ist keine Rechtsfolge, die eine Regel
  erzeugen könnte. Formalisiert sind die BEDINGUNGEN der Erklärungen.
* **Unabhängige Erwartung.** Das Rechenwerk der §§ 1373 und 1378 Abs. 1 ist
  gegen das Rechenbeispiel der amtlichen BMJ-Themenseite „Güterrecht“ belegt
  (`sources/bmj-gueterrecht/`, sha256 in `PINS.sha256`, Zeuge `z09`): dieselben
  Eingaben, dieselben 40 000 € Ausgleichsforderung. Die übrigen Beträge der
  Zeugen sind von Hand aus dem Text nachgerechnet und in den Kommentaren der
  Szenarien offengelegt.
* **Die Höhe des Unterhalts** (§ 1578 Abs. 1 „nach den ehelichen
  Lebensverhältnissen“) ist ein Eingang des Falls: der Text nennt weder Quote
  noch Tabelle, und die Düsseldorfer Tabelle ist kein Recht.
* **Der Korridor vor 2009** (Anfangsvermögen ohne § 1374 Abs. 3, Obergrenze
  ohne § 1378 Abs. 2 Satz 2) gehört zu `de.bgb.uebergang`; dieses Paket führt
  nur den geltenden Text und belegt ihn mit `t01`, `t02`.
* **Der Güterrechtsregister-Titel** (früher §§ 1558–1563) steht nicht mehr im
  geltenden Text und daher auch nicht im Register DOKNR; die Wirkung
  gegenüber Dritten trägt § 1412, und die Eintragung selbst ist ein äußerer
  Eingang (`eintragung_im_gueterrechtsregister`).

## Szenarien

Neun Familien, 47 Szenarien, beide Auswerter, Differential byteweise
(110 evaluate-Aufrufe):

| Familie | Szenarien | Paar an der Schwelle |
|---|---|---|
| `#gueterstand-pilot` | 3 | Pilot B1 |
| `#verloebnis-und-eingehung` | 8 | `v05`/`v06` — Vollendung des 16. Lebensjahrs |
| `#aufhebung` | 5 | `a03`/`a04` — letzter Tag der Jahresfrist des § 1317 |
| `#wirkungen-und-1362` | 5 | `w01`/`w02` — Getrenntleben (§ 1357 Abs. 3) |
| `#zugewinnausgleich` | 9 | `z03`/`z04` — Obergrenze § 1378 Abs. 2; `z06`/`z07` — zwei Wochen § 1366 Abs. 3 |
| `#guetergemeinschaft` | 4 | `gg03` — Quote des § 1478 Abs. 1 |
| `#scheidung-und-trennung` | 5 | `s01`/`s02` — letzter Tag des Trennungsjahres |
| `#nachehelicher-unterhalt` | 6 | `u01`/`u02` — drei Jahre § 1570; `u04`/`u05` — fiktiver Pflichtteil |
| `#uebergang-2009` | 2 | negatives Anfangsvermögen, erhöhte Obergrenze |

## Prüfung (nur punktuell)

```sh
./law engine check corpus/laws/de/bgb/ehe
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-12 --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-ehe.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.ehe#zugewinnausgleich"
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.ehe#zugewinnausgleich"
```
