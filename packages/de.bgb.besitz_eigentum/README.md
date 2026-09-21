# de.bgb.besitz_eigentum — BGB Buch 3, Abschnitte 1–3: Besitz, Rechte an Grundstücken, Eigentum

Paket BG-10 der vollständigen Formalisierung des geltenden BGB
(`docs/foundations/de-bgb/`, DECISION-0319). Geltungsbereich §§ 854–1017:
161 geltende Paragraphen mit 261 Absätzen und eine Bereichsposition
(§§ 1012–1017, mit dem Erbbaurecht weggefallen), als Fragmente §194 in
`sources/de-bgb-besitz-eigentum/` gepinnt — generiert aus dem Register DOKNR,
nicht von Hand ändern. Importe: `de.bgb.core` (Personen, Sachen, Anspruch) und
`de.bgb.fristen` (Berechnung aller Fristen, DECISION-0319 Р4). Richtung
`besitz_eigentum → fristen → core`, kein Rückimport. `Besitz`, `Eigentum`
(als `eigentuemer`/`eigentum_erworben`), `Grundstueck` und `Recht` sind `pub`
und stehen dem Paket BG-11 (`dingliche_rechte`) zur Verfügung.

## Stand (18.09.2026): dritter Anlauf — materielles Grundbuchrecht und Drittrechte nachgeholt

| Maß | Wert |
|---|---|
| Paragraphen im Geltungsbereich | 161 (Stand 2026-09-17) |
| EXECUTABLE §33.1 | 139 |
| SOURCE_ONLY §33.1 | 22 |
| Absätze mit Regeln (`analysis/saetze.json`) | 204 EXECUTED, 12 BOUNDARY, 45 TODO von 261 |
| Regeln im CLIR | 369 |
| Szenarien (zwölf Familien) | 115, beide Auswerter, Differential (alle Runden zusammen: 237 evaluate-Aufrufe byteweise) |

**Dritter Anlauf (18.09.2026):** der Koordinator wies zurück, dass §§ 874,
877, 880–882, 885, 887, 890, 895–897 fälschlich als reine GBO-Prozedur
(Grund `gbo`) galten, obwohl sie materielle Rechtsfolgen regeln (Rangfolge,
Vormerkung, Berichtigung); ebenso lagen §§ 949, 950 Abs. 2, 952 fälschlich
als „BG-11/BG-04-Territorium“, obwohl sie im Geltungsbereich dieses Pakets
liegen und nur lokale Fakteneingaben (`recht_dritter_an_sache`,
`glaeubiger_der_forderung`) brauchen, keine fremde Entität. Beide Einschätzungen
waren falsch und sind revidiert (D-10-13). Zusätzlich: § 1003 Abs. 1/Abs. 2
im selben Fall (`NEITHER`-Fehler behoben durch phasengetrennte, positive
Prämissen mit `not_known(...)` statt eines gemeinsamen Ausschluss-Kopfes),
§ 974 (wiederverwendet dieselbe Technik), § 976 Abs. 2 (zweiter
Ausschlussgrund plus Gemeinde-Erwerb, wie Abs. 1), § 955 Abs. 3 und
§ 926 Abs. 2 (beide durch Wiederverwendung bestehender Mechanik erfüllt,
kein neuer Kopf nötig). Ein latenter Fehler im bereits vor dieser Sitzung
EXECUTED § 950 Abs. 1 wurde beim Erstzugriff sichtbar (REQUIRES_JUDGMENT
durch geteilten Tatbestand mit der Wertungsregel, dasselbe Muster wie
§ 997 Abs. 2) und ohne Änderung des bestehenden `pub` der Wertungsrelation
behoben.

