# Kündigung und Mieterhöhung

Six registered dossiers for the Mietrecht demo: the three notice-period
stages of § 573c, the third working day of the notice month, rent increases
within and beyond the § 558 capping limit, and late consent under § 558b.

The collection adds no norms to `de.bgb.miete`. Local authority labels belong
to the case-player story; the model leaves questions reserved for the court
open. The collection is not a legal advice tool.

Deadline policy `BGB_MIETE_KALENDER` is declared locally (§168.4). The BGB
calendar policies stay unexported. The calendar resource is the same snapshot
the canon uses: `urn:de:corpus:clir:bgb-fristen#KALENDER_BUNDESWEIT`.

From the checkout root:

```sh
./law engine lock corpus/laws/de/bgb/miete/examples/kuendigung-und-mieterhoehung \
  --clir corpus/clir --plain-descriptors --write \
  --calendar corpus/clir/de-bgb-fristen.lawir.json
python3 packs/examples/cases/materialize_deps.py \
  corpus/laws/de/bgb/miete/examples/kuendigung-und-mieterhoehung --clir corpus/clir
python3 corpus/laws/de/bgb/miete/examples/kuendigung-und-mieterhoehung/check.py
```
