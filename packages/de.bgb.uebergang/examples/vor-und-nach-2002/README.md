# Vor und nach 2002

Vier registrierte Fälle zum Verjährungskorridor des Art. 229 § 6 EGBGB:

1. Die neue, kürzere Frist läuft ab dem 1. Januar 2002.
2. Die längere alte Frist läuft trotzdem früher ab.
3. Ein Anspruch entsteht erst nach dem Stichtag und fällt nicht in den
   Korridor.
4. Die neue Frist ist länger; maßgeblich bleibt das frühere Ende nach altem
   Recht.

Das Paket importiert `de.bgb.uebergang` und `de.bgb.core`. Es erweitert den
Kanon nicht um Sachnormen. Alte Frist, alter Beginn und neue Frist sind
Eingaben des jeweiligen Falls; die Anwendung des Rechts vor 2002 ist damit
eine ausdrücklich benannte Grenze des Modells, keine Aussage, dass vor 2002
kein Recht galt.

Die Erwartungswerte stehen im Text der Fälle und werden von `check.py`
geprüft. Der Test umfasst Status, angewandte Regel, Quellenanker,
Rust/Python-Identität und Replay.

```sh
python3 corpus/laws/de/bgb/uebergang/examples/vor-und-nach-2002/check.py \
  --out /tmp/bgd-p4
```
