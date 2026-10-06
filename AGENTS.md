# Instructies voor wie deze website bewerkt

Dit bestand is voor taalmodellen en mensen die ADHDoula wijzigen. Lees het vóór je een pagina, een kleur of een zin aanpast.

Het staat live op https://www.adhdoula.nl/AGENTS.md.

Citeerbare feiten voor bezoekers staan in [ai-knowledge-pack.md](https://www.adhdoula.nl/ai-knowledge-pack.md). Kleuren en het logo staan in [README.md](https://www.adhdoula.nl/README.md), onder **Voor agents**. HTML is de pagina voor mensen. Een `.md`-spiegel is alleen een afschrift.

## Voor wie je bouwt

De eigenaar is Kayleigh Huijbregts. Zij is de doula. Zij moet de site zelf kunnen bijhouden. Ze is moeder van drie jonge kinderen. Ze heeft ADHD en autisme.

Dat is publiek, in deze zin, in de ik-vorm:

“Ik heb ADHD en autisme. Daarom heet de praktijk ADHDoula.”

Die zin blijft zo. Maak er geen pagina over diagnoses van. Gebruik niet het oude woord “klassiek autisme”.

ADHD en autisme betekenen hier iets concreets voor de bouw. Een nieuwe pagina, een extra menu of een afwijkende opbouw is werk dat ze later moet onthouden, midden in volle dagen. De site blijft daarom klein. Elke pagina heeft dezelfde vorm. Er is één volgende stap. Het formulier op de kennismaking blijft dit ene formulier: vier velden, vaste volgorde, daarna een bevestigingspagina.

## Voor wie de site is

ADHDoula is er met en voor neurodivergente mensen. Iedereen is welkom. Een diagnose is niet nodig. Neurodivergentie is een specialisatie. Het is geen drempel en geen gesloten groep.

Bezoekers kunnen overprikkeld, moe of vol in hun hoofd binnenkomen, rond een geboorte of in de weken daarna. Dezelfde duidelijkheid die Kayleigh zelf fijn vindt, is de duidelijkheid voor hen. Gewone woorden. Eén onderwerp tegelijk. Een vaste volgorde. Ruimte om te pauzeren.

Schrijf dus niet alleen “toegankelijk” als label. Bouw de pagina zo dat iemand hem kan volgen zonder een verrassing, zonder een tweede taak, en zonder een tekst die ze moet herlezen om de volgende stap te vinden.

## Wat je daardoor doet

- Houd weinig pagina's. Dezelfde kop, dezelfde voettekst, één volgende stap: de kennismaking.
- Zet het antwoord bovenaan. Korte zinnen. Gewone woorden. Eén onderwerp per alinea.
- Laat lopende tekst donker op crème. Gebruik alleen de kleuren uit de README. Geen nieuwe kleur, geen carrousel, geen autoplay, geen pop-up.
- Laat een keuze een echte keuze zijn. Een pauze is normaal. Een partner of naaste is welkom. Schrijf dat zonder druk en zonder belofte over de afloop.
- Houd de grens met de zorg helder. Kayleigh geeft steun. De verloskundige of de arts blijft verantwoordelijk voor medische beslissingen. Ze vervangt de kraamzorg niet. Ze maakt geen geboorteverslag.
- Na een wijziging aan HTML draai je `python3 scripts/generate_llm.py` en zet je de uitvoer mee in git.

## Wat je laat staan tot het echt is

Verzin geen opleidingsnaam, geen prijzen, geen NBvD of ander keurmerk, geen lijst van plaatsen rond Tilburg, en geen portret. Het werkgebied is Tilburg en tot 30 kilometer. Daarbuiten is bespreekbaar in de kennismaking. Een bevalling kan thuis of in het ziekenhuis. Contact blijft `kayleigh@adhdoula.nl` en +31 6 44 00 55 69. Dat mobiele nummer is ook voor WhatsApp. Facebook en Instagram staan in de voettekst van elke pagina en op Over mij. Het formulier stuurt naar kayleigh@adhdoula.nl. Een agent boekt niet en stuurt geen bericht namens een bezoeker.

- Facebook: https://www.facebook.com/p/ADHDoula-61594809255128/
- Instagram: https://www.instagram.com/adhdoula_/

## Bestanden

- `AGENTS.md` — dit bestand. Met de hand. Dit is de uitleg voor wie bouwt.
- `ai-knowledge-pack.md` — feiten die je mag citeren. Met de hand.
- `README.md` — kleuren, logo, en dezelfde afspraken in het kort.
- HTML — de canonieke pagina's voor bezoekers.
- Paginaspiegels, `llms.txt`, `llms-full.txt` en `sitemap.xml` — uitvoer van `scripts/generate_llm.py`. Niet met de hand bewerken. Een nieuwe HTML-pagina hoort in de lijst `PAGES` in dat script.
