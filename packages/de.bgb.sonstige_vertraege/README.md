# BG-08 `de.bgb.sonstige_vertraege`

Buch 2 Abschnitt 8 des geltenden BGB, soweit er nicht anderen Paketen der
Aufgabe `docs/foundations/de-bgb/` zugewiesen ist: **§§ 481–534, §§ 598–610,
§§ 652–811** — 300 Einheiten des Registers, davon 295 in Kraft und fünf
weggefallen (§§ 509, 610, 764, 786, 795). Rechtsstand `legal_cutoff`
2026-09-17 (gesetze-im-internet.de, zuletzt geändert durch Art. 6 G v.
23.7.2026 I Nr. 226).

Sprache dieses Pakets: Deutsch und Englisch (DECISION-0319 Р7). Der gepinnte
Text steht in `sources.law` und `sources/de-bgb-sonstige-vertraege/`; er wird
vom Generator geschrieben, nicht von Hand.

## Karte der Dateien

| Datei | Bereich |
|---|---|
| `package.law` | Politiken der Fristen §86, Kalender §85, **Titel 16 Gesellschaft** §§ 705–740c inklusive **Liquidation** §§ 730–736d |
| `titel-03-darlehen.law` | **Titel 3** Darlehen, Verbraucherdarlehen, Finanzierungshilfen, Ratenlieferung §§ 488–515 |
| `titel-04-schenkung.law` | **Titel 4** Schenkung §§ 516–534 |
| `titel-12-auftrag-zahlungsdienste.law` | **Titel 12** Auftrag, Geschäftsbesorgung, Zahlungsdienste §§ 662–676c |
| `titel-17-gemeinschaft.law` | **Titel 17** Gemeinschaft nach Bruchteilen §§ 741–758 |
| `titel-20-buergschaft.law` | **Titel 20** Bürgschaft §§ 765–778 |
| `titel-uebrige.law` | Titel 2, 6, 7, 10, 11, 13, 14, 15, 19, 21, **23 Anweisung** §§ 783–792, **24 Schuldverschreibung auf den Inhaber** §§ 793–801, 803–808, **25 Vorlegung von Sachen** §§ 809–811 |

Der Stand je Paragraph steht in `analysis/saetze.json`: 209 Einheiten tragen
Regeln (`RULE`), 91 sind `SOURCE_ONLY` — gepinnter Text ohne Regelmaschinerie.

## Was das Paket rechnet

### Deontische Pakete P3

§§ 488 (Darlehen), 662 (Auftrag) und 604 (Leihe) haben die Positionen
`Duty488Verfuegung`, `Duty488Rueckzahlung`, `Duty662Geschaeftsbesorgung` und
`Duty604Rueckgabe`; dafür gibt es 8 Szenarien `evaluate positions()`.

**Die drei Stufen des § 709 Absatz 3.** Stimmkraft und Anteil an Gewinn und
Verlust richten sich vorrangig nach den vereinbarten Beteiligungsverhältnissen,
hilfsweise nach dem Verhältnis der vereinbarten Werte der Beiträge, hilfsweise
nach Köpfen. Jede Stufe ist eine eigene Regel; die nachrangige verlangt
`not_known` der vorrangigen Anknüpfung. Der Anteil ist ein Paar ganzer Zahlen
(`anteil_bruch`) und wird erst am Ende zu einem exakten `Rational` (`anteil`).

**Die Mehrheit nach Anteilen (§ 745 Absatz 1 Satz 2).** Sie wird ohne
Bruchrechnung entschieden: die Zähler der Anteile stehen auf einem gemeinsamen
Nenner, ihre Summe wird verdoppelt und mit dem gemeinsamen Nenner verglichen.
Genau die Hälfte ist keine Mehrheit (Szenario `m04`).

**Die Haftungsgrenze des Gastwirts (§ 702 Absatz 1).** Das Hundertfache des
Beherbergungspreises für einen Tag ist ein eigener Schluss; die drei Stufen
(mindestens 600 Euro, höchstens 3 500 Euro, für Wertsachen höchstens 800 Euro)
sind drei Regeln mit Variablenvergleich.

**Die Schwellen des Verbraucherdarlehens.** 200 Euro (§ 491 Absatz 2 Satz 2
Nummer 1), 75 000 Euro (§ 494 Absatz 6 Satz 2, § 513), 10 / 5 / 2,5 Prozent des
Nennbetrags (§ 498), 1 und 0,5 Prozent des vorzeitig zurückgezahlten Betrags
(§ 502 Absatz 3 Nummer 1). Jede Schwelle ist in beiden Richtungen belegt.

