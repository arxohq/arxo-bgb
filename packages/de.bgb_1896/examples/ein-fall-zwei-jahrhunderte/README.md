# Ein Fall, zwei Jahrhunderte

Five registered dossiers, one claim: four years against thirty, thirty-one
years against three, and a payment after limitation. Each living pattern is
read by the first edition of 1896 and — where the living Code speaks in
dates — by today’s BGB.

1. Four years. 1896: the regular period of thirty years is not completed
   (§ 195). Today: the claim arose on 15 March 2020; limitation entered on
   31 December 2023 (§§ 195, 199).
2. Thirty-one years. 1896: limitation is completed and the debtor may refuse
   (§ 222). Today: the claim arose on 15 March 1990; limitation entered on
   31 December 1993.
3. After thirty-one years a payment was made. 1896: what was rendered cannot
   be reclaimed (§ 222 (2)).

`check.py` reads those outcomes from the paragraphs, then checks status,
applied rule, anchor, Rust/Python identity and replay.

From the checkout root:

```sh
./law engine lock corpus/laws/de/bgb-1896/examples/ein-fall-zwei-jahrhunderte \
  --clir corpus/clir --plain-descriptors --write
python3 packs/examples/cases/materialize_deps.py \
  corpus/laws/de/bgb-1896/examples/ein-fall-zwei-jahrhunderte --clir corpus/clir
python3 corpus/laws/de/bgb-1896/examples/ein-fall-zwei-jahrhunderte/check.py \
  --out /tmp/p11
```
