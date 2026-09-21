# de.bgb.fristen — BGB Buch 1, Abschnitte 4 und 5: Fristen, Termine, Verjährung

Paket BG-02 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Geltungsbereich: §§ 186–193
(Fristen und Termine) und §§ 194–218 (Verjährung); §§ 219–225 sind
weggefallene Positionen des Inventars. **Einziger Eigentümer der
Fristenberechnung** der Familie `de.bgb.*`: besondere Verjährungsfristen
(§ 438, § 548, § 634a) und besondere Fristen (§ 355, § 356, § 573c, § 622)
bleiben bei ihren Normen in den Fachpaketen und lesen die Mechanik von hier.

Quelle: konsolidierter Text von gesetze-im-internet.de (XML, builddate
20260910215507, abgerufen 2026-09-17), 34 Paragraphen als Fragmente §194,
`sources/de-bgb-fristen/bgb-de.txt` und `xml/` — generiert von
`corpus/tools/sources/sync/sync_de_bgb_packages.py` aus dem Register
`docs/foundations/de-bgb/registry/DOKNR.json`. Nicht von Hand ändern.

## Stand: Pilot B0 der drei Mechaniken (17.09.2026)

| Mechanik | Form im Kern (ohne Änderung des Kerns) | Zeugen |
|---|---|---|
| Tagesfrist §§ 187 Abs. 1, 188 Abs. 1 und Verlegung § 193 | `add_business_days(Ereignis, n calendar_day)` unter `BGB_FRISTEN_TAG` (start_count next_day, include_end, roll next_working_day); Kalender §85 mit Sonnabend, Sonntag und bundesweiten Feiertagen | `tests/p01`–`p03` |
| Monats-/Jahresfrist § 188 Abs. 2–3 und § 193 | `add_calendar_period` unter `BGB_FRISTEN_KALENDER` (same_day, month_end last_day_of_month); Verlegung als Regel `add_business_days(Ende, 1 business_day)` | `tests/p04`, `p05` |
| Ultimo § 199 Abs. 1 und regelmäßige Frist § 195 | zwölf Kandidaten `month_end_of(month_start_of(e) + k Monate)` und Auswahl des Dezembers über die Monatslängen 31/31/≤29 (Ledger D-02); Jahresschritt 3 Jahre | `tests/p06`, `p07`, `p12` |
| Hemmung § 209, Mindestfrist § 203 S. 2 | Verschiebung um Hemmungstage (`days_between` + 1, `with_unit` als calendar_day-Schritt); Mindestfrist drei Monate nach Ende der Verhandlungen; Auswahl des späteren Tages | `tests/p08`–`p11` |
| Lebensalter § 187 Abs. 2 S. 2, § 188 Abs. 2 (Beginnfrist) | Jahresschritt vom Geburtstag, dann Tagesschritt um die Tage minus eins (`with_unit`): das Lebensjahr ist mit Ablauf des Vortags des Geburtstags vollendet (Ledger D-09) | `tests/p13` |

Familie `de.bgb.fristen#mechanik-pilot`: 13 Szenarien, beide Auswerter,
Differential byteweise, Kanarienvogel: eine
invertierte Erwartung färbt beide rot.

## Politiken §86 (eine je Fall)

| Politik | Felder | Normen |
|---|---|---|
| `BGB_FRISTEN_TAG` | start_count next_day; include_end true; roll next_working_day | § 187 Abs. 1, § 188 Abs. 1, § 193 (Roll) |
| `BGB_FRISTEN_KALENDER` | start_count same_day; include_end true; roll no_roll; month_end last_day_of_month | § 188 Abs. 2–3, § 195, § 199, § 203 S. 2, § 209; § 193 als Regel `Verlegung193` |

