#!/usr/bin/env python3
"""Matrix „§ → Absatz → Zustand“ of `de.bgb.schuldrecht_at` (task section 7.2).

The RULE rows and their witnesses are read from the package CLIR: a rule
anchored to the fragment of the paragraph is the witness of every Absatz of
that paragraph which this table does not classify otherwise. The AUTHORED half
is the table `CLASSIFIED` below: every Absatz whose operative content is NOT a
rule of this package —

  CHANNEL   the text delegates an evaluation to the court (DECISION-0194,
            §47.3): the Absatz is executed conditionally on the judgment
            relation named in `witness`;
  EXTERNAL  the content lies outside this act (EGBGB information duties, ZPO,
            HGB, InsO, KWG, TKG, Kapitalanlagegesetzbuch): the case supplies
            the fact, the content is not formalised here;
  DONE      the Absatz is a definition, a reference to other provisions or a
            rule of construction whose effect is carried by the rules of the
            neighbouring Absätze (named in `witness`).

    python3 corpus/laws/de/bgb/schuldrecht-at/tools/gen_saetze.py [--check]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[6]
CLIR = ROOT / "corpus/clir/de-bgb-schuldrecht-at.lawir.json"
ARTICLES = PACKAGE / "sources/de-bgb-schuldrecht-at/articles.json"
OUT = PACKAGE / "analysis/saetze.json"

#: Absätze whose operative content is not a rule of this package.
#: {paragraph: {absatz: (status, witness, note)}}
CLASSIFIED: dict[str, dict[int, tuple[str, str, str]]] = {
    "242": {1: ("CHANNEL", "verstoss_gegen_treu_und_glauben", "Treu und Glauben — Wertung des Gerichts")},
    "244": {2: ("EXTERNAL", "kurswert_zur_zeit_der_zahlung", "Kurswert am Zahlungsort — Eingang des Falls, keine Zahl des Gesetzes")},
    "247": {2: ("EXTERNAL", "basiszinssatz.lawparam.json", "Bekanntmachung im Bundesanzeiger — Handlung der Deutschen Bundesbank; der geltende Satz ist A3-Parameter aus dem Schnappschuss"),
            3: ("EXTERNAL", "SOURCES.json.external", "Amtlicher Hinweis auf die Richtlinie 2000/35/EG"),
            4: ("EXTERNAL", "SOURCES.json.external", "Fußnote zum Kursivdruck des Absatzes 1")},
    "250": {1: ("CHANNEL", "frist_zur_herstellung_angemessen", "angemessene Frist — Wertung des Gerichts")},
    "251": {2: ("CHANNEL", "herstellung_nur_mit_unverhaeltnismaessigen_aufwendungen_moeglich", "Unverhältnismäßigkeit der Aufwendungen — Wertung des Gerichts")},
    "252": {1: ("CHANNEL", "entgangener_gewinn_wahrscheinlich", "Wahrscheinlichkeit des entgangenen Gewinns — Wertung des Gerichts")},
    "253": {2: ("CHANNEL", "billige_entschaedigung_in_geld", "billige Entschädigung — Wertung des Gerichts")},
    "254": {1: ("CHANNEL", "mitverschulden_anteil", "Mitwirkendes Verschulden und sein Anteil — Wertung des Gerichts (Anteil als Paar ganzer Zahlen, D-04-05)"),
            2: ("CHANNEL", "mitverschulden_anteil", "Absatz 2 stellt Unterlassen der Warnung und der Schadensabwendung gleich — derselbe Kanal")},
    "259": {2: ("DONE", "EidesstattlicheVersicherungBeiZweifeln", "eidesstattliche Versicherung — Regel des Absatzes 2 liegt in der Datei"),
            3: ("DONE", "EidesstattlicheVersicherungBeiZweifeln", "Ausnahme geringer Bedeutung als ausdrückliche Verneinung des Falls")},
    "261": {1: ("EXTERNAL", "gericht_kann_versicherung_aendern", "Beschluss des Gerichts über die Änderung der Versicherung — Verfahren außerhalb des BGB")},
    "264": {2: ("CHANNEL", "frist_zur_wahl_angemessen", "angemessene Frist zur Vornahme der Wahl — Wertung des Gerichts")},
    "271a": {1: ("CHANNEL", "grob_unbillig_im_hinblick_auf_die_belange_des_glaeubigers", "grobe Unbilligkeit — Wertung des Gerichts; die Zahl 60 Tage steht im Text"),
             3: ("CHANNEL", "grob_unbillig_im_hinblick_auf_die_belange_des_glaeubigers", "grobe Unbilligkeit der Überprüfungsfrist — Wertung des Gerichts"),
             6: ("EXTERNAL", "SOURCES.json.external", "Vorbehalt sonstiger Vorschriften außerhalb dieses Abschnitts"),
             7: ("EXTERNAL", "SOURCES.json.external", "Amtlicher Hinweis und Fußnote (§ 34 BGBEG)")},
    "275": {2: ("CHANNEL", "grobes_missverhaeltnis_von_aufwand_und_leistungsinteresse", "grobes Missverhältnis — Wertung des Gerichts"),
            3: ("CHANNEL", "persoenliche_leistung_nicht_zumutbar", "Unzumutbarkeit der persönlichen Leistung — Wertung des Gerichts"),
            4: ("DONE", "UnmoeglichkeitSchliesstDenLeistungsanspruchAus", "Verweisung auf §§ 280, 283 bis 285, 311a, 326"),
            5: ("EXTERNAL", "SOURCES.json.external", "Amtlicher Hinweis auf die Richtlinie 1999/44/EG")},
    "281": {1: ("CHANNEL", "frist_zur_leistung_angemessen", "angemessene Frist und Unerheblichkeit der Pflichtverletzung — Wertungen des Gerichts"),
            2: ("CHANNEL", "besondere_umstaende_rechtfertigen_sofortige_geltendmachung", "besondere Umstände — Wertung des Gerichts")},
    "282": {1: ("CHANNEL", "leistung_durch_den_schuldner_nicht_mehr_zumutbar", "Unzumutbarkeit der Leistung — Wertung des Gerichts")},
    "284": {1: ("DONE", "ErsatzVergeblicherAufwendungen", "billigerweise gemachte Aufwendungen als Eingang des Falls; die Ausnahme ist ausdrückliche Verneinung")},
    "286": {2: ("CHANNEL", "sofortiger_verzugseintritt_gerechtfertigt", "Nummer 4: besondere Gründe für den sofortigen Verzugseintritt — Wertung des Gerichts; Nummern 1 bis 3 sind Regeln"),
            6: ("DONE", "VerzugDerEntgeltforderungGegenueberUnternehmer", "Verweisung auf § 271a Abs. 1 bis 5 für abweichende Vereinbarungen"),
            7: ("EXTERNAL", "SOURCES.json.external", "Amtlicher Hinweis auf die Richtlinie 2000/35/EG"),
            8: ("EXTERNAL", "SOURCES.json.external", "Fußnote (§ 34 BGBEG)")},
    "288": {3: ("DONE", "WeitererVerzugsschadenBleibtErsatzfaehig", "höhere Zinsen aus anderem Rechtsgrund — Eingang des Falls"),
            7: ("EXTERNAL", "SOURCES.json.external", "Amtlicher Hinweis auf die Richtlinie 2000/35/EG"),
            8: ("EXTERNAL", "SOURCES.json.external", "Fußnote (§ 34 BGBEG)")},
    "291": {1: ("EXTERNAL", "rechtshaengigkeit_seit", "Eintritt der Rechtshängigkeit — Tatsache des Prozesses (ZPO), Eingang des Falls")},
    "292": {1: ("EXTERNAL", "haftung_nach_eigentuemer_besitzer_recht", "Verweisung auf das Eigentümer-Besitzer-Verhältnis (§§ 987 ff., Paket de.bgb.besitz_eigentum)"),
            2: ("EXTERNAL", "haftung_nach_eigentuemer_besitzer_recht", "dasselbe für Nutzungen und Verwendungen")},
    "299": {1: ("DONE", "KeinAnnahmeverzugBeiVoruebergehenderVerhinderung", "angemessene Zeit der Ankündigung — ausdrückliche Verneinung des Falls")},
    "305c": {1: ("CHANNEL", "klausel_ist_ueberraschend", "überraschende Klausel — Wertung des Gerichts")},
    "306": {3: ("CHANNEL", "festhalten_am_vertrag_unzumutbare_haerte", "unzumutbare Härte — Wertung des Gerichts")},
    "307": {1: ("CHANNEL", "unangemessene_benachteiligung", "unangemessene Benachteiligung entgegen Treu und Glauben — Wertung des Gerichts"),
            4: ("DONE", "ZweifelsregelAbweichungVonGrundgedanken", "Absatz 3 begrenzt die Absätze 1 und 2 auf abweichende Regelungen")},
    "308": {1: ("CHANNEL", "klausel_verstoesst_gegen_308", "Klauselverbote MIT Wertungsmöglichkeit — jede Nummer verlangt eine Wertung des Gerichts")},
    "310": {2: ("EXTERNAL", "SOURCES.json.external", "Absatz 1a: Bank-, Finanz- und Wertpapierdienstleistungen nach KWG, WpIG, ZAG, KAGB, BörsG mit den Schwellen 250 Arbeitnehmer, 50 und 43 Millionen Euro — Eingang des Falls"),
             3: ("EXTERNAL", "SOURCES.json.external", "Fortsetzung des Absatzes 1a"),
             4: ("EXTERNAL", "SOURCES.json.external", "Fortsetzung des Absatzes 1a"),
             5: ("EXTERNAL", "SOURCES.json.external", "Fortsetzung des Absatzes 1a"),
             22: ("EXTERNAL", "SOURCES.json.external", "Fußnote (§ 34 BGBEG)")},
    "312": {2: ("EXTERNAL", "ausgenommener_vertrag", "Nummern 1 bis 14 verweisen auf andere Gesetze (GewO, PBefG, Kapitalanlagegesetzbuch) — Vertragsart ist Eingang des Falls"),
            5: ("EXTERNAL", "SOURCES.json.external", "Finanzdienstleistungen mit aufeinanderfolgenden Vorgängen — Reihe von Vorgängen als Eingang"),
            23: ("EXTERNAL", "SOURCES.json.external", "Fußnote zum Kursivdruck des Absatzes 2 Nummer 12")},
    "312a": {2: ("EXTERNAL", "informationspflicht_nach_246a_erfuellt", "Informationspflicht nach Artikel 246 EGBGB — Inhalt außerhalb dieses Pakets")},
    "312d": {1: ("EXTERNAL", "informationspflicht_nach_246a_erfuellt", "Artikel 246a EGBGB"),
             2: ("EXTERNAL", "informationspflicht_nach_246a_erfuellt", "Artikel 246b EGBGB (Finanzdienstleistungen, Online-Benutzeroberfläche)")},
    "312e": {1: ("DONE", "KeineKostenOhneInformation", "Rechtsfolge der unterlassenen Information ist die Regel dieses Paragraphen")},
    "312f": {3: ("EXTERNAL", "bestaetigung_des_vertrags_geschuldet", "Artikel 246a EGBGB; Zustimmung und Kenntnisbestätigung bei digitalen Inhalten"),
             4: ("DONE", "AbschriftUndBestaetigungDesVertrags", "Absatz 4 nimmt Finanzdienstleistungen aus")},
    "312i": {2: ("DONE", "AllgemeinePflichtenImElektronischenGeschaeftsverkehr", "Ausnahme individueller Kommunikation als ausdrückliche Verneinung"),
             3: ("EXTERNAL", "SOURCES.json.external", "weitergehende Informationspflichten anderer Vorschriften")},
    "312j": {1: ("EXTERNAL", "pflichten_im_elektronischen_geschaeftsverkehr", "Angaben zu Lieferbeschränkungen und Zahlungsmitteln — Gestaltung der Webseite"),
             2: ("EXTERNAL", "informationspflicht_nach_246a_erfuellt", "Artikel 246a § 1 EGBGB")},
    "312k": {3: ("EXTERNAL", "kuendigung_ueber_schaltflaeche_abgegeben", "Speicherbarkeit der Erklärung auf einem dauerhaften Datenträger — technische Gestaltung")},
    "312l": {1: ("EXTERNAL", "informationspflicht_des_marktplatzbetreibers", "Artikel 246d EGBGB")},
    "313": {1: ("CHANNEL", "festhalten_am_unveraenderten_vertrag_nicht_zumutbar", "Unzumutbarkeit des Festhaltens — Wertung des Gerichts"),
            3: ("CHANNEL", "anpassung_nicht_moeglich_oder_nicht_zumutbar", "Unmöglichkeit oder Unzumutbarkeit der Anpassung — Wertung des Gerichts")},
    "314": {1: ("CHANNEL", "wichtiger_grund_zur_kuendigung", "wichtiger Grund — Wertung des Gerichts"),
            2: ("CHANNEL", "sofortige_kuendigung_gerechtfertigt", "Entbehrlichkeit der Abhilfefrist — Wertung des Gerichts"),
            3: ("CHANNEL", "kuendigung_innerhalb_angemessener_frist", "angemessene Frist der Kündigung — Wertung des Gerichts")},
    "315": {3: ("CHANNEL", "bestimmung_entspricht_der_billigkeit", "Billigkeit der Bestimmung — Wertung des Gerichts")},
    "318": {2: ("CHANNEL", "anfechtung_unverzueglich_erklaert", "Unverzüglichkeit der Anfechtung — bewertendes Merkmal; die dreißig Jahre sind Regel")},
    "319": {1: ("CHANNEL", "bestimmung_des_dritten_offenbar_unbillig", "offenbare Unbilligkeit — Wertung des Gerichts")},
    "320": {2: ("CHANNEL", "verweigerung_verstiesse_gegen_treu_und_glauben", "Verstoß gegen Treu und Glauben bei geringfügigem Rückstand — Wertung des Gerichts")},
    "321": {1: ("CHANNEL", "gegenleistungsanspruch_durch_mangelnde_leistungsfaehigkeit_gefaehrdet", "erkennbare Gefährdung des Gegenleistungsanspruchs — Wertung des Gerichts"),
            2: ("CHANNEL", "frist_zur_gegenleistung_oder_sicherheit_angemessen", "angemessene Frist — Wertung des Gerichts")},
    "322": {3: ("DONE", "KlageDesVorleistungspflichtigenBeiAnnahmeverzug", "Verweisung auf § 274 Abs. 2 für die Zwangsvollstreckung")},
    "323": {2: ("CHANNEL", "besondere_umstaende_rechtfertigen_sofortigen_ruecktritt", "Nummer 3: besondere Umstände — Wertung des Gerichts; Nummern 1 und 2 sind Regeln"),
            4: ("CHANNEL", "eintritt_der_ruecktrittsvoraussetzungen_offensichtlich", "Offensichtlichkeit des künftigen Rücktrittsgrundes — Wertung des Gerichts"),
            5: ("CHANNEL", "pflichtverletzung_unerheblich", "Unerheblichkeit der Pflichtverletzung — Wertung des Gerichts"),
            6: ("CHANNEL", "glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich", "alleinige oder weit überwiegende Verantwortlichkeit — Wertung des Gerichts"),
            7: ("EXTERNAL", "SOURCES.json.external", "Amtlicher Hinweis auf die Richtlinie 1999/44/EG")},
    "324": {1: ("CHANNEL", "festhalten_am_vertrag_nicht_mehr_zumutbar", "Unzumutbarkeit des Festhaltens — Wertung des Gerichts")},
    "326": {2: ("CHANNEL", "glaeubiger_allein_oder_weit_ueberwiegend_verantwortlich", "Verantwortlichkeit des Gläubigers — Wertung des Gerichts"),
            3: ("DONE", "RueckforderungDerNichtGeschuldetenGegenleistung", "Minderung nach § 441 Abs. 3 bei Herausgabe des Ersatzes — Paket de.bgb.kauf"),
            7: ("EXTERNAL", "SOURCES.json.external", "Amtlicher Hinweis auf die Richtlinie 1999/44/EG")},
    "327": {6: ("EXTERNAL", "ausnahme_digitale_produkte", "Nummern 1 bis 8 verweisen auf TKG, GlüStV, KWG und das Informationsweiterverwendungsgesetz — Vertragsart ist Eingang des Falls")},
    "327e": {3: ("DONE", "ProduktmangelWegenObjektiverAnforderungen", "objektive Anforderungen als Tatsache des Falls; öffentliche Äußerungen und ihre Berichtigung ebenso"),
             4: ("DONE", "PflichtZurMangelfreienBereitstellung", "Anforderungen an die Integration als Tatsache des Falls")},
    "327f": {1: ("CHANNEL", "erforderliche_aktualisierung_nicht_bereitgestellt", "erwartbarer Aktualisierungszeitraum (Satz 3 Nummer 2) — Wertung; die Pflicht selbst ist Regel"),
             2: ("CHANNEL", "installation_der_aktualisierung_unterlassen", "angemessene Frist der Installation — Wertung")},
    "327j": {5: ("DONE", "VerjaehrungZweiJahreAbBereitstellung", "Verweisung auf § 218 für die Rechte des § 327i Nummer 2")},
    "327k": {3: ("DONE", "BeweislastumkehrImErstenJahr", "Ausschluss der Vermutung als ausdrückliche Verneinung des Falls"),
             4: ("DONE", "BeweislastumkehrImErstenJahr", "Information über die technischen Anforderungen — Voraussetzung des Ausschlusses")},
    "327l": {2: ("CHANNEL", "nacherfuellung_unmoeglich_oder_unverhaeltnismaessig", "unverhältnismäßige Kosten der Nacherfüllung — Wertung des Gerichts")},
    "327m": {2: ("CHANNEL", "mangel_unerheblich", "Unerheblichkeit des Mangels — Wertung des Gerichts")},
    "327n": {2: ("CHANNEL", "geminderter_preis", "Wertverhältnis der Minderung — Wertung des Gerichts"),
             3: ("CHANNEL", "geminderter_preis", "Schätzung der Minderung — Wertung des Gerichts")},
    "327q": {2: ("CHANNEL", "fortsetzung_nach_widerruf_nicht_zumutbar", "Unzumutbarkeit der Fortsetzung — Wertung des Gerichts")},
    "327r": {2: ("CHANNEL", "zugriff_oder_nutzbarkeit_beeintraechtigt", "angemessene Frist der Information und Unerheblichkeit der Beeinträchtigung — Wertungen")},
    "327u": {5: ("EXTERNAL", "SOURCES.json.external", "§ 377 HGB bleibt unberührt")},
    "343": {1: ("CHANNEL", "angemessener_betrag_der_strafe", "unverhältnismäßig hohe Strafe und angemessener Betrag — Wertung des Gerichts"),
            2: ("CHANNEL", "angemessener_betrag_der_strafe", "dasselbe für Strafversprechen außerhalb der §§ 339, 342")},
    "350": {1: ("CHANNEL", "frist_zur_ausuebung_des_ruecktritts_angemessen", "angemessene Frist zur Ausübung — Wertung des Gerichts")},
    "352": {1: ("CHANNEL", "aufrechnung_unverzueglich_nach_ruecktritt_erklaert", "Unverzüglichkeit der Aufrechnung — bewertendes Merkmal")},
    "353": {1: ("CHANNEL", "erklaerung_unverzueglich_zurueckgewiesen", "Unverzüglichkeit der Zurückweisung — bewertendes Merkmal")},
    "355": {3: ("CHANNEL", "widerruf_fristgerecht", "Unverzüglichkeit der Rückgewähr — bewertendes Merkmal; die Höchstfristen stehen in §§ 357, 357b")},
    "356": {1: ("EXTERNAL", "eingangsbestaetigung_zu_uebermitteln", "Muster-Widerrufsformular nach Anlage 2 zu Artikel 246a EGBGB"),
            3: ("EXTERNAL", "unterrichtung_ueber_das_widerrufsrecht_am", "Artikel 246a und 246b EGBGB — Inhalt der Unterrichtung außerhalb dieses Pakets")},
    "356a": {2: ("EXTERNAL", "widerruf_ueber_widerrufsfunktion_versandt_am", "Angaben der Widerrufsfunktion — technische Gestaltung"),
             3: ("EXTERNAL", "widerruf_ueber_widerrufsfunktion_versandt_am", "Bestätigungsfunktion — technische Gestaltung"),
             6: ("EXTERNAL", "SOURCES.json.external", "Fußnote (§ 8 Abs. 1 VVG 2008)")},
    "356b": {2: ("EXTERNAL", "pflichtangaben_nachgeholt_am", "Pflichtangaben nach § 492 Abs. 2 und Artikel 247 EGBGB — Paket de.bgb.sonstige_vertraege"),
             3: ("EXTERNAL", "vertragsurkunde_zur_verfuegung_gestellt_am", "§ 494 Abs. 7 — Paket de.bgb.sonstige_vertraege")},
    "356c": {1: ("EXTERNAL", "widerruf_erklaert_am", "Textform der Widerrufserklärung — § 126b, Paket de.bgb.allgemeiner_teil"),
             3: ("EXTERNAL", "vorvertragliche_informationen_unvollstaendig", "§ 482 Abs. 1 und Artikel 242 EGBGB — Paket de.bgb.sonstige_vertraege"),
             4: ("EXTERNAL", "vorvertragliche_informationen_unvollstaendig", "§ 482a — Paket de.bgb.sonstige_vertraege")},
    "356d": {1: ("EXTERNAL", "unterrichtung_ueber_das_widerrufsrecht_am", "Artikel 246 Abs. 3 EGBGB")},
    "356e": {1: ("EXTERNAL", "unterrichtung_ueber_das_widerrufsrecht_am", "Artikel 249 § 3 EGBGB; § 650i Abs. 1 — Paket de.bgb.dienst_werk")},
    "356f": {1: ("EXTERNAL", "unterrichtung_ueber_das_widerrufsrecht_am", "§ 514 Abs. 2 Satz 3 — Paket de.bgb.sonstige_vertraege")},
    "357": {5: ("EXTERNAL", "unterrichtung_ueber_ruecksendekosten", "Artikel 246a § 1 Abs. 2 Satz 1 Nummer 2 EGBGB"),
            8: ("DONE", "KeineRuecksendepflichtBeiAbholung", "Verweisung auf § 327p für digitale Produkte")},
    "357a": {1: ("EXTERNAL", "unterrichtung_ueber_das_widerrufsrecht_am", "Artikel 246a EGBGB als Voraussetzung des Wertersatzes"),
             2: ("EXTERNAL", "unterrichtung_ueber_das_widerrufsrecht_am", "Wertersatz für Dienstleistungen: Artikel 246a EGBGB und Marktwert"),
             3: ("DONE", "WertersatzFuerWertverlustDerWare", "kein Wertersatz bei digitalen Inhalten")},
    "357b": {1: ("DONE", "RueckgewaehrfristDreissigTageBeiFinanzdienstleistungen", "dreißig Tage als Regel dieser Datei"),
             2: ("EXTERNAL", "finanzdienstleistungsvertrag", "§ 506 Abs. 4 und Wertersatz für Finanzdienstleistungen — Paket de.bgb.sonstige_vertraege"),
             3: ("EXTERNAL", "finanzdienstleistungsvertrag", "Sollzins des Verbraucherdarlehens und Artikel 247 EGBGB — Paket de.bgb.sonstige_vertraege")},
    "358": {3: ("DONE", "WiderrufErfasstDenVerbundenenDarlehensvertrag", "wirtschaftliche Einheit als Tatsache des Falls"),
            4: ("DONE", "WiderrufErfasstDenVerbundenenDarlehensvertrag", "Verweisung auf §§ 355, 357 bis 357c für die Rückabwicklung"),
            5: ("EXTERNAL", "verbundener_darlehensvertrag", "Finanzinstrumente — Kapitalanlagegesetzbuch")},
    "359": {2: ("DONE", "EinwendungsdurchgriffBeiVerbundenenVertraegen", "Ausnahme für Finanzinstrumente und die Grenze von 200 Euro stehen in der Regel")},
    "360": {2: ("DONE", "WiderrufErfasstDenZusammenhaengendenVertrag", "Begriff des zusammenhängenden Vertrags als Tatsache des Falls")},
    "361": {3: ("DONE", "BeweislastDesUnternehmersFuerDenFristbeginn", "Beweislast des Unternehmers ist die Regel dieses Absatzes")},
    "363": {1: ("DONE", "BeweislastNachAnnahmeAlsErfuellung", "Beweislast des Gläubigers ist die Regel dieses Paragraphen")},
    "366": {2: ("DONE", "TilgungDerFaelligenSchuldOhneBestimmung", "Reihenfolge Sicherheit–Lästigkeit–Alter: die Regel nimmt die Fälligkeit; die weiteren Stufen sind TODO des Ledgers")},
    "374": {2: ("CHANNEL", "anzeige_der_hinterlegung_unterlassen_und_tunlich", "Unverzüglichkeit und Untunlichkeit der Anzeige — Wertung des Gerichts")},
    "383": {2: ("EXTERNAL", "versteigerung_zulaessig", "Form der öffentlichen Versteigerung: Versteigerer, Gerichtsvollzieher, virtuelle und hybride Versteigerung"),
            3: ("EXTERNAL", "versteigerung_zulaessig", "öffentliche Bekanntmachung von Zeitpunkt, Ort und Zugangsdaten"),
            4: ("EXTERNAL", "versteigerung_zulaessig", "Ausnahme für eingetragene Schiffe und Schiffsbauwerke"),
            9: ("EXTERNAL", "SOURCES.json.external", "Fußnote (§§ 1236, 1237)")},
    "384": {2: ("CHANNEL", "anzeige_der_hinterlegung_unterlassen_und_tunlich", "Unverzüglichkeit der Benachrichtigung — Wertung des Gerichts"),
            3: ("DONE", "AndrohungDerVersteigerung", "Untunlichkeit von Androhung und Benachrichtigung")},
    "385": {1: ("EXTERNAL", "boersen_oder_marktpreis", "Börsen- oder Marktpreis und die Person des Handelsmaklers — Eingang des Falls")},
    "392": {1: ("EXTERNAL", "forderung_beschlagnahmt_am", "Beschlagnahme der Forderung — Akt der Zwangsvollstreckung (ZPO), Eingang des Falls")},
    "394": {1: ("EXTERNAL", "forderung_unpfaendbar", "Unpfändbarkeit nach §§ 850 ff. ZPO; Kranken-, Hilfs- und Sterbekassen — Eingang des Falls")},
    "395": {1: ("EXTERNAL", "leistung_an_dieselbe_kasse", "Kassenzugehörigkeit der öffentlich-rechtlichen Körperschaft — Eingang des Falls")},
    "396": {1: ("CHANNEL", "aufrechnungsbestimmung_getroffen", "Unverzüglichkeit des Widerspruchs — bewertendes Merkmal; die Bestimmung selbst ist Regel"),
            2: ("DONE", "AufrechnungNachBestimmungDesAufrechnenden", "Verweisung auf § 367 für Zinsen und Kosten")},
    "400": {1: ("EXTERNAL", "forderung_unpfaendbar", "Unpfändbarkeit nach §§ 850 ff. ZPO — Eingang des Falls")},
    "401": {2: ("DONE", "NebenUndVorzugsrechteGehenMitUeber", "Vorzugsrecht im Insolvenzverfahren — InsO, Eingang des Falls")},
    "405": {1: ("DONE", "EinwandDesScheingeschaeftsBeiUrkundenvorlegungAusgeschlossen", "Kenntnis des neuen Gläubigers als festgestellte Tatsache")},
    "407": {2: ("EXTERNAL", "rechtskraeftiges_urteil_im_rechtsstreit_mit_dem_bisherigen_glaeubiger", "rechtskräftiges Urteil — Tatsache des Prozesses (ZPO)")},
    "408": {2: ("EXTERNAL", "nochmalige_abtretung_an_dritten", "gerichtlicher Überweisungsbeschluss — ZPO")},
    "410": {1: ("CHANNEL", "leistung_nur_gegen_urkunde_geschuldet", "Unverzüglichkeit der Zurückweisung von Kündigung und Mahnung — bewertendes Merkmal")},
    "411": {1: ("EXTERNAL", "gehaltsabtretung_einer_amtsperson", "Dienst- und Versorgungsrecht der Amtsperson — außerhalb des BGB")},
    "415": {2: ("DONE", "VerweigerteGenehmigungLaesstDieSchulduebernahmeEntfallen", "Frist zur Erklärung über die Genehmigung: Fristsetzung durch die Parteien"),
            3: ("DONE", "UebernehmerMussVorDerGenehmigungBefriedigen", "Pflicht des Übernehmers vor der Genehmigung")},
    "416": {2: ("EXTERNAL", "empfang_der_mitteilung_des_veraeusserers", "Eintragung des Erwerbers im Grundbuch — Paket de.bgb.besitz_eigentum"),
            3: ("DONE", "GenehmigungGiltNachSechsMonatenAlsErteilt", "Mitteilungs- und Benachrichtigungspflichten des Veräußerers")},
    "418": {2: ("EXTERNAL", "buergschaften_und_pfandrechte_erloschen", "Vorzugsrecht im Insolvenzverfahren — InsO")},
    "425": {2: ("DONE", "AndereTatsachenWirkenNurEinzeln", "Aufzählung der einzelwirkenden Tatsachen als Aufzählungswert")},
    "429": {3: ("DONE", "VerzugEinesGesamtglaeubigersWirktGegenAlle", "Verweisung auf §§ 422, 423, 425")},
    "432": {2: ("DONE", "TatsacheInDerPersonEinesGlaeubigersWirktNichtFuerDieUebrigen", "Wirkung nur für den betroffenen Gläubiger ist die Regel dieses Absatzes")},
}


def rule_anchors() -> dict[str, list[str]]:
    ir = json.loads(CLIR.read_text(encoding="utf-8"))
    anchors: dict[str, list[str]] = {}

    def walk(node):
        if isinstance(node, dict):
            yield node
            for value in node.values():
                yield from walk(value)
        elif isinstance(node, list):
            for value in node:
                yield from walk(value)

    for node in walk(ir):
        if isinstance(node, dict) and str(node.get("kind", "")).lower().startswith("rule"):
            text = json.dumps(node, ensure_ascii=False)
            name = node.get("id") or node.get("name") or ""
            local = str(name).rsplit("#", 1)[-1].rsplit(":", 1)[-1]
            for paragraph in set(re.findall(r"#BGB_P([0-9]+[a-z]?)", text)):
                anchors.setdefault(paragraph, [])
                if local and local not in anchors[paragraph]:
                    anchors[paragraph].append(local)
    return anchors


def build() -> dict:
    articles = json.loads(ARTICLES.read_text(encoding="utf-8"))
    edition = articles["editions"][0]
    scope = edition["scope"]
    declared = dict(edition.get("declared", {}))
    # Absatz count comes from the SAME place as docs/foundations/de-bgb/tools/build_inventory.py
    # reads it — the register DOKNR (`lines` of the norm) — so that the indices match.
    register = json.loads((ROOT / "docs/foundations/de-bgb/registry/DOKNR.json").read_text(encoding="utf-8"))
    lines = {norm["number"]: (norm["lines"] or []) for norm in register["norms"] if norm.get("kind") == "paragraph"}
    anchors = rule_anchors()
    out = {
        "$comment": ("Matrix „§ → Absatz → Zustand“ des Pakets de.bgb.schuldrecht_at, gelesen von "
                     "docs/foundations/de-bgb/tools/build_inventory.py. RULE-Zeilen und ihre Zeugen kommen aus dem "
                     "CLIR; CHANNEL, EXTERNAL und DONE stehen in der Tabelle CLASSIFIED von tools/gen_saetze.py "
                     "und sind von Hand vergeben. Erzeugt: tools/gen_saetze.py."),
        "act": "de-bgb-schuldrecht-at",
        "legal_cutoff": articles["legal_cutoff"],
    }
    body: dict[str, dict] = {}
    for paragraph in scope:
        rows = {}
        count = max(1, len(lines.get(paragraph, [])))
        for index in range(1, count + 1):
            classified = CLASSIFIED.get(paragraph, {}).get(index)
            if classified:
                status, witness, note = classified
                rows[str(index)] = {"status": status, "witness": witness, "note": note}
            elif paragraph in declared:
                rows[str(index)] = {"status": "BOUNDARY", "witness": "articles.json",
                                    "note": declared[paragraph]}
            elif paragraph in anchors:
                rows[str(index)] = {"status": "RULE", "witness": ";".join(anchors[paragraph][:4])}
            else:
                rows[str(index)] = {"status": "TODO", "witness": ""}
        body[paragraph] = rows
    # build_inventory.py looks the rows up by the paragraph number at the TOP level
    # ({"<number>": {"<absatz>": {...}}}); the three metadata keys are ignored there.
    out.update(body)
    return out


def main() -> int:
    payload = build()
    rendered = json.dumps(payload, ensure_ascii=False, indent=1) + "\n"
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != rendered:
            print(f"stale: {OUT.relative_to(ROOT)}")
            return 1
        return 0
    OUT.write_text(rendered, encoding="utf-8")
    counts: dict[str, int] = {}
    for key, rows in payload.items():
        if not isinstance(rows, dict) or key.startswith("$") or key in ("act", "legal_cutoff"):
            continue
        for row in rows.values():
            counts[row["status"]] = counts.get(row["status"], 0) + 1
    print(f"written {OUT.relative_to(ROOT)}: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
