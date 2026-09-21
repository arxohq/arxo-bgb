# Fristenrechner — worked cases

Eight registered dossiers over `de.bgb.fristen`. The page does not add
days: the canon answers `frist_ende`, `verjaehrung_eingetreten_am`,
`hoechstfrist_ende` and `lebensjahr_vollendet_am`. Each case asks the day
that follows from the text and a neighbouring day that does not.

Day-count files (`Ereignisfrist14`, `Samstag193`) declare `BGB_FRISTEN_TAG`.
The live calculator carries `BGB_FRISTEN_KALENDER` (month-end, year-end,
Höchstfrist, age). Mixing both policies in one live world would be wrong.

| Case | Facts | Day | Why |
|---|---|---|---|
| `Ereignisfrist14` | event 6 Mar 2026, 14 days, TAG | **20 Mar 2026** | § 187 (1), § 188 (1); weekday, no roll |
| `Samstag193` | event 7 Mar 2026, 14 days, TAG | **23 Mar 2026** | end Saturday → Monday (§ 193 roll of TAG) |
| `UltimoMonatsfrist` | event 31 Jan 2026, one month | **2 Mar 2026** | 28 Feb missing; Saturday → Monday (§ 188 (3), § 193) |
| `VerjaehrungUltimo` | arose and known 15 Mar 2020 | **31 Dec 2023** | three years from year-end 2020 (§§ 195, 199 (1)) |
| `Verhandlungen203` | talks 1–15 Nov 2023 | **15 Feb 2024** | three-month floor after suspension (§ 203 sentence 2) |
| `Klageerhebung204` | action 1 Mar–30 Apr 2022 | **1 Mar 2024** | suspension by prosecution of rights (§ 204 (1) no. 1, § 209) |
| `HoechstfristKoerper` | bodily harm 1 May 2010 | **1 May 2040** | thirty years from commission (§ 199 (2)) |
| `LebensjahrSchalt` | born 29 Feb 2000, 25th year | **27 Feb 2025** | day before the corresponding birthday; 29 Feb 2025 missing |

`check.py` takes those days from the articles, then checks status, applied
rule, anchor, Rust/Python identity and replay.

From the checkout root:

```sh
./law engine lock corpus/laws/de/bgb/fristen/examples/fristenrechner \
  --clir corpus/clir --plain-descriptors --write \
  --calendar corpus/clir/de-bgb-fristen.lawir.json
python3 packs/examples/cases/materialize_deps.py \
  corpus/laws/de/bgb/fristen/examples/fristenrechner --clir corpus/clir
python3 corpus/laws/de/bgb/fristen/examples/fristenrechner/check.py
```