**Welle B6 (18.09.2026, Aufgabe V3-BG-10-08), Block 1 von 4:** §§ 966–970, 975,
977, 978 Abs. 3 Fund vollständig geschnitten — Verwahrungs- und
Ablieferungspflicht, beschränkter Haftungsmaßstab, Befreiung durch Herausgabe,
Aufwendungsersatz, Rechte nach Ablieferung, Bereicherungsanspruch mit eigener
Dreijahres-Klagefrist (§ 977) und Finderlohn gegen den nach § 981 Abs. 1
Berechtigten mit einer weiteren, unabhängigen Dreijahresfrist (§ 978 Abs. 3).
Anschließend §§ 991–999, 1003 des Eigentümer-Besitzer-Verhältnisses — Haftung
des Besitzmittlers (§ 991) und des deliktischen Besitzers (§ 992), Übermaß­
früchte des redlichen Besitzers (§ 993 Abs. 1), Lasten als notwendige
Verwendungen (§ 995), Wegnahmerecht mit drei Ausschlussgründen (§ 997),
Bestellungskosten (§ 998), Rechtsnachfolge in den Verwendungsersatz (§ 999),
Befriedigungsrecht des Besitzers (§ 1003; die Fristlänge ist eine Angabe des
Besitzers, kein Urteilskanal, D-10-09). Damit revidiert: § 972 (Zurück­
behaltungsrecht des Finders) und § 976 Abs. 1 (Eigentumsübergang auf die
Gemeinde bei Verzicht) sind jetzt EXECUTED statt Grenze — „gilt entsprechend“
liest denselben Kopf (§ 972 → `verwendungsersatzanspruch`), zwei sich
gegenseitig ausschließende Produzenten lösen § 976 Abs. 1 ohne Konflikt (D-10-09).
§§ 972 Abs. 2-Zusammenspiel mit § 1003 (beide Wege in einem Fall), § 974,
§ 976 Abs. 2 und §§ 979–983 bleiben Grenzen mit Grund (`analysis/saetze.json`,
Status `BOUNDARY`) — siehe „Was das Paket nicht tut und warum“.

**Block 2:** § 948 Vermischung (Brücke zu § 947), § 951 Abs. 2 Satz 2
(Wegnahmerecht auch ohne Besitz der Hauptsache), §§ 954–957 Erzeugniserwerb
(dinglich Berechtigter, gutgläubiger Eigenbesitzer, Gestattung mit und ohne
Berechtigung) — die Rangfrage § 953 vs. §§ 954–957 trennt eine ausdrückliche
Falleingabe (D-10-10). §§ 949, 950 Abs. 2, 952 bleiben Grenzen: Drittrechte-
und Forderungskonzepte, die dieses Paket nicht führt (BG-11/BG-04-Territorium).

**Block 3:** §§ 884, 886 (Vormerkung: Erbenhaftung, Beseitigungsanspruch),
§ 893 („gilt entsprechend“ § 892), § 926 Abs. 1 (Zubehör-Erwerb als
widerlegliche Vermutung „im Zweifel“, eigener Kopf `eigentum_durch_zubehoerregel_erworben`
— eine Direktschreibung auf den Sammelkopf `eigentum_erworben` löste zunächst
REQUIRES_JUDGMENT aus, D-10-11). § 889 erfüllt sich durch Abwesenheit einer
konsolidationsbedingten Erlöschensregel, keine eigene Regel nötig. § 926
Abs. 2 (gutgläubiger Erwerb von Zubehör nach §§ 932–936) bleibt Grenze.

**Block 4:** § 920 Grenzverwirrung — drei Regeln nach dem Text selbst
(Besitzstand maßgebend, sonst gleich großes Stück, Billigkeitskorrektur im
Urteilskanal §47.3), eigene Entität `Grenzstreit`, kein Flächenmodell nötig
(D-10-12; revidiert die ursprüngliche Einschätzung „ohne Flächenmodell bleibt
sie SOURCE_ONLY“).

