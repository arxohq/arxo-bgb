# de.bgb.verfuegungen — BGB Buch 5, Abschnitte 3–9: Testament, Erbvertrag, Pflichtteil

Paket BG-16 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Geltungsbereich §§ 2064–2385
(305 Paragraphen als Fragmente §194, `sources/de-bgb-verfuegungen/`,
generiert aus dem Register DOKNR). Importe: `de.bgb.core`, `de.bgb.ehe`,
`de.bgb.erbfolge` (gesetzlicher Erbteil als Bruch), `calc.kinship`.

## Stand (18.09.2026, mehrsitzungsfortsetzung abgeschlossen) — alle sieben Module der Aufgabe bearbeitet

Mess §33.1 registriert (`verify/ci/data/formalization-depth.json`):
**EXECUTABLE 292 / 305** (SOURCE_ONLY 13, UNEXPLAINED 1); Metriken §218
(`corpus/ratchets/label-ratchet.json`): Wörterbuch 1119, Normen 562, ohne
Anker 0. Elf Szenario-Familien, beide Auswerter, differential byteweise
(mehrere hundert evaluate-Aufrufe summiert über alle Familien). Module und
Dateien:

| Modul | §§ | Datei | Familie(n) |
|---|---|---|---|
| Testament, Pflichtteil-Kern | 2064–2156, 2303–2338 (Kern) | `package.law` | `pflichtteil-pilot` (33), `pflichtteil-entziehung-und-grenzen` |
| Vermächtnis | 2157–2196 | `abschnitt-03-titel-04-vermaechtnis.law` | `vermaechtnis-anwachsung-und-wirksamkeit` |
| Vermächtnis-Belastungen | 2164–2191 | `abschnitt-03-titel-04b-vermaechtnis-belastungen.law` | `vermaechtnis-belastungen-und-erfuellung` |
| Testamentsvollstrecker | 2197–2227 | `abschnitt-03-titel-06-testamentsvollstrecker.law` | `testamentsvollstrecker` |
| Errichtung/Aufhebung | 2229–2263 | `abschnitt-03-titel-07-errichtung-und-aufhebung.law` | `errichtung-und-aufhebung` |
| gemeinschaftliches Testament | 2265–2272 | `abschnitt-03-titel-08-gemeinschaftliches-testament.law` | `gemeinschaftliches-testament` |
| Erbvertrag | 2274–2302 | `abschnitt-04-erbvertrag.law` | `erbvertrag` |
| Pflichtteil-Rest 2329 | 2329 | `abschnitt-03-pflichtteil-2329.law` | `pflichtteil-entziehung-und-grenzen` |
| Erbunwürdigkeit | 2339–2345 | `abschnitt-06-erbunwuerdigkeit.law` | `erbunwuerdigkeit` |
| Erbschaftskauf | 2372–2385 | `abschnitt-09-erbschaftskauf.law` | `erbschaftskauf` |
| Erbschein | 2353, 2361–2370 | `abschnitt-08-erbschein.law` | `erbschein` |
| Erbverzicht-Rest | 2347, 2349, 2350, 2352 | `abschnitt-07-erbverzicht-rest.law` | `erbverzicht-rest` |
| Pflichtteil-Rest + Brücke 2316 | 2308, 2310 S. 2, 2312, 2316 | `abschnitt-05-pflichtteil-2308-2312-2316-bruecke.law` | `pflichtteil-anfechtung-landgut-und-ausgleichungsbruecke` |
| Nachlassgericht + Hypothek | 2200, 2228, 2166 | `abschnitt-diverse-2200-2228-2254-2166.law` | `nachlassgericht-und-hypothekenbelastung` |
| Vorerbe-Rest + Erbverzichtsform | 2133, 2135, 2348 | `abschnitt-03-titel-03-vorerbe-rest-und-2348.law` | `vorerbe-rest-und-erbverzichtsform` |

## Stand: B5-Teil 1 (18.09.2026) — Pflichtteil als Geld, Ergänzung mit Abschmelzung