Welche Norm welche Politik verlangt, steht je Zeile in
`docs/foundations/de-bgb/DEADLINES.json`. Der Kalender
`corpus/clir/de-feiertage-bundesweit.calendar.json` wird von
`corpus/gen_kz_clir.py` erzeugt; `tools/gen_kalender.py` schreibt ihn und die
Lock-Zeile im punktuellen Modus (`--check` prüft Bytes, Hash und Lock).

## Aufgabenkarte (Welle B2)

| § | Inhalt | Stand |
|---|---|---|
| 186 | Geltungsbereich der Auslegungsvorschriften | Fragment; Regel folgt (Definition) |
| 187 Abs. 2 | Beginnfrist, Lebensalter (Verbraucher `de.wohngeld`) | Lebensalter erledigt (`p13`, D-09); Beginnfrist für andere Termine und der 29. Februar in Nicht-Schaltjahren — TODO |
| 189–192 | halbes Jahr, Vierteljahr, halber Monat; Verlängerung; Monat = 30 Tage; Anfang/Mitte/Ende | TODO |
| 194 | Anspruch; unverjährbare Ansprüche aus familienrechtlichem Verhältnis | TODO |
| 196–197, 200–201 | zehn- und dreißigjährige Fristen; Beginn anderer Fristen | TODO |
| 199 Abs. 1 Nr. 2 | grob fahrlässige Unkenntnis — Kanal §47.3 (`external judgment relation … authority Court`) | TODO |
| 199 Abs. 2–4 | Höchstfristen 10/30 Jahre, frühere Frist maßgeblich | TODO |
| 202 | Unzulässigkeit von Vereinbarungen | TODO |
| 204, 204a–208 | Hemmungstatbestände als Regeln; Vereinigung überschneidender Zeiträume | TODO |
| 210–212 | Ablaufhemmung; Neubeginn | TODO |
| 213–218 | Wirkung der Verjährung, Aufrechnung, Sicherheiten, Nebenleistungen, Rücktritt | TODO |
| Art. 229 § 6 EGBGB | Korridor 2002 (Paket `de.bgb.uebergang`) | Abs. 1 S. 1, 3, 4 ausgeführt (`uebergang#verjaehrung-2002`); Abs. 1 S. 2–3, Abs. 2 — TODO |
| Landesfeiertage | Kalender je Land (Leistungsort, § 193) — Datenpakete | TODO |

Ein `TODO` ist keine Grenze: Grenzen werden nach dem Text des Paragraphen
erklärt, nicht nach dem Umfang der Arbeit.

## Was das Paket nicht tut und warum

- **Mehrere Hemmungszeiträume je Anspruch** werden im Pilot nicht vereinigt:
  `hemmung(a, von, bis)` trägt `key(a)`. Die Vereinigung überschneidender
  Zeiträume ist Regelarbeit der Welle B2, keine Grenze des Kerns.
- **Landesfeiertage** fehlen im Kalender: § 193 stellt auf den Leistungs-
  oder Erklärungsort ab, und die Feiertage sind Landesrecht. Der Kalender
  enthält nur die in allen Ländern anerkannten Tage (Gebiet „bundesweit“).
- **Ob § 193 auf Verjährungsfristen anzuwenden ist**, entscheidet der Pilot
  nicht: die Verlegung ist an der generischen `Frist` gezeigt; für die
  Verjährung wird die Lesart in B2 als Interpretation §152 erklärt.
- **Kenntnis (§ 199 Abs. 1 Nr. 2)** ist eine festgestellte Tatsache
  (`origin adjudicated`), keine Fallaussage über das Ergebnis; die grob
  fahrlässige Unkenntnis ist Wertung und wird in B2 als Kanal erklärt.

## Prüfung (nur punktuell)

```sh
./law engine check corpus/laws/de/bgb/fristen
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-02 --check
python3 corpus/laws/de/bgb/fristen/tools/gen_kalender.py --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-fristen.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.fristen#mechanik-pilot"
python3 corpus/run_kz_regression.py --only "de.bgb.fristen#mechanik-pilot" --write-manifest
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.fristen#mechanik-pilot"
```