Verbleibend `TODO` ohne Grenze: §§ 929a, 932a (Schiffe — eigenständiges
Subsystem, Schiffsregister). Verbleibend Grenze mit Grund `gbo`: der
überwiegend verfahrensrechtliche Rest des Grundbuchrechts (§§ 874, 877,
880–882, 885, 887, 890, 895–897) — `docs/foundations/de-bgb/TASKS.json`,
Aufgabe `V3-BG-10-08` (Handoff unten).

## Aufgabenkarte

| Norm | Form | Zeugen |
|---|---|---|
| § 854 Abs. 1, 2 Besitzerwerb; § 855 Besitzdiener | zwei ausdrückliche Eingaben („für sich“ / „weisungsgebunden“), keine Verneinung durch Schweigen | `b01`, `b05` |
| § 856 Beendigung, § 857 Erbe, § 865 Teilbesitz, § 866 Mitbesitz | Regeln über die Besitzlage; § 856 Abs. 2 als Defeater | `b01`, `b05` |
| § 858 verbotene Eigenmacht, Fehlerhaftigkeit und ihre Fortwirkung | `keine_gesetzliche_gestattung` als Eingabe; Nachfolge über `monotone` | `b01`, `b02` |
| § 859 Selbsthilfe (Abs. 1–3) | Abs. 3 „sofort“ im Urteilskanal §47.3 | `b08`, `b09` |
| §§ 861, 862 Besitzschutzansprüche mit dem Ausschluss des letzten Jahres | Jahresfrist §§ 187 Abs. 1, 188 Abs. 2; beide Seiten des Grenztags | `b03`, `b04` |
| § 863 petitorische Einwendung | eigenes Prädikat; die Anspruchsregeln lesen das Recht zum Besitz nicht | `b10` |
| § 864 Erlöschen nach einem Jahr | Frist aus `de.bgb.fristen` mit der Verlegung des § 193 | `b06`, `b07` |
| §§ 868, 870, 871 mittelbarer Besitz | mehrstufig über `monotone(mittelbarer_besitzer)` | `b11` |
| §§ 873–878 Erwerb, Bezugnahme, Aufhebung, Bindung, Rechtsänderungen | vier Bindungsformen des Abs. 2 als vier Regeln; § 874 Bezugnahme als Defeater; § 877 durch generische Formulierung bereits erfüllt | `g01`, `gb06` |
| §§ 879–882 Rangverhältnis, Rangänderung, Rangvorbehalt, Höchstbetrag | Reihenfolge/Tag/gleicher Rang; § 880 vier Regeln inkl. Zwischenrecht; § 881 Vorrang mit begrenzter Wirkung bei Zwischenbelastung | `g05`, `gb07`–`gb10`, `gb18` |
| §§ 883, 884, 886–888 Vormerkung | relative Unwirksamkeit, Erbenhaftung, Beseitigungs-, Zustimmungs- und Voraussetzungsanspruch, Aufgebotsverfahren | `gb01`, `gb02`, `gb11`, `gb12` |
| § 890 Vereinigung/Zuschreibung, §§ 895–897 Berichtigung | Eintragung als Tatbestand; § 897 defeasibel mit Kanarei | `gb13`–`gb17` |
| § 893 Rechtsgeschäft mit dem Eingetragenen | „gilt entsprechend“ § 892 — ein Kopf, keine zweite Regelkette | `gb03` |
| § 926 Zubehör des Grundstücks | Abs. 1 Vermutung „im Zweifel“ (presume/unless); Abs. 2 durch Wiederverwendung der §§ 929–934-Kette erfüllt | `gb04`, `gb05` |
| §§ 891, 894, 898, 899 Vermutung und Berichtigung | `presumption` mit beiden Seiten | `g01`, `g02` |
| § 892 öffentlicher Glaube | widerlegliche Regel; Widerspruch und Kenntnis als strikte Angriffe; Abs. 2 maßgebende Zeit | `g03`, `g04` |
| § 900 Buchersitzung | dreißig Jahre, Hemmung durch eingetragenen Widerspruch (§ 209 entsprechend) | `g06`, `g07` |
| §§ 903–909 Inhalt des Eigentums, Notstand, Anlagen, Vertiefung | § 904 mit zwei Urteilskanälen | `n01`, `n02` |
| § 906 Immissionen | Regelvermutung der Grenzwerte (Abs. 1 Satz 2) und vier Wertungen des Gerichts | `n03`, `n04`, `n05` |
| §§ 910, 911 Überhang und Überfall | „angemessene Frist“ im Urteilskanal | — |
| §§ 912, 913 Überbau und Rente | zwei Defeater: Verschulden und „sofort … Widerspruch“ | `n06`, `n07` |
| §§ 917, 918 Notweg | Duldungspflicht, Rente, Ausschluss bei willkürlicher Handlung | — |
| §§ 919, 921, 922, 923 Grenze, Grenzanlagen, Grenzbaum | „zu gleichen Teilen“ als Paar ganzer Zahlen | `n08` |
| § 920 Grenzverwirrung | drei Regeln: Besitzstand, gleich großes Stück, Billigkeit im Urteilskanal | `n09`–`n11` |
| §§ 925, 928 Auflassung, Aufgabe, Fiskus | Bedingung und Zeitbestimmung als Defeater | — |
| §§ 929–931 Übereignung und ihre Surrogate | ein Tatbestand, drei Wege | `e01` |
| §§ 932–936 gutgläubiger Erwerb | Kenntnis als Tatsache, grobe Fahrlässigkeit als Wertung; § 935 mit der Ausnahme des Abs. 2 | `e02`–`e06` |
| §§ 937–944 Ersitzung | zehn Jahre, Hemmung, Unterbrechung, § 938 Vermutung, §§ 943, 944 Anrechnung | `r01`–`r05` |
| §§ 946–951 Verbindung, Verarbeitung, Vergütung | Wertverhältnis als Bruch; „erheblich geringer“ im Urteilskanal (Wertungs-Defeater ohne geteilten Tatbestand, D-10-13); § 948 Vermischung als Brücke zu § 947; § 951 Abs. 2 Satz 2 zweite Quelle des Wegnahmerechts | `vk01`–`vk03` |
| §§ 953–957 Erzeugniserwerb | Rangfolge § 953 vs. §§ 954–957 als Falleingabe (D-10-10); § 955 gutgläubiger Eigenbesitzer mit Ausschluss, Abs. 3 durch Abwesenheit einer Unterbrechungsregel erfüllt; §§ 956/957 Gestattung mit gutem Glauben als Voraussetzung | `vk04`–`vk09` |
| §§ 949, 950 Abs. 2, 952 Rechte Dritter, Eigentum an Schuldurkunden | lokale Eingaben (`recht_dritter_an_sache`, `glaeubiger_der_forderung`), keine BG-11-Entität (D-10-13) | `rd01`–`rd05` |
| §§ 958–963 Aneignung | „unverzüglich verfolgt“ im Urteilskanal; § 963 Anteile nach der Zahl der Schwärme | — |
| §§ 965–984 Fund | Schwellen 10 €, 50 €, 500 €; Staffel 5/3 %; sechs Monate; Schatz je zur Hälfte; §§ 966–970, 975 Verwahrung/Ablieferung/Haftung/Befreiung/Aufwendungen; §§ 977, 978 Abs. 3 je eine eigene Dreijahres-Klagefrist | `f01`–`f17` |
| §§ 985–1002 Herausgabe und Eigentümer-Besitzer-Verhältnis | Rechtshängigkeit und Kenntnis als Tatsachen; § 1002 als Klagefrist | `h01`–`h04`, `h08` |
| §§ 991–999, 1003 Besitzmittler, deliktischer/redlicher Besitzer, Lasten, Wegnahmerecht, Rechtsnachfolge, Befriedigungsrecht | Zwei alt-Regeln (§ 991 Abs. 1); "gilt entsprechend" als ein Prädikat (§ 995 Satz 2, § 972); Fakteneingabe statt Rückbezug bei § 999 (LDC-E4102); § 1003 Abs. 1/2 phasengetrennt mit `not_known` (D-10-13) | `eb01`–`eb13` |
| § 974 Eigentumserwerb nach Verschweigung, § 976 Abs. 2 Übergang auf die Gemeinde | wiederverwenden dieselbe `not_known`-Technik wie § 1003 bzw. § 976 Abs. 1 | `f20`–`f22` |
| § 1004 Beseitigung und Unterlassung | Abs. 2 gespeist aus den Duldungspflichten der §§ 904, 906 | `h05`, `h06` |
| §§ 1006, 1007 Vermutung und Ansprüche des früheren Besitzers | Vermutung mit der Grenze des Abs. 1 Satz 2 | `h01`, `h07` |
| §§ 1008, 1011 Miteigentum | Quote als exakter Bruch; Ansprüche jedes Miteigentümers | `f11`, `n08` |

