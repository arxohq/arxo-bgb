# de.bgb.uebergang — EGBGB Art. 229: Überleitungsvorschriften der BGB-Reformen

Paket BG-17 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Es hält nur Quellen,
Anknüpfungsmomente und Übergangsregeln; die Sachnormen bleiben in den
Fachpaketen. Einheiten: Paragraphen des Art. 229 EGBGB, gepinnt aus dem
bgbeg-Snapshot von gesetze-im-internet.de (Register `DOKNR-bgbeg.json`,
Auswahl `egbgb` in `PACKAGES.json`: §§ 5, 6, 23; die Liste wächst mit den
Korridoren der Pakete). Importe: `de.bgb.core`, `de.bgb.fristen`.

## Stand: Welle B2, erster Schnitt (17.09.2026) — Verjährungskorridor 2002

| Norm | Form | Zeugen |
|---|---|---|
| Art. 229 § 6 Abs. 1 Satz 1 — neue Verjährungsvorschriften für am 1.1.2002 bestehende, nicht verjährte Ansprüche | `anspruch_am_stichtag_bestehend`, `alte_frist_ende`, `korridor_2002_anwendbar` | `u01`–`u04` |
| § 6 Abs. 1 Satz 2 — Beginn vor 2002 nach altem Recht | Eingabe `alte_verjaehrung_begann_am` | alle |
| § 6 Abs. 3 — neue Frist länger: alte Frist maßgeblich | `neue_frist_laenger` → `verjaehrung_vollendet_am` | `u04` |
| § 6 Abs. 4 Satz 1 — kürzere neue Frist vom 1.1.2002 an | `neue_frist_ende_ab_stichtag` (Stichtag mitgerechnet, Vortag des entsprechenden Tages) | `u01` |
| § 6 Abs. 4 Satz 2 — längere alte Frist läuft früher ab | `VollendungMitFrueherAblaufenderAlterFrist` | `u02` |
| gleich lange Fristen | `fristen_gleich_lang` → altes Ende | — (Zeuge B2) |

Familie `de.bgb.uebergang#verjaehrung-2002`: 4 Szenarien, Erwartungen von
Hand aus dem Text, beide Auswerter, Differential byteweise.

## Was das Paket nicht tut und warum (Welle B2 — `TODO`, keine Grenze)

- **Alte und neue Frist sind Eingaben.** Die alte Frist steht im BGB der
  Fassung bis 2001 (z. B. § 195 a.F. dreißig Jahre — Text im Denkmal
  `de.bgb_1896`, Fragment `BGB_P195`); die neue kommt in B2 aus
  `de.bgb.fristen` (§§ 195–197). Der Beginn nach altem Recht (§ 198, § 201
  a.F.) ist ebenfalls Eingabe.
- **Lesart des BGH** zum Beginn der kürzeren Frist (subjektive
  Voraussetzungen des § 199 Abs. 1 auch im Korridor, Ultimo): in B2 als
  Interpretation §152 (`any_of`); der Pilot rechnet vom 1.1.2002 als
  Beginnfrist (§ 187 Abs. 2) — bei Kenntnis bis 2002 ist das Ergebnis
  dasselbe (31.12.2004).
- **§ 6 Abs. 1 Satz 3, Abs. 2** (Unterbrechung/Hemmung vor 2002),
  **Abs. 5–6**, **§ 5** (allgemeine Überleitung, Dauerschuldverhältnisse),
  **§ 23** (Reform 2010: Erbfälle, Verjährung erbrechtlicher Ansprüche) —
  gepinnt, Regeln folgen mit den Paketen, deren Materie sie steuern.

## Prüfung (nur punktuell)

```sh
./law engine check corpus/laws/de/bgb/uebergang
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-17 --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-uebergang.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-corpus.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.uebergang#verjaehrung-2002"
```
