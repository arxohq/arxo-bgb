# de.bgb.dingliche_rechte — BGB Buch 3 Abschnitte 4 bis 8

Paket BG-11 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Gepinnt sind alle 273 geltenden
Paragraphen der Abschnitte 4 bis 8 (§§ 1018–1296, 439 Absätze,
`legal_cutoff` 2026-09-17); **alle fünf Abschnitte 4 bis 8 sind durch
Regelwerk abgedeckt** (§§ 1018–1296): Hypothek, Grundschuld, Rentenschuld
(Abschnitt 7), Pfandrecht (Abschnitt 8), Dienstbarkeiten und Nießbrauch
(Abschnitt 4, §§ 1059a–e Grenze), Vorkaufsrecht (Abschnitt 5) und
Reallasten (Abschnitt 6).

| Zahl | Stand |
|---|---|
| gepinnte Paragraphen | 273 von 273 |
| EXECUTABLE (§33.1) | 268 von 273 — alle Abschnitte 4 bis 8 |
| Absätze des Abschnitts 7 | 154 EXECUTED, 5 BOUNDARY, 3 TODO von 162 |
| Absätze des Abschnitts 8 | 109 EXECUTED, 2 BOUNDARY, 9 TODO von 120 |
| Absätze der §§ 1018–1029 (Grunddienstbarkeiten) | 16 EXECUTED von 16 (§§ 1021 f. Verweis auf Reallasten dokumentiert, nicht zweimal gerechnet) |
| Absätze der §§ 1030–1089 (Nießbrauch) | EXECUTED bis auf §§ 1059a–e (Grenze: Landesbehörde-Verfahren) und die Höhe von GoA-Ersatz/Kündigungsfrist (terminal, D-11-10) |
| Absätze der §§ 1090–1093 (beschränkte persönliche Dienstbarkeit) | 4 von 4 EXECUTED |
| Absätze der §§ 1094–1104 (Vorkaufsrecht) | 11 von 11 EXECUTED; § 469 Abs. 2 lokal nachgebildet (D-11-11) |
| Absätze der §§ 1105–1112 (Reallasten) | 8 von 8 EXECUTED |
| Pflichten / Positions | 61 normative position heads, 2 prohibition pairs under §137, 122 position witnesses |
| Szenarien | 105 in dreizehn Familien, beide Auswerter, byte-identisch (§§ 1139, 1170, 1171 Abs. 3 — V5-11-04 — in `#fristen`) |
| Rest (SOURCE_ONLY) | 5 von 273 — genau §§ 1059a–e (Landesbehörde-Verfahren, GRENZE) |

Offen bleiben nur §§ 1059a–e (Übertragbarkeit des Nießbrauchs bzw. der
beschränkten persönlichen Dienstbarkeit bei juristischer Person, § 1092
Abs. 2, § 1098 Abs. 3) als dokumentierte GRENZE (Landesbehörde-Verfahren,
kein Rechenschritt dieses Pakets) und D-Q11-1 (§ 1133 Satz 3, offen).

## Aufgabenkarte der §§ 1018–1029 (Grunddienstbarkeiten)

| Norm | Was das Paket rechnet | Zeuge |
|---|---|---|
| § 1018, § 1019 Satz 1 | wirksame Bestellung mit dem Vorteil für das herrschende Grundstück | `tests/n01` |
| § 1019 Satz 2 | Unwirksamkeit über das Vorteilsmaß hinaus | Regel, terminale Folge (D-11-09) |
| § 1020 | Schonungspflicht und Erhaltungspflicht der Anlage — Wertung des Gerichts | `tests/n03`, `tests/n04` |
| §§ 1021, 1022 | vereinbarte Unterhaltungspflicht; Verweis auf Reallasten dokumentiert, nicht gerechnet | Regeln |
| § 1023 | Anspruch auf Verlegung der Ausübung und Kostenlast — zwei Wertungskanäle | Regeln |
| § 1024 | Anspruch auf Regelung nach billigem Ermessen bei gleichem Rang (§ 879 Nachbarpaket) | `tests/n05` |
| §§ 1025, 1026 | Teilung des herrschenden und des belasteten Grundstücks | `tests/n06` |
| § 1027 | Beseitigungs- und Unterlassungsanspruch bei Beeinträchtigung (§ 1004 lokal nachgebildet) | `tests/n07`, `tests/n08` |
| § 1028 | Verjährung des Beseitigungsanspruchs nach §§ 195, 199 (de.bgb.fristen); Erlöschen der Dienstbarkeit | `tests/n09`, `tests/n10` |
| § 1029 | Besitzschutz bei Störung innerhalb eines Jahres seit der letzten Ausübung | `tests/n11`, `tests/n12` |

