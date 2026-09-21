# Offene Fragen — `de.bgb.miete`

## § 540 Abs. 1 Satz 1 — Fenster der Position `Unterlassung540`

**Quelle.** `BGB_P540`: «Der Mieter ist ohne die Erlaubnis des Vermieters nicht berechtigt, den Gebrauch der Mietsache einem Dritten zu überlassen».

**Geschlossen.** `action` der Position ist die empirische Überlassung `gebrauch_einem_dritten_ueberlassen`, nicht die institutionelle Folge `gebrauchsueberlassung_ohne_erlaubnis_unzulaessig` (die schon aus `vermieter` folgt). Ohne Überlassung ist der Prohibitiv `ACTIVE`; mit Überlassung `VIOLATED` (E-0179).

**Grenze.** Das Positionsfenster bleibt `[beginn, infinity)`. `beendigung_am` schließt es nicht: nach Ende ohne Überlassung bleibt `Unterlassung540` in der Modellierung `ACTIVE`. Das ist nicht der Wortlaut des § 540 nach Beendigung (dann § 546), und nicht erfunden als Datum-Funktion. Eine zweite Regel oder ein unäres `mietverhaeltnis_beendet` wäre neue Form, nicht der Satz 1. Szenario «nach Ende» wartet deshalb `not VIOLATED`, nicht `not ACTIVE`.

**Closed.** The position `action` is the empirical letting to a third party, not the institutional “unzulässig” conclusion (already entailed by `vermieter`). Without letting, the prohibition is `ACTIVE`; with letting, `VIOLATED`.

**Boundary.** The window stays `[beginn, infinity)`. End of the lease does not close it; after end without letting the prohibition remains `ACTIVE` in this encoding. That is a positions-window limit, not a rewrite of § 540.
