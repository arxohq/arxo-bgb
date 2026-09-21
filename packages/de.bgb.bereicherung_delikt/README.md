# de.bgb.bereicherung_delikt — BGB Buch 2 Abschnitt 8 Titel 26–27 (§§ 812–853)

Paket BG-09 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Es senkt die beiden gesetzlichen
Schuldverhältnisse des Abschnitts 8 ab: die **ungerechtfertigte Bereicherung**
(Titel 26, §§ 812–822) und die **unerlaubten Handlungen** (Titel 27,
§§ 823–853). Quellen: `sources.law`, erzeugt aus dem Register DOKNR, Stand
`legal_cutoff` 2026-09-17; § 835 und § 847 sind weggefallene Positionen und als
Grenze mit Grund aus der Publikation selbst erklärt.

Tiefe § 33.1 (`audit.py --fast`): **EXECUTABLE 41 von 43** — aus jedem
geltenden Paragraphen wird etwas abgeleitet; SOURCE_ONLY 2 sind genau die
beiden weggefallenen Positionen. 187 Regeln, 34 Szenarien in sechs Familien,
beide Auswerter, 81 `evaluate`-Aufrufe byteweise identisch.

## Aufgabenkarte

## Pflichten / Positions

Die P3-Positionen stehen neben den institutionellen Rechtsfolgen:
`Herausgabe812`, `Wertersatz818`, `Schadensersatz823`,
`Schadensersatz824`, `DeliktischerSchadensersatz249`,
`GeminderterErsatz254` und `Schadensersatz826` sind durch eigene
`evaluate positions()`-Szenarien abgesichert. §391 bleibt im Paket
`de.bgb.schuldrecht-at`; die bestehenden Köpfe der §§825, 829, 839 und
852 werden dort als `EXISTING` im P3-Ledger referenziert.