### Rundung

Wo ein Bruch in Geld umgerechnet wird — § 728a und § 737 (Fehlbetrag nach
Anteil), § 743 Absatz 1 (Früchteanteil), § 748 (Lasten und Kosten), § 498
(Rückstandsschwelle), § 502 Absatz 3 (Obergrenze) — geschieht das **einmal**,
mit `div_round(Wert × Zähler, Nenner × 1.0, 2, "HALF_UP")`: kaufmännische
Rundung auf zwei Nachkommastellen. Zwischenergebnisse werden nicht gerundet.

### Fristen

Die Mechanik gehört `de.bgb.fristen`. Dieses Paket erklärt zwei Politiken:
`BGB_SONSTIGE_TAG` (Tagesfristen mit Verlegung nach § 193) und
`BGB_SONSTIGE_KALENDER` (Wochen-, Monats- und Jahresfristen). Ausgeführt sind
§ 489 Absatz 1 Nummer 2 und Absatz 3, § 498 Absatz 1 Satz 1 Nummer 2, § 516
Absatz 2, § 529 Absatz 1, § 532 Satz 1, § 606, § 675u Satz 3, § 676b Absatz 2,
§ 725 Absatz 1, § 728b Absatz 1, § 739 Absatz 1 und § 801 Absatz 1 und 2.
Alle Zeilen stehen in `docs/foundations/de-bgb/DEADLINES.json` unter `BG-08`.

Eine Frist, an deren Ende eine **Erklärung gegenüber einem Adressaten** steht
(§ 532 Widerruf, § 676b Unterrichtung), liest `frist_ende` — also mit der
Verlegung nach § 193. Eine Frist, die nur **abgelaufene Zeit misst** (§ 529
Absatz 1: „seit der Leistung … zehn Jahre verstrichen"), liest
`frist_ende_kalender` ohne Verlegung.

### Bewertende Merkmale

Nach DECISION-0194 als `external judgment relation … { authority Court; }`:
grober Undank (§ 530), angemessener Unterhalt (§§ 519, 528), erforderliche
Aufwendungen (§§ 670, 693, 716), wichtiger Grund (§§ 715, 725, 727, 749),
unverhältnismäßig hoher Maklerlohn (§ 655), Interesse und Wille des
Geschäftsherrn (§ 683), wesentliche Verschlechterung (§ 490), berechtigtes
Interesse an vorzeitiger Erfüllung (§ 500), Aussichtslosigkeit der
Zwangsvollstreckung (§ 773 Absatz 1 Nummer 4), Kündigung zur Unzeit (§ 671).

**„Unverzüglich" ist ein bewertendes Merkmal, keine Nullfrist** (§§ 663, 673,
675u Satz 2, 676b Absatz 1, 703, 777). Wo der Text daneben eine kalendarische
Höchstgrenze nennt (§ 675u Satz 3, § 676b Absatz 2), ist diese Grenze eine
Frist des § 86 mit eigener Zeile.

### Die Anweisung und die Schuldverschreibung auf den Inhaber (Titel 23–25)

**Eine Sache, drei Rollen (§§ 783–792).** Die Sache `Anweisung` trägt
Anweisender, Angewiesener und Anweisungsempfänger über Faktprädikate, nicht
über getrennte Typen. Zentraler Fakt ist die Aushändigung an den
Anweisungsempfänger (§ 783); von ihr hängen beide Ermächtigungen, der Widerruf
(§ 790, nur vor Annahme oder Leistung) und die Übertragung (§ 792) ab
(D-08-09).

**„Gilt entsprechend" bei Inhaberkarten (§ 807, D-08-10).** Eine Karte oder
Marke ohne Gläubigerbezeichnung, unter verpflichtungswilligen Umständen
ausgegeben, erfüllt denselben Prädikat `schuldverschreibung_ausgestellt`, den
§§ 793, 794, 796, 797 lesen — kein zweiter Regelsatz.

**§ 802 bleibt offen.** Die Hemmung der Vorlegungsfrist durch die
Zahlungssperre braucht eine Brücke zwischen dem Hemmungsmechanismus von
`de.bgb.fristen` (an den Typ `Anspruch` gebunden) und dem Typ `Frist` dieses
Pakets; offen als `D-Q08-2` / `BG-08-TODO-2`.

### Der Korridor MoPeG

