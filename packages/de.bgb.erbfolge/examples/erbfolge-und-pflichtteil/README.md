# Erbfolge und Pflichtteil

Eight registered dossiers. Statutory shares are exact fractions
(`gesetzlicher_erbteil`); their sum is one. The compulsory portion is money
(`pflichtteil`). The page does not partition the estate. The BMJ brochure
„Erben und Vererben“ (July 2025) is an external check for two files
(spouse with parents; daughter’s Pflichtteil) and is not reproduced.

1. First parentela with a Stamm: surviving spouse in Zugewinngemeinschaft,
   one living child, two grandchildren of a predeceased child
   (§ 1924 Abs. 3, § 1931, § 1371 Abs. 1) — 1/2, 1/4, 1/8, 1/8.
2. Spouse and both parents (BMJ example): spouse 3/4, each parent 1/8.
3. Gütertrennung with two children: equal thirds (§ 1931 Abs. 4).
4. Second parentela: surviving father 1/2; mother’s Stamm 1/2.
5. Disclaimer in time (§ 1953): the disclaimant’s child takes the Stamm.
6. Daughter excluded by will (BMJ example): Pflichtteil 25 000 € of a
   100 000 € estate.
7. Deprivation of the Pflichtteil (§ 2333) without a court finding —
   left to the court.
8. Disclaimer one day after the period: the inheritance is deemed accepted
   (§ 1943).

`check.py` reads those outcomes from the articles, then checks status,
applied rule, anchor, Rust/Python identity and replay.

From the checkout root:

```sh
./law engine lock corpus/laws/de/bgb/erbfolge/examples/erbfolge-und-pflichtteil \
  --clir corpus/clir --plain-descriptors --write
python3 packs/examples/cases/materialize_deps.py \
  corpus/laws/de/bgb/erbfolge/examples/erbfolge-und-pflichtteil --clir corpus/clir
python3 corpus/laws/de/bgb/erbfolge/examples/erbfolge-und-pflichtteil/check.py --out /tmp/p2
```