| Norm | Form | Zeugen |
|---|---|---|
| § 2303 Abs. 1, 2 Pflichtteilsberechtigte; Hälfte des Wertes des gesetzlichen Erbteils | `pflichtteilsberechtigt`; Quote `(z, 2n)` aus `gesetzlicher_erbteil_bruch` | `p01`, `p02` |
| § 2310 Mitzählen der Ausgeschlossenen | die Erbfolge rechnet ohne Rücksicht auf die Verfügung | `p01` |
| § 2311 Abs. 1 Nachlasswert zur Zeit des Erbfalls | Eingabe `nachlasswert`; Betrag `div_round(Wert × z, n, 2, HALF_UP)` | `p01`, `p02` |
| § 2325 Abs. 1, 3 Ergänzung, Abschmelzung um ein Zehntel je Jahr, nichts nach zehn Jahren | Jahresfenster vom Tag der Leistung (`add_calendar_period`, Politik `BGB_VERFUEGUNGEN_JAHR`), Zehntel, Summe über die Schenkungen | `p03`, `p04` |
| § 2325 Abs. 2 Niederstwertprinzip | Wert bei Leistung; ist der Wert beim Erbfall geringer, gilt dieser niedrigere Wert | `p05` |
| § 2325 Abs. 3 Satz 3 Schenkung an Ehegatten | Beginn ist der spätere von Leistung und Auflösung der Ehe; die Auflösung bleibt bis zur BG-12-Brücke Fallangabe | `p05` |
| § 2325 Abs. 3 Jahresgrenze | Der gleichzahlige Tag nach einem Jahr liegt im zweiten Fenster (neun Zehntel) | `p06` |
| § 2305 Zusatzpflichtteil | Differenz zwischen dem Wert des hinterlassenen Erbteils und der Hälfte des gesetzlichen Erbteils; einmal auf den Cent gerundet | `p07` |
| §§ 2306–2307 Ausschlagung | Ausschlagung eines beschränkten Erbteils oder eines Vermächtnisses eröffnet den Pflichtteilsanspruch | `p08` |
| § 2309 | Ein näherer Abkömmling schließt den entfernteren Berechtigten aus, wenn er Pflichtteil verlangt oder das Hinterlassene annimmt | `p08` |
| § 2317 | Anspruch entsteht mit dem Erbfall und ist vererblich sowie übertragbar | `p01` |

Familie `de.bgb.verfuegungen#pflichtteil-pilot`: 8 Szenarien; `p01` ist das
Beispiel der amtlichen Broschüre des BMJ „Erben und Vererben“ (Stand Juli
2025, S. 20; `corpus/laws/de/bgb/erbfolge/sources/bmj-erben-und-vererben/`):
Ehemann als Alleinerbe, Tochter, Nachlass 100.000 €, Pflichtteilsquote ¼,
Anspruch 25.000 €. Beide Auswerter, Differential byteweise.

## Rundung — Politik des Pakets, keine Norm (Ledger D-07)

Das Gesetz nennt keine Rundung, und `Money × Rational` ist nur bei
10-glattem Ergebnis exakt (E-0085). Das Paket rundet **einmal je Anspruch,
auf den Cent, kaufmännisch (HALF_UP), über den exakten Quotienten**:
`div_round(Wert × Zähler, Nenner, 2, "HALF_UP")`; Pflichtteil und
Ergänzungsanspruch sind getrennte Ansprüche und werden getrennt gerundet.
Die Quote selbst bleibt exakter Bruch. Zeuge der Rundung: `p02`
(100.000 € × 1/6 = 16.666,67 €).

## Was das Paket nicht tut und warum (Stand 18.09.2026, jede verbleibende Einheit mit Grund)

**SOURCE_ONLY (13 von 305) — vollständig verursacht, `analysis/saetze.json`:**

- **Zwölf `(weggefallen)`-Platzhalter ohne Normtext**: §§ 2230, 2260, 2261,
  2262, 2264, 2273, 2277, 2334, 2335 (Titel 7/Abschnitt 4/6),
  §§ 2360, 2364, 2369 (Erbschein, Verfahrensrecht 2015 ins FamFG
  übertragen). Bestätigt durch `sync_de_bgb_packages.py`: kein Fragment mit
  Normtext, nur der amtliche Platzhaltertitel. Das Paket führt keine
  `articles.json` mit `excluded`-Liste (§33.1-Kategorie `EXCLUDED`); das
  Anlegen einer solchen Liste nur für zwölf Platzhalter wurde als Aufwand/
  Risiko gegenüber dem Nutzen nicht für verhältnismäßig gehalten — sie
  bleiben `SOURCE_ONLY` mit Grund in diesem Absatz und in `saetze.json`.
