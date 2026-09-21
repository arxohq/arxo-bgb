# de.bgb.erbfolge — BGB Buch 5, Abschnitte 1–2: Erbfolge, rechtliche Stellung des Erben

Paket BG-15 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Geltungsbereich §§ 1922–2063
(143 Paragraphen als Fragmente §194, `sources/de-bgb-erbfolge/`, generiert
aus dem Register DOKNR — nicht von Hand ändern). Importe: `de.bgb.core`
(Personen), `de.bgb.ehe` (Güterstand, § 1371 Abs. 1), `de.bgb.fristen`
(Kalender §85 für § 193), `calc.kinship` (Graph der Familie, DECISION-0217).
Richtung `erbfolge → ehe`, kein Rückimport.

## Stand: Abschnitte 1 und 2 vollständig (18.09.2026)

Tiefe §33.1: **EXECUTABLE 143 von 143** — aus jedem Paragraphen des
Geltungsbereichs wird etwas abgeleitet. 34 Szenarien in neun Familien,
beide Auswerter, Differential byteweise (128 `evaluate`-Aufrufe).

| Abschnitt / Titel | Normen | Familie |
|---|---|---|
| Abschnitt 1, Ordnungen 1–3, Ehegatte | §§ 1922–1926, 1930, 1931 Abs. 1 S. 1, Abs. 2–4, § 1371 Abs. 1 | `#erbfolge-pilot` |
| Abschnitt 1, Rest | § 1923 Abs. 2 Nasciturus, § 1927 mehrere Erbteile, §§ 1928–1929 vierte und fernere Ordnungen, § 1931 Abs. 1 S. 2, §§ 1932–1936, §§ 1937–1941 (nur Begriffe) | `#ordnungen-4-und-mehrfach`, `#ausschluss-und-wegfall` |
| Abschnitt 2 Titel 1 | §§ 1942–1966 Annahme, Ausschlagung, Anfechtung, Nachlasspflegschaft, Fiskus | `#annahme-ausschlagung` |
| Abschnitt 2 Titel 2 | §§ 1967–2017 Nachlassverbindlichkeiten, Aufgebot, Nachlassverwaltung, Inventar, aufschiebende Einreden | `#haftung-des-erben` |
| Abschnitt 2 Titel 3 | §§ 2018–2031 Erbschaftsanspruch | `#erbschaftsanspruch` |
| Abschnitt 2 Titel 4 | §§ 2032–2063 Erbengemeinschaft, Vorkaufsrecht, Verwaltung, Auseinandersetzung, Ausgleichung, Haftung der Miterben | `#erbengemeinschaft`, `#ausgleichung` |
| Korridor 2010 | EGBGB Art. 229 § 23 Abs. 4 über den Tag des Erbfalls | `#uebergang-2010` |

`e04` ist das Beispiel der amtlichen Broschüre des BMJ „Erben und Vererben“
(Stand Juli 2025, S. 17; `sources/bmj-erben-und-vererben/`, sha256 in
`PINS.sha256`): Ehefrau bei Zugewinngemeinschaft neben den Eltern ¾, Eltern
je ⅛. Kanarienvögel: `e08` („ein Erbe weniger“), `w01b` (ohne
Scheidungsantrag bleibt das Ehegattenerbrecht bestehen), `a01b` (einen Tag
nach dem Fristende gilt die Erbschaft als angenommen), `g03b` (eine Stimme
weniger erreicht die Mehrheit nicht).

## Brüche

Die Stammanteile entstehen nur durch Multiplikation, deshalb als Paar
ganzer Zahlen `(Zähler, Nenner)`; der exakte `Rational` folgt durch
Division. Kein kleinstes gemeinsames Vielfaches, keine Dezimalzahl.

Wer aus MEHREREN Gründen erbt — in verschiedenen Stämmen (§ 1927), als
Ehegatte und zugleich als Verwandter (§ 1934) oder als Ehegatte mit dem
Zuschlag des § 1931 Abs. 1 Satz 2 —, hält mehrere besondere Erbteile.
`gesetzlicher_erbteil_bruch` trägt `key(e, p)` und kann das nicht sagen,
deshalb führt das Paket zwei Schichten:

* `stammanteil_im_stamm(e, Stamm, p, Ordnung, z, n)` — der Anteil JE STAMM,
  mit dem Haupt des Stammes im Schlüssel; daraus `erbteil_aus_stamm`;
* `gesamterbteil_bruch(e, p, z, n)` — die SUMME der besonderen Erbteile
  über den gemeinsamen Nenner: `(z₁·n₂ + z₂·n₁, n₁·n₂)`.