## Fristen

Alle Fristen rechnet `de.bgb.fristen` (DECISION-0319 Р4); dieses Paket nennt
Ereignis und Länge und liest das Ende. **Erwerbsfristen** (§ 900 dreißig Jahre,
§ 937 zehn Jahre, § 973 sechs Monate) lesen `frist_ende_kalender` — die
Verlegung des § 193 gehört zu ihnen nicht; **Klagefristen** (§ 864 ein Jahr,
§ 977 Satz 2 und § 978 Abs. 3 Satz 2 je drei Jahre — zwei unabhängige Fristen
mit eigenem Beginn, D-10-08 —, § 1002 ein Monat / sechs Monate) lesen
`frist_ende` mit der Verlegung. Der
Unterschied ist an zwei Zeugen sichtbar: `g06` endet an einem Sonntag
(15. Juni 2025) und bleibt dort, `b06` und `h03` werden vom Sonntag auf den
Montag verlegt. Zeilenweise Rechenschaft: `docs/foundations/de-bgb/DEADLINES.json`,
Abschnitt `BG-10`. Die Politik des Falls ist `BGB_BESITZ_EIGENTUM_KALENDER`
(eine Politik je Fall, §168.2).

## Rundung

Das Gesetz nennt keine Rundung. Der Finderlohn (§ 971 Abs. 1 Satz 2, § 978
Abs. 2 Satz 2) wird **einmal je Anspruch** auf den Cent kaufmännisch gerundet:
`div_round(Wert × Prozentsatz, 100.0, 2, "HALF_UP")`, bei der Staffel erst die
Summe, dann die Rundung; der halbe Finderlohn teilt denselben Zwischenwert
(Divisor 200.0). Brüche („zur Hälfte“, „zu gleichen Teilen“, Wertverhältnis
des § 947) bleiben exakt: Paar ganzer Zahlen, `Rational` erst durch Division.

