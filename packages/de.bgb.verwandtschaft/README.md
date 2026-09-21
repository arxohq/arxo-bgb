# de.bgb.verwandtschaft — BGB Buch 4 Abschnitt 2 (§§ 1589–1772)

Paket BG-13 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Es senkt Buch 4 Abschnitt 2
Verwandtschaft ab: Titel 1 Allgemeine Vorschriften (§§ 1589, 1590), Titel 2
Abstammung (§§ 1591–1600d), Titel 3 Unterhaltspflicht (§§ 1601–1615n), Titel 4
Rechtsverhältnis zwischen Eltern und Kind (§§ 1616–1625), Titel 5 Elterliche
Sorge (§§ 1626–1698b), Titel 6 Beistandschaft (§§ 1712–1717), Titel 7 Annahme
als Kind (§§ 1741–1772). Quellen: `sources.law`, erzeugt aus dem Register
DOKNR, Stand `legal_cutoff` 2026-09-17; nach D-13-01 (Korrektur der Maße
`de_paragraph` in `act_split.py`, `check_source_pinning.py` und
`sync_de_bgb_packages.py` — sechs Absätze im ganzen BGB begannen mit einer
Querverweiszeile, die als Kopf gezählt wurde).

Tiefe § 33.1 (`check_formalization_depth.py`, Stand 18.09.2026):
**EXECUTABLE 153 von 161** Einheiten; ANCHORED 0; SOURCE_ONLY 8 — und diese
acht sind sämtlich als Grenze MIT GRUND erklärt (§§ 1633, 1647, 1665, 1672,
1676, 1679, 1683, 1697, alle `(weggefallen)`). Die neun Bereichspositionen des
Registers (§§ 1615b–1615k, 1621–1623, 1634–1637, 1650–1663, 1668–1670,
1689–1692, 1694–1695, 1699–1711, 1718–1740) sind `range_repealed` und tragen
keinen Fragmenttext. 472 Regeln
(`check_label_coverage.py`: Wörterbuch 714/0, Normen 472/0, ohne Anker 0).
**72 Szenarien in elf Familien**, beide Auswerter, **156 `evaluate`-Aufrufe
byteweise identisch** (`check_kz_differential.py`). `analysis/saetze.json`
trägt keine Einheit mehr als `TODO`.

## Brücke zu `calc.kinship` (Ledger D-13-02)

§ 1589 Abs. 1 Satz 3 (Grad nach der Zahl der Geburten) und §§ 1754–1756, 1770
(Wirkung der Annahme) sind über den gemeinsamen Rechner `calc.kinship`
ausgeführt, nach demselben Muster wie `de.bgb.erbfolge` (Schicht A). Die
Adoptionspolitik ist Sache der FAMILIE, nicht der einzelnen Annahme:
`ReplacesBlood` ist der Grundfall (jede Familie ohne Volljährigenannahme —
Ledger D-13-02 misst, dass eine Familie ohne gesetzte Politik überhaupt
`kin_line`/`kin_degree` verweigert), `AddsBranch` gilt nur, wenn in der
Familie ein Volljähriger angenommen ist (§ 1770). Beide Regeln und die
Kanten-Brücken sind `pub`; `de.bgb.erbfolge` erklärt beide Politiken heute
noch bei sich mit dem Kommentar „Paket de.bgb.verwandtschaft“ — der
Koordinator stellt bei der Zusammenführung auf diese Brücke um (reine
Umbenennung).

## Rundung (Ledger D-13-05)

§ 1612a Abs. 2 Satz 2 nennt das Verfahren selbst: der Mindestunterhaltsanteil
wird EINMAL `div_round(Mindestunterhalt × Prozentsatz, 100.0, 0, "CEILING")`
gerechnet (Aufrundung auf volle Euro). § 1612b Abs. 1 Nr. 1 nennt das
Verfahren NICHT: die Hälfte des Kindergeldes wird einmal kaufmännisch auf den
Cent gerundet (`div_round(Kindergeld, 2.0, 2, "HALF_UP")`), danach vom
Barbedarf abgezogen. Der Mindestunterhalt selbst ist EINGANG mit
Geltungszeitraum (§ 1612a Abs. 4 delegiert an eine Rechtsverordnung); die
Düsseldorfer Tabelle ist kein Recht und kommt im Paket nicht vor.

## Sroki (Fristen, `DEADLINES.json` Abschnitt BG-13)