Titel 16 gilt in dieser Nummerierung erst seit dem 1.1.2024 (Art. 137 MoPeG,
Art. 229 § 61 EGBGB). Alle Regeln des Titel 16 tragen
`effective [@2024-01-01, infinity)`. Für einen Fall mit früherem `legal_time`
schweigt das Paket, statt die alte Fassung zu behaupten — Szenarien `g04`
(31.12.2023, `NEITHER`) und `g05` (1.1.2024, `TRUE_ONLY`).

## Was das Paket nicht tut und warum

- **Es behauptet nicht die Fassung vor dem 1.1.2024.** Der Gegenstand der
  Aufgabe ist der Schnitt des geltenden Rechts; die Übergangsmatrix gehört
  `de.bgb.uebergang` (Koordinator).
- **Es führt kein Gesellschaftsregister.** §§ 707–707d, 733, 736c, 738 setzen
  Registervorgänge voraus; die Eintragung ist ein Eingang des Falls
  (`im_gesellschaftsregister_eingetragen`), kein Schluss dieses Pakets. Das
  Registerrecht selbst steht im HGB und der GesRV, nicht im BGB.
- **Es rechnet keinen effektiven Jahreszins.** § 491a und § 492 verweisen auf
  Artikel 247 EGBGB, § 502 auf die Berechnung des Schadens; die Formeln stehen
  in der Preisangabenverordnung, nicht im BGB. Der Sollzinssatz, der
  Basiszinssatz und der marktübliche Zinssatz sind Eingänge des Falls.
- **Es prüft keine Zahlungsdiensteaufsicht.** § 675v Absatz 4 verweist auf § 1
  Absatz 24 ZAG, § 675d auf Artikel 248 EGBGB; die starke Kundenauthentifizierung
  ist ein Eingang, keine Regel. Die EWR-/SEPA-Ausnahmen der §§ 675s, 675t,
  675x, 675y, 675z, die auf § 675d Absatz 6 verweisen, bleiben aus demselben
  Grund Text ohne Regel (D-08-13); ausgeführt ist der jeweilige Hauptsatz.
- **Es entscheidet keine Wertung selbst.** Die oben genannten Merkmale bleiben
  ohne Antwort `REQUIRES_JUDGMENT`; ein flacher Fall-Fakt, der die Wertung
  nachspricht, ist verboten.
- **§ 802 rechnet keine Hemmung.** Siehe oben, `D-Q08-2`.
- **91 Einheiten sind `SOURCE_ONLY`.** Sie tragen den gepinnten Text und die
  §33.1-Einheit, aber keine Regelmaschinerie — überwiegend die
  Informationspflichten der §§ 481a, 481b, 482 Absatz 1, 2, 482a, 483
  Absatz 1, 2, 491a, 492, 505b, 505c, 505e (Artikel 242/247 EGBGB, D-08-14,
  D-08-15) und die Begriffsbestimmungen/übrigen Ausführungsregeln der
  Zahlungsdienste §§ 675a–675r, dazu die reine Registerverfahrens-Prozedur
  ohne eigenes materielles Ergebnis §§ 707, 707b, 707c Absatz 1–4, 707d und
  der Kommanditisten-Status nach dem HGB § 724 (D-08-17), sowie verstreute
  Einzelnormen in Darlehen, Schenkung, Leihe, Mäklervertrag, Geschäftsführung
  ohne Auftrag und Verwahrung. Titel 17 Gemeinschaft (§§ 741–758) ist
  vollständig ausgeführt (D-08-16). Der genaue Stand je Paragraph steht in
  `analysis/saetze.json`, der nächste Schritt in
  `docs/foundations/de-bgb/TASKS.json` (`BG-08-TODO-1`, `BG-08-TODO-2`).

### Gesellschaft, Fortsetzung (§§ 707a Absatz 2, 708, 711a–722, 726, 729, 740a–740c, D-08-17)