## Urteilskanal und Schließung

Zwölf Wertungen stehen im Kanal §47.3 (`external judgment relation`,
`authority Court`): §§ 859 Abs. 3, 862 Abs. 1 Satz 2, 904 (zwei), 906 (vier),
910 Abs. 1 Satz 2, 912 Abs. 1 (zwei), 932 Abs. 2, 937 Abs. 2, 950 Abs. 1,
960 Abs. 2/961, 989, 996, 1004 Abs. 1 Satz 2. Zwei Beobachtungen, die die
Zeugen festhalten:

- steht die Wertung als **positive Prämisse** (§ 859 Abs. 3, § 904, § 906
  Abs. 2), so antwortet das Recht ohne Urteil `REQUIRES_JUDGMENT` mit einer
  Urteilsanfrage (`b08`, `n01`) und nach der Antwort `COMPUTED` (`b09`, `n02`);
- steht sie im **Defeater** (§ 932 Abs. 2, § 912 Abs. 1, § 950 Abs. 1), so
  entsteht keine Anfrage: wer den guten Glauben oder die Unverhältnismäßigkeit
  bestreitet, trägt die Feststellung. Das ist die Beweislast des BGB, nicht
  eine Lücke des Modells (Ledger D-10-04).

Die Zahl der offenen Anfragen hängt an der **Schließung des gefragten Kopfes**,
nicht an der einzelnen Norm: wer `eigentuemer` fragt, fragt alle
Erwerbstatbestände mit. Deshalb hat jeder Erwerbsgrund einen eigenen Kopf
(`eigentum_durch_uebereignung_erworben`, `…_ersitzung_…`, `…_fund_…`), und die
Szenarien fragen diesen Kopf (Ledger D-10-07).

