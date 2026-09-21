# Ein Fall, drei Kodizes

Six registered dossiers, one claim. Accrual on 15 March 2010 or 15 March 2014;
the action is filed on 2 January 2016. Each living pattern is read by the BGB,
the Code civil, and chapter 10 of the UNIDROIT Principles, then by the shared
head `doctrine.ius_privatum::remedium_exclusum`.

The 2016 Principles enter into force on 10 May 2016 (`in_force` of
`PICC_2016_EN`). The PICC branch is therefore asked on 1 June 2016; expiry
and its assertion remain facts of article 10.9, not a count from the filing
day. The five-year and two-year patterns are the same as for the codes.

1. Five years. BGB: regular limitation entered on 31 December 2013 (§§ 195,
   199, 214). Code civil: the five-year period from knowledge ended on
   15 March 2015; the action on 2 January 2016 is time-barred (art. 2224,
   2229). PICC: expiry has been asserted (art. 10.9(2)). All three exclude
   the comparative remedy.
2. Two years. None of the three texts has yet taken the remedy: the BGB
   period ends on 31 December 2017 (asking whether it entered on
   31 December 2016 is NEITHER: the living Code names the day of entry, not
   the negation of another day — `so01`), the Code civil period on
   15 March 2019, and the Principles do not treat expiry as asserted.

`check.py` reads those outcomes from the paragraphs, then checks status,
applied rule, anchor, Rust/Python identity and replay.

From the checkout root:

```sh
./law engine lock corpus/laws/de/bgb/fristen/examples/ein-fall-drei-kodizes \
  --clir corpus/clir --plain-descriptors --write
python3 packs/examples/cases/materialize_deps.py \
  corpus/laws/de/bgb/fristen/examples/ein-fall-drei-kodizes --clir corpus/clir
python3 corpus/laws/de/bgb/fristen/examples/ein-fall-drei-kodizes/check.py \
  --out /tmp/p12
```