Seit dem 18.09.2026 trägt der Abschnitt **21 Zeilen, alle `EXECUTED`**. Neu
hinzugekommen sind: § 1617 Abs. 4 (ein Monat nach der Geburt, MIT § 193, weil
innerhalb der Frist eine Erklärung gegenüber dem Standesamt abzugeben ist),
§ 1629a Abs. 4 (drei Monate), § 1631d Abs. 2 (sechs Monate), § 1643 Abs. 4 (ein
Jahr nach der Volljährigkeit), § 1748 Abs. 2 Satz 1 und 3 (drei und fünf
Monate), § 1750 Abs. 4 Satz 2 (drei Jahre) und § 1762 Abs. 2 (ein Jahr
innerhalb von drei Jahren).


Zwölf Zeilen über `de.bgb.fristen`: § 1593 (300 Tage), § 1598 Abs. 2 (fünf
Jahre, Heilung ohne § 193), § 1600b (zwei Jahre, mit § 193), § 1600d Abs. 3
(Empfängniszeit), § 1612a (sechstes/zwölftes Lebensjahr), § 1613 (Erster des
Monats, Jahresfrist des Sonderbedarfs), § 1615l (sechs/acht Wochen, drei
Jahre, vier Monate), § 1743 (25/21 Jahre), § 1746 (14 Jahre), § 1747 (acht
Wochen); zwei Zeilen (§ 1748 Abs. 2 Jugendamts-Verfahren, § 1750 Abs. 4
Kraftverlust der Einwilligung) sind `TODO` — Verfahrensfristen außerhalb der
Zuständigkeit des Familiengerichts nach diesem Paket.

**Negativer Tagesschritt wird von beiden Auswertern abgelehnt (Ledger
D-13-03).** `add_calendar_period(d, -N calendar_day)` liefert bei keinem der
beiden Auswerter ein Ergebnis (lawc: `NEITHER`, lawref: `MISSING_POLICY`) —
gemessen, kein Auswerterunterschied. Fristen „vor dem Ereignis“ (§ 1600d
Abs. 3, § 1615l Abs. 1, Abs. 2 Satz 3) sind deshalb VOM FRÜHEREN TAG AUS
VORWÄRTS gerechnet: die Empfängniszeit fragt, ob die Geburt zwischen dem
181. und dem 300. Tag NACH der Beiwohnung liegt; § 1615l fragt, ob der
geprüfte Tag höchstens sechs Wochen vor der Geburt liegt, indem er selbst
plus sechs Wochen mit der Geburt verglichen wird. Beide Formen sind
äquivalente Lesarten desselben Textes, keine Annäherung.

## Urteilskanal (DECISION-0194)

- **Wertung** (`external judgment relation`): Bedürftigkeit (§ 1602 Abs. 1),
  Leistungsfähigkeit (§ 1603 Abs. 1), angemessener Unterhalt (§ 1610),
  Billigkeit (§ 1611 Abs. 1, § 1615l Abs. 2 Satz 4), sozial-familiäre
  Beziehung (§ 1600 Abs. 3, 5), schwerwiegende Zweifel (§ 1600d Abs. 2 Satz 2),
  Kindeswohl (§ 1626 Abs. 3, § 1626a Abs. 2, § 1666, § 1687, § 1696, § 1741,
  § 1745, § 1748, § 1769), sittliche Rechtfertigung (§ 1767 Abs. 1), wichtiger
  Grund (§ 1771).
- **Festgestellte Tatsache** (`origin adjudicated`): gerichtliche Feststellung
  der Vaterschaft (§ 1592 Nr. 3), rechtskräftige Nichtvaterschaft (§ 1599
  Abs. 1), Annahme ausgesprochen (§ 1752, § 1768), Genehmigung/Ersetzung
  einer Einwilligung (§ 1596 Abs. 2, § 1748), gerichtliche Sorgeentscheidung
  (§ 1626a Abs. 1 Nr. 3, § 1671, § 1696).
- **Vermutungen** (`presume … unless`): § 1595a/§ 1594 Abs. 2 (Vaterschaft
  eines anderen — positiver Verdrängungskopf, Muster D-03-05), § 1600c
  (Abstammung im Anfechtungsverfahren), § 1666 Abs. 2 (Vermögensgefährdung —
  Ledger D-13-06: OHNE Antwort fragt das Dokument, `REQUIRES_JUDGMENT`, nicht
  Schweigen; MIT verneinter Antwort hält die Vermutung, Zeugen `s05`/`s05b`).

## Aufgabenkarte