Grenze: nur eine Norm, deren Text selbst auf einen externen Akt verweist,
OHNE eigenes materielles Ergebnis, bleibt `SOURCE_ONLY` — das Gesellschafts­
register selbst ist ein Eingang (`im_gesellschaftsregister_eingetragen`),
die Rechtsfolgen schreibt das BGB. Ausgeführt: Namenszusatz eGbR
(§ 707a Absatz 2), Gestaltungsfreiheit (§ 708), Unübertragbarkeit der
Gesellschafterrechte mit zwei Ausnahmen (§ 711a), Anwachsung/Minderung der
Anteile (§ 712, § 712a), Gesellschaftsvermögen (§ 713), Notgeschäftsführung
(§ 715a), Gesellschafterklage (§ 715b), Informationsrechte (§ 717),
Rechnungsabschluss zum Kalenderjahresende (§ 718), Entstehung und
Vertretung gegenüber Dritten (§ 719, § 720), Einwendungen des Gesellschafters
(§ 721b), Zwangsvollstreckung (§ 722), Kündigung durch den Privatgläubiger
mit derselben Ultimo-Mechanik wie § 725 (§ 726), Auflösungsgründe (§ 729)
und die Verweisungsnormen für die nicht rechtsfähige Gesellschaft
(§§ 740a–740c, Muster D-08-07). §§ 707, 707b, 707c Absatz 1–4, 707d bleiben
`SOURCE_ONLY`: reines Registerverfahren (Gerichtszuständigkeit, Inhalt der
Anmeldung, Statuswechsel-Verfahren, Verordnungsermächtigung) ohne eigenes
materielles Ergebnis außerhalb des Registriervorgangs. § 724 bleibt
`SOURCE_ONLY`: die Norm regelt den Kommanditisten-Status nach § 107 Absatz 1
HGB — eine Rechtsfolge des HGB, nicht des BGB.

### Teilzeit-Wohnrechte (§§ 482 Absatz 3, 483 Absatz 3, 484 Absatz 1, 486a, D-08-15)

Ausgeführt ohne die externe Verweisungskette (Artikel 242 EGBGB) der
vorvertraglichen Informationspflichten: das Verbot, ein Teilzeit-Wohnrecht
als Geldanlage zu bewerben (§ 482 Absatz 3), die Nichtigkeit bei
Sprachverstoß (§ 483 Absatz 3), die Schriftform (§ 484 Absatz 1) und beide
Zweiwochenfristen des § 486a — die Zahlungsaufforderung vor Fälligkeit
(Vorwärtsvergleich wie § 493) und die Kündigungsfrist ab Zugang
(`frist_dauer_kalender` mit `2 calendar_week`).

### Verbraucherdarlehen-Information (§§ 492a, 492b, 493, 504a, 505, D-08-14)