Die Regeln des Piloten bleiben für den gewöhnlichen Fall unverändert; sie
sind mit `not_known(mehrfach_verwandt(e, p))` abgeschirmt, damit der Fall
des § 1927 keinen Schlüsselkonflikt auslöst (Ledger D-08, D-15-01).
Rechenwachen: `erbschaft_vollstaendig_verteilt` (Summe der
`gesetzlicher_erbteil`) und `nachlass_vollstaendig_verteilt` (Summe der
`gesamterbteil`, auch für §§ 1927, 1928, 1934).

## Wegfall

§ 1953 Abs. 2 sagt, die Erbschaft falle demjenigen an, „welcher berufen
sein würde, wenn der Ausschlagende zur Zeit des Erbfalls nicht gelebt
hätte“. Deshalb trägt das Paket EIN Prädikat `weggefallen` mit vier
Erzeugern — Vorversterben, Ausschlagung (§ 1953), Erbunwürdigkeit (§ 2344)
und Erbverzicht (§ 2346) —, und die Stämme lesen es statt `vorverstorben`.
Die letzten beiden sind Eingaben des Falls; ihre Normen stehen bei
`de.bgb.verfuegungen`. Der Ausschluss des Ehegattenerbrechts (§ 1933) geht
einen anderen Weg: er nimmt dem Ehegatten die Stellung als
`ueberlebender_ehegatte` und damit auch den Voraus (§ 1932).

## Fristen

Eine einzige Kalenderpolitik `BGB_ERBFOLGE_KALENDER` für das ganze Paket
(§ 168.2; Feldsatz wie `BGB_FRISTEN_KALENDER`: `same_day`, `include_end`,
`no_roll`, `month_end`). § 193 wird AUSDRÜCKLICH gerechnet
(`add_business_days(Ende, 1 business_day)`) bei den Fristen, innerhalb
derer eine Erklärung abzugeben oder ein Schriftstück einzureichen ist:
§§ 1944, 1954, 1996 Abs. 2, 1997, 2034 Abs. 2, 2061 Abs. 1. Die reinen
Zeitablauffristen (§ 1969 Dreißigster, § 1974 fünf Jahre, § 1981 Abs. 2
zwei Jahre, § 2031 Abs. 1 ein Jahr, § 2044 Abs. 2 dreißig Jahre, § 2014
drei Monate, § 2015 ein Jahr) rollen nicht. Der Kalenderknoten
`KALENDER_BUNDESWEIT` ist derselbe Datensatz wie bei `de.bgb.fristen` und
`de.bgb.ehe`; ein eigener Knoten ist nötig, damit die Achse `calendar` des
Falls eindeutig bleibt (AMBIGUOUS_CALENDAR), und jeder Fall wählt
`deadline_policy BGB_ERBFOLGE_KALENDER; calendar KALENDER_BUNDESWEIT;`.

Zwei Fristbeginne des § 1944 Abs. 2 (Kenntnis, Bekanntgabe der Verfügung):
der SPÄTERE gewinnt, ausgedrückt durch zwei Regeln mit Garde, nicht durch
`max`. Die Hemmung des Satzes 3 (§§ 206, 210 entsprechend) kommt als ZAHL
DER HEMMUNGSTAGE des Falls und wird über `with_unit` an das Ende gehängt;
`de.bgb.fristen::hemmung` ist an `Anspruch` geschlüsselt und passt auf die
Ausschlagungsfrist nicht (Ledger D-15-03).

## Rundung

Das Gesetz nennt keine Rundung. Das Paket rechnet Geld nur in Titel 4 und
rundet dort EINMAL je Miterbe und Anspruch, kaufmännisch auf den Cent:
`div_round(Betrag × Zähler, Nenner × 1.0, 2, "HALF_UP")` — § 2047 Abs. 1
(Überschuss), § 2055 Abs. 1 (Ausgleichungsmasse), § 2056 Satz 1
(Mehrempfang). Den RESTCENT verteilt das Paket NICHT: § 2047 Abs. 1 sagt
nur „nach dem Verhältnis der Erbteile“ und nennt kein Verfahren für den
Rest. Die Rechenwache `ueberschuss_vollstaendig_verteilt` feuert dann
nicht, und der Fall zeigt die Lücke, statt sie zu verbergen (Ledger
D-15-02). §§ 1990, 1973 rechnen nicht, sie VERGLEICHEN Money.

## Wertungen