## Aufgabenkarte der §§ 1030–1067 (Nießbrauch an Sachen)

| Norm | Was das Paket rechnet | Zeuge |
|---|---|---|
| § 1030, § 1032, § 1033 | Inhalt, Bestellung an beweglichen Sachen (Übergabe und Einigkeit), Ersitzung | `tests/nb01`, `tests/nb02` |
| § 1031, § 1034, § 1035 | Zubehör, Zustandsfeststellung, Verzeichnis bei Sachinbegriff | Regeln |
| § 1036, § 1041 | Besitzrecht, Pflicht ordnungsmäßiger Wirtschaft, Erhaltung/gewöhnliche Unterhaltung — zwei Wertungskanäle | `tests/nb03`, `tests/nb04` |
| § 1037, § 1038 | Umgestaltungsverbot, neue Bodenanlagen (Wertung), Wirtschaftsplan | Regeln |
| § 1039, § 1040 | übermäßige Fruchtziehung mit Wertersatz und Sicherheit; Schatzanteil | Regeln |
| § 1042, §§ 1043 f. | Anzeigepflicht, außergewöhnliche Ausbesserung (selbst oder Duldung) | Regeln |
| §§ 1045, 1046 | Versicherungspflicht, Verwendung der Versicherungssumme — Wertungskanal | `tests/nb05`, `tests/nb06` |
| § 1047, § 1048 | Lastentragung, Verfügung über Inventar | Regeln |
| § 1049 | Verwendungsersatz nach GoA (terminal, D-11-10), Wegnahmerecht | Regel |
| § 1050 | keine Verantwortlichkeit bei ordnungsmäßiger Ausübung — Wertungskanal | `tests/nb07`, `tests/nb08` |
| §§ 1051–1054 | Sicherheitsleistung, gerichtliche Verwaltung nach Fristablauf, Unterlassungsklage | `tests/nb09`, `tests/nb10` |
| § 1055, § 1056 | Rückgabepflicht; Kündigungsrecht bei Miet-/Pachtverhältnis (terminal) | Regeln |
| § 1057 | Verjährung der Ersatzansprüche in sechs Monaten seit Rückgabe, ohne § 193 (wie § 1226) | `tests/nb11`, `tests/nb12` |
| § 1058, § 1059 | Besteller gilt als Eigentümer (gutgläubig); Unübertragbarkeit, Überlassung der Ausübung | `tests/nb13` |
| §§ 1059a–e | Übertragbarkeit bei juristischer Person — GRENZE (Landesbehörde-Verfahren) | — |
| § 1060 | Zusammentreffen mehrerer Nutzungsrechte → § 1024 (Nachbarpaket-Rang gelesen) | Regel |
| § 1061, § 1063 | Erlöschen durch Tod, Konsolidation mit Ausnahme rechtlichen Interesses | `tests/nb14`, `tests/nb15` |
| § 1062, § 1064 | Zubehör-Aufhebung im Zweifel, formfreie Aufhebung bei beweglichen Sachen | Regeln |
| § 1065 | Beseitigungsanspruch bei Beeinträchtigung (§ 1004 lokal nachgebildet, D-11-09) | Regel |
| § 1066 | Nießbrauch am Miteigentumsanteil | Regel |
| § 1067 | verbrauchbare Sachen: Eigentumserwerb, Wertersatzpflicht nach Beendigung | `tests/nb16` |

## Aufgabenkarte des Abschnitts 7