| Norm | Form im Paket | Zeuge |
|---|---|---|
| § 812 Abs. 1 Satz 1, Satz 2 | vier Kondiktionen mit je eigenem Anspruchskopf | `b01`, `b03` |
| § 812 Abs. 2 | Anerkenntnis gilt als Leistung (Regel, keine Fiktion) | `b05` |
| § 813 Abs. 1 | Rückforderung trotz dauernder Einrede; Satz 2 liest `de.bgb.fristen` (§ 214 Abs. 2) | `b01`–`b04` (Kette), Regel `EinredeWarVerjaehrung` |
| § 813 Abs. 2 | betagte Verbindlichkeit — `unless` an `Rueckforderung813` | Regel |
| § 814 | Kenntnis der Nichtschuld: **Tatsache** `adjudicated`; sittliche Pflicht: **Wertung** § 47.3 | `b02` |
| § 815 | Ausschluss NUR der Zweckverfehlungskondiktion | `b04` |
| § 816 Abs. 1, 2 | Verfügung und Leistung an einen Nichtberechtigten, drei Regeln | Regeln |
| § 817 Satz 1, Satz 2 | eigene Kondiktion; Ausschluss mit Gegenausnahme (Eingehung einer Verbindlichkeit) | Regeln |
| § 818 Abs. 1–4 | Nutzungen, Surrogat, Wertersatz, Entreicherung, Rechtshängigkeit | `b06`, `b07` |
| § 819, § 820 | verschärfte Haftung ab Empfang / ab Kenntnis; Zinsen ab Erfahren | Regeln |
| § 821, § 822 | Einrede der Bereicherung; Herausgabepflicht des Dritten | Regeln |
| § 823 Abs. 1 | sechs Rechtsgüter — **eine Regel je Position**, kein `or`-Körper | `h01`, `h06` |
| § 823 Abs. 1 Verschulden | Wertung § 47.3 (`vorsatz`, `fahrlaessigkeit`) | `h02` (ohne Antwort), `h01` (mit Antwort) |
| § 823 Abs. 2 Satz 1, 2 | Schutzgesetz als Eingabe; Verschulden nur, wo das Gesetz es verlangt | `h03` |
| § 824 Abs. 1, 2 | Kreditgefährdung; berechtigtes Interesse als `unless` | `h05` |
| § 825 | drei Bestimmungsmittel, drei Regeln | Regeln |
| § 826 | gute Sitten und Vorsatz — beides Wertung | `h04` |
| § 827 Satz 1, 2 | Unverantwortlichkeit; Selbstversetzung als Gegenregel mit `unless` | Regeln |
| § 828 Abs. 1–3 | **7 / 10 / 18 Jahre** über `de.bgb.fristen::lebensjahr_vollendet_am` | `v01`–`v05` |
| § 829 | Billigkeit — Wertung § 47.3, dazu ausdrückliche Angabe zum Aufsichtspflichtigen | `v05` |
| § 830 Abs. 1, 2 | Mittäter, Urheberzweifel, Anstifter und Gehilfen | Regeln |
| § 831, § 832 | **Vermutung** mit zwei Entlastungsgründen (`presume … unless`) | `p01`, `p02`, `p03` |
| § 833 Satz 1, 2 | Gefährdungshaftung mit geschlossenem Erfolgskatalog; Nutztier-Entlastung | `p04`, `p05` |
| § 834 | Tieraufseher, eigene Vermutung | Regel |
| § 836 Abs. 1–3 | Vermutung des Besitzers; **Jahresfrist** des Absatzes 2; Eigenbesitzer | `p06`, `p07` |
| § 837, § 838 | Gebäudebesitzer und Unterhaltungspflichtiger an Stelle des Besitzers | Regeln |
| § 839 Abs. 1–3 | Vorsatz ohne, Fahrlässigkeit mit Subsidiarität; Spruchrichterprivileg als `unless`-Kette | Regeln |
| § 839a | Sachverständiger: Vorsatz oder grobe Fahrlässigkeit; § 839 Abs. 3 entsprechend | Regeln |
| § 840, § 841 | Gesamtschuld und drei Regeln des Innenverhältnisses | Regeln |
| § 842, § 843 | Erwerbsnachteile; Geldrente, Kapitalabfindung, Unterhalt eines anderen | `d05` |
| § 844 Abs. 1–3 | Beerdigungskosten, Unterhaltsrente, Nasciturus, **Hinterbliebenengeld mit Vermutung** | `d01`, `d02`, `d03` |
| § 845, § 846 | entgangene Dienste; Quote des § 254 mit der einzigen Division | `d04` |
| § 848–§ 851 | Zufallshaftung, Verzinsung, Verwendungen, befreiende Leistung | Regeln |
| § 852 Satz 1, 2 | Restschadensersatz nach Verjährung; **10 Jahre / 30 Jahre**, früheres Ende | `j01`–`j03` |
| § 853 | Arglisteinrede | `j04` |

## Drei Kanäle der bewertenden Merkmale (DECISION-0194)

Der Abschnitt delegiert besonders viel an das Gericht. Jeder Fall folgt dem
Wortlaut des Paragraphen:

- **Wertung** (`external judgment relation … { authority Court; }`) — „vorsätzlich
  oder fahrlässig“ (§ 823 Abs. 1, § 839 Abs. 1), „gegen die guten Sitten“
  (§ 817, § 826), „die im Verkehr erforderliche Sorgfalt beobachtet“ und „auch
  bei Anwendung dieser Sorgfalt entstanden“ (§§ 831–834, 836), „die zur
  Erkenntnis der Verantwortlichkeit erforderliche Einsicht“ (§ 828 Abs. 3),
  „soweit die Billigkeit … erfordert“ (§ 829), „ein wichtiger Grund“
  (§ 843 Abs. 3), „eine angemessene Entschädigung in Geld“ (§ 844 Abs. 3),
  „grobe Fahrlässigkeit“ (§ 839a, § 851), die Quote des § 254 (§ 846).
  Ohne Antwort: `REQUIRES_JUDGMENT` und eine Frage an das Gericht (`h02`);
  mit Antwort — auch mit VERNEINENDER (`not … { origin adjudicated; }`) —
  rechnet das Paket zu Ende.
