# de.bgb.core — Bürgerliches Gesetzbuch: Nabe der Pakete de.bgb.*

Paket BG-01 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Die Nabe pinnt keinen
Paragraphen: jeder § liegt genau einmal im Fachpaket, dem sein Bereich gehört
(`docs/foundations/de-bgb/PACKAGES.json`). Sie erklärt die Typen, die mehrere
Pakete teilen, damit ein Anspruch in `fristen`, `kauf` und `erbfolge` dieselbe
Sache ist.

## Eingefrorene API (17.09.2026, nach dem Pilot B1)

| Deklaration | Zweck |
|---|---|
| `Person : Actor`, `NatuerlichePerson : Person`, `JuristischePerson : Person` | jedes Rechtssubjekt; `Actor` für `has_role` §43 und `calc.kinship` |
| `Sache`, `Tier` | § 90, § 90a — `Tier` ist kein Untertyp von `Sache`; die entsprechende Anwendung erklärt `de.bgb.allgemeiner_teil` |
| `Schuldverhaeltnis`, `schuldverhaeltnis_glaeubiger`, `schuldverhaeltnis_schuldner` | § 241: wer von wem eine Leistung fordern kann |
| `Anspruch`, `anspruch_aus_schuldverhaeltnis`, `anspruchsinhaber`, `anspruchsgegner`, `anspruch_geldbetrag`, `anspruch_entstanden_am` | § 194 Abs. 1: eigener Träger des Anspruchs mit Grund, Parteien und Entstehungstag (§ 199, § 200); kein Untertyp von `calc.obligations::Position` |
| `Gericht` (enum) | vom Text benannte Gerichte und Behörden für Tatsachen mit `origin adjudicated` |

Die API ist seit dem Pilot B1 (`de.bgb.fristen`, `de.bgb.ehe`,
`de.bgb.erbfolge`, `de.bgb.verfuegungen` — 34 Szenarien, beide Auswerter)
**eingefroren**. Jede Änderung der Nabe senkt alle Importeure und ihre Locks
neu ab und läuft ausschließlich über den Koordinator
(`docs/foundations/de-bgb/PARALLEL.md`, Eintrag in `DECISIONS.md`). Ein
Paket, das einen fehlenden Typ braucht, erklärt ihn bei sich (`pub`) und
meldet ihn in `DECISIONS.md`; Aliase in den Fachpaketen:
`type Person = de.bgb.core::Person;`, `type Anspruch = de.bgb.core::Anspruch;`.

## Vertrag der Urteilsanfrage (DECISION-0194)

Das BGB überlässt Wertungen dem Gericht; jedes Paket erklärt sie **pro
Paragraph**, nie in einem gemeinsamen Katalog:

```law
@source(BGB_P254)
pub external judgment relation mitverschulden_anteil(s: Schaden, p: Person, anteil: Rational) {
    authority Court;
    label de official "Mitwirkendes Verschulden des Beschädigten: Verpflichtung zum Ersatz und Umfang hängen von den Umständen ab (§ 254 Abs. 1)";
    label en unofficial "contributory fault of the injured party: liability and its extent depend on the circumstances (§ 254 (1))";
}
```

Drei Kanäle, gewählt nach dem Text der Norm:

- der Text **delegiert eine Wertung** (gute Sitten § 138, Treu und Glauben
  § 242, Mitverschulden § 254, angemessene Frist, Kindeswohl, grobe
  Fahrlässigkeit § 199 Abs. 1 Nr. 2) → `external judgment relation … { authority Court; }`;
  ohne Antwort `REQUIRES_JUDGMENT`, die Antwort ist `adjudicated`;
- der Text **verlangt eine festgestellte Tatsache** (Kenntnis und ihr Tag
  § 199 Abs. 1 Nr. 2, Scheidungsurteil, Eintragung im Grundbuch, Erbschein)
  → `relation … kind empirical`, im Fall mit `origin adjudicated`
  (Beispiel: `de.bgb.fristen::kenntnis_erlangt_am`);
- die **Lesarten gehen auseinander** (§§ 133, 157) →
  `interpretation … of <Fragment> { status disputed; }` in einer Gruppe
  `any_of` (§152); `exactly_one` würde jede abhängige Frage ausschalten.

Eine Fallaussage, die die rechtliche Schlussfolgerung nachspricht („der
Anspruch ist verjährt“), ist verboten: der Lint
`evaluative-fact-without-producer` weist sie zurück.

## Sprache

In `.law`, `.lawtest`, Kommentaren, `label` und README der Pakete `de.bgb.*`
nur Deutsch und Englisch (DECISION-0319, Р7): `label de official` trägt
Normtext oder Bezeichnung, `label en unofficial` die Übersetzung.

## Prüfung

```sh
./law engine check corpus/laws/de/bgb/core
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-core.lawir.json
```
