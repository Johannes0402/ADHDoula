# ADHDoula

Praktijkwebsite van Kayleigh Huijbregts, doula voor geboorte en postpartum. Live op [https://www.adhdoula.nl/](https://www.adhdoula.nl/). `www` is de canonieke host. Het kale domein stuurt daarheen door.

Andere agents: lees [AGENTS.md](./AGENTS.md) voordat je iets wijzigt. Dat bestand legt uit voor wie de site is, en waarom neurodivergentie de bouw stuurt. Het staat ook live op https://www.adhdoula.nl/AGENTS.md. Hieronder staan dezelfde afspraken, plus de kleuren. Citeerbare feiten staan in [ai-knowledge-pack.md](./ai-knowledge-pack.md). De korte index voor taalmodellen is [llms.txt](./llms.txt).

## Pagina's

- `index.html` — home
- `geboorte.html` — geboortedoula
- `net-zwanger.html` — net zwanger: drie stappen, verloskundige of huisarts eerst
- `postpartum.html` — postpartum doula
- `over-mij.html` — bio
- `wel-en-niet.html` — grens van het werk
- `werkgebied.html` — Tilburg en tot 30 km, daarbuiten bespreekbaar
- `vragen.html` — veelgestelde vragen
- `tarieven.html` — pakketten en bedragen
- `kennismaking.html` — eerste stap

Elke HTML-pagina heeft een markdown-spiegel met hetzelfde pad plus `.md` (home: `index.md`). HTML blijft de pagina voor bezoekers. Die spiegels, `llms.txt`, `llms-full.txt` en `sitemap.xml` worden gemaakt door de generator. Niet met de hand bewerken.

```bash
python3 scripts/generate_llm.py
```

Na een HTML-wijziging draai je dat commando en zet je de uitvoer mee in git. `python3 scripts/generate_llm.py --check` stopt met een fout als de uitvoer achterloopt. In deze repo weigert de pre-commit hook zo'n commit zodra `git config core.hooksPath scripts/git-hooks` gezet is. `ai-knowledge-pack.md` blijft met de hand: de generator eist dat de profiel-URL's van Over mij daar ook in staan. `scripts/` staat in `robots.txt` op Disallow.

Lokaal bekijken, alleen vanuit deze map:

```bash
cd /Users/johannesaloijsius/websites/doula-test
python3 -m http.server 8765 --bind 127.0.0.1
```

Daarna: http://127.0.0.1:8765/

## Voor agents

### Eigenaar

- Eigenaar van praktijk en website: **Kayleigh Huijbregts**. Moeder van drie jonge kinderen.
- Praktijknaam = websitenaam: **ADHDoula**.
- Publieke zin, ik-vorm, niet herschrijven naar een diagnose-pagina: “Ik heb ADHD en autisme. Daarom heet de praktijk ADHDoula.” Niet “klassiek autisme”.
- Iedereen is welkom. Neurodivergentie is een specialisatie, geen gesloten doelgroep. Een diagnose is niet nodig.
- De site blijft voor Kayleigh behapbaar: weinig pagina's, dezelfde opbouw, één volgende stap (kennismaking), geen CMS. Er is één contactformulier, op de kennismaking, met vier velden en een bevestigingspagina.

### Kleuren

Huiskleuren in Johannes' woorden: **appeltjesgroen** en **blauw-paars**. Crème komt uit het logo. Tokens in `css/styles.css`:

| Token | Hex | Gebruik |
| --- | --- | --- |
| `--cream` | `#fdf9f0` | Pagina-achtergrond |
| `--ink` | `#2c2444` | Lopende tekst en koppen |
| `--ink-soft` | `#4a4166` | Zachtere tekst |
| `--apple` | `#7eae2e` | Appeltjesgroen, vlakken en de streep |
| `--apple-deep` | `#2f5d12` | Groene tekst en links op crème |
| `--apple-soft` | `#e7f6cf` | Zachte groene band |
| `--apple-mid` | `#d5eea4` | Iets sterkere groene band |
| `--purple` | `#4e3a78` | Blauw-paars, knoppen |
| `--purple-soft` | `#ede4f8` | Zachte paarse band |

Lopende tekst blijft donker op crème. Knoptekst is wit op paars. De bovenste streep is half appeltjesgroen, half blauw-paars. Geen nieuwe kleuren, geen carrousel, geen autoplay, geen pop-up.

### Logo

- Gebruik `assets/logo.png`. Niet nabouwen.
- Bron: `Desktop/ADHDoulav2.JPG`. Dat bestand blijft op het bureaublad.
- Alt-tekst: “Logo van ADHDoula: twee witte lelies boven de naam.”
- Lettertypen: Atkinson Hyperlegible (tekst) en Fraunces (koppen), zelf gehost in `assets/fonts`.

### Wat je niet verzint

- Geen opleidingsnaam, school of certificaat tot de letterlijke naam is aangeleverd.
- Geen NBvD, AGB of ander keurmerk. Kayleigh is nog geen NBvD-lid. Prijzen staan op `tarieven.html`. Verzin geen andere bedragen.
- Geen lijst van dorpen of steden rond Tilburg. Het werkgebied is Tilburg en tot 30 km. Daarbuiten is bespreekbaar in de kennismaking.
- Geen portret. Er is alleen het logo.
- Geen medische zorg, geen belofte over hoe een bevalling loopt, geen geboorteverslag.
- Cochrane 2017 alleen zoals op `wel-en-niet.html`, met bron, en niet als garantie.
- Bevalling: thuis én ziekenhuis.
- Contact blijft `kayleigh@adhdoula.nl` en `+31 6 44 00 55 69` (`tel:+31644005569`). Hetzelfde nummer is ook WhatsApp: `https://wa.me/31644005569`.
- Profielen, alleen de schone URL zonder volg-parameters: Facebook `https://www.facebook.com/p/ADHDoula-61594809255128/` en Instagram `https://www.instagram.com/adhdoula_/`. Zichtbaar op Over mij.

### Live site

- Repo: `Johannes0402/ADHDoula`, branch `main`. Vercel, framework **Other**, geen build.
- DNS blijft bij mijn.host. Geen Vercel-nameservers, anders valt de mail weg.
- Canonieke URL's gebruiken `https://www.adhdoula.nl/`.

## Nog niet ingevuld

Opleidingsnaam en een portretfoto. NBvD niet noemen tot ze lid is.