- **Festgestellte Tatsache** (`kind empirical`, im Fall `origin adjudicated`) —
  „gewusst hat, dass er zur Leistung nicht verpflichtet war“ (§ 814), „kennt
  den Mangel des rechtlichen Grundes“ (§ 819 Abs. 1), „die Pflichtverletzung
  besteht in einer Straftat“ (§ 839 Abs. 2), Kausalität, Tag der Handlung.
- **Lesarten** (§ 152) — hier nicht gebraucht: der Abschnitt streitet über
  Wertungen, nicht über den Wortsinn.

Ein flacher Fall-Fakt „X haftet“ ist verboten; jede Haftung ist Schluss einer
Regel.

## Warum jede Kondiktion einen eigenen Kopf hat

Die Ausschlüsse des Titels 26 treffen NICHT alle Kondiktionen: § 814 nur das
zur Erfüllung einer Verbindlichkeit Geleistete, § 815 nur die Rückforderung
„wegen Nichteintritts des bezweckten Erfolgs“. Ein gemeinsamer Anspruchskopf
mit gesammelten `unless` hätte jeden Grund verziehen, den der Text stehen
lässt. Deshalb trägt jede Kondiktion ihren Kopf, die Gründe werden strikt
gesammelt und je Kopf steht GENAU EINE defeasible Regel: zwei defeasible Regeln
mit demselben Kopfliteral löschen einander.

Aus demselben Grund ist die Verantwortlichkeit der §§ 827, 828 einstellig
(`nicht_verantwortlich(h)`) und die Parteien kommen erst eine Regel später
dazu: der Ausnahmesatz muss jede Variable des Kopfes binden (§ 190).

## Rundung

Das BGB nennt in diesem Abschnitt weder Zinssatz noch Rundung. Beträge kommen
als `EUR` aus dem Fall und werden nur addiert und subtrahiert (§ 818 Abs. 2
und 3: Wert abzüglich der weggefallenen Bereicherung). Die EINZIGE Division
steht bei § 846 i. V. m. § 254: die Quote des mitwirkenden Verschuldens kommt
als Paar ganzer Zahlen vom Gericht, und der geminderte Betrag wird EINMAL je
Anspruch gerundet — `div_round(Betrag × (Nenner − Zähler), Nenner × 1.0, 2,
"HALF_UP")` (Ledger `D-09-02`). Zeuge `d04`: 9.000,00 € bei einer Quote von
1/3 ergeben 6.000,00 €.

## Fristen

| Norm | Einheit | Politik | Zeuge |
|---|---|---|---|
| § 836 Abs. 2 | 1 Jahr ab Beendigung des Besitzes | `BGB_DELIKT_JAHR` | `p06` (letzter Tag), `p07` (einen Tag später) |
| § 852 Satz 2 Alt. 1 | 10 Jahre ab Entstehung | `BGB_DELIKT_JAHR` | `j01` |
| § 852 Satz 2 Alt. 2 | 30 Jahre ab Begehung | `BGB_DELIKT_JAHR` | `j02` |
| § 828 Abs. 1–3 | 7 / 10 / 18 Lebensjahre | `de.bgb.fristen` (§ 187 Abs. 2, § 188 Abs. 2) | `v01`–`v05` |

Die Politik `BGB_DELIKT_JAHR` trägt denselben Feldsatz wie
`BGB_FRISTEN_KALENDER`; eine Politik je Fall (§ 168.2). Zeilen:
`docs/foundations/de-bgb/DEADLINES.json`, Abschnitt BG-09.

## Abwesenheit ist keine Verneinung