| Norm | Form im Paket | Zeuge |
|---|---|---|
| § 1589 | Grad und Linie aus `calc.kinship::kin_degree`/`kin_line` | — |
| § 1590 | Schwägerschaft vermittelt über Ehegatte, bestehend und aufgelöst | — |
| § 1591, § 1592, § 1593 | Mutterschaft; drei Zuordnungsgründe je eigener Kopf; 300-Tage-Frist | `a01`, `a02`, `a03`, `a04` |
| §§ 1594–1598 | geschlossener Katalog der Unwirksamkeitsgründe (D-03-05-Muster), Heilung nach fünf Jahren | `a05` |
| § 1595a | Verdrängungskopf gegen § 1594 Abs. 2 | — |
| § 1596 | persönliche Erklärung / Vertreter mit Genehmigung | — |
| § 1599 | Nichtvaterschaft als Tatsache, rückwirkender Wegfall | — |
| § 1600 | vier Anfechtungsberechtigte, Ausschlüsse Abs. 2/3/6 | — |
| § 1600a | Anfechtung nicht durch Bevollmächtigten | — |
| § 1600b | zwei Jahre ab Kenntnis, § 193 gilt | `a06` |
| § 1600c | Vermutung im Anfechtungsverfahren | `a09` |
| § 1600d | Empfängniszeit vorwärts gerechnet, Vermutung Abs. 2 | `a07`, `a08` |
| §§ 1601–1603 | Anspruch in gerader Linie, Bedürftigkeit, Leistungsfähigkeit, gesteigerte Pflicht | `u01` |
| § 1605 | Auskunftspflicht in gerader Linie | `u12` |
| § 1606 | Rang aus dem Grad, anteilige Haftung (Summe = Eingang, D-13-04) | — |
| § 1607, § 1608 | Ersatzhaftung, Rang des Ehegatten | `u13` |
| § 1609 | geschlossene Rangfolge, sieben Ränge | — |
| § 1610 | Maß des Unterhalts — Wertung | — |
| § 1611 | Beschränkung/Wegfall, Ausnahme für minderjährige Kinder | — |
| § 1612, § 1612a | Geldrente; drei Altersstufen 87/100/117 %, Aufrundung | `u02`–`u04` |
| § 1612b, § 1612c | Kindergeld zur Hälfte/voll | `u05`, `u06` |
| § 1613 | Erster des Monats, Jahresfrist des Sonderbedarfs | `u07`, `u08` |
| § 1614, § 1615 | Verzicht unwirksam, Erlöschen bei Tod | — |
| §§ 1615l–1615n | Unterhalt aus Anlass der Geburt, Fortbestand trotz Tod/Totgeburt | `u09`–`u11` |
| § 1615m | Beerdigungskosten der Mutter | — |
| § 1619, § 1624 | Dienstleistungen, Ausstattung über dem Maß | — |
| § 1626, § 1626a | Zuordnung der Sorge, geschlossener Katalog § 1626e | `s01`–`s03` |
| § 1629 | Vertretung gemeinschaftlich/allein/bei Gefahr im Verzug | — |
| § 1631, § 1632 | Inhalt der Personensorge, Herausgabe | — |
| § 1666, § 1666a | Gefährdung, Maßnahmenkatalog, Vermutung Abs. 2 | `s04`, `s05`, `s05b` |
| § 1684, § 1687 | Umgangsrecht, Alleinentscheidung | `s06` |
| § 1696 | Abänderung/Aufhebung kindesschutzrechtlicher Maßnahmen | — |
| §§ 1712–1717 | Beistandschaft: Eintritt mit dem Zugang, Antragsberechtigte, Inlandsaufenthalt | `bs01`, `bs02` |
| § 1604 | Gütergemeinschaft: Güterstand qualifiziert aus `de.bgb.ehe` (D-13-09) | `ur01` |
| § 1610, § 1610a | Maß des Unterhalts (Wertung) und Katalog Abs. 2; Deckungsvermutung | `ur02`–`ur04` |
| § 1615a | Kollisionsnorm des Untertitels 2 | `ur05` |
| §§ 1616–1617i | Namensrecht als Bedingungen der Erklärungen (D-13-07): Bestimmungsrecht, Einwilligungen, Beglaubigung, Monatsfrist | `ek01`–`ek06` |
| § 1618, § 1620, § 1625 | Beistand und Rücksicht; zwei Vermutungen „im Zweifel“ | `ek07`, `ek08` |
| §§ 1626b–1626d | Wirksamkeit, persönliche Abgabe, Beurkundung und Mitteilung | — |
| § 1627, § 1628 | Ausübung und Entscheidungsbefugnis des Familiengerichts | — |
| § 1629a | Haftungsbeschränkung, Vermutung Abs. 4 (drei Monate) | `sr01` |
| § 1630, §§ 1631a–1631e | Pflegerbestellung; Ausbildung, Unterbringung, Sterilisation, Beschneidung, Varianten der Geschlechtsentwicklung | `sr02`, `sr03` |
| §§ 1638–1649 | Vermögenssorge: Ausschluss, Verzeichnis (15 000 €), Schenkungsverbot, Anlegung, Genehmigungen, Einkünfte | `vs01`–`vs06` |
| § 1664, § 1666a, § 1667 | Eigenübliche Sorgfalt; Verhältnismäßigkeit; Maßnahmen bei Vermögensgefährdung | `sr06` |
| §§ 1673–1682 | Ruhen, Wiederaufleben, Tod und Todeserklärung, Verbleibensanordnung | `sr04` |
| §§ 1685–1688 | Umgang der Bezugspersonen, Auskunft, leiblicher Vater, Befugnisse | `sr05` |
| §§ 1693, 1697a, 1698–1698b | Maßregeln, Kindeswohlprinzip, Herausgabe und Fortführung | — |
| §§ 1742–1753 | Sperre, Probezeit, Verbote, Ersetzung der Einwilligung, Form und Kraftverlust, Beschluss | `ar03`, `ar04`, `ar01`, `ar02` |
| §§ 1757–1766a | Name, Offenbarungsverbot, Aufhebung samt Fristen und Wirkungen | `ar05` |
| §§ 1768–1772 | Volljährigenannahme: Antrag, Verbot, Aufhebung, Wirkungen der Minderjährigenannahme | `ar06` |
| §§ 1741–1750 | Zulässigkeit, Mindestalter, Einwilligungen des Kindes und der Eltern | `n01`–`n06` |
| §§ 1754–1756 | Wirkung, Erlöschen/Bestehenbleiben der Verwandtschaft | `n07` |
| §§ 1767–1771 | Annahme Volljähriger: Zulässigkeit, keine Schwägerschaft, Fortbestand | `n08`, `n09` |