| Norm | Was das Paket rechnet | Zeuge |
|---|---|---|
| § 1113 Abs. 1, § 1115 | Inhalt der Hypothek, vollständige Bezeichnung der Forderung | `tests/h01` |
| § 1116, § 1117 | Brief- und Buchhypothek, Erwerb, Vermutung der Übergabe mit beiden Seiten | `tests/h02`, `tests/h03` |
| § 1118, § 1119 | gesetzliche Zinsen und Kosten; „bis zu fünf vom Hundert“ mit beiden Seiten | `tests/h04`, `tests/h05` |
| §§ 1120–1122 | Haftungsverband und Enthaftung; Kanarienvogel „eine Bedingung weniger“ | `tests/h06`, `tests/h07` |
| § 1123 Abs. 2 | Jahresfrist der Enthaftung, Vorausmiete mit beiden Seiten des 15. Tages | `tests/f01`–`tests/f03`, `tests/f06`, `tests/f07` |
| §§ 1124–1126 | Vorausverfügung, Aufrechnungssperre, wiederkehrende Leistungen | Regeln, ohne eigenen Zeugen |
| §§ 1127–1130 | Versicherungsforderung; Monatsfrist des § 1128 mit der Verlegung des § 193 | `tests/f04`, `tests/f05` |
| §§ 1131, 1132 | Zuschreibung, Gesamthypothek | Regeln |
| §§ 1133–1136 | Gefährdung, Unterlassungsklage, Nichtigkeit der Verfügungsbeschränkung | Urteilskanäle |
| §§ 1137, 1157 | Einreden des Eigentümers, auch gegen den neuen Gläubiger | Regeln |
| §§ 1138–1140 | öffentlicher Glaube für Forderung und Einreden; Brief und Unrichtigkeit | Regeln |
| § 1139 | Monatsfrist für den Antrag auf Widerspruch (Handlungsfrist) | `tests/w01`, `tests/w02` |
| §§ 1141–1152 | Kündigung, Befriedigung, Übergang, Teilung | Regeln |
| §§ 1153–1156, 1158–1162 | Übertragung, Abtretung, Briefvorlage, Aufgebot | Regeln |
| §§ 1163–1169 | Eigentümerhypothek, Übergang auf den Schuldner, Verzicht | Regeln |
| § 1170, § 1171 | zehn und dreißig Jahre, Ausschluss und Hinterlegung | `tests/w03`-`tests/w06` |
| §§ 1172–1176 | Gesamthypothek; **Teilbetrag nach dem Wertverhältnis** | `tests/g06` |
| § 1177, §§ 1178–1183 | Verwandlung in eine Grundschuld, Löschung, Auswechslung, Aufhebung | Regeln |
| § 879 (Nachbarpaket), § 1181 | **Verteilung des Erlöses nach dem Rang**, drei Belastungen, unzureichender Erlös | `tests/r01` |
| §§ 1184–1190 | Sicherungs- und Höchstbetragshypothek, Papierhypothek, Grundbuchvertreter | Regeln |
| §§ 1191–1198 | Grundschuld; § 1192 Abs. 1a; **sechs Monate des § 1193** mit beiden Seiten des Absatzes 2 | `tests/g01`–`tests/g04` |
| §§ 1199–1203 | Rentenschuld, Ablösungssumme, § 1202 Abs. 2 (30 Jahre) | `tests/g05` |

## Aufgabenkarte des Abschnitts 8

| Norm | Was das Paket rechnet | Zeuge |
|---|---|---|
| § 1204, § 1205, § 1206 | Inhalt und Bestellung durch Einigung und Übergabe, drei Übergabeersätze; Kanarienvogel „ohne Übergabe“ | `tests/p01`, `tests/p02` |
| § 1207, § 1248 | gutgläubiger Erwerb mit beiden Seiten; die Vermutung des § 1248 fällt mit derselben Kenntnis | `tests/p03`, `tests/p04` |
| § 1208, § 1209 | Vorrang vor dem Recht des Dritten; **Rang nach der Zeit der Bestellung**, auch bei künftiger Forderung | `tests/p05` |
| §§ 1210–1216 | Umfang der Haftung, Einreden des Verpfänders, Nutzungspfand, Verwahrung, Wegnahmerecht | Regeln |
| §§ 1217–1222 | erhebliche Rechtsverletzung, drohender Verderb, Androhung, freihändiger Verkauf | Urteilskanäle |
| §§ 1223–1227 | Rückgabe, Einlösung, Forderungsübergang, **§ 1226 sechs Monate ohne Verlegung**, Schutz | `tests/p09` |
| § 1228, § 1229 | Pfandreife mit beiden Wegen; Nichtigkeit der Verfallvereinbarung | `tests/p06`–`tests/p08` |
| §§ 1230–1241 | Auswahl, Herausgabe, Ausführung, **§ 1234 Abs. 2 ein Monat mit der Verlegung des § 193**, Versteigerung, Edelmetallwert | `tests/p06` |
| §§ 1242–1249 | rechtmäßige und unrechtmäßige Veräußerung, **Erlös und Überschuss**, Ablösungsrecht | `tests/p07`, `tests/p08` |
| §§ 1250–1259 | Übertragung, Erlöschen mit beiden Seiten der Vermutung des § 1253 Abs. 2, gesetzliches und gewerbliches Pfand | `tests/p10`, `tests/p11` |
| §§ 1273–1280 | Pfandrecht an Rechten, Bestellung, **Anzeige an den Schuldner** mit Kanarienvogel | `tests/q01`, `tests/q02` |
| §§ 1281–1290 | zwei Lagen der Einziehung: gemeinschaftlich vor, allein nach der Pfandreife und nur soweit erforderlich | `tests/q01`, `tests/q03` |
| § 1287 | die Leistung eines Grundstücks verschafft dem Pfandgläubiger eine **Sicherungshypothek** (§ 1184, Abschnitt 7) | `tests/q04` |
| §§ 1291–1296 | Grund- und Rentenschuld, Order- und Inhaberpapiere, Zinsscheine | Regeln |