Wo der Text eine Entlastung, einen Rechtfertigungsgrund oder das Ausbleiben
einer Entreicherung voraussetzt, verlangt das Paket eine AUSDRÜCKLICHE Angabe
des Falls: `kein_rechtfertigungsgrund`, `keine_entreicherung`,
`kein_ersatz_vom_aufsichtspflichtigen`, `leistung_bestand_nicht_in_eingehung`,
`ohne_verschulden_in_den_zustand_geraten`, `auch_ohne_entziehung_eingetreten`,
`anderweitiger_ersatz_nicht_erlangbar`, `verstoss_nur_mit_verschulden_moeglich`,
`verpflichtung_des_empfaengers_infolgedessen_ausgeschlossen`. Das Schweigen des
Falls schaltet keine Norm frei (Zeugen `b07`, `h06`).

Fünf Prämissen sind reine Fall-Eingaben ohne eigenen Erzeuger
(`anstifter_oder_gehilfe`, `nebeneinander_verantwortlich`,
`aufsichtspflichtiger_im_falle_829`, `betagte_verbindlichkeit_vorzeitig_erfuellt`,
`auch_ohne_entziehung_eingetreten`). Das ist kein Warteschlangen-Stub: der Text
nennt sie als Tatsachen des Falls, nicht als Rechtsfolge einer anderen Norm
dieses Abschnitts.

## Was das Paket nicht tut und warum

- **Die Rechtsfolge „Schadensersatz“ selbst** (§§ 249–254: Naturalrestitution,
  Geldersatz, Mitverschulden) gehört `de.bgb.schuldrecht_at` (BG-04). Hier steht,
  WER WEM dem Grunde nach haftet; die Quote des § 254, auf die § 846 verweist,
  ist bis zur Zusammenführung lokal als Urteilsanfrage erklärt (`D-09-01`).
- **Fremde Gesetze** werden nicht formalisiert, sondern als typisierte Eingabe
  genommen: Schutzgesetze (§ 823 Abs. 2), Inhalt der Amtspflicht und Art. 34 GG
  (§ 839), StVG, ProdHaftG, die Schadensschätzung des § 287 ZPO
  (`docs/foundations/de-bgb/SOURCES.json`, `external`).
- **Die Rechte des Besitzers gegenüber dem Eigentümer wegen Verwendungen**
  (§ 850 → §§ 994 ff.) liegen bei `de.bgb.besitz_eigentum` (BG-10); § 850 gibt
  hier nur die Verweisung.
- **Der Zinssatz des § 849** steht nicht in § 849, sondern in § 246 (BG-04):
  das Paket leitet den Beginn der Verzinsung ab, nicht die Höhe.
- **Die Rente des § 843 Abs. 2 Satz 1** verweist auf § 760 (BG-08); nur die
  Sicherheitsleistung des Satzes 2 ist hier als Wertung erklärt.
- **Die regelmäßige Verjährung des Ersatzanspruchs** (§§ 195, 199) und ihre
  dreißigjährige Höchstfrist für Leben, Körper, Gesundheit und Freiheit
  (§ 199 Abs. 2) gehören `de.bgb.fristen` und werden hier nicht wiederholt;
  § 852 liest sie (`j03`).
- **Doktrin des BGH** ist keine Norm: das Paket enthält weder
  Rahmenrecht am Unternehmen noch das allgemeine Persönlichkeitsrecht als
  eigenen Tatbestand — beides käme im Modell über `verletzung_sonstiges_recht`
  als festgestellte Tatsache des Falls herein.

## Prüfung

```sh
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
./law engine check corpus/laws/de/bgb/bereicherung-delikt
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-bereicherung-delikt.lawir.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.bereicherung_delikt#bereicherung"
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.bereicherung_delikt#bereicherung"
```