Drei Kanäle nach DECISION-0194, jeder durch den Text des Paragraphen
bestimmt. Urteil des Gerichts (§47.3): „unverzüglich“ § 1980 Abs. 1
(Wertungsmerkmal, KEIN Nullfristbeginn), „angemessene Vergütung“ § 1987,
„erhebliche Unvollständigkeit … absichtlich“ § 2005 Abs. 1, „mit der
erforderlichen Sorgfalt“ § 2028 Abs. 2, „Gefährdung“ § 1981 Abs. 2,
„angemessener Unterhalt“ § 1963, „zur Führung eines angemessenen
Haushalts benötigt“ § 1932 Abs. 1 S. 2, „übermäßig“ § 2050 Abs. 2,
„offenbar unbillig“ § 2048 S. 3, „Billigkeit“ § 2057a Abs. 3,
„Voraussetzungen der Scheidung“ § 1933 S. 1. Festgestellte Tatsache
(`origin adjudicated`): Anordnung der Nachlassverwaltung, Eröffnung des
Nachlassinsolvenzverfahrens, Bestellung des Pflegers und des Verwalters,
Ausschluss im Aufgebotsverfahren, Dauer der Inventarfrist, Feststellung
des § 1964. Vermutungen (`presumption … unless`): § 1949 Abs. 2, § 1964
Abs. 2, § 2009, § 2049 Abs. 1, § 2051 Abs. 2, § 2052.

## Korridor 2010

EGBGB Art. 229 § 23 Abs. 4: für Erbfälle VOR dem 1. Januar 2010 gilt das
BGB in der vor diesem Tag geltenden Fassung. Connecting factor ist der Tag
des Erbfalls (`erbfall_am`), und der Fall weist die Fassung aus
(`alte_fassung_vor_2010_anwendbar` / `neue_fassung_ab_2010_anwendbar`).
Die alte Fassung selbst ist in diesem Paket NICHT festgeschrieben —
`sources.law` trägt allein die konsolidierte Fassung auf den 17.09.2026 —,
deshalb rechnet das Paket sie nicht: § 2057a bleibt bei einem Erbfall vor
2010 stumm. Zeugenpaar `t01` / `t02`.

## Was das Paket nicht tut und warum

- **Verfahrensrecht**: Aufgebotsverfahren (ZPO/FamFG), Nachlassinsolvenz
  (InsO), Todeserklärung (VerschG), Beurkundung (BeurkG) — Eingänge und
  festgestellte Tatsachen, keine Normen (`SOURCES.json.external`).
- **Verweisungen in fremde Bücher**: §§ 406–408, 743/745/746/748,
  749–758, 812 ff., 823 ff., 987 ff., 1000–1003, 259–261, 1569–1586b.
  Das Paket stellt fest, WELCHES Regime gilt; die Rechtsfolge bleibt bei
  BG-04, BG-09, BG-10 und BG-13.
- **§ 1927 mit drei und mehr Stämmen**: die Summe ist für zwei Stämme
  ausbuchstabiert; drei Stämme brauchen eine Kette und sind `TODO`.
- **§ 1931 Abs. 1 Satz 2 bei ungleichen Stammanteilen**: der Zuschlag wird
  als Vielfaches EINES Anteils gebildet und verlangt, dass alle nur durch
  Abkömmlinge besetzten Großelternstämme denselben Anteil tragen; sonst
  feuert die Regel nicht und die Rechenwache zeigt die Lücke.
- **Adoption**: Politik „ersetzt“ (§ 1755, Minderjährigenannahme); die
  Annahme Volljähriger (§ 1770) fügt hinzu und braucht im Rechner einen
  Modus `AddsBranch`, den `calc.kinship` nicht kennt (Ledger D-15-05).
- **Erbunwürdigkeit (§§ 2339–2345) und Erbverzicht (§§ 2346–2352)**:
  Normen bei `de.bgb.verfuegungen`; hier nur als Wegfallgrund-Eingang.

Der Erblasser selbst wird im Graphen als Kind seiner Eltern geführt; da er
weder `lebt_beim_erbfall` noch `weggefallen` trägt, ist sein Knoten in den
Ordnungen 2 und 3 ein unbesetzter Endknoten.

## Prüfung (nur punktuell)

```sh
./law engine check corpus/laws/de/bgb/erbfolge
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-15 --check
python3 corpus/laws/de/bgb/fristen/tools/gen_kalender.py --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-erbfolge.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.erbfolge#erbfolge-pilot"
python3 corpus/run_kz_regression.py --only "de.bgb.erbfolge#erbfolge-pilot" --write-manifest
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.erbfolge#erbfolge-pilot"
```