## Form des Pakets

1. **Jede Belastung ist ein `Recht` des Nachbarpakets.** `Belastung` ist ein
   Untertyp von `de.bgb.besitz_eigentum::Recht`, `Grundpfandrecht` ein
   Untertyp von `Belastung`. Eintragung (§ 873), Rang (§ 879) und
   öffentlicher Glaube (§ 892) gelten damit unmittelbar; der Rang wird hier
   NICHT ein zweites Mal gerechnet (Ledger D-11-01).
2. **Eine Entität, eine Art.** § 1192 Abs. 1 und § 1200 Abs. 1 ordnen die
   entsprechende Anwendung an; `art_des_grundpfandrechts` unterscheidet
   Hypothek, Sicherungshypothek, Höchstbetragshypothek, Grundschuld,
   Sicherungsgrundschuld und Rentenschuld (D-11-02).
3. **Drei Kanäle für bewertende Merkmale** (DECISION-0194): „ordnungsmäßige
   Wirtschaft“ (§ 1122, § 1135), „Gefährdung der Sicherheit“ und „angemessene
   Frist“ (§ 1133, § 1134) sind Wertungen des Gerichts; Eintragung,
   Beschlagnahme, Rechtskraft, Kenntnis und Übergabe sind festgestellte
   Tatsachen (`origin adjudicated`). Ein flacher Fallsatz über das Ergebnis
   ist verboten.
4. **`not` nur über einer Eingabe des Falls.** Zweimal gemessen (§ 1207,
   § 1281): eine Verneinung über einem ABGELEITETEN Kopf greift nie, weil
   klassische Verneinung einen festgestellten negativen Literal verlangt. Wo
   der Text ein Negativ braucht, steht entweder eine positive Gegen-Kopfnorm
   (`guter_glaube_des_pfandglaeubigers`) oder eine ausdrückliche Eingabe
   (`voraussetzungen_des_1228_abs2_noch_nicht_eingetreten`) — Ledger D-11-07.
5. **Fehlen eines Faktums ist keine Verneinung.** Wo der Text ein Negativ
   verlangt, trägt der Fall die ausdrückliche Eingabe
   (`keine_beschlagnahme`, `brieferteilung_nicht_ausgeschlossen`,
   `erstrangige_belastung`, `kein_anerkenntnis`) oder einen ausdrücklichen
   `assert not`.

## Fristen: § 193 nur bei einem Adressaten

Die Trennung ist an EINEM Tag gemessen — Sonntag, dem 15.03.2026:

- § 1123 Abs. 2 Satz 1 ist eine **Enthaftungsfrist**: das Recht erlischt durch
  den bloßen Ablauf, niemand hat innerhalb der Frist zu handeln. Das Ende
  bleibt der Sonntag (`tests/f01`).
- § 1128 Abs. 1 ist eine **Handlungsfrist**: innerhalb ihrer darf der
  Hypothekengläubiger widersprechen. § 193 verlegt das Ende auf Montag, den
  16.03.2026 (`tests/f04`).

- § 1234 Abs. 2 ist wieder eine **Wartefrist mit Adressaten**: innerhalb des
  Monats nach der Androhung darf der Verpfänder noch befriedigen (§ 1223
  Abs. 2). Das Ende wandert auf denselben Montag; ein Verkauf an diesem Tag
  ist noch zu früh (`tests/p06`).
- § 1226 ist eine **Verjährungsfrist** und bleibt auf dem Sonntag
  (`tests/p09`).

