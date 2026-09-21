# Verzugszinsen — worked cases

Five registered dossiers over `de.bgb.schuldrecht_at`. The collection keeps
the calculation deliberately narrow: the canon returns the annual rate and
the interest for one full year, including the €40 lump sum where applicable.

The page and the cases do not invent a day-count convention. **For a period
shorter than a full year, the BGB names no method for calculating the
interest; the model therefore returns no partial-year amount.** The
Bundesbank base rate is read on the case's `legal_time` and changes on
1 January and 1 July.

| Case | Facts | Result |
|---|---|---|
| `VerbraucherFuenfPunkte` | consumer transaction, €10,000, default from 1 June 2026 | 6.52% and €652.00 for one full year |
| `UnternehmerNeunPunkte` | remuneration claim between businesses, €5,000 | 10.52% and €526.00 for one full year |
| `PauschaleVierzigEuro` | the same business claim with €150.00 recovery costs | €40.00 lump sum; €110.00 remaining costs |
| `HalbjahrwechselBasiszinssatz` | base rate read at 1 July 2025 | 1.27% base, 6.27% consumer rate |
| `VerzugOhneMahnung` | performance date fixed by the calendar, no reminder | default starts on the fixed date |

The package declares `BGB_VERZUG_KALENDER` locally under §168.4. It does not
add a norm to `de.bgb.schuldrecht_at`, `de.bgb.fristen` or `de.bgb.core`.