- **§ 2254** „Der Widerruf erfolgt durch Testament“: strukturell bereits von
  JEDER Widerrufsregel des Pakets getragen (§§ 2253, 2255–2258 typisieren
  das widerrufende Instrument durchweg als `t: Testament` — es gibt im
  Modell keine andere Widerrufsform). Eine eigene Regel hätte keinen
  eigenständigen Inhalt (bestätigte Vorgänger-Grenze, siehe
  `abschnitt-diverse-2200-2228-2254-2166.law`).

**Fachliche Grenzen innerhalb formalisierter Paragraphen:**

- **§§ 2167, 2168, 2168a** (Gesamthypothek/-grundschuld): die Verpflichtung
  ist ein Anteil nach dem WERTVERHÄLTNIS zweier Grundstücke — ein Quotient
  zweier Money-Größen, nicht zweier ganzer Zahlen wie beim gesetzlichen
  Erbteil. `Money × Money` ist undefiniert; eine korrekte Umrechnung über
  Cent-Ganzzahlen (Rechenwache) wurde nicht geprüft. Bleiben QUALITATIV
  formalisiert (Pflicht besteht, Anteil als Fallangabe) — bewusste Grenze,
  keine riskante Näherung (D-16-01). § 2166 selbst (Vergleich zweier
  Geldbeträge, kein Quotient) ist dagegen vollständig formalisiert.
- **§ 2311 Abs. 2** Schätzung des Wertes (Kanal Sachverständiger/Gericht)
  und Feinheiten außerhalb der formalisierten Fälle in §§ 2327–2331 sind
  offen.
- **§ 2325 Abs. 2** Sonderregel für verbrauchbare Sachen ist noch nicht als
  eigener Gegenstandstyp ausdifferenziert (Wert kommt als Fallangabe).
- **§ 2332 Abs. 1, Abs. 2** (Verjährung): lokal berechnet
  (`verjaehrungsbeginn_anspruch_2329_2332`), NICHT an die gemeinsame Linie
  `de.bgb.fristen::sonderverjaehrung_beginn/_dauer` angeschlossen (Muster
  BG-05, Commit `1295d09bd9`, § 438) — Hemmung §§ 203–213 und Wirkung
  §§ 214–218 erreichen den Anspruch aus § 2329 daher nicht. Aufgabe in
  `TASKS.json` (D-16-05).

**Erledigt in dieser Fortsetzung (18.09.2026), vormals offen:**

- **§ 2316 Abs. 1 S. 1 ← Ausgleichung** `de.bgb.erbfolge` §§ 2050–2057a:
  gebrückt über das bereits `pub` vorhandene `rechnerischer_erbteil_2055`
  (D-16-02); die alte Fallangabe bleibt als zweiter Produzent bestehen.
- **§ 2276 Abs. 2** (Erbvertrag ↔ Ehevertragsform): bereits in einer
  früheren Sitzung dieser Fortsetzung gebrückt (`pub` bei `de.bgb.ehe`
  ergänzt).
- **§§ 2339, 2344** Erbunwürdigkeit, **§ 2346 ff.** Erbverzicht: vollständig
  formalisiert; die Brücke zum Wegfall-Prädikat bei `de.bgb.erbfolge` bleibt
  wie in `de.bgb.erbfolge`s eigenem README vorgesehen Fallangabe.
- Zeugenlücken: mit dieser Fortsetzung hat jede neue Präsumtion/Gegenausnahme
  Zeugen auf beiden Seiten (§§ 2166 Abs. 2, 2350, 2373, 2383 Abs. 2 u. a.).

## Prüfung (nur punktuell)

```sh
./law engine check corpus/laws/de/bgb/verfuegungen
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-16 --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-verfuegungen.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.verfuegungen#pflichtteil-pilot"
python3 corpus/run_kz_regression.py --only "de.bgb.verfuegungen#pflichtteil-pilot" --write-manifest
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.verfuegungen#pflichtteil-pilot"
```