## Was das Paket nicht tut und warum

- **Das Grundbuch wird nicht geführt** — Eintragung, Löschung, Abteilung, Tag
  und Reihenfolge sind Eingaben des Falls (`origin adjudicated`, Grundbuchamt);
  das VERFAHREN selbst (wie beantragt, geprüft und vollzogen wird) gehört der
  Grundbuchordnung, nicht diesem Paket. Das war zunächst zu grob gefasst:
  §§ 874, 877, 880–882, 885, 887, 890, 893, 895–897 regeln materielle
  Rechtsfolgen (Rangfolge, Vormerkung, Berichtigung, Bezugnahme) und sind seit
  dem dritten Anlauf EXECUTED (D-10-13) — Eintragung/Bewilligung/Brief bleiben
  Fakteneingaben, aber das ERGEBNIS wird berechnet. Nur § 925a (Urkunde über
  das Grundgeschäft als Wirksamkeitsvoraussetzung der Entgegennahme) und
  § 1010 (Vereinbarungen der Miteigentümer, im Grundbuch nicht eingetragen,
  nur gegen Sondernachfolger unwirksam — reine GBO-Drittwirkungsfrage) bleiben
  `SOURCE_ONLY`, Grund `gbo`.
- **Verweisungen in andere Bücher** führt das Paket nicht aus: der Umfang der
  Deliktshaftung des § 992 und die Bereicherungshöhe der §§ 951, 993 Abs. 1
  bleiben Eingaben des Falls (`de.bgb.bereicherung_delikt`/`de.bgb.schuldrecht_at`,
  Welle B6 folgend — nur DASS die jeweilige Haftung eingreift, ist hier
  ausgeführt); ebenso § 993 Abs. 2 (§ 101, Verteilung der Früchte bei
  Besitzwechsel — anderes Buch, Status `BOUNDARY`), § 922 Satz 4 (Gemeinschaft),
  § 1011 (§ 432), § 927 (FamFG). § 972 (Zurückbehaltungsrecht des Finders:
  entsprechende Anwendung der §§ 1000–1002 auf die Ansprüche der §§ 970, 971)
  und § 976 Abs. 1 (Eigentumsübergang auf die Gemeinde bei Verzicht) sind seit
  der Formalisierung der §§ 991–999, 1003 EXECUTED — „gilt entsprechend“ liest
  denselben Kopf (§ 972 → `verwendungsersatzanspruch`), zwei sich gegenseitig
  ausschließende Produzenten lösen § 976 Abs. 1 ohne Konflikt (D-10-09,
  revidiert D-10-08). § 972 selbst bleibt insofern begrenzt, als das
  Zusammenspiel von § 1003 Abs. 1 und Abs. 2 IN EINEM Fall nicht getestet ist
  (D-10-09, TODO ohne Textgrund).
