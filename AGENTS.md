# ADHDOULA — instructies voor agents

Lees [README.md](./README.md), het deel **Voor agents**, voordat je de site wijzigt. Daar staan eigenaar, kleuren en de dingen die je niet verzint.

Citeerbare feiten voor bezoekers en taalmodellen staan in [ai-knowledge-pack.md](./ai-knowledge-pack.md). De index is [llms.txt](./llms.txt). HTML blijft de canonieke pagina. Een `.md`-bestand is alleen de spiegel.

Na een wijziging aan HTML draai je `python3 scripts/generate_llm.py` en commit je de uitvoer mee. Het script schrijft de paginaspiegels, `llms.txt`, `llms-full.txt` en `sitemap.xml`. Die bestanden niet met de hand bijwerken. Een nieuwe HTML-pagina hoort in de lijst `PAGES` in dat script. Het kennisbestand blijft met de hand, inclusief de profiel-URL's.