## Was das Paket nicht tut und warum

- **Der NAME selbst** wird nicht gerechnet (Ledger D-13-07). Aus welchen
  Zeichen ein Doppelname besteht, ob ein Bindestrich steht, welcher Name
  alphabetisch voransteht und wie eine „geschlechtsangepasste Form“ lautet, ist
  Zeichenarbeit und keine Rechtsfolge aus Merkmalen; der gewählte Name ist
  Eingang und Ausgang des Standesamts. AUSGEFÜHRT sind die Bedingungen, die
  §§ 1616–1617i an die Erklärungen knüpfen: wer bestimmen darf, wessen
  Einwilligung nötig ist, wann öffentlich zu beglaubigen ist, welche Frist läuft
  und was bei ihrem Ablauf eintritt.
- **Die Verweisung des § 1643 Abs. 1 auf die §§ 1850–1854** wird nicht
  nachgebaut (Ledger D-13-08): das genehmigungsbedürftige Grundgeschäft ist ein
  Eingang des Falls, ausgeführt sind die ABWEICHUNGEN der Absätze 2 bis 5. So
  hängt BG-13 nicht an dem parallel bearbeiteten Paket `de.bgb.betreuung`; die
  Umstellung bei der Zusammenführung ist eine reine Umbenennung des Eingangs.
- **Die Kommission des § 1631e Abs. 4, 5** (Zusammensetzung, Inhalt der
  Stellungnahme, Aufbewahrung der Behandlungsakte bis zum 48. Lebensjahr) ist
  Organisations- und Berufsrecht; ausgeführt ist die RECHTSFOLGE, die der Text
  daran knüpft — die Vermutung des Absatzes 3 Satz 3.
- **Verfahrensrecht des FamFG** (Anhörung, Beschwerde, Wirksamwerden der
  Beschlüsse) gehört nicht ins BGB-Paket; die Beschlüsse des Familiengerichts
  sind Tatsachen des Falls mit `origin adjudicated`.
- **§ 1762 Abs. 2 Satz 3** verweist für die Antragsfrist der Aufhebung auf die
  §§ 206, 210 (Hemmung und Ablaufhemmung der Verjährung). Die Frist selbst ist
  gerechnet, die Hemmung nicht — `TODO` in `TASKS.json` (`V6-13-15`).
- **Unabhängige Ausdrücke** (Mindestunterhaltsverordnung, BMJ-Broschüre „Das
  Kindschaftsrecht“, BGH zu § 1612b) sind NICHT als Schnappschuss in
  `sources/` gepinnt — `TODO`, siehe HANDOFF-Abschnitt des Statusberichts;
  der Mindestunterhalt selbst ist als typisierter Eingang mit
  Geltungszeitraum modelliert (`mindestunterhalt`), keine erfundene Zahl.