Kopplungsgeschäfte (§§ 492a, 492b): Verbotsnorm mit zwei unabhängigen
Tatbeständen (Immobiliar, Allgemein) und zwei unabhängigen Zulässigkeitsgründen
(Konto zur Kapitalansammlung, Versicherung mit freier Anbieterwahl) — jeweils
ein gemeinsames Prädikat, Muster D-08-11. Die Drei-Monats-Frist des § 493 ist
RÜCKWÄRTS gerichtet („spätestens drei Monate VOR Ende der Sollzinsbindung");
negative Kalenderperioden sind unausdrückbar (D-06-08 des Nachbarn `miete`),
daher ein Vorwärtsvergleich: Unterrichtung plus drei Monate darf das Ende
nicht überschreiten. Prozentschwellen ohne Bruchrechnung (D-08-01): 75 Prozent
des Höchstbetrags (§ 504a) und die Hälfte des Geldeingangs (§ 505 Absatz 2)
sind je ein `div_round`-Schluss, verglichen als Money-Variablen im Rumpf.

### Zahlungsdienste-Ausführung (§§ 675s, 675t, 675w–676a, D-08-13)

Geschäftstag-Fristen: Ausführungsfrist ein Geschäftstag, bei Papierform zwei
(§ 675s); Wertstellung bei Nichtverbrauchern ein Geschäftstag, bei Verbraucher-
Bareinzahlungen unverzüglich, Wertstellungsdatum spätestens der Eingangstag
(§ 675t). Diese Fristen laufen über `de.bgb.fristen::frist_dauer_tage` mit
`deadline_policy BGB_SONSTIGE_TAG` — **nicht** `BGB_SONSTIGE_KALENDER`, das für
Wochen-/Monats-/Jahresfristen gilt; die Verwechslung ergab beim ersten Lauf
`NEITHER` statt des erwarteten Datums (gefunden vor dem Commit, Szenarien
korrigiert). Nachweispflichten (§§ 675w, 676) und der Ausgleichsanspruch
(§ 676a) folgen demselben Muster wie § 676c; die Haftungsbegrenzung auf
12 500 Euro (§ 675z) und der Erstattungsanspruch mit Achtwochen-Ausschluss
(§ 675x) sind Money- beziehungsweise `not_known`-Defeater-Regeln wie an
anderer Stelle im Paket (§§ 801, 804).

### Liquidation der Gesellschaft (§§ 730–736d, D-08-11, D-08-12)

Drei unabhängige Auflösungsgründe (Tod/Insolvenz eines Gesellschafters nach
Vereinbarung § 730, Kündigung aus wichtigem Grund § 731, Dreiviertelmehrheits-
beschluss § 732) führen jeder zu `gesellschaft_aufgeloest(g)` — mehrere Regeln
mit demselben Kopf, wie schon bei `schuldversprechen_gueltig`. Die
Dreiviertelmehrheit der §§ 732, 734 Absatz 2 rechnet nach den ABGEGEBENEN
Stimmen (`hat_abgestimmt`), nicht nach den stimmberechtigten wie § 714: ohne
Bruchrechnung `4 × Zustimmungen ≥ 3 × abgegebene Stimmen`. § 736d Absatz 4–6
ordnet die Liquidatoren dreistufig: zuerst die Gläubiger der Gesellschaft,
dann die Rückerstattung der Beiträge (Geld, Sachwert bei Einbringung, im
Zweifel kein Ersatz für Dienste), zuletzt die Verteilung des Überschusses
nach dem Verhältnis der Anteile — dieselbe Rundungspolitik wie § 728a/§ 737
(D-08-01).

## Szenarien

Zehn Familien, 141 Szenarien, je ein Test pro Datei; alle Erwartungen sind
vor der Ausführung aus dem Text geschrieben:

| Familie | Szenarien | Schwerpunkt |
|---|---|---|
| `#gesellschaft` | g01–g31 | drei Stufen des § 709 Absatz 3, Korridor MoPeG beidseitig, § 721a, § 725/§ 726 Frist und Kalenderjahresende-Termin beidseitig, Namenszusatz eGbR, Übertragbarkeit, Anwachsung, Notgeschäftsführung, Gesellschafterklage, Informationsrechte, Rechnungsabschluss, Entstehung/Vertretung ggü. Dritten, Einwendungen, Zwangsvollstreckung, Auflösungsgründe, Verweisungen für die nicht rechtsfähige Gesellschaft |
| `#liquidation` | l01–l12 | Auflösung durch Tod/Kündigung/Beschluss, Dreiviertelmehrheit beidseitig, Liquidator kraft Gesetzes gegen abweichende Bestellung, Anmeldepflicht, Reihenfolge der Berichtigung, Verteilung nach Anteilen, Liquidationsnotwendigkeit beidseitig |
| `#buergschaft` | b01–b05 | Einrede der Vorausklage und zwei Ausschlussgründe, Umfang mit und ohne Kosten |
| `#darlehen` | d01–d08 | 200-Euro-Schwelle beidseitig, Zehnprozentschwelle beidseitig, § 497 Absatz 4, § 502 beide Stufen, § 489 |
| `#verbraucherdarlehen-information` | v01–v11 | Kopplungsgeschäfte Immobiliar/Allgemein und ihre Zulässigkeitsgründe, rückwärts gerichtete Dreimonatsfrist § 493 beidseitig, Siebzig-fünf-Prozent-Schwelle § 504a beidseitig, geduldete Überziehung § 505 |
| `#schenkung` | s01–s07 | Jahresfrist § 532 beidseitig, § 534, Zehnjahresfrist § 529 beidseitig, Heilung § 518 |
| `#zahlungsdienste` | z01–z19 | 50 Euro und ihre Ausnahmen, § 675u, Dreizehnmonatsfrist beidseitig, Ausführungsfrist § 675s, Wertstellung § 675t, Nachweispflichten, Erstattung/Achtwochen-Ausschluss § 675x, Haftungsbegrenzung § 675z beidseitig |
| `#gemeinschaft` | m01–m12 | gleiche Anteile, Früchteanteil, Mehrheit nach Anteilen beidseitig, Lasten, Sondernachfolger, Verfügung, Forderungsverkauf/-einziehung, Berichtigung, Gewährleistung — Titel 17 vollständig |
| `#teilzeit-wohnrechte` | w01–w07 | Verbot der Werbung als Geldanlage, Nichtigkeit bei Sprachverstoß, Schriftform, § 486a Zahlungsaufforderungsfrist und Kündigungsfrist beidseitig |
| `#uebrige` | u01–u10, a01–a06, n01–n11, v01–v02 | vier Stufen des § 702, § 606, § 801 Absatz 2, § 762/763, § 656c beidseitig, Anweisung §§ 783–792, Schuldverschreibung §§ 793–800, 803–808, Vorlegung §§ 809, 811 |