Das Lock dieses Pakets trägt die Kalenderzeile des importierten
`de.bgb.fristen` (`urn:de:corpus:clir:bgb-fristen#KALENDER_BUNDESWEIT`) und
`lockVersion` 0.2: `lock --write` eines Verbrauchers findet den Datensatz der
Abhängigkeit nicht und ließe 0.1 stehen, was `lawc test` für § 85 zurückweist.

## Querschnitt § 823 Abs. 1 → § 254 → § 249 → §§ 195, 199 (D-09-08)

Familie `de.bgb.bereicherung_delikt#querschnitt-delikt-mitverschulden-verjaehrung`
(MULTISESSION-PROMPT.ru.md §10 Nr. 6), 5 Szenarien; unabhängige Ausdrücke, VOR
der Ausführung von Hand gerechnet:

- **q01** (Hauptfall): Schaden 10.000,00 €, Mitverschulden 1/4 (§ 254 Abs. 1) →
  10.000,00 × 3/4 = **7.500,00 €**; Kenntnis am Tag der Verletzung
  (10.05.2023) → regelmäßige Verjährung Schluss 2023 + 3 Jahre → **Ablauf des
  31.12.2026**, noch nicht eingetreten.
- **q02** (negativ zu § 254): ohne festgestelltes Mitverschulden bleibt der
  volle Schaden **10.000,00 €** (§ 254 Abs. 1 im Umkehrschluss).
- **q03** (Unvollständigkeit): ohne Antwort des Gerichts zu Vorsatz/
  Fahrlässigkeit (§47.3) bleibt der Haftungsgrund offen — `REQUIRES_JUDGMENT`
  für die Haftung dem Grunde nach; der Betrag bleibt `NEITHER`/`COMPUTED`.
- **q04** (Kanarienvogel, minus `kein_rechtfertigungsgrund`): kein
  Haftungsgrund, kein Betrag.
- **q05** (§ 199 Abs. 2 Höchstfrist): Körperverletzung 15.06.1990, Kenntnis
  erst 10.01.2020 — regelmäßige Verjährung endete rechnerisch erst mit
  Ablauf des 31.12.2023, die dreißigjährige Höchstfrist ohne Rücksicht auf
  Kenntnis aber bereits mit Ablauf des **15.06.2020** — die frühere Frist ist
  maßgeblich (§ 199 Abs. 2, `de.bgb.fristen::GesamtfristHoechstfristMassgeblich`).

Brücke: die eigene institutionelle Feststellung `schadensersatzpflicht`
(§ 823 Abs. 1) trägt über die neue Tatsachenidentifikation `schaden_fuer_249`
in `de.bgb.schuldrecht_at::ersatzbetrag_nach_mitverschulden` (§§ 249, 252,
254); die Verjährung liegt, wie bei § 852, bei `de.bgb.fristen` über
denselben `Anspruch`. Der § 846-Kanal des `Ersatzanspruchs des Dritten`
(D-09-01) bleibt UNVERÄNDERT lokal: BG-04 und BG-09 führen je ein eigenes,
nominal verschiedenes `entity Schaden` — eine echte Umstellung wäre ein
Typumbau, kein Rename (D-09-08, `V4-BG-09-03`).

**Kalenderfalle.** `de.bgb.schuldrecht_at` deklariert selbst
`calendar KALENDER_BUNDESWEIT`; sobald es im `world` steht, wird ein
unqualifiziertes `calendar KALENDER_BUNDESWEIT;` im Fall zweideutig
(`AMBIGUOUS_CALENDAR`), sofern dieses Paket nicht ebenfalls seine EIGENE,
byteidentische Kopie deklariert (jetzt in `package.law`) — jedes Szenario
des Pakets, das mit `de.bgb.fristen`-Kalenderarithmetik rechnet, braucht
seitdem die explizite Achse `calendar KALENDER_BUNDESWEIT;` im `context`
(alle 38 Szenarien des Pakets tragen sie jetzt; D-09-08).