Nach demselben Merkmal sind § 1139 (Antrag — Verlegung) und §§ 1170, 1171
Abs. 3, 1193 Abs. 1, 1202 Abs. 1 (Ablauf allein — keine Verlegung) getrennt
(Ledger D-11-04, D-11-07; Zeilen in `docs/foundations/de-bgb/DEADLINES.json`).

## Rundung

Geld entsteht in diesem Paket an zwei Stellen, und an jeder wird **einmal je
Anspruch** auf den Cent gerundet (`HALF_UP`, Ledger D-11-05):

- § 1119 Abs. 1: `div_round(Geldsumme × 5,0; 100,0; 2; HALF_UP)`;
- § 1172 Abs. 2: Werte als GANZE Zahlen in Cent, dann
  `div_round(Geldsumme × Wert; Summe × 1,0; 2; HALF_UP)`.

Ein Produkt zweier Geldbeträge kennt § 58 nicht (gemessen: LDC-E2108); das
Gesetz nennt weder Einheit noch Bewertungsverfahren.

## Was das Paket nicht tut und warum

- **Das Verteilungsverfahren der Zwangsversteigerung.** § 1147 sagt, dass die
  Befriedigung im Wege der Zwangsvollstreckung erfolgt; wie der Erlös verteilt
  wird, steht im ZVG (geringstes Gebot, bar zu zahlender Teil, Bestehenbleiben
  von Rechten, Teilungsplan — §§ 10, 44, 52, 105 ff.). Das Paket rechnet nur,
  was das BGB selbst sagt: Reihenfolge nach § 879, Geldsumme aus dem
  Grundstück nach § 1113 Abs. 1 und Erlöschen durch Befriedigung nach § 1181
  Abs. 1 (Ledger D-11-03).
- **Grundbuchverfahren (GBO), Aufgebotsverfahren (FamFG),
  Hinterlegungsordnung, Versicherungsvertragsrecht (VVG).** Eintragung,
  Löschung, Rechtskraft des Ausschließungsbeschlusses und die Hinterlegung
  sind FESTGESTELLTE TATSACHEN des Falls, nicht Rechenschritte des Pakets.
- **§ 1133 Satz 3 ohne Zahl.** Die Norm gewährt nur die abgezinste Summe,
  nennt aber weder Zinssatz (§ 246 gehört zu `de.bgb.schuldrecht_at`) noch
  Abzinsungsverfahren. Die Regel stellt das Rechtsfolgenurteil fest und
  rechnet keine Zahl; die Frage steht offen als D-Q11-1 — TODO, nicht Grenze.
- **§ 1114 § 3 Abs. 6 GBO, § 1187 Wechsel- und Wertpapierrecht, § 801
  Vorlegungsfrist.** Fremde Gesetze; sie erscheinen als Eingaben, nicht als
  Regeln.
- **Das Versteigerungsverfahren selbst.** § 1236 und § 1237 Satz 1 verweisen
  auf § 383 (Paket `de.bgb.schuldrecht_at`); Durchführung und öffentliche
  Bekanntmachung sind festgestellte Tatsachen des Falls. § 1246 Abs. 2 („so
  entscheidet das Gericht“) ist eine Verfahrensnorm, kein Ableitungsschritt.
- **§ 1217 Abs. 2 Satz 2** trägt dieselbe offene Größe wie § 1133 Satz 3: die
  abgezinste Summe ohne genannten Zinssatz und ohne Abzinsungsverfahren
  (D-Q11-1) — TODO, keine Grenze.
- **Abschnitte 4, 5 und 6.** In diesem Schnitt nicht ausgeführt — TODO mit
  benanntem nächsten Schritt, KEINE erklärte Grenze.

## Prüfung

```sh
./law engine check corpus/laws/de/bgb/dingliche-rechte
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-dingliche-rechte.lawir.json
export LAW_WORK_PROFILE_STATE=<eigene Datei nach PARALLEL.md §2>
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.dingliche_rechte#hypothek"
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.dingliche_rechte#hypothek"
python3 corpus/laws/de/bgb/dingliche-rechte/analysis/build_saetze.py
```

Familien: `#hypothek` (7), `#fristen` (7), `#rang-und-erloes` (1),
`#grundschuld` (6), `#pfandrecht` (11), `#pfandrecht-an-rechten` (4),
`#positionen-wellen-02-04` (6).