- **Doktrin des BGH** (soziale Elternschaft, Kindeswohlmaßstäbe außerhalb des
  Textes) ist keine Norm; das Paket führt nur, was der Wortlaut selbst als
  Maßstab, Frist oder Prozentsatz nennt.
- **§ 193 bei Erwerbsfristen.** § 1743, § 1746, § 1747 sind Schwellen des
  ERWERBS (Annahmevoraussetzung), keine Klagefristen — sie lesen
  `lebensjahr_vollendet_am`/direkte Addition, nicht `frist_ende` mit
  Verlegung (Muster D-10-05).

## Querschnitt Ehe → Zugewinn → Scheidung → Unterhalt (D-13-12)

Familie `de.bgb.verwandtschaft#querschnitt-familie-und-geld`
(MULTISESSION-PROMPT.ru.md §10 Nr. 7), 3 Szenarien; unabhängige Ausdrücke,
VOR der Ausführung von Hand gerechnet:

- **fam01** (Hauptfall): A (Anfangsvermögen 20.000,00 € → Endvermögen
  30.000,00 €, Zugewinn 10.000,00 €) und B (60.000,00 € → 40.000,00 €,
  Zugewinn 0 nach § 1373) sind seit 30.09.2025 rechtskräftig geschieden
  (§§ 1564–1566). Überschuss 10.000,00 €, Hälfte **5.000,00 €**
  Ausgleichsforderung des B gegen A (§ 1378 Abs. 1). B betreut das
  gemeinsame Kind K (geb. 15.07.2024) und erhält von A binnen der drei Jahre
  ohne Billigkeitsprüfung nachehelichen Unterhalt wegen Kindesbetreuung
  (§ 1570 Abs. 1 Satz 1). K lebt nicht bei A und ist im April 2024 in der
  ersten Altersstufe: Mindestunterhalt 87 % von 537,00 € = 467,19 €,
  aufgerundet **468,00 €** (§ 1612a). Drei unabhängige Ansprüche, NICHT
  addiert.
- **fam02** (Unvollständigkeit): dasselbe Zahlenbild, aber ohne
  rechtskräftiges Scheidungsurteil — Zugewinn, nachehelicher und
  Kindesunterhalt lassen sich je für sich weiter berechnen, die
  Querschnittsfeststellung selbst (die die Scheidung voraussetzt) bleibt aus.
- **fam03** (Kanarienvogel, minus Mindestunterhalt-Angabe): Scheidung,
  Zugewinn und nachehelicher Unterhalt stehen fest, der Kindesunterhalt und
  damit die Querschnittsfeststellung nicht.

Die kombinierende Regel `FamilienrechtlicheLageNachScheidungBerechnen` liest
DREI bereits institutionelle Ergebnisse zusammen (`de.bgb.ehe::
ehe_geschieden_am`, `de.bgb.ehe::ausgleichsforderung`, `de.bgb.ehe::
nachehelicher_unterhaltsanspruch`) plus die eigene `mindestunterhaltsanspruch`
(§ 1612a) — Vorbild: `de.bgb.verfuegungen` auf `de.bgb.erbfolge::
gesetzlicher_erbteil_bruch` (D-13-02). Neun zuvor paketprivate Relationen von
`de.bgb.ehe` wurden `pub` gesetzt (§24 verlangt es für den `when`-Zugriff
von außen): `scheidungsurteil_rechtskraeftig_am`,
`gueterstand_auf_andere_weise_als_durch_tod_beendet`,
`keine_hinzurechnung_zum_anfangsvermoegen`, `keine_illoyale_minderung`,
`betreuungsfrist_1570`, `pflege_oder_erziehung_des_kindes`, `bewertungstag`,
`geburt_des_kindes_am`, `gemeinschaftliches_kind` — reine Fallangaben, keine
Regeländerung.

**Kalenderfalle (D-09-08 analog).** `de.bgb.ehe` deklariert selbst
`calendar KALENDER_BUNDESWEIT`; sobald zwei Nachbarn (`de.bgb.fristen` und
`de.bgb.ehe`) denselben Kalendernamen deklarieren, wird ein
unqualifiziertes `calendar KALENDER_BUNDESWEIT;` zweideutig, sobald ein
Szenario tatsächlich Kalenderarithmetik beider Pakete auslöst — auch wenn
es selbst keine `add_calendar_period` aufruft. Dieses Paket deklariert
seitdem ebenfalls seine eigene, byteidentische Kopie, und ALLE 75 Szenarien
des Pakets tragen jetzt die explizite Achse `calendar KALENDER_BUNDESWEIT;`
im `context` (vorher genügte die stillschweigende Auflösung mit einem
einzigen Kandidaten).