- **Das Verwertungsverfahren der §§ 979–983** (öffentliche Versteigerung durch
  die Behörde, Bekanntmachung, Verordnungsermächtigung, Zuordnung des Erlöses
  nach Trägerschaft, entsprechende Anwendung bei unanbringbaren Sachen) ist ein
  Verwaltungsverfahren wie die Grundbuchordnung. Es liefert für das Modell
  keinen entscheidungsrelevanten Tatbestand außer der bei § 978 Abs. 3
  vorausgesetzten Zuordnung des Erlöses, die als Eingabe des Falls
  (`berechtigter_nach_981`) übernommen wird (Status `BOUNDARY`, D-10-08).
  § 974 (Eigentumserwerb nach Verschweigung, Aufforderungsverfahren nach § 1003
  ohne eine im Text benannte Erklärungsfrist — anders als bei § 976 Abs. 1
  fehlt hier kein Mechanismus, sondern die Verzahnung mit der Sechsmonatsfrist
  des § 973 wäre ein eigenes, noch nicht entworfenes Regelwerk) und § 976
  Abs. 2 (Eigentumsübergang auf die Gemeinde durch NICHTVERLANGEN binnen
  gesetzter Frist — anders als Abs. 1 wirkt dieser Übergang NACH bereits
  erfolgtem Erwerb des Finders; der Kunstgriff zweier sich ausschließender
  Produzenten (wie bei Abs. 1) trägt hier nicht risikofrei, weil eine bereits
  vergebene Eigentümerstellung nachträglich umgewidmet würde) bleiben Grenzen
  (Status `BOUNDARY`, D-10-09).
- **§§ 977 Satz 2, 978 Abs. 3 Satz 2** (Klagefristen mit eigenem Fristbeginn)
  trennen den Anspruch selbst (Satz 1, zeitunabhängig) vom Erlöschensdatum
  (Satz 2, `…_erloschen_am(f, X)`): welches der beiden für den Fall
  entscheidungsrelevant ist, vergleicht die aufrufende Seite mit ihrem
  `legal_time` — wie bei § 864 dieses Pakets gibt es keinen dritten,
  zeitunabhängig immer feuernden „ausgeschlossen“-Schalter (D-10-08).
- **Seeschiffe** (§§ 929a, 932a) und der **Bienen-Untertitel** über § 963
  hinaus (§§ 962, 964) sind nicht geschnitten — TODO, keine Grenze.
- **Ein Hemmungszeitraum je Lage** (§ 900 Abs. 1 Satz 3, § 939): die
  Vereinigung mehrerer Zeiträume und die Ablaufhemmung (§ 1002 Abs. 2 mit
  §§ 206, 210, 211) sind TODO wie im Pilot `de.bgb.fristen` (Ledger D-04).
- **§ 920 Grenzverwirrung** verlangt den Besitzstand und die Billigkeit
  (Abs. 2) — die Billigkeitsentscheidung ist eine Wertung des Gerichts über
  eine Fläche; ohne Flächenmodell bleibt sie SOURCE_ONLY.
- **Keine Rechtsprechung als Norm**: die Zeugen nennen nur den Gesetzestext;
  BGH-Lesarten zu §§ 906 und 932 sind nicht eingebaut (DECISION-0319, R8).

## Prüfung (nur punktuell)

```sh
./law engine check corpus/laws/de/bgb/besitz-eigentum
python3 corpus/tools/sources/sync/sync_de_bgb_packages.py --only BG-10 --check
python3 docs/foundations/de-bgb/tools/gen_clir_only.py de-bgb-besitz-eigentum.lawir.json
export LAW_WORK_PROFILE_STATE=$PWD/.work/state-bg10.json
python3 verify/ci/gates/compiler/check_lawtest_suites.py --only "de.bgb.besitz_eigentum#besitz" --only "de.bgb.besitz_eigentum#grundbuch" --only "de.bgb.besitz_eigentum#erwerb-929-936" --only "de.bgb.besitz_eigentum#ersitzung" --only "de.bgb.besitz_eigentum#fund" --only "de.bgb.besitz_eigentum#nachbarrecht" --only "de.bgb.besitz_eigentum#herausgabe-985"
python3 corpus/run_kz_regression.py --only "de.bgb.besitz_eigentum#besitz" … --write-manifest
python3 verify/ci/gates/differential/check_kz_differential.py --only "de.bgb.besitz_eigentum#besitz" …
```
