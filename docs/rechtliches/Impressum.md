---
render_macros: true
---

# Impressum

{% set i = impressum %}
{% set adresse = [i.anbieter.name, i.anbieter.einheit, i.anbieter.strasse, i.anbieter.ort, i.anbieter.land] | select | join("<br>\n") %}
{% if adresse %}
## Angaben gemäß § 5 DDG

{{ adresse }}
{% endif %}
{% if i.vertreten_durch %}
## Vertreten durch

{{ i.vertreten_durch }}
{% endif %}
{% if i.kontakt.telefon or i.kontakt.email %}
## Kontakt

{{ ["Telefon: " ~ i.kontakt.telefon if i.kontakt.telefon, "E-Mail: " ~ i.kontakt.email if i.kontakt.email] | select | join("<br>\n") }}
{% endif %}
{% if i.verantwortlich.name %}
## Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV

{{ i.verantwortlich.name }}<br>
{{ i.verantwortlich.anschrift or ([i.anbieter.strasse, i.anbieter.ort] | select | join(", ")) }}
{% endif %}

## Haftung für Inhalte

Die Inhalte dieser Seiten wurden mit größter Sorgfalt erstellt. Für die
Richtigkeit, Vollständigkeit und Aktualität der Inhalte kann jedoch keine
Gewähr übernommen werden. Verpflichtungen zur Entfernung oder Sperrung der
Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon
unberührt. Bei Bekanntwerden von Rechtsverletzungen werden die betreffenden
Inhalte umgehend entfernt.

## Haftung für Links

Diese Dokumentation enthält Links zu externen Websites Dritter, auf deren
Inhalte kein Einfluss besteht. Für diese fremden Inhalte wird keine Gewähr
übernommen; verantwortlich ist stets der jeweilige Anbieter oder Betreiber der
verlinkten Seiten. Bei Bekanntwerden von Rechtsverletzungen werden derartige
Links umgehend entfernt.

## Urheberrecht

Die Inhalte dieser Dokumentation unterliegen dem deutschen Urheberrecht. Der
Quellcode von PlanLos steht unter der GNU General Public License v2.0, soweit
nicht anders angegeben.

{% if i.datenschutz_url %}
## Datenschutz

Hinweise zur Verarbeitung personenbezogener Daten finden sich in der
Datenschutzerklärung: <a href="{{ i.datenschutz_url }}">{{ i.datenschutz_url }}</a>
{% endif %}
